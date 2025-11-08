# tests/test_todo.py

import os
import sys

# Garante que a pasta raiz do projeto entre no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.todo import ToDoList


def test_adicionar_tarefa_cria_uma_tarefa():
    """
    Cenário de teste:
    - Quando eu adiciono uma tarefa com um título
    - Então a lista deve ter 1 tarefa com esse título
    - E o status deve ser 'pendente'
    """
    lista = ToDoList()
    lista.adicionar_tarefa("Estudar TDD")

    tarefas = lista.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar TDD"
    assert tarefas[0]["status"] == "pendente"


def test_concluir_tarefa_muda_status_para_concluida():
    """
    Cenário:
    - Tenho uma tarefa pendente
    - Quando concluo essa tarefa
    - Então o status dela deve mudar para 'concluida'
    """
    lista = ToDoList()
    lista.adicionar_tarefa("Estudar pytest")

    lista.concluir_tarefa("Estudar pytest")

    tarefas = lista.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar pytest"
    assert tarefas[0]["status"] == "concluida"

def test_remover_tarefa_remove_da_lista():
    """
    Cenário:
    - Tenho duas tarefas
    - Quando removo uma pelo título
    - Então ela não deve mais aparecer na lista
    """
    lista = ToDoList()
    lista.adicionar_tarefa("Lavar a louça")
    lista.adicionar_tarefa("Estudar TDD")

    lista.remover_tarefa("Lavar a louça")

    titulos = [t["titulo"] for t in lista.listar_tarefas()]
    assert "Lavar a louça" not in titulos
    assert "Estudar TDD" in titulos
