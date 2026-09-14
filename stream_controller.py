
from models.stream_model import get_stream_data

def fetch_streams():
    streams = get_stream_data()

    return {
        "status": "success",
        "data": streams
    }