import pytest
from pages.login_page import LoginPage
from test_data.login_data import (
    VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD,
    EXPECTED_SUCCESS, EXPECTED_ERROR
)

@pytest.mark.smoke
def test_valid_login(driver):
    page = LoginPage(driver)
    page.login(VALID_USERNAME, VALID_PASSWORD)
    assert page.get_success_message() == EXPECTED_SUCCESS

@pytest.mark.regression
def test_invalid_username(driver):
    page = LoginPage(driver)
    page.login(INVALID_USERNAME, VALID_PASSWORD)
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.regression
def test_invalid_password(driver):
    page = LoginPage(driver)
    page.login(VALID_USERNAME, INVALID_PASSWORD)
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.regression
def test_both_credentials_invalid(driver):
    page = LoginPage(driver)
    page.login(INVALID_USERNAME, INVALID_PASSWORD)
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.regression
def test_empty_username(driver):
    page = LoginPage(driver)
    page.enter_password(VALID_PASSWORD)
    page.click_login()
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.regression
def test_empty_password(driver):
    page = LoginPage(driver)
    page.enter_username(VALID_USERNAME)
    page.click_login()
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.regression
def test_both_fields_empty(driver):
    page = LoginPage(driver)
    page.click_login()
    assert page.get_error_message() == EXPECTED_ERROR

@pytest.mark.smoke
def test_password_is_masked(driver):
    page = LoginPage(driver)
    assert page.get_password_type() == "password"

@pytest.mark.regression
def test_forgot_password_navigation(driver):
    page = LoginPage(driver)
    page.click_forgot_password()
    assert "Password Recovery" in driver.title
