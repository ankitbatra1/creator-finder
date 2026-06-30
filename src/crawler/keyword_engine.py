import json

from config import KEYWORDS_PATH


class KeywordEngine:

    def __init__(self):

        with open(
            KEYWORDS_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

    # =====================================================

    def all_keywords(self):

        keywords = []

        for category in self.data.values():

            for language in category.values():

                keywords.extend(language)

        return sorted(

            list(set(keywords))

        )

    # =====================================================

    def category_keywords(

        self,

        category_name

    ):

        if category_name not in self.data:

            return []

        keywords = []

        category = self.data[category_name]

        for language in category.values():

            keywords.extend(language)

        return sorted(

            list(set(keywords))

        )