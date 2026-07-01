from itertools import product

from src.crawler.keyword_engine import KeywordEngine


class QueryGenerator:
    """
    Generates thousands of search queries
    from a small keyword list.
    """

    def __init__(self):

        self.engine = KeywordEngine()

        self.locations = [

            "india",

            "delhi",
            "mumbai",
            "bangalore",
            "hyderabad",
            "pune",
            "jaipur",
            "chandigarh",
            "lucknow",
            "patna",
            "kolkata",
            "surat",
            "ahmedabad",

            "punjab",
            "haryana",
            "rajasthan",
            "uttar pradesh",
            "bihar",
            "gujarat",
            "maharashtra",
            "madhya pradesh",
            "uttarakhand",
            "himachal"

        ]

        self.modifiers = [

            "",

            "girl",
            "boy",

            "hindi",

            "vlog",

            "daily",

            "new",

            "2026",

            "channel"

        ]

    # ====================================================

    def generate(self):

        queries = set()

        roots = self.engine.all_keywords()

        for root in roots:

            queries.add(root)

            for modifier in self.modifiers:

                if modifier:

                    queries.add(

                        f"{root} {modifier}"

                    )

            for location in self.locations:

                queries.add(

                    f"{root} {location}"

                )

            for location, modifier in product(

                self.locations,

                self.modifiers

            ):

                if modifier == "":

                    continue

                queries.add(

                    f"{root} {location} {modifier}"

                )

        return sorted(list(queries))

    # ====================================================

    def save(

        self,

        path="data/generated_queries.txt"

    ):

        queries = self.generate()

        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:

            for query in queries:

                f.write(query + "\n")

        return len(queries)