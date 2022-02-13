import json
import os
from google.oauth2 import service_account


class GCPClient:

    def __init__(self):
        self.key = os.environ['gcp_key']  # GCP SA
        self.project_id = self.get_project()
        self.creds = self.get_creds()

    def get_project(self):
        with open(self.key) as f:
            project_id = json.load(f)['project_id']
            print(project_id)
        f.close()
        return project_id

    def get_creds(self):
        creds = service_account.Credentials.from_service_account_file(self.key)
        return creds
