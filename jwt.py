import sys
import base64
import click


@click.command()
@click.option("--token", prompt="Token", help="Inform token")
def main(token):
    try:
        h, d, s = tuple(
            [
                base64.urlsafe_b64decode(x + "========").decode(
                    "utf-8", errors="ignore"
                )
                for x in token.rsplit(".")
            ]
        )
        print(f"\n{h}\n{d}\n{s}")
    except:
        print("\nERROR: Informe o token JWT")


if __name__ == "__main__":
    main()
