from googleapiclient.errors import HttpError

from src.api.api_manager import APIManager


class YouTubeAPI:

    def __init__(self):

        self.api = APIManager()

    # =====================================================

    def _execute(self, request):

        while True:

            try:

                return request.execute()

            except HttpError as e:

                status = getattr(e.resp, "status", None)

                if status == 403:

                    print("API quota reached. Rotating key...")

                    self.api.rotate()

                    continue

                raise

    # =====================================================

    def channel(self, channel_id: str):

        request = self.api.client().channels().list(

            part="snippet,statistics",

            id=channel_id

        )

        response = self._execute(request)

        items = response.get("items", [])

        if not items:
            return None

        item = items[0]

        snippet = item["snippet"]

        stats = item["statistics"]

        return {

            "channel_id": item["id"],

            "title": snippet.get("title", ""),

            "description": snippet.get("description", ""),

            "country": snippet.get("country", ""),

            "published_at": snippet.get("publishedAt", ""),

            "custom_url": snippet.get("customUrl", ""),

            "subscriber_count": int(
                stats.get("subscriberCount", 0)
            ),

            "view_count": int(
                stats.get("viewCount", 0)
            ),

            "video_count": int(
                stats.get("videoCount", 0)
            )

        }

    # =====================================================

    def channels(self, ids):

        ids = list(set(ids))

        results = []

        for i in range(0, len(ids), 50):

            batch = ids[i:i + 50]

            request = self.api.client().channels().list(

                part="snippet,statistics",

                id=",".join(batch)

            )

            response = self._execute(request)

            for item in response.get("items", []):

                snippet = item["snippet"]

                stats = item["statistics"]

                results.append({

                    "channel_id": item["id"],

                    "title": snippet.get("title", ""),

                    "description": snippet.get("description", ""),

                    "country": snippet.get("country", ""),

                    "published_at": snippet.get("publishedAt", ""),

                    "custom_url": snippet.get("customUrl", ""),

                    "subscriber_count": int(
                        stats.get("subscriberCount", 0)
                    ),

                    "view_count": int(
                        stats.get("viewCount", 0)
                    ),

                    "video_count": int(
                        stats.get("videoCount", 0)
                    )

                })

        return results