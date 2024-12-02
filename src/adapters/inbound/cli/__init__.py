import asyncio

from src.adapters.inbound.cli.users import get_users

if __name__ == "__main__":
    users = asyncio.get_event_loop().run_until_complete(get_users())
    print(users)
