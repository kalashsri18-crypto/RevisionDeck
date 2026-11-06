<div align="center">

# 🧠 RevisionDeck

### Spaced-Repetition Flashcards for Smarter Revision

Learn actively, review at the right time, and make every revision session count.

![Status](https://img.shields.io/badge/Status-Implemented-brightgreen?style=for-the-badge)
![Planned Python](https://img.shields.io/badge/Planned-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Planned Flask](https://img.shields.io/badge/Planned-Flask-black?style=for-the-badge&logo=flask&logoColor=white)

</div>

---

## 📌 Overview

**RevisionDeck** is a Flask + SQLite flashcard app built around active recall and spaced repetition. The goal is to help students test their memory through active recall, rate how well they remembered each answer, and prioritize cards that are due for review.

> **Current status:** Implemented with a Flask backend, SQLite persistence, browser UI, flashcard CRUD, review ratings, and due-date scheduling.

## ✨ Features

- 📚 Create and organize flashcard decks by subject
- ✍️ Add question-and-answer cards
- 🧠 Review cards using active recall
- ⭐ Rate recall quality after each card
- ⏳ Schedule the next review based on the recall rating
- 📈 Track due cards and basic learning progress
- 💾 Store decks and review history persistently

## 🛠️ Tech Stack

| Technology | Intended use |
|---|---|
| Python 3.10+ | Core programming language |
| Flask | Web application |
| SQLite | Local data storage |
| HTML, CSS, JavaScript | User interface |
| pytest | Automated testing |

## 🧩 Review Workflow

1. Create a deck and add flashcards.
2. Start a review session and try to recall each answer.
3. Reveal the answer and rate your recall: **Again**, **Hard**, **Good**, or **Easy**.
4. Use the rating and previous review interval to calculate the next due date.
5. Return when cards become due.

The scheduling approach is a proposed learning aid, not a validated scientific assessment tool.

## 🗺️ Roadmap

- [ ] Set up Flask application and SQLite schema
- [ ] Implement deck and flashcard management
- [ ] Build the review-session interface
- [x] Implement review scheduling
- [ ] Add due-card and progress views
- [ ] Write automated tests and add a sample deck
- [ ] Add screenshots and deployment instructions

## 🚀 Getting Started

```bash
git clone https://github.com/kalashsri18-crypto/RevisionDeck.git
cd RevisionDeck
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Run tests with `pytest -q`.

## 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
├── templates/
├── static/
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

## 👨‍💻 Author

**Kalash Srivastava**  
[GitHub](https://github.com/kalashsri18-crypto) · [LinkedIn](https://www.linkedin.com/in/kalash-srivastava-b6592a3b3) · [Email](mailto:kalashsri18@gmail.com)

---

<div align="center">
  Documentation and project direction by Kalash
</div>
