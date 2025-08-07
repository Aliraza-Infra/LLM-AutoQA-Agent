import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_tasks_from_sheets(sheet_url: str, worksheet_name: str = "Sheet1") -> list:
    """
    Load prompt-response pairs from a Google Sheet
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(worksheet_name)
    data = worksheet.get_all_records()

    return [{"prompt": row["prompt"], "response": row["response"]} for row in data]
