# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

ANSW = Credentials.from_service_account_file('answ.json')
SCOPED_ANSW = ANSW.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_ANSW)
SHEET = GSPREAD_CLIENT.open('wcup_survey')