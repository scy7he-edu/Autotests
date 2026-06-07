from playwright.sync_api import Page
from pages.sign_in_page import SignInPage

def test_sign_in(page: Page):
    sign_in_page = SignInPage(page)
    sign_in_page.open_page()
    sign_in_page.fill_email()
    sign_in_page.fill_email_proceed()
    sign_in_page.fill_password()
    sign_in_page.fill_password_proceed()