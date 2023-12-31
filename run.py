import datetime
import time
import tabulate
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
            run_time = float(time_str)
            if run_time > 0:
                return run_time
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


def calculate_avg_speed(distance, run_time):
    """Calculate average speed"""
    speed = round(distance / (run_time / 60), 2)
    return speed


def calculate_pace(distance, run_time):
    """Calculate average pace"""
    pace = round(run_time / distance, 2)
    return pace


def calculate_burned_calories(weight, distance):
    """Calculate burned calories"""
    return round(distance * weight * 0.75)


def update_worksheet(data):
    log = SHEET.worksheet("log")
    log.append_row(data)
    print("Your Running Tracker updated successfully!")


def show_data():
    """Display all data from the 'log' worksheet in a nice table view"""
    log = SHEET.worksheet("log")
    all_data = log.get_all_values()
    headers = all_data[1]
    data_rows = all_data[2:]
    table = tabulate.tabulate(data_rows, headers=headers, tablefmt="grid")
    print(table)


def main():
    """Run all program functions"""
    date = get_date()
    weight = get_weight()
    run_time = get_time()
    distance = get_distance()
    print("Calculating your statistics")
    print(". . . . . . . . . . . . ")
    time.sleep(1)
    pace = calculate_pace(distance, run_time)
    print(f"Your pace is {pace} m/km.")
    print(". . . . . . . . . . . . ")
    time.sleep(1)
    speed = calculate_avg_speed(distance, run_time)
    print(f"Your average speed  is {speed} km/h.")
    print(". . . . . . . . . . . . ")
    time.sleep(1)
    burned_calories = calculate_burned_calories(weight, distance)
    print(f"You have burned {burned_calories} calories.")
    print(". . . . . . . . . . . . ")
    time.sleep(1)
    run_data = [date, distance, run_time, pace, speed, burned_calories]
    update_worksheet(run_data)
    print("* * * * * * * * * * * *")
    time.sleep(1)
    check_data = input("Do you want to display all running data? (yes/no):\n ")
    if check_data.lower() == 'yes':
        print("Sure! Just a second.")
        time.sleep(1)
        show_data()


print("Welcome to Running Training Tracker!")
time.sleep(1.5)
main()
