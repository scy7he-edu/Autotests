from config import UserCredentials as uc

class InboxPage:

    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto('https://mail.google.com/mail/u/0/#inbox', wait_until='commit')

    def click_compose_button(self):
        button = self.page.locator('[style="user-select: none"]')
        button.click()

    def select_recepient(self):
        recepient_field = self.page.locator('[aria-label="To recipients"]')
        recepient_field.fill(uc.RECEPIENT)

    def fill_subject(self):
        subject_field = self.page.locator('[name="subjectbox"]')
        subject_field.fill(uc.MSG_SUBJECT)

    def fill_message(self):
        message_field = self.page.locator('[aria-multiline="true"]')
        message_field.fill(uc.MSG_TEXT)

    def send_message(self):
        button = self.page.locator('div[aria-label*="Send"]')
        button.click()