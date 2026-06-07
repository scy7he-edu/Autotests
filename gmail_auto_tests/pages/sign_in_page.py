from config import UserCredentials as uc

class SignInPage:
        
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto('https://gmail.com', wait_until='commit')

    def fill_email(self):
        email_field = self.page.locator('[type="email"]')
        email_field.fill(uc.EMAIL_ADDRESS)

    def fill_email_proceed(self):
        button = self.page.locator('#identifierNext')
        button.click()

    def fill_password(self):
        password_field = self.page.locator('[type="password"]')
        password_field.fill(uc.PASSWORD)

    def fill_password_proceed(self):
        button = self.page.locator('#passwordNext')
        button.click()