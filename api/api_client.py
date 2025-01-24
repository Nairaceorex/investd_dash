import os

from aiohttp.log import client_logger
from tinkoff.invest import Client, GetAccountsResponse
from tinkoff.invest.schemas import PortfolioResponse
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("INVEST_TOKEN")  # Укажите API-ключ


class TinkoffAPIClient:
    def __init__(self, token: str):
        self.token = token

    def get_accounts(self) -> GetAccountsResponse:
        with Client(self.token) as client:
            accounts = client.users.get_accounts()


            return accounts
    def get_portfolios(self,accounts: GetAccountsResponse) -> list[PortfolioResponse]:
        with Client(self.token) as client:
            portfolios = client.operations.get_portfolio(account_id=accounts.accounts[0].id)
            portfolios = [client.operations.get_portfolio(account_id=account.id) for account in self.get_accounts().accounts]

            return portfolios


cli = TinkoffAPIClient(TOKEN)
accs = cli.get_accounts()
print(accs)
print(cli.get_portfolios(accs)[1])