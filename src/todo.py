# src/todo.py

class ToDoList:
    """
    Classe simples para gerenciar uma lista de tarefas.

    Cada tarefa é representada por um dicionário com:
    - 'titulo': texto da tarefa
    - 'status': 'pendente' ou 'concluida'
    """

    def __init__(self):
        # Lista interna de tarefas
        self._tarefas = []

    def adicionar_tarefa(self, titulo: str) -> None:
        """
        Adiciona uma nova tarefa com o título informado.

        Na fase GREEN, fazemos o mínimo necessário para o teste passar.
        """
        tarefa = {
            "titulo": titulo,
            "status": "pendente",
        }
        self._tarefas.append(tarefa)

    def listar_tarefas(self):
        """
        Retorna a lista de tarefas.
        Por enquanto, retornamos diretamente.
        Podemos melhorar isso depois no REFACTOR.
        """
        return self._tarefas
