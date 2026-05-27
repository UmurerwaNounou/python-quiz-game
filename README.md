# 🧠 Python Quiz Game

> A colorful terminal quiz game built in Python — test your knowledge across General Knowledge, Science, and Tech!

![Python](https://img.shields.io/badge/Python-3.6+-4ade80?style=flat-square&logo=python&logoColor=black)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Questions](https://img.shields.io/badge/questions-10-yellow?style=flat-square)

## Preview

```
  ╔═══════════════════════════════╗
  ║       🧠  PYTHON QUIZ         ║
  ║     Test your knowledge!      ║
  ╚═══════════════════════════════╝

Question 1/10

  Which planet is known as the Red Planet?

  A. Venus
  B. Mars
  C. Jupiter
  D. Saturn

  Your answer (A/B/C/D):
```

## Features

- 10 questions across 3 categories
- Randomized question order every game
- Color-coded feedback (correct / wrong)
- Score summary with percentage and time
- Play again option
- No dependencies — pure Python standard library

## Getting Started

**Requirements:** Python 3.6+

```bash
# Clone the repo
git clone https://github.com/UmurerwaNounou/python-quiz-game.git
cd python-quiz-game

# Run the game
python3 quiz.py
```

On Windows:
```bash
python quiz.py
```

## Project Structure

```
python-quiz-game/
├── quiz.py          # Game logic
├── questions.json   # Quiz questions
└── README.md        # This file
```

## Add Your Own Questions

Edit `questions.json` — each question follows this format:

```json
{
  "question": "Your question here?",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "answer": 0,
  "category": "General Knowledge"
}
```

> `"answer"` is the index of the correct option (0 = A, 1 = B, 2 = C, 3 = D)

---

Made with Python 🐍 · MIT License
