import os
import json

from google.auth.transport import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def authorize() -> Credentials:
    """Ensure valid credentials for calling the Meet REST API."""
    CLIENT_SECRET_FILE = "./client_secret.json"
    credentials = None

    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json')

    if credentials is None:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=[
                'https://www.googleapis.com/auth/meetings.space.created',
            ])
        flow.run_local_server(port=0)
        credentials = flow.credentials

    if credentials and credentials.expired:
        credentials.refresh(requests.Request())

    if credentials is not None:
        with open("token.json", "w") as f:
            f.write(credentials.to_json())

    return credentials

USER_CREDENTIALS = authorize()

#if __name__ == "__main__":
    #main()