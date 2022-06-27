from datetime import datetime
import requests
import json

response = requests.get("https://ct-mock-tech-assessment.herokuapp.com/").json()
partners = response["partners"]


class Country:

    def __init__(self, country):
        self.country = country
        self.country_partners = []
        self.count = {}
        self.attendee = []
        self.startDate = {}
        self.name = {}
        self.best_dates = []
        self.all_dates = []
        self.available_days = []
        self.available_partners = []
        self.indexes = []
        self.highest_count = []
        self.data = {}
        self.start = ""
        self.available_meeting_dates = []

    def get_partners(self):
        for partner in partners:
            if partner["country"] == self.country:
                self.country_partners.append(partner)
        return self.country_partners

    def get_meeting_dates(self):

        for partner in self.country_partners:
            available_dates = partner["availableDates"]
            self.available_days.append(available_dates)
        for dates in self.available_days:
            self.all_dates.append(dates)
            for day in dates:
                self.best_dates.append(day)
        for date in self.best_dates:
            x = self.best_dates.index(date)
            self.indexes.append(str(x))
        for item in self.indexes:
            y = self.indexes.count(item)
            self.highest_count.append(y)
            best = max(self.highest_count)
        time_consuming = list(zip(self.best_dates, self.indexes, self.highest_count))
        for date in time_consuming:
            if best == date[2]:
                self.available_meeting_dates.append(date[0])
        self.start = self.available_meeting_dates[0]
        self.startDate["startDate"] = self.start
        return self.startDate

    def get_attendees(self):
        for partner in self.country_partners:
            attendee_email = partner["email"]
            if self.startDate["startDate"] in partner["availableDates"]:
                self.attendee.append(attendee_email)
                self.name["name"] = partner["country"]
                self.count["attendeeCount"] = len(self.attendee)
        return self.name, self.count, self.attendee


united_states = Country("United States")
us_partners = united_states.get_partners()
us_meeting_date = united_states.get_meeting_dates()
us_attendees = united_states.get_attendees()

ireland = Country("Ireland")
ir_partners = ireland.get_partners()
ir_meeting_date = ireland.get_meeting_dates()
ir_attendees = ireland.get_attendees()

spain = Country("Spain")
sp_partners = spain.get_partners()
sp_meeting_date = spain.get_meeting_dates()
sp_attendees = spain.get_attendees()

mexico = Country("Mexico")
m_partners = mexico.get_partners()
m_meeting_date = mexico.get_meeting_dates()
m_attendees = mexico.get_attendees()

canada = Country("Canada")
c_partners = canada.get_partners()
c_meeting_date = canada.get_meeting_dates()
c_attendees = canada.get_attendees()

singapore = Country("Singapore")
si_partners = singapore.get_partners()
si_meeting_date = singapore.get_meeting_dates()
si_attendees = singapore.get_attendees()

japan = Country("Japan")
j_partners = japan.get_partners()
j_meeting_date = japan.get_meeting_dates()
j_attendees = japan.get_attendees()

united_kingdom = Country("United Kingdom")
uk_partners = united_kingdom.get_partners()
uk_meeting_date = united_kingdom.get_meeting_dates()
uk_attendees = united_kingdom.get_attendees()

france = Country("France")
f_partners = france.get_partners()
f_meeting_date = france.get_meeting_dates()
f_attendees = france.get_attendees()

data = {
    "us_country": us_attendees,
    "us_start__date": us_meeting_date,
    "ir_country": ir_attendees,
    "ir_start_date": ir_meeting_date,
    "sp_country": sp_attendees,
    "sp_start_date": sp_meeting_date,
    "mex_country": m_attendees,
    "mex_start_date": m_meeting_date,
    "can_country": c_attendees,
    "can_start_date": c_meeting_date,
    "s_country": si_attendees,
    "s_start_date": si_meeting_date,
    "j_country": j_attendees,
    "j_start_date": j_meeting_date,
    "uk_country": uk_attendees,
    "uk_start_date": uk_meeting_date,
    "f_country": f_attendees,
    "f_start_date": f_meeting_date,
}
url = "https://ct-mock-tech-assessment.herokuapp.com/"
with open("data.json", "w") as data_file:
    json.dump(data, data_file)
requests.post(url, json= data)


