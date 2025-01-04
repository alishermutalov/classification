import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def save_to_gsheet(data, initiated_by):
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    client = gspread.authorize(credentials)
    spreadsheet = client.open('Being Classification Data')
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    
    if data['type']=='Human':
        worksheet = spreadsheet.worksheet('Human')
        new_row = list(data.values())
        new_row.append(initiated_by)
        new_row.append(formatted_date)
        worksheet.append_row(new_row)
    elif data['type']=='Animal':
        worksheet = spreadsheet.worksheet('Animal')
        new_row = list(data.values())
        new_row.append(initiated_by)
        new_row.append(formatted_date)
        worksheet.append_row(new_row)
    else:
        worksheet = spreadsheet.worksheet('Alien')
        new_row = list(data.values())
        new_row.append(initiated_by)
        new_row.append(formatted_date)
        worksheet.append_row(new_row)

