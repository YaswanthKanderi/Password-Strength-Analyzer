# 🔐 Password Strength Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-NIST_800--63B-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A Python tool to analyse password strength, detect weak patterns, and recommend improvements — built on **NIST SP 800-63B** guidelines.

**Author:** Yaswanth Kanderi | Master of Cyber Security, La Trobe University

---

## 📋 Features

- 🔍 **NIST 800-63B compliance** checks
- 📏 Length & character variety scoring
- 🚫 Common password detection (top 24 bad passwords)
- ⌨️ Keyboard walk detection (qwerty, asdfgh, zxcvbn...)
- 🔁 Repeated & sequential character detection
- 📊 Shannon entropy calculation
- 💡 Actionable improvement tips
- 🎨 Visual strength bar with colour-coded rating

---

## 🚀 Usage

```bash
python3 password_analyzer.py
```

### Example Output

```
==================================================
  Password Strength Analyzer
  Author: Yaswanth Kanderi | NIST 800-63B
==================================================

Enter password to analyse (hidden):

  Strength : 🟢 STRONG
  Score    : [██████░░] 6/8
  Length   : 14 chars
  Entropy  : 91.4 bits

  💡 Tips:
     • Add special characters (!, @, #, $...)
     • Estimated entropy: 91.4 bits
```

---

## 📊 Scoring System

| Score | Rating | Description |
|-------|--------|-------------|
| 0–2 | 🔴 Very Weak | Immediate risk |
| 3–4 | 🟠 Weak | Easily crackable |
| 5–6 | 🟡 Moderate | Acceptable |
| 7 | 🟢 Strong | Recommended |
| 8 | ✅ Very Strong | Excellent |

---

## 🛠️ Tech Stack

- **Python 3** — standard library only (no dependencies)
- `re` — pattern matching
- `math` — entropy calculation
- `getpass` — secure hidden input

---

## 📚 References

- [NIST SP 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

## ⚠️ Disclaimer

This tool is for **educational and authorised use only**. Always follow your organisation's security policies.

---

*Built by [Yaswanth Kanderi](https://github.com/YaswanthKanderi) | Aspiring Cyber Security Analyst*
