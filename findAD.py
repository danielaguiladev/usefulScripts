import os
import sys
import click


@click.command()
@click.option("--domain", prompt="Domain", help="Inform domain")
def main(domain):
    try:
        os.system(f"nltest /dclist:{domain}")
    except:
        print("DAMN! Informe o dominio")


if __name__ == "__main__":
    main()
