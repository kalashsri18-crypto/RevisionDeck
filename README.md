# RevisionDeck
### Spaced-Repetition Flashcards for Smarter Revision

RevisionDeck is a flashcard learning project designed around spaced repetition. The goal is to help students revise actively, rate how well they remembered each answer, and prioritize cards that are due for review.

> **Repository description:** A spaced-repetition flashcard learning app concept for creating decks, reviewing cards, tracking recall, and scheduling revisions.

## Planned product features
- Create and organize flashcard decks by subject
- Add question-and-answer cards
- Review cards using active recall
- Rate recall quality after each card
- Schedule the next review based on the recall rating
- See due cards and basic learning progress
- Store decks and review history persistently

## Planned technology
- Python 3.10+
- Flask for the web application
- SQLite for local persistence
- HTML, CSS and vanilla JavaScript
- pytest for automated tests

## Intended project structure
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

## Development status
**Planning / README scaffold.** The repository currently contains the project description; the application code, database models, tests, and setup files have not yet been added. Feature descriptions above are planned scope, not claims of implemented functionality.

## Proposed review algorithm
A review session should ask the learner to recall the answer before revealing it. The learner then rates recall (for example: Again, Hard, Good, or Easy). The app uses that rating and the previous review interval to calculate the next due date. This project is intended as a study aid, not a validated scientific assessment tool.

## Roadmap
- [ ] Implement Flask application and SQLite schema
- [ ] Add deck and flashcard CRUD
- [ ] Implement review scheduling
- [ ] Add due-card and progress views
- [ ] Add automated tests and sample deck
- [ ] Add screenshots and deployment instructions

## License
See [LICENSE](LICENSE) if a license file is added to this repository.
