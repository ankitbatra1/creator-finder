from src.crawler.contact_manager import ContactManager

from src.database.channel_repository import ChannelRepository

from src.database.contact_repository import ContactRepository


class ContactService:

    def __init__(

        self,

        browser,

        db

    ):

        self.manager = ContactManager(

            browser

        )

        self.channels = ChannelRepository(

            db

        )

        self.contacts = ContactRepository(

            db

        )

    # =====================================================

    async def run(self):

        pending = self.channels.get_unprocessed()

        print()

        print(

            f"Channels : {len(pending)}"

        )

        print()

        for i, channel in enumerate(

            pending,

            start=1

        ):

            print(

                "=" * 60

            )

            print(

                f"{i}/{len(pending)}"

            )

            print(

                channel["channel_name"]

            )

            data = await self.manager.scrape(

                dict(channel)

            )

            data["channel_id"] = channel["channel_id"]

            self.contacts.save(

                data

            )

            self.channels.mark_processed(

                channel["channel_id"]

            )

            print(

                "Email :",

                data.get(

                    "final_email",

                    ""

                )

            )

            print(

                "Phone :",

                data.get(

                    "final_phone",

                    ""

                )

            )

        print()

        print(

            "Finished."

        )