from googleapiclient.discovery import build
from datetime import datetime
import os
from dotenv import load_dotenv
import gmailauth
from gmailauth import get_credentials

load_dotenv()
creds = get_credentials()
print("Loaded SHEET_ID:", os.getenv("SHEET_ID"))


def read_sheet(creds, spreadsheet_id, range_name='Sheet1!A1:D10'):
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name
    ).execute()

    rows = result.get('values', [])
    for row in rows:
        print(row)

def get_upcoming_events(creds):
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=5, singleEvents=True, orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start}: {event.get('summary', 'No title')}")

def list_unread_emails(creds):
    gmail_service = build('gmail', 'v1', credentials=creds)
    results = gmail_service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No unread messages.")
    else:
        print("Unread emails:")
        for msg in messages:
            msg_data = gmail_service.users().messages().get(userId='me', id=msg['id']).execute()
            subject = next(header['value'] for header in msg_data['payload']['headers'] if header['name'] == 'Subject')
            print(f"- {subject}")

list_unread_emails(creds)

# Calendar
get_upcoming_events(creds)

# Sheets
read_sheet(creds, spreadsheet_id=os.getenv("SHEET_ID"))