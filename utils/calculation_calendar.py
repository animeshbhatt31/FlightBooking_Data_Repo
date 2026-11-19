from datetime import date, timedelta


class calendarDates:

    def selectDates(self,departure_days_from_today,return_days_from_today):
        departure_date = date.today() + timedelta(days=departure_days_from_today)
        return_date = departure_date + timedelta(days=return_days_from_today)
        departure_date = departure_date.strftime("%Y-%m-%d")
        return_date = return_date.strftime("%Y-%m-%d")
        print("Today Date:", departure_date)
        print("Return Date:", return_date)
        return departure_date, return_date
