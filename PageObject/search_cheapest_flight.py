class cheapestflight:
    def __init__(self,page):
        self.page=page

    def non_stop_filter(self, non_stop_only):
        checkbox = self.page.get_by_role("checkbox", name="Non-stop only")
        if non_stop_only is True:
            checkbox.check()
        else:
            checkbox.uncheck()

    def search_departure_row(self):
        departure = self.page.get_by_test_id("flight-departure-list")
        departure_rows = departure.locator(".align-items-center.g-3.row")
        return self.cheapest_flight(departure_rows)
    def search_return_row(self):
        returnFlight = self.page.get_by_test_id("flight-return-list")
        return_rows = returnFlight.locator(".align-items-center.g-3.row")
        return self.cheapest_flight(return_rows)

    def cheapest_flight(self,flight_rows,):


        print("Row Count:", flight_rows.count())
        prices = []
        for i in range(flight_rows.count()):
            # print(i,rows.nth(i).inner_text())
            priceVal = flight_rows.nth(i).locator(".h5.fw-bold.text-primary.mb-1").inner_text()
            # print("Price:",price)
            priceVal = int(priceVal.replace("$", ""))
            print("Prices:", priceVal)
            prices.append(priceVal)
        lowestPrice = min(prices)
        print("Lowest Price:", lowestPrice)
        lowestPriceIndex = prices.index(lowestPrice)
        print("Price Index:", lowestPriceIndex)
        flight_rows.nth(lowestPriceIndex).get_by_role("button", name="Select").click()
        return lowestPrice
    def Continue_to_passenger_details_page(self):
        self.page.get_by_role("button", name="Continue to passenger details →").click()