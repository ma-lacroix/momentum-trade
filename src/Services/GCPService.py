from src.Models.GCPRequest import GCPRequest
from src.Models.GCPResponse import GCPResponse
from src.Utils.functions import timeit


@timeit
def upload_df_to_bigquery(df, destination, write_type):
    request = GCPRequest(df, destination, write_type)
    request.to_gbq()


@timeit
def get_df_from_bigquery(query_string):
    response = GCPResponse(query_string)
    return response.data_frame

