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
        titulo_normalizado = titulo.strip()

        if not titulo_normalizado:
            raise ValueError("Título da tarefa não pode ser vazio.")

        for tarefa in self._tarefas:
            if tarefa["titulo"] == titulo_normalizado:
                raise ValueError("Já existe uma tarefa com esse título.")

        tarefa = {
            "titulo": titulo_normalizado,
            "status": "pendente",
        }
        self._tarefas.append(tarefa)

    def listar_tarefas(self):
        """
        Retorna uma cópia da lista de tarefas.
        """
        return list(self._tarefas)

    def concluir_tarefa(self, titulo: str) -> None:
        """
        Marca uma tarefa como concluída, alterando o status para 'concluida'.

        Se não encontrar a tarefa, não faz nada (para manter simples).
        """
        titulo_normalizado = titulo.strip()

        for tarefa in self._tarefas:
            if tarefa["titulo"] == titulo_normalizado:
                tarefa["status"] = "concluida"
                return
