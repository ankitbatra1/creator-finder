import json
import re


class YouTubeParser:

    def __init__(self, html: str):

        self.html = html

        self.data = self._extract_json()

    # =====================================================

    def _extract_json(self):

        patterns = [

            r"var ytInitialData = (.*?);</script>",

            r'window\["ytInitialData"\] = (.*?);</script>',

            r"ytInitialData = (.*?);</script>"

        ]

        for pattern in patterns:

            match = re.search(

                pattern,

                self.html,

                re.DOTALL

            )

            if match:

                try:

                    return json.loads(

                        match.group(1)

                    )

                except:

                    pass

        return {}

    # =====================================================

    def _walk(

        self,

        obj

    ):

        if isinstance(obj, dict):

            yield obj

            for value in obj.values():

                yield from self._walk(value)

        elif isinstance(obj, list):

            for item in obj:

                yield from self._walk(item)

    # =====================================================

    def all_channels(self):

        channels = {}

        for node in self._walk(self.data):

            renderer = node.get(

                "videoRenderer"

            )

            if renderer:

                owner = renderer.get(

                    "ownerText",

                    {}

                )

                runs = owner.get(

                    "runs",

                    []

                )

                if not runs:

                    continue

                run = runs[0]

                name = run.get(

                    "text",

                    ""

                )

                endpoint = run.get(

                    "navigationEndpoint",

                    {}

                )

                browse = endpoint.get(

                    "browseEndpoint",

                    {}

                )

                browse_id = browse.get(

                    "browseId",

                    ""

                )

                canonical = browse.get(

                    "canonicalBaseUrl",

                    ""

                )

                if canonical:

                    url = (

                        "https://www.youtube.com"

                        + canonical

                    )

                else:

                    url = (

                        "https://www.youtube.com/channel/"

                        + browse_id

                    )

                if browse_id:

                    channels[browse_id] = {

                        "channel_id": browse_id,

                        "channel_name": name,

                        "channel_url": url,

                        "source": "video"

                    }

        for node in self._walk(self.data):

            renderer = node.get(

                "channelRenderer"

            )

            if renderer is None:

                continue

            cid = renderer.get(

                "channelId",

                ""

            )

            name = renderer.get(

                "title",

                {}

            ).get(

                "simpleText",

                ""

            )

            canonical = renderer.get(

                "navigationEndpoint",

                {}

            ).get(

                "browseEndpoint",

                {}

            ).get(

                "canonicalBaseUrl",

                ""

            )

            if canonical:

                url = (

                    "https://www.youtube.com"

                    + canonical

                )

            else:

                url = (

                    "https://www.youtube.com/channel/"

                    + cid

                )

            if cid:

                channels[cid] = {

                    "channel_id": cid,

                    "channel_name": name,

                    "channel_url": url,

                    "source": "channel"

                }

        return list(

            channels.values()

        )