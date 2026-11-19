import json

from playwright.sync_api import Playwright, expect

from PageObject.Passenger_details import PassengerDetails
from PageObject.Search_flight import SearchFlight
from PageObject.login import LoginPage
from PageObject.payment_page import PaymentPage
from PageObject.search_cheapest_flight import cheapestflight
from utils.calculation_calendar import calendarDates
from utils.load_test_data_file import load_test_data_file


def test_one_way_booking(page_instance):

    # with open("All_test_data/testing_data.json", "r") as f:
    #     one_way_data = json.load(f)
    one_way_data=load_test_data_file()
    one_way_details=one_way_data["one_way"]
    departure_days_from_today=one_way_details["departure_days_from_today"]
    passenger_all_details = one_way_data["passenger_details"]
    card_all_details=one_way_data["payment_details"]
    non_stop_only = one_way_data["choose_flight"]["checkbox"]["non_stop_only"]



    login_page_obj=LoginPage(page_instance)
    login_page_obj.navigate_flight_booking()
    calender_dates_obj=calendarDates()
    departure_date,_=calender_dates_obj.selectDates(departure_days_from_today,0)
    search_flight_obj=SearchFlight(page_instance)
    search_flight_obj.one_way_flight(one_way_details,departure_date)
    cheapest_flight_obj=cheapestflight(page_instance)
    cheapest_flight_obj.non_stop_filter(non_stop_only)
    departure_price=cheapest_flight_obj.search_departure_row()
    cheapest_flight_obj.Continue_to_passenger_details_page()
    passenger_details_obj=PassengerDetails(page_instance)
    passenger_details_obj.passenger_details(passenger_all_details)
    payment_page_obj=PaymentPage(page_instance)
    payment_page_obj.card_details(card_all_details)
    payment_page_obj.verify_payment_amount(one_way_details,departure_price)
    payment_page_obj.Pay_and_Confirm_Booking()
    expect(page_instance.locator("#flight-booking-success")).to_have_text("Booking Confirmed!")






