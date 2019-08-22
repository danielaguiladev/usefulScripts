import random
import sys
import click


@click.command()
@click.option(
    "--n",
    prompt="Number of cnpj's to gerenate",
    help="Inform number of cnpj's to generate",
    default=1,
)
def main(n):
    def cnpj():
        n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)

    cnpjs = []
    try:
        for i in range(n):
            c = cnpj()
            if c not in cnpjs:
                cnpjs.append(c)
        print("\n".join(cnpjs))
    except:
        print("\nERROR: Informe quantidade de cnpjs para gerar")


if __name__ == "__main__":
    main()
