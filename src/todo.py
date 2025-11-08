# src/todo.py

class ToDoList:
    """
    Gerenciador simples de tarefas.

    Regras:
    - Não permite tarefa sem título.
    - Não permite título duplicado.
    """

    def __init__(self):
        # Lista interna de tarefas
        self._tarefas = []

    def adicionar_tarefa(self, titulo: str) -> None:
        """
        Adiciona uma nova tarefa com o título informado.

        Regras de validação:
        - Título não pode ser vazio ou só espaços.
        - Não permite duas tarefas com o mesmo título.
        """
        # Remove espaços do início e do fim
        titulo_normalizado = titulo.strip()

        # Verifica se o título está vazio
        if not titulo_normalizado:
            raise ValueError("Título da tarefa não pode ser vazio.")

        # Verifica se já existe tarefa com o mesmo título
        for tarefa in self._tarefas:
            if tarefa["titulo"] == titulo_normalizado:
                raise ValueError("Já existe uma tarefa com esse título.")

        # Se passou nas validações, adiciona a nova tarefa
        tarefa = {
            "titulo": titulo_normalizado,
            "status": "pendente",
        }
        self._tarefas.append(tarefa)

    def listar_tarefas(self):
        """
        Retorna uma cópia da lista de tarefas.
        Usamos list(...) para evitar que o código de fora
        modifique a lista interna diretamente.
        """
        return list(self._tarefas)
