import asyncio
import os

from tinkoff.invest import AsyncClient
from dotenv import load_dotenv, dotenv_values

load_dotenv()

TOKEN = os.getenv("INVEST_TOKEN")


async def main():
    async with AsyncClient(TOKEN) as client:
        accs = await client.users.get_accounts()
        print(accs.accounts[0])
        print(accs.accounts[1])
        accounts_id = [account.id for account in [accs.accounts[0], accs.accounts[1]]]

        response = await client.operations.get_positions(account_id=accounts_id[0])
        inst = await client.instruments.find_instrument(query=response.securities[1].figi)
        print(response.securities)
        print(inst.instruments[0].__dict__)
        price = await client.market_data.get_last_prices(figi=[inst.instruments[0].figi])
        print(price)



if __name__ == "__main__":
    asyncio.run(main())
