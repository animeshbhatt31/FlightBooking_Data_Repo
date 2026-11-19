class SearchFlight:

    def __init__(self,page):
        self.page = page

    def flight_search(self,round_trip_details,departure_date,return_date):
        self.page.locator("#flight-from").select_option(round_trip_details["from_city"])
        self.page.get_by_test_id("flight-to").select_option(round_trip_details["to_city"])
        self.page.locator("#flight-departure-date").fill(departure_date)
        self.page.locator("#flight-return-date").fill(return_date)
        self.page.locator("#flight-passengers").fill(round_trip_details["passengers_count"])
        self.page.locator("#flight-class").select_option(round_trip_details["flight_class"])
        # page.pause()
        self.page.get_by_role("button", name="Search Flights").click()



    def one_way_flight(self,one_way_details,departure_date):
        self.page.locator("#flight-from").select_option(one_way_details["from_city"])
        self.page.get_by_test_id("flight-to").select_option(one_way_details["to_city"])
        self.page.locator("#flight-departure-date").fill(departure_date)
        self.page.locator("#flight-passengers").fill(one_way_details["passengers_count"])
        self.page.locator("#flight-class").select_option(one_way_details["flight_class"])
        self.page.get_by_test_id("flight-one-way").check()
        self.page.get_by_role("button", name="Search Flights").click()




