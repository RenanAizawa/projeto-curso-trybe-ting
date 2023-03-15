import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    file_read = txt_importer(path_file)
    add_obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_read),
        "linhas_do_arquivo": file_read
    }
    for file in instance._data:
        if file['nome_do_arquivo'] == path_file:
            return None
    print(add_obj, file=sys.stdout)
    instance.enqueue(add_obj)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return print('Não há elementos', file=sys.stdout)
    else:
        path_file = instance.dequeue()['nome_do_arquivo']
        return print(
            f" Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        procurado = instance.search(position)
        return print(procurado, file=sys.stdout)
    except IndexError:
        return print('Posição inválida', file=sys.stderr)
