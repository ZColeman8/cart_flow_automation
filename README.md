# 🛒 SauceDemo Cart Flow Test Automation

This project is an end-to-end test automation suite for the [SauceDemo](https://www.saucedemo.com) website. It simulates a full user journey from logging in to purchasing an item, verifying the flow using Selenium WebDriver and `pytest` with structured Page Object Model (POM) architecture.

## ✅ Features

- End-to-end test for login → add to cart → checkout → order confirmation
- Page Object Model structure for maintainability
- Pytest for test execution and reporting
- Logging for test observability and debugging
- Automatic screenshots on failure
- Optional HTML test report generation

## 🗂️ Project Structure

```
data_scraper/
├── .github/
│   └── workflows/
│       └── ci.yml
├── reports/ 
├── logs/  
├── src/
│   └── pages/
│       ├── sign_in_page.py
│       ├── inventory_page.py
│       ├── cart_page.py
│       ├── checkout_page.py
│       └── checkout_finalize_page.py
│   └── utils/
│       └── logger.py
│
├── tests/
│   └── cart_flow_test.py
│
├── screenshots/
│   └── *.png (on failure)
│
├── conftest.py
├── pytest.ini
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run test with Pytest

```bash
pytest -v
```

### 3. Run with HTML report (optional)

```bash
pytest --html=reports/report.html
```

## 🔍 HTML Reporting (Optional)

Ensure you have `pytest-html` installed:

```bash
pip install pytest-html
```

## 🧪 Test Flow

1. **Login Page:** Log in using standard credentials.
2. **Inventory Page:** Choose and add a product to the cart.
3. **Cart Page:** Confirm item presence, proceed to checkout.
4. **Checkout Page:** Enter user details.
5. **Finalize Page:** Complete order and assert confirmation.

## 📸 Screenshots on Failure

Failed tests will generate a screenshot in the `screenshots/` directory with a timestamp.

## 🛠 Technologies

- Python 3.11+
- Selenium WebDriver
- Pytest
- pytest-html
- WebDriver Manager

## 🧹 Improvements to Consider

- Add parameterized tests for different users/products
- Integrate CI (e.g., GitHub Actions)
- Extend coverage for negative test cases
- Add visual validation tools (e.g., Percy, Applitools)

---

📬 Maintained by Zach Coleman as part of QA automation portfolio projects.