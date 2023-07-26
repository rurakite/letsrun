import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("running_tracker")


def get_date():
    """Get and validate date from user input"""
    while True:
        date = input("Enter the date of your run (DD-MM-YYYY):\n")
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
            return date
        except ValueError:
            print("Invalid date format. Please enter in DD-MM-YYYY format.")


def get_weight():
    """Get and validate weight from user input"""
    while True:
        weight_str = input("Enter your weight in kg:\n")
        try:
            weight = float(weight_str)
            if weight > 0:
                return weight
            else:
                print("Weight must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


def get_time():
    """Get and validate time from user input"""
    while True:
        time_str = input("Enter time of your run in minutes:\n")
        try:
            time = float(time_str)
            if time > 0:
                return time
            else:
                print("Time must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


def get_distance():
    """Get and validate distance from user input"""
    while True:
        distance_str = input("Enter the distance you done in km:\n")
        try:
            distance = float(distance_str)
            if distance > 0:
                return distance
            else:
                print("Distance must be greater than zero.")
        except ValueError:
            print("Invalid data. Please enter a number.")


get_date()
get_weight()
get_distance()
