from app import app, db
import pytest

@pytest.fixture
def client(tmp_path):
    app.config["TESTING"]=True
    app.config["DATABASE"]=str(tmp_path/"test.sqlite3")
    with app.app_context():
        from app import init_db
        init_db()
    return app.test_client()

def test_create_review_and_delete_card(client):
    r=client.post("/api/cards",json={"deck":"Python","question":"What is a list?","answer":"An ordered collection"})
    assert r.status_code==201
    card=r.get_json()
    assert client.post(f"/api/cards/{card['id']}/review",json={"rating":"good"}).status_code==200
    assert client.delete(f"/api/cards/{card['id']}").status_code==204
