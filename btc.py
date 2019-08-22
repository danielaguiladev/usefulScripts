import requests
import json
import time
import os
import click


@click.command()
@click.option("--date", prompt="Date", help="YYYY/MM/DD")
def main(date):
    while True:
        data = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker")
        resumo = requests.get(
            f"https://www.mercadobitcoin.net/api/BTC/day-summary/{date}"
        )
        data = json.loads(data.text)
        resumo = json.loads(resumo.text)
        os.system("cls")
        print(f"MAIOR: R${resumo['highest']}.00")
        print(f"MENOR: R${resumo['lowest']}.00")
        print(f"ATUAL: R${data['ticker']['last'][:-6]}")
        time.sleep(30)


if __name__ == "__main__":
    main()
