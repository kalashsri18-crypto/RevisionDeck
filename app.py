import os, sqlite3
from datetime import date, timedelta
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
app.config["DATABASE"]=os.environ.get("DATABASE","revisiondeck.sqlite3")

def db():
    c=sqlite3.connect(app.config["DATABASE"]); c.row_factory=sqlite3.Row; return c

def init_db():
    with db() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS cards(
            id INTEGER PRIMARY KEY, deck TEXT NOT NULL, question TEXT NOT NULL,
            answer TEXT NOT NULL, interval_days INTEGER NOT NULL DEFAULT 0,
            due_on TEXT NOT NULL, reviews INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        c.execute("CREATE INDEX IF NOT EXISTS idx_cards_due ON cards(due_on)")

@app.get("/")
def home(): return render_template("index.html")

@app.get("/api/cards")
def list_cards():
    deck=request.args.get("deck","").strip()
    with db() as c:
        if deck: rows=c.execute("SELECT * FROM cards WHERE deck=? ORDER BY due_on,id",(deck,)).fetchall()
        else: rows=c.execute("SELECT * FROM cards ORDER BY due_on,id").fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/api/cards")
def add_card():
    d=request.get_json(silent=True) or {}
    deck=str(d.get("deck","")).strip(); q=str(d.get("question","")).strip(); a=str(d.get("answer","")).strip()
    if not all((deck,q,a)): return jsonify(error="Deck, question and answer are required."),400
    with db() as c:
        cur=c.execute("INSERT INTO cards(deck,question,answer,due_on) VALUES(?,?,?,?)",(deck,q,a,date.today().isoformat()))
        row=c.execute("SELECT * FROM cards WHERE id=?",(cur.lastrowid,)).fetchone()
    return jsonify(dict(row)),201

@app.post("/api/cards/<int:card_id>/review")
def review_card(card_id):
    d=request.get_json(silent=True) or {}; rating=d.get("rating")
    intervals={"again":0,"hard":1,"good":3,"easy":7}
    if rating not in intervals: return jsonify(error="Rating must be again, hard, good or easy."),400
    with db() as c:
        row=c.execute("SELECT * FROM cards WHERE id=?",(card_id,)).fetchone()
        if not row: return jsonify(error="Card not found."),404
        days=intervals[rating] if rating=="again" else max(intervals[rating],row["interval_days"]*({"hard":1.2,"good":2.0,"easy":2.8}[rating]))
        due=(date.today()+timedelta(days=round(days))).isoformat()
        c.execute("UPDATE cards SET interval_days=?,due_on=?,reviews=reviews+1 WHERE id=?",(round(days),due,card_id))
        updated=c.execute("SELECT * FROM cards WHERE id=?",(card_id,)).fetchone()
    return jsonify(dict(updated))

@app.delete("/api/cards/<int:card_id>")
def delete_card(card_id):
    with db() as c: cur=c.execute("DELETE FROM cards WHERE id=?",(card_id,))
    return ("",204) if cur.rowcount else (jsonify(error="Card not found."),404)

@app.get("/api/stats")
def stats():
    today=date.today().isoformat()
    with db() as c:
        total=c.execute("SELECT COUNT(*) n FROM cards").fetchone()["n"]
        due=c.execute("SELECT COUNT(*) n FROM cards WHERE due_on<=?",(today,)).fetchone()["n"]
        decks=c.execute("SELECT COUNT(DISTINCT deck) n FROM cards").fetchone()["n"]
    return jsonify(total=total,due=due,decks=decks)

with app.app_context(): init_db()
if __name__=="__main__": app.run(debug=os.environ.get("FLASK_DEBUG")=="1")
