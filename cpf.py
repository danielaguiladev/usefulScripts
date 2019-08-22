import random
import sys
import click


@click.command()
@click.option(
    "--n",
    prompt="Number of cpf's to gerenate",
    help="Inform number of cpf's to generate",
    default=1,
)
def main(n):
    def cpf_funcional():
        n = [random.randrange(10) for i in range(9)]

        # calcula digito 1 e acrescenta ao numero
        s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
        d1 = 11 - s % 11
        if d1 >= 10:
            d1 = 0
        n.append(d1)

        # calcula digito 2 e acrescenta ao numero
        s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
        d2 = 11 - s % 11
        if d2 >= 10:
            d2 = 0
        n.append(d2)
        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

    cpfs = []
    try:
        for x in range(n):
            c = cpf_funcional()
            if c not in cpfs:
                cpfs.append(c)
                print(c)
    except:
        print("\nERROR: Informe quantidade de cpfs para gerar")


if __name__ == "__main__":
    main()
