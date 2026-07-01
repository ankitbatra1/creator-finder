import argparse
import asyncio
import sys

from src.services.discovery_service import DiscoveryService


async def run_discover(args):

    service = DiscoveryService()

    await service.run(

        limit=args.limit,

        workers=args.workers

    )


async def main():

    parser = argparse.ArgumentParser(
        prog="Creator Finder"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ------------------------------------------------------

    discover = subparsers.add_parser(
        "discover",
        help="Discover YouTube creators"
    )

    discover.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum creators to collect"
    )

    discover.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Concurrent browser workers"
    )

    # ------------------------------------------------------

    contacts = subparsers.add_parser(
        "contacts",
        help="Collect creator contacts"
    )

    contacts.add_argument(
        "--limit",
        type=int,
        default=100
    )

    # ------------------------------------------------------

    export = subparsers.add_parser(
        "export",
        help="Export CSV"
    )

    # ------------------------------------------------------

    full = subparsers.add_parser(
        "full",
        help="Run complete pipeline"
    )

    full.add_argument(
        "--limit",
        type=int,
        default=100
    )

    # ------------------------------------------------------

    args = parser.parse_args()

    if args.command == "discover":

        await run_discover(args)

    elif args.command == "contacts":

        print("Contacts module not implemented yet.")

    elif args.command == "export":

        print("Export module not implemented yet.")

    elif args.command == "full":

        await run_discover(args)

        print("\nContacts module not implemented.")

        print("Export module not implemented.")

    else:

        parser.print_help()

        sys.exit(1)


if __name__ == "__main__":

    asyncio.run(main())