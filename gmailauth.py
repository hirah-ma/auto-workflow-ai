import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# # import os.path
# # import pickle
# # from google.auth.transport.requests import Request
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from googleapiclient.discovery import build

# # # Scope to read Gmail metadata
# # SCOPES = [
# #     'https://www.googleapis.com/auth/gmail.readonly',
# #     'https://www.googleapis.com/auth/spreadsheets',
# #     'https://www.googleapis.com/auth/calendar'
# # ]

# def main():
#     creds = None
#     token_file = 'token.pickle'

#     # Load saved token if available
#     if os.path.exists(token_file):
#         with open(token_file, 'rb') as token:
#             creds = pickle.load(token)

#     # If no valid creds, log in
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)

#         # Save credentials for next run
#         with open(token_file, 'wb') as token:
#             pickle.dump(creds, token)

#     # Access Gmail
#     service = build('gmail', 'v1', credentials=creds)

#     # Get list of labels
#     results = service.users().labels().list(userId='me').execute()
#     labels = results.get('labels', [])

#     print("Labels:")
#     for label in labels:
#         print(f"- {label['name']}")

# if __name__ == '__main__':
#     main()

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]

def get_credentials():
    creds = None
    token_file = 'token.pickle'

    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    
    return creds
