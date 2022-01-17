from src.Clients.GCPClient import GCPClient
import pandas_gbq


class GCPRequest:

    def __init__(self, df, destination_table) -> None:
        self.destination_table = destination_table
        self.client = GCPClient()
        self.data_frame = df

    def to_gbq(self):
        pandas_gbq.to_gbq(self.data_frame, destination_table=self.destination_table,
                          project_id=self.client.project_id, credentials=self.client.creds,
                          if_exists="replace")
