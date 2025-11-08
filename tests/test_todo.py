import pytest
from src.todo import ToDoList


def test_adicionar_tarefa_cria_uma_tarefa():
    """
    Cenário de teste:
    - Quando eu adiciono uma tarefa com um título
    - Então a lista deve ter 1 tarefa com esse título
    - E o status deve ser 'pendente'
    """
    lista = ToDoList()  # ainda não existe -> esse é o RED
    lista.adicionar_tarefa("Estudar TDD")

    tarefas = lista.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar TDD"
    assert tarefas[0]["status"] == "pendente"
