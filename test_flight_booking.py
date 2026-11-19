import json

from playwright.sync_api import expect

from utils.calculation_calendar import calendarDates
from PageObject.Passenger_details import  PassengerDetails
from PageObject.Search_flight import SearchFlight
from PageObject.payment_page import PaymentPage
from PageObject.login import LoginPage
from PageObject.search_cheapest_flight import cheapestflight
from utils.load_test_data_file import load_test_data_file


def test_flight_booking(page_instance):

    ##load JSON file
    # with open("All_test_data/testing_data.json", "r") as f:
    #     test_data = json.load(f)
    test_data=load_test_data_file()
    user_cred=test_data["credentials"]
    round_trip_details=test_data["round_trip"]
    passenger_all_details=test_data["passenger_details"]
    card_all_details=test_data["payment_details"]
    choose_flight_details=test_data["choose_flight"]
    non_stop_only = choose_flight_details["checkbox"]["non_stop_only"]
    departure_days_from_today=round_trip_details["departure_days_from_today"]
    return_days_from_today=round_trip_details["return_days_from_today"]



    LoginPageObj=LoginPage(page_instance)
    LoginPageObj.navigate()

    LoginPageObj.login(user_cred)
    expect(page_instance.get_by_test_id("login-success")).to_have_text("Login Successful! Welcome to Premium Banking.")
    

    LoginPageObj.navigate_flight_booking()


    calendarDatesObj=calendarDates()
    departure_date, return_date=calendarDatesObj.selectDates(departure_days_from_today,return_days_from_today)


    searchflightObj = SearchFlight(page_instance)
    searchflightObj.flight_search(round_trip_details, departure_date, return_date)



    ##Departure


    cheapestflightObj=cheapestflight(page_instance)
    cheapestflightObj.non_stop_filter(non_stop_only)
    departure_price=cheapestflightObj.search_departure_row()

    ##Return

    return_price=cheapestflightObj.search_return_row()
    cheapestflightObj.Continue_to_passenger_details_page()


    #passanger_details

    PassengerDetailsObj=PassengerDetails(page_instance)
    PassengerDetailsObj.passenger_details(passenger_all_details)

    #card details
    PaymentPageObj=PaymentPage(page_instance)
    PaymentPageObj.card_details(card_all_details)

    # confirm verify the payment is correct
    PaymentPageObj.verify_payment_amount(round_trip_details, departure_price, return_price)


    PaymentPageObj.Pay_and_Confirm_Booking()

    expect(page_instance.locator("#flight-booking-success")).to_have_text("Booking Confirmed!")





