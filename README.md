# FutureTech Selenium Python Complete Automation Framework

## Real-World QA Automation Project Using Selenium WebDriver + Python + pytest

A production-style Selenium automation framework designed for students
and aspiring QA Automation Engineers. This project demonstrates how to
build maintainable, scalable UI automation using Page Object Model
(POM), reusable Base Page methods, explicit waits, pytest fixtures,
centralized test data, screenshots, logging, and HTML reporting.

------------------------------------------------------------------------

## Project Overview

Most beginners learn Selenium by writing individual scripts.
Professional QA teams build automation frameworks.

This repository bridges that gap by demonstrating how to organize
Selenium automation into reusable components that can easily scale from
a Login page to complete enterprise applications.

### Technologies Used

-   Python 3.10+
-   Selenium WebDriver 4
-   pytest
-   pytest-html
-   Page Object Model (POM)
-   Chrome Browser
-   Git & GitHub

------------------------------------------------------------------------

## Features

-   Page Object Model architecture
-   Reusable Base Page methods
-   Explicit waits with WebDriverWait
-   pytest fixtures
-   Smoke & Regression test markers
-   Failure screenshots
-   HTML reporting
-   Centralized configuration
-   Local demo web application
-   Portfolio-ready project structure

------------------------------------------------------------------------

## Project Structure

``` text
futuretech-selenium-python-complete-framework/
│
├── config/
│   └── config.py
├── demo_app/
│   ├── login.html
│   └── password-recovery.html
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   └── test_login.py
├── test_data/
│   └── login_data.py
├── utils/
│   ├── logger.py
│   └── screenshot.py
├── screenshots/
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md
```

------------------------------------------------------------------------

## Framework Architecture

``` text
Test Case
    ↓
pytest
    ↓
Fixture
    ↓
Page Object
    ↓
Base Page
    ↓
WebDriver
    ↓
Browser
    ↓
Application
    ↓
Assertion
    ↓
Report / Screenshot
```

Each layer has a single responsibility, making the framework easier to
maintain and extend.

------------------------------------------------------------------------

## Installation

### Clone the repository

``` bash
git clone https://github.com/santhulak/futuretech-selenium-python-complete-framework.git
cd futuretech-selenium-python-complete-framework
```

### Create Virtual Environment

**Windows**

``` bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Running Tests

### Execute All Tests

``` bash
pytest -v
```

### Smoke Tests

``` bash
pytest -m smoke -v
```

### Regression Tests

``` bash
pytest -m regression -v
```

### Generate HTML Report

``` bash
pytest --html=reports/report.html --self-contained-html -v
```

------------------------------------------------------------------------

## Demo Login Credentials

  Username   Password
  ---------- --------------
  testuser   Password@123

------------------------------------------------------------------------

## Test Scenarios

  \#   Scenario                     Type
  ---- ---------------------------- ------------
  1    Valid Login                  Smoke
  2    Invalid Username             Regression
  3    Invalid Password             Regression
  4    Both Credentials Invalid     Regression
  5    Empty Username               Regression
  6    Empty Password               Regression
  7    Empty Fields                 Regression
  8    Password Masking             Smoke
  9    Forgot Password Navigation   Regression

------------------------------------------------------------------------

## Page Object Model

The framework separates **test logic** from **UI implementation**.

**Without POM**

``` python
driver.find_element(...)
driver.find_element(...)
driver.find_element(...)
```

**With POM**

``` python
page.login(username, password)
```

Benefits:

-   Cleaner tests
-   Reusable methods
-   Easier maintenance
-   Centralized locators

------------------------------------------------------------------------

## Base Page Responsibilities

The Base Page contains reusable browser operations:

-   click()
-   type_text()
-   get_text()
-   get_attribute()
-   find_visible()
-   find_clickable()

Every new page inherits these methods.

------------------------------------------------------------------------

## Why Explicit Waits?

Instead of using:

``` python
time.sleep(5)
```

The framework waits until elements are actually ready:

``` python
WebDriverWait(driver,10).until(...)
```

This creates faster and more reliable automation.

------------------------------------------------------------------------

## Screenshot Handling

Whenever a test fails:

1.  Screenshot captured automatically
2.  Timestamp added
3.  Saved inside `/screenshots`

Example:

``` text
screenshots/
test_invalid_login_20260831_153010.png
```

------------------------------------------------------------------------

## Smoke vs Regression

### Smoke Suite

Critical functionality only.

``` bash
pytest -m smoke
```

### Regression Suite

Complete application validation.

``` bash
pytest -m regression
```

------------------------------------------------------------------------

## HTML Reporting

Generate professional reports with:

``` bash
pytest --html=reports/report.html --self-contained-html
```

Reports include:

-   Pass / Fail summary
-   Test duration
-   Individual test results

------------------------------------------------------------------------

## How to Add a New Page

Example: Dashboard Page

1.  Create `dashboard_page.py`
2.  Inherit `BasePage`
3.  Add locators
4.  Add page methods
5.  Write tests

The framework is designed to grow without duplicating Selenium code.

------------------------------------------------------------------------

## Future Improvements

-   Data-driven testing (CSV/Excel/JSON)
-   Cross-browser execution
-   Parallel testing
-   GitHub Actions CI/CD
-   Allure Reporting
-   API + UI testing
-   Docker execution
-   Selenium Grid

------------------------------------------------------------------------

## Learning Outcomes

After completing this project, you'll understand:

-   Selenium WebDriver
-   pytest automation
-   Page Object Model
-   Base Page design
-   Explicit waits
-   Test fixtures
-   Automation architecture
-   Smoke & Regression testing
-   HTML reporting
-   GitHub portfolio development

------------------------------------------------------------------------

## Portfolio Description

> Developed a scalable Selenium WebDriver automation framework using
> Python and pytest. Implemented Page Object Model, reusable Base Page
> methods, explicit waits, centralized test data, smoke and regression
> testing, automated screenshots, and HTML reporting for maintainable UI
> automation.

------------------------------------------------------------------------

## Author

**FutureTech Simulation Academy**

*Don't Just Learn Technology. Simulate the Job.*
