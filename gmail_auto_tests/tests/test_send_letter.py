from playwright.sync_api import Page
from pages.send_letter_page import InboxPage
from pages.sign_in_page import SignInPage

def test_send_letter(page: Page):
    sign_in_page = SignInPage(page)
    sign_in_page.open_page()
    sign_in_page.fill_email()
    sign_in_page.fill_email_proceed()
    sign_in_page.fill_password()
    sign_in_page.fill_password_proceed()
    send_letter_page = InboxPage(page)
    send_letter_page.click_compose_button()
    send_letter_page.select_recepient()
    send_letter_page.fill_subject()
    send_letter_page.fill_message()
    send_letter_page.send_message()