import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)

filename = "GmailCredentials"
spreadsheet = client.open(filename)
worksheet = spreadsheet.sheet1
