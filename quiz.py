#!/usr/bin/env python3
"""
quiz.py — Terminal Quiz Game
Run: python3 quiz.py
"""

import json
import os
import random
import time


# ── Colours ────────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    DIM    = "\033[2m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"""
{C.CYAN}{C.BOLD}
  ╔═══════════════════════════════╗
  ║       🧠  PYTHON QUIZ         ║
  ║     Test your knowledge!      ║
  ╚═══════════════════════════════╝
{C.RESET}""")


# ── Load questions ──────────────────────────────────────────
def load_questions(path="questions.json"):
    with open(path, "r") as f:
        return json.load(f)


# ── Ask a single question ───────────────────────────────────
def ask_question(number, total, question):
    print(f"{C.DIM}Question {number}/{total}{C.RESET}")
    print(f"\n{C.BOLD}{question['question']}{C.RESET}\n")

    options = question["options"]
    labels  = ["A", "B", "C", "D"]

    for label, option in zip(labels, options):
        print(f"  {C.CYAN}{label}{C.RESET}. {option}")

    print()
    while True:
        answer = input("  Your answer (A/B/C/D): ").strip().upper()
        if answer in labels[:len(options)]:
            break
        print(f"  {C.RED}Please enter A, B, C or D.{C.RESET}")

    correct_index  = question["answer"]        # 0-based index
    correct_label  = labels[correct_index]
    chosen_index   = labels.index(answer)

    if chosen_index == correct_index:
        print(f"\n  {C.GREEN}{C.BOLD}✓ Correct!{C.RESET}")
        return True
    else:
        print(f"\n  {C.RED}{C.BOLD}✗ Wrong!{C.RESET} "
              f"The answer was {C.YELLOW}{correct_label}. {options[correct_index]}{C.RESET}")
    return False


# ── Score summary ───────────────────────────────────────────
def show_results(score, total, elapsed):
    pct = int((score / total) * 100)

    if pct == 100:
        grade, colour = "Perfect! 🏆", C.GREEN
    elif pct >= 70:
        grade, colour = "Great job! 🎉", C.GREEN
    elif pct >= 40:
        grade, colour = "Not bad! 📚", C.YELLOW
    else:
        grade, colour = "Keep studying! 💪", C.RED

    print(f"""
{C.BOLD}{'─' * 35}{C.RESET}
  Score   : {colour}{C.BOLD}{score}/{total}  ({pct}%){C.RESET}
  Result  : {colour}{grade}{C.RESET}
  Time    : {C.DIM}{elapsed:.1f} seconds{C.RESET}
{C.BOLD}{'─' * 35}{C.RESET}
""")


# ── Main game loop ──────────────────────────────────────────
def play(questions):
    random.shuffle(questions)
    score     = 0
    start     = time.time()

    for i, q in enumerate(questions, 1):
        clear()
        banner()
        correct = ask_question(i, len(questions), q)
        if correct:
            score += 1
        time.sleep(1.2)

    clear()
    banner()
    print(f"  {C.BOLD}Quiz complete!{C.RESET}\n")
    show_results(score, len(questions), time.time() - start)


# ── Entry point ─────────────────────────────────────────────
def main():
    clear()
    banner()

    questions = load_questions()

    print(f"  {C.DIM}Loaded {len(questions)} questions.{C.RESET}\n")
    print(f"  {C.BOLD}Categories:{C.RESET} General Knowledge, Science, Tech\n")

    input(f"  Press {C.CYAN}Enter{C.RESET} to start...")

    play(questions)

    while True:
        again = input("  Play again? (y/n): ").strip().lower()
        if again == "y":
            play(load_questions())
            break
        elif again == "n":
            print(f"\n  {C.CYAN}Thanks for playing! Goodbye 👋{C.RESET}\n")
            break


if __name__ == "__main__":
    main()
