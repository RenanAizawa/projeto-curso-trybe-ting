import pytest

from ting_file_management.priority_queue import PriorityQueue

mock_dt1 = {
  "nome_do_arquivo": "bela_adormecida.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
mock_dt2 = {
    "nome_do_arquivo": "branca_de_neve.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": [...]
}



def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    prt_queue = PriorityQueue()
    prt_queue.enqueue(mock_dt1)
    prt_queue.enqueue(mock_dt2)

    assert prt_queue.is_priority(mock_dt2) is False
    assert len(prt_queue) == 2

    procura = prt_queue.search(0)
    assert procura == mock_dt1

    prt_queue.dequeue()
    assert len(prt_queue) == 1
    assert 0 < len(prt_queue) <= 1

    with pytest.raises(IndexError):
        prt_queue.search(-1)
