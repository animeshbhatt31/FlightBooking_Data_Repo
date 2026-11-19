from playwright.sync_api import expect


class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate(self):
        self.page.goto("https://www.qapractice.com/practice-login-form")

    def login(self,user_cred):
        self.page.get_by_placeholder("Enter your email").fill(user_cred["username"])
        self.page.get_by_test_id("login-password").fill(user_cred["password"])
        self.page.get_by_role("button", name="Sign in").click()



    def navigate_flight_booking(self):
        self.page.goto("https://www.qapractice.com/flight-booking-scenarios")

