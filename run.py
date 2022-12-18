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

        if validate_people(people_data):
            print(f"Welcome {first_name} {surename}!\n")
            break

    return people_data

def validate_people(values):
    """
    Inside the try, verify name entry
    Raises ValueError 
    """
    try:
        if len(values) != 5:
            raise ValueError(
                "These fields are required"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_people_worksheet(data):
    """
    Update people worksheet, add new row with the list data provided
    """
    print("Updating people worksheet...\n")
    people_worksheet = SHEET.worksheet("people")
    people_worksheet.append_row(data)
    print("People worksheet updated successfully.\n")

def get_choices_ind():
    """
    It will start the survey questions and create a data list
    """
    while True:
        print("Enter your survey answers!\n")
        print("It is about Fifa World Cup 2022!\n")

        survey_info = []
        first_option = input("Which team would you like to win?\n")
        survey_info.append(first_option)
        second_option = input("Which would be your second option?\n")
        survey_info.append(second_option)
        good_surprise = input("Which team would be a great surprise?\n")
        survey_info.append(good_surprise)
        no_way = input("Which one you think has no chance?\n")
        survey_info.append(no_way)

        choices_ind = survey_info

        if validate_choices(choices_ind):
            print("Nice pick!\n")
            break
    
    return choices_ind

def validate_choices(values):
    """
    Inside the try, verify name entry
    Raises ValueError 
    """
    try:
        if len(values) != 4:
            raise ValueError(
                "These fields are required"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_choices_worksheet(ind):
    """
    Update choices worksheet, add new row with the list data provided
    """

    print("Updating people worksheet...\n")
    choices_worksheet = SHEET.worksheet("choices")
    choices_worksheet.append_row(ind)
    print("Choices worksheet updated successfully.\n")

def main():
    """
    Run all programm functions
    """
    data = get_people_data()
    people_data = [str.capitalize(char) for char in data]
    update_people_worksheet(people_data)
    ind = get_choices_ind()
    choices_ind = [str.capitalize(char) for char in ind]
    update_choices_worksheet(choices_ind)

print("Welcome to automation part\n")
main()
