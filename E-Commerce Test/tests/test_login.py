from pages.login_page import LoginPage


def test_login_with_incorrect_password(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "test@example.com",
        "WrongPassword123!"
    )

    error_message = login_page.get_error_message()

    assert "Login was unsuccessful" in error_message