import os
import click


@click.command()
@click.option("-cmd", required=False)
@click.option("-taskmgr", required=False)
@click.option("-regedit", required=False)
@click.option("-variables", required=False)
def main(cmd, taskmgr, regedit, variables):
    if cmd:
        os.system("PsExec.exe -s -i -d cmd.exe")
    elif taskmgr:
        os.system("PsExec.exe -s -i -d taskmgr")
    elif regedit:
        os.system("PsExec.exe -s -i -d regedit")
    elif variables:
        os.system("rundll32 sysdm.cpl,EditEnvironmentVariables")


if __name__ == "__main__":
    main()
