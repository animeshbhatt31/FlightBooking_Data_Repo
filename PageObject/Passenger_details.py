class PassengerDetails:


    def __init__(self,page):
        self.page = page

    def passenger_details(self,passenger_all_details):
        self.page.get_by_test_id("flight-passenger-name").fill(passenger_all_details["passenger_name"])
        self.page.get_by_placeholder("you@example.com").fill(passenger_all_details["passenger_email"])
        self.page.get_by_test_id("flight-passenger-phone").fill(passenger_all_details["passenger_phone"])
        self.page.get_by_role("button", name="Continue to payment →").click()