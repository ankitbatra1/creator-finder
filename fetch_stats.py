from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)

def get_channel_stats(channel_id):

    request = youtube.channels().list(
        part="statistics,snippet",
        id=channel_id
    )

    response = request.execute()

    if not response["items"]:
        return None

    item = response["items"][0]

    stats = item["statistics"]
    snippet = item["snippet"]

    return {
        "subscribers":
        int(stats.get("subscriberCount",0)),

        "total_views":
        int(stats.get("viewCount",0)),

        "video_count":
        int(stats.get("videoCount",0)),

        "country":
        snippet.get("country","")
    }