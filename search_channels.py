from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)

def search_channels(keyword,max_results=50):

    channels=[]

    request = youtube.search().list(
        q=keyword,
        part="snippet",
        maxResults=max_results,
        type="channel"
    )

    response=request.execute()

    for item in response["items"]:

        channels.append({
            "channel_id":
            item["snippet"]["channelId"],

            "channel_name":
            item["snippet"]["title"]
        })

    return channels