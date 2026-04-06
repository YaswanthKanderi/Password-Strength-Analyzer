#!/usr/bin/env python3
"""
Password Strength Analyzer
Author: Yaswanth Kanderi
Description: Analyses password strength based on NIST 800-63B guidelines.
             Detects weak patterns, common passwords, and gives improvement tips.
"""

import re
import string
import math
from getpass import getpass


COMMON_PASSWORDS = {
    "123456","password","123456789","12345678","12345","1234567",
    "qwerty","abc123","000000","password1","iloveyou","admin",
    "letmein","monkey","dragon","master","sunshine","princess",
    "welcome","shadow","superman","michael","football","baseball"
}

KEYBOARD_WALKS = ["qwerty","asdfgh","zxcvbn","qazwsx","123456","654321"]


def entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32
    return len(password) * math.log2(charset) if charset else 0


def check_strength(password):
    issues  = []
    tips    = []
    score   = 0

    # Length checks (NIST recommends >= 8, ideally >= 12)
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    elif len(password) < 12:
        tips.append("Consider using 12+ characters for better security")
        score += 1
    else:
        score += 2

    # Character variety
    if re.search(r'[a-z]', password): score += 1
    else: tips.append("Add lowercase letters")

    if re.search(r'[A-Z]', password): score += 1
    else: tips.append("Add uppercase letters")

    if re.search(r'[0-9]', password): score += 1
    else: tips.append("Add numbers")

    if re.search(r'[^a-zA-Z0-9]', password): score += 2
    else: tips.append("Add special characters (!, @, #, $...)")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        issues.append("This is a commonly used password — change it immediately")
        score = max(0, score - 4)

    # Keyboard walk detection
    pw_lower = password.lower()
    for walk in KEYBOARD_WALKS:
        if walk in pw_lower:
            issues.append(f"Contains keyboard pattern '{walk}'")
            score = max(0, score - 2)
            break

    # Repeated characters
    if re.search(r'(.)\1{2,}', password):
        issues.append("Contains repeated characters (e.g. 'aaa')")
        score = max(0, score - 1)
        tips.append("Avoid repeating the same character 3+ times")

    # Sequential numbers
    if re.search(r'(012|123|234|345|456|567|678|789|987|876)', password):
        issues.append("Contains sequential numbers")
        score = max(0, score - 1)

    # Entropy
    ent = entropy(password)
    tips.append(f"Estimated entropy: {ent:.1f} bits")

    # Rating
    if score <= 2:   rating, colour = "VERY WEAK",  "🔴"
    elif score <= 4: rating, colour = "WEAK",        "🟠"
    elif score <= 6: rating, colour = "MODERATE",    "🟡"
    elif score <= 7: rating, colour = "STRONG",      "🟢"
    else:            rating, colour = "VERY STRONG", "✅"

    return {
        "score":   score,
        "rating":  rating,
        "colour":  colour,
        "issues":  issues,
        "tips":    tips,
        "entropy": round(ent, 2)
    }


def display(result, password_len):
    bar_filled = min(result["score"], 8)
    bar = "█" * bar_filled + "░" * (8 - bar_filled)
    print(f"\n  Strength : {result['colour']} {result['rating']}")
    print(f"  Score    : [{bar}] {result['score']}/8")
    print(f"  Length   : {password_len} chars")
    print(f"  Entropy  : {result['entropy']} bits")

    if result["issues"]:
        print("\n  ⚠️  Issues:")
        for i in result["issues"]: print(f"     • {i}")

    if result["tips"]:
        print("\n  💡 Tips:")
        for t in result["tips"]: print(f"     • {t}")
    print()


def main():
    print("=" * 50)
    print("  Password Strength Analyzer")
    print("  Author: Yaswanth Kanderi | NIST 800-63B")
    print("=" * 50)
    while True:
        password = getpass("\nEnter password to analyse (hidden): ")
        if not password:
            print("No input. Exiting.")
            break
        result = check_strength(password)
        display(result, len(password))
        again = input("Analyse another? (y/n): ").strip().lower()
        if again != 'y':
            break


if __name__ == "__main__":
    main()
