# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# import os.path
# import json
# from datetime import datetime
# from typing import Dict, Any, Optional
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class SheetsManager:
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
#     def __init__(self, spreadsheet_id: str, credentials_path: str = 'credentials.json'):
#         self.spreadsheet_id = spreadsheet_id
#         self.credentials_path = credentials_path
#         self.service = None
#         self._authenticate()

#     def _authenticate(self):
#         """Authenticate with Google Sheets API"""
#         creds = None
        
#         # Load credentials from token.json if it exists
#         if os.path.exists('token.json'):
#             with open('token.json', 'r') as token:
#                 creds = Credentials.from_authorized_user_info(json.load(token))

#         # If credentials are not valid, refresh or get new ones
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     self.credentials_path, self.SCOPES)
#                 creds = flow.run_local_server(port=0)
            
#             # Save credentials for future use
#             with open('token.json', 'w') as token:
#                 token.write(creds.to_json())

#         self.service = build('sheets', 'v4', credentials=creds)

#     def append_conversation(self, conversation_data: Dict[str, Any]) -> bool:
#         """Append conversation data to the spreadsheet"""
#         try:
#             # Format the data according to the required structure
#             values = [
#                 [
#                     conversation_data.get('modality', 'NA'),
#                     conversation_data.get('call_time', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
#                     conversation_data.get('phone_number', 'NA'),
#                     conversation_data.get('call_outcome', 'NA'),
#                     conversation_data.get('room_name', 'NA'),
#                     conversation_data.get('booking_date', 'NA'),
#                     conversation_data.get('booking_time', 'NA'),
#                     conversation_data.get('number_of_guests', 'NA'),
#                     conversation_data.get('call_summary', 'NA')
#                 ]
#             ]

#             body = {
#                 'values': values
#             }

#             # Append the data to the spreadsheet
#             result = self.service.spreadsheets().values().append(
#                 spreadsheetId=self.spreadsheet_id,
#                 range='Sheet1!A:I',  # Adjust range based on your sheet
#                 valueInputOption='RAW',
#                 insertDataOption='INSERT_ROWS',
#                 body=body
#             ).execute()

#             logger.info(f"Successfully logged conversation: {conversation_data.get('call_time')}")
#             return True

#         except Exception as e:
#             logger.error(f"Error logging conversation: {str(e)}")
#             # Implement error recovery mechanism
#             self._handle_logging_error(conversation_data)
#             return False

#     def _handle_logging_error(self, conversation_data: Dict[str, Any]):
#         """Handle logging errors by saving to a local file"""
#         try:
#             error_log_path = 'failed_logs.json'
#             failed_logs = []
            
#             # Load existing failed logs if any
#             if os.path.exists(error_log_path):
#                 with open(error_log_path, 'r') as f:
#                     failed_logs = json.load(f)
            
#             # Add timestamp to the failed log
#             conversation_data['failed_at'] = datetime.now().isoformat()
#             failed_logs.append(conversation_data)
            
#             # Save updated failed logs
#             with open(error_log_path, 'w') as f:
#                 json.dump(failed_logs, f, indent=2)
            
#             logger.info(f"Saved failed log to {error_log_path}")
            
#         except Exception as e:
#             logger.error(f"Error saving failed log: {str(e)}")

#     def retry_failed_logs(self) -> int:

#         try:
#             error_log_path = 'failed_logs.json'
#             if not os.path.exists(error_log_path):
#                 return 0

#             with open(error_log_path, 'r') as f:
#                 failed_logs = json.load(f)

#             successful_retries = 0
#             remaining_logs = []

#             for log in failed_logs:
#                 if self.append_conversation(log):
#                     successful_retries += 1
#                 else:
#                     remaining_logs.append(log)

#             # Update failed logs file with remaining logs
#             with open(error_log_path, 'w') as f:
#                 json.dump(remaining_logs, f, indent=2)

#             return successful_retries

#         except Exception as e:
#             logger.error(f"Error retrying failed logs: {str(e)}")
#             return 0