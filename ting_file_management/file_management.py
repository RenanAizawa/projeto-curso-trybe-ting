import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file) as read_file:
            return read_file.read().split('\n')
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
