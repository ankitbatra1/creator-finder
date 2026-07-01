import re


class PhoneExtractor:
    """
    Extracts phone numbers from text.
    Primarily optimized for Indian mobile numbers.
    """

    PHONE_PATTERNS = [

        # +91 9876543210
        r"\+91[\s\-]?[6-9]\d{9}",

        # 91 9876543210
        r"\b91[\s\-]?[6-9]\d{9}\b",

        # 9876543210
        r"\b[6-9]\d{9}\b",

        # (987) 654-3210 style
        r"\(\d{3}\)\s*\d{3}[-\s]?\d{4}",

        # Generic international
        r"\+\d{1,3}[\s\-]?\d{6,14}"

    ]

    # =====================================================

    @classmethod
    def extract(cls, text: str):

        if not text:
            return []

        phones = set()

        for pattern in cls.PHONE_PATTERNS:

            matches = re.findall(

                pattern,

                text,

                flags=re.IGNORECASE

            )

            for phone in matches:

                number = re.sub(

                    r"\D",

                    "",

                    phone

                )

                # Remove country code if present

                if number.startswith("91") and len(number) == 12:

                    number = number[2:]

                # Keep only valid Indian mobile numbers

                if len(number) == 10 and number[0] in "6789":

                    phones.add(number)

                # Keep international numbers

                elif len(number) > 10:

                    phones.add(number)

        return sorted(phones)

    # =====================================================

    @classmethod
    def first(cls, text: str):

        phones = cls.extract(text)

        if phones:

            return phones[0]

        return ""