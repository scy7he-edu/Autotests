from playwright.sync_api import Page
from pages.sign_up_page import SignUpPage

def test_sign_up(page: Page):
    sign_up_page = SignUpPage(page)
    sign_up_page.open_page()
    sign_up_page.create_account_click_button()
    sign_up_page.choose_for_personal_use()
    sign_up_page.fill_first_name()
    sign_up_page.fill_last_name()
    sign_up_page.collect_name_proceed()
    sign_up_page.fill_birthday_gender()
    sign_up_page.birthday_gender_proceed()
    sign_up_page.choose_email_address()
    sign_up_page.email_address_proceed()
    sign_up_page.create_password()
    sign_up_page.password_proceed()
    page.pause()