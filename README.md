# QA Technical Task - Marina Jakovljević

This repository contains my solution for the QA technical task. It includes automated and manual testing of the [FishingBooker](https://fishingbooker.com/) dev web application.

---

## 🔧 1. Automated UI Tests

- Framework: **Python + Selenium + Pytest**
- Design Pattern: **Page Object Model (POM)**
- Tests cover: Sign up / Login flow, Update profil, etc.
- Folder: `automation_tests/`


## 📄 2. Manual Test Cases

- **Tool:** Qase.io  
- **Format:** Test cases exported as PDF  
- **Location:** `manual_tests/TestCases_Marina_Jakovljevic.pdf`


## 🐞 3. Bug Reports

- **Reported during:** Exploratory testing  
- **Tool:** Google Docs → exported as PDF  
- **Location:** `manual_tests/bug_report_Marina_Jakovljevic.pdf`




> To run automated tests:

```bash
pip install -r requirements.txt
pytest
