import json
from google.cloud import bigquery
from google.oauth2 import service_account

class GCPRequest:

    def __init__(self) -> None:
        self.key = 'key/key.json' # GCP SA
        self.project_id = self.get_project()
        self.client = self.get_client()
        # TODO: bigQuery query requests
    
    def get_project(self):
        with open(self.key) as f:
            project_id = json.load(f)['project_id']
            print(project_id)
        f.close()
        return project_id
    
    def get_client(self):
        client = service_account.Credentials.from_service_account_file(self.key)
        return client
