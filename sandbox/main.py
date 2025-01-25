from sandbox.client.sandbox_api_client import TAPISandboxClient
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SANDBOX_INVEST_TOKEN")


def main() -> None:
    try:
        cli = TAPISandboxClient(TOKEN)
        account = cli.get_accounts().accounts[0]
        print(cli.get_account(account_id=f'{account.id}'))
        print(cli.get_portfolio(account_id=f'{account.id}'))
    except Exception as e:
        print(f"Error^ {e}")


if __name__ == '__main__':
    main()
