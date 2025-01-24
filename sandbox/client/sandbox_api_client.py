from decimal import Decimal

from tinkoff.invest import MoneyValue, GetAccountsResponse, SandboxPayInResponse, GetInfoResponse, \
    OpenSandboxAccountResponse, Account, PortfolioResponse
from tinkoff.invest.sandbox.client import SandboxClient

from tinkoff.invest.utils import decimal_to_quotation


class TAPISandboxClient:
    def __init__(self, token: str):
        self.token = token

    def create_account(self, name: str) -> OpenSandboxAccountResponse:
        with SandboxClient(self.token) as client:
            account = client.sandbox.open_sandbox_account(name=f"{name}")

            return account

    def add_money_sandbox(self, account_id: str, money: int, currency: str = "rub") -> SandboxPayInResponse:
        with SandboxClient(self.token) as client:
            money = decimal_to_quotation(Decimal(money))
            return client.sandbox.sandbox_pay_in(
                account_id=account_id,
                amount=MoneyValue(units=money.units, nano=money.nano, currency=currency),
            )

    def get_accounts(self) -> GetAccountsResponse:
        with SandboxClient(self.token) as client:
            return client.users.get_accounts()

    def get_account(self, account_id: str) -> Account | None:
        with SandboxClient(self.token) as client:
            return next((account for account in self.get_accounts().accounts if account.id == account_id), None)

    def get_portfolio(self, account_id: str) ->  PortfolioResponse:
        with SandboxClient(self.token) as client:
            return client.sandbox.get_sandbox_portfolio(account_id=account_id)

    def get_info(self) -> GetInfoResponse:
        with SandboxClient(self.token) as client:
            return client.users.get_info()
