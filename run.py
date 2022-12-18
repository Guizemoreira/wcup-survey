# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

ANSW = Credentials.from_service_account_file('answ.json')
SCOPED_ANSW = ANSW.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_ANSW)
SHEET = GSPREAD_CLIENT.open('wcup_survey')

def get_people_data():
    """
    It will get info from people to respond the survey
    """
    while True:
        print("Please enter your personal data for our survey")
        
        people_info = []
        first_name = input("Inform your First Name:\n")
        people_info.append(first_name)
        surename = input("Inform your Last Name:\n")
        people_info.append(surename)
        gender = input("Gender (M/F:\n")
        people_info.append(gender)
        dob = input("Inform the month of your Birthday:\n")
        people_info.append(dob)
        nationality = input("Inform your nationality:\n")
        people_info.append(nationality)

        people_data = people_info


    return people_data

def update_people_worksheet(data):
    """
    Update people worksheet, add new row with the list data provided
    """
    print("Updating people worksheet...\n")
    people_worksheet = SHEET.worksheet("people")
    people_worksheet.append_row(data)
    print("People worksheet updated successfully.\n")

def main():
    """
    Run all programm functions
    """
    data = get_people_data()
    people_data = [str.capitalize(char) for char in data]
    update_people_worksheet(people_data)

print("Welcome to automation part\n")
main()
