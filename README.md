# FutureTech Selenium Python Complete Automation Framework

Portfolio-ready Selenium WebDriver automation framework using Python and pytest.

## Stack
- Python 3.10+
- Selenium WebDriver
- pytest
- Page Object Model
- Explicit waits
- Test data separation
- Failure screenshots
- HTML reporting
- Smoke/regression markers
- Local demo application

## Setup
python -m venv .venv

Windows:
.venv\\Scripts\\activate

macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

## Run
pytest -v
pytest -m smoke -v
pytest -m regression -v
pytest --html=reports/report.html --self-contained-html -v

## Project flow
Test Case -> pytest -> Fixture -> Page Object -> Base Page -> WebDriver -> Browser -> Application -> Assertion -> Report/Screenshot

## Test scenarios
1. Valid login
2. Invalid username
3. Invalid password
4. Both credentials invalid
5. Empty username
6. Empty password
7. Both fields empty
8. Password masking
9. Forgot-password navigation

Modern Selenium releases include Selenium Manager, so a separate ChromeDriver download is normally not required.
