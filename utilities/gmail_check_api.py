import base64
import os.path
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main(address):
  """
  Returns activation link from the newest mail from looktv@info
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        str(address), SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  # -------------------------------------------------------------------------------------------------------------------
  try:
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(userId="me", q=" in:anywhere from:(info@looktv.mn) newer_than:1d", maxResults=1).execute()
    print(results)
    if not results['resultSizeEstimate']:    #if there is no email for the filter
      print("No result found.")
      return None

    message_ids = []
    print("Results:", results)

    for i in results['messages']:
      # print(i['id']) # print m_id
      message_ids.append(i['id'])

    for ids in message_ids:
      message = service.users().messages().get(userId='me', id=ids, format='full').execute()

      message_body = message['payload']
      # print("message_body: ", message_body)

      if not message_body['body']:
        print("No body found.")
        return "No body found"

      body_data = message_body['body']['data']
      # print(body_data)
      body_text = base64.urlsafe_b64decode(body_data.encode('ASCII')).decode('utf-8')
      # print(body_text)

      pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
      links = re.findall(pattern, body_text)
      print(links[0])
      return links[0]    # maileer irsen linkee butsaana

  except HttpError as error:
    print(f"An error occurred: {error}")

  # -------------------------------------------------------------------------------------------------------------------
