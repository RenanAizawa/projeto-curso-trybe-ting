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

    for num in range(len(instance) - 1):
        if instance.search(num)['nome_do_arquivo'] == path_file:
            return None

    instance.enqueue(add_obj)

def remove(instance: Queue):
    """Aqui irá sua implementação"""


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
