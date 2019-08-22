import string
import random
import click


@click.command()
@click.option(
    "--n", prompt="Number of characters", help="Inform number of characters", type=int
)
def main(n):
    def pw_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
        return "".join(random.choice(chars) for _ in range(size))

    try:
        print(pw_gen(n))
    except:
        print("\nERROR: Informe quantidade de caracteres")


if __name__ == "__main__":
    main()
