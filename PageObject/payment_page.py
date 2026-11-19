class PaymentPage:

    def __init__(self,page):
        self.page=page

    def card_details(self,card_all_details):
        self.page.get_by_test_id("flight-card-number").fill(card_all_details["card_number"])
        self.page.get_by_placeholder("MM/YY").fill(card_all_details["expiry_date"])
        self.page.get_by_test_id("flight-cvv").fill(card_all_details["cvv"])

    def verify_payment_amount(self,flight_details,departure_price,return_price=None):
        total = self.page.get_by_test_id("flight-total").inner_text()
        print("TOTAL", total)
        flight_total = int(total.replace("$", ""))
        passenger_count = int(flight_details["passengers_count"])
        if return_price is None:
            total_price = departure_price * passenger_count
        else:
            total_price = departure_price * passenger_count + return_price * passenger_count
        assert flight_total == total_price
        print("Total matches: PASS")

    def Pay_and_Confirm_Booking(self):
        self.page.get_by_role("button", name="Pay & Confirm Booking").click()


