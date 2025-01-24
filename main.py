import os
from dotenv import load_dotenv, dotenv_values
from api.api_client import TinkoffAPIClient

load_dotenv()

TOKEN = os.getenv("INVEST_TOKEN")


def main():
    try:
        cli = TinkoffAPIClient(TOKEN)
        accounts = cli.get_accounts()
        print(cli.get_portfolios(accounts))
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
