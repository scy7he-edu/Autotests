from config import UserCredentials as uc

CREATE_ACCOUNT_BUTTON = '[aria-haspopup="menu"]'

class SignUpPage:

    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto('https://gmail.com', wait_until='commit')

    def create_account_click_button(self):
        button = self.page.locator(CREATE_ACCOUNT_BUTTON)
        button.click()

    def choose_for_personal_use(self):
        selector = self.page.get_by_role('menuitem').nth(0)
        selector.click()

    def fill_first_name(self):
        first_name_field = self.page.locator('#firstName')
        first_name_field.fill(uc.FIRST_NAME)

    def fill_last_name(self):
        last_name_field = self.page.locator('#lastName')
        last_name_field.fill(uc.LAST_NAME)

    def collect_name_proceed(self):
        button = self.page.locator('#collectNameNext')
        button.click()

    def fill_birthday_gender(self):
        month_dropdown = self.page.locator('#month')
        month_dropdown.click()
        month_selector = self.page.locator(f'[data-value="{uc.BIRTH_MONTH}"]:visible')
        month_selector.click()
        day = self.page.locator('#day')
        day.fill(uc.BIRTH_DAY)
        year = self.page.locator('#year')
        year.fill(uc.BIRTH_YEAR)
        gender_dropdown = self.page.locator('#gender')
        gender_dropdown.click()
        gender_selector = self.page.locator(f'[data-value="{uc.GENDER}"]:visible')
        gender_selector.click()

    def birthday_gender_proceed(self):
        button = self.page.locator('#birthdaygenderNext')
        button.click()

    def choose_email_address(self):
        email_option = self.page.get_by_role('radio').nth(2)
        email_option.click()
        custom_email = self.page.locator('[name="Username"]')
        custom_email.fill(uc.EMAIL_ADDRESS)
    
    def email_address_proceed(self):
        button = self.page.locator('#next')
        button.click()

    def create_password(self):
        password_field = self.page.locator('[name="Passwd"]')
        password_field.fill(uc.PASSWORD)
        confirm_password_field = self.page.locator('[name="PasswdAgain"]')
        confirm_password_field.fill(uc.PASSWORD)

    def password_proceed(self):
        button = self.page.locator('#createpasswordNext')
        button.click()