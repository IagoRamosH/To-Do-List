# tests/test_todo.py

import os
import sys

# Adiciona a pasta raiz do projeto no sys.path
# Assim o Python consegue encontrar o pacote "src"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.todo import ToDoList


def test_adicionar_tarefa_cria_uma_tarefa():
    """
    Cenário de teste:
    - Quando eu adiciono uma tarefa com um título
    - Então a lista deve ter 1 tarefa com esse título
    - E o status deve ser 'pendente'
    """
    lista = ToDoList()  # esse é o objeto que vamos implementar em src/todo.py
    lista.adicionar_tarefa("Estudar TDD")

    tarefas = lista.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar TDD"
    assert tarefas[0]["status"] == "pendente"
