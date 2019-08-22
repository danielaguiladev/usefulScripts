import requests
import sys
import json
import click


@click.command()
@click.option(
    "--value", prompt="Value", help="Inform how much to convert with fees", type=float
)
def main(value):
    def percentage(percent, whole):
        return (percent * whole) / 100.0

    re = requests.get("http://economia.awesomeapi.com.br/json/USDT-BRL")
    dolar = float(json.loads(re.content)[0]["ask"])
    try:
        print(f"\nDolar hoje: R$ {dolar}\n")
        value += percentage(7, value)
        print(f"\nR$ {value} + 7% = " + "R$ %.2f" % value)
        value = value * dolar
        print(f"\nR$ %.2f * dolar (R$ {dolar}) = " % value + "R$ %.2f" % value)
        final = percentage(6.379, value) + value
        print(f"\nR$ %.2f + 6,379%% = " % value + "R$ %.2f" % final)
        print("\nTotal a ser pago: R$ %.2f" % final)
    except:
        print(f"Dolar hoje: R$ {dolar}\n")
        print(
            "valor para conversao nao informado\
			\nOu talvez o valor informado esta com , e nao com ."
        )
        sys.exit()


if __name__ == "__main__":
    main()
