import re


class EmailExtractor:

    EMAIL_PATTERN = re.compile(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )

    @classmethod
    def extract(cls, text: str):

        if not text:
            return []

        emails = cls.EMAIL_PATTERN.findall(text)

        cleaned = []

        for email in emails:

            email = email.lower().strip()

            if email.endswith(".png"):
                continue

            if email.endswith(".jpg"):
                continue

            if email.endswith(".jpeg"):
                continue

            if email.endswith(".webp"):
                continue

            if "example" in email:
                continue

            cleaned.append(email)

        return sorted(list(set(cleaned)))

    @classmethod
    def first(cls, text: str):

        emails = cls.extract(text)

        if emails:

            return emails[0]

        return ""