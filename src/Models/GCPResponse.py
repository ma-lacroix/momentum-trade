from src.Clients.GCPClient import GCPClient
import pandas as pd


class GCPResponse:

    def __init__(self, query_string) -> None:
        self.query = query_string
        self.client = GCPClient()
        self.data_frame = self.from_gbq()

    def from_gbq(self):
        return pd.read_gbq(query=self.query, project_id=self.client.project_id,
                           credentials=self.client.creds)

