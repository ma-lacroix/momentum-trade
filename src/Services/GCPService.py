from src.Models.GCPRequest import GCPRequest
from src.Models.GCPResponse import GCPResponse


def upload_df_to_bigquery(df, destination):
    request = GCPRequest(df, destination)
    request.to_gbq()


def get_df_from_bigquery(query_string):
    response = GCPResponse(query_string)
    return response.data_frame

