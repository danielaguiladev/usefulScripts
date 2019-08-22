import datetime
import click


@click.command()
@click.option("--s", prompt="Seconds", help="Inform seconds to convert", type=int)
def main(s):
    try:
        print(str(datetime.timedelta(seconds=s)))
    except:
        print("\nERROR: Informe segundos para converter")


if __name__ == "__main__":
    main()
