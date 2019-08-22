import os
import sys
import click


@click.command()
@click.option("--url", prompt="Url", help="Inform url to scan")
def main(url):
    try:
        os.system(f"docker run --rm -t isona/dirble {url}")
    except:
        os.system("docker run --rm -t isona/dirble --help")


if __name__ == "__main__":
    main()
