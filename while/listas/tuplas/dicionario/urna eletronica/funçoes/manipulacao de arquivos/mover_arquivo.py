from shutil import move

def mover_arquivo():
    move('teste.txt', 'docs/teste.txt')


def main():
    mover_arquivo()


main()

    