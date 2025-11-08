# 📝 To-Do List – Atividade TDD

## 🎯 Projeto escolhido
Gerenciador de Tarefas (To-Do List)

## 💻 Linguagem e Ferramenta de Teste
- Python  
- Pytest  

## 🧱 Estrutura do Projeto

To-Do-List/
│
├── src/
│ ├── init.py
│ └── todo.py
│
├── tests/
│ └── test_todo.py
│
├── venv/
├── README.md
└── requirements.txt



## 🧪 Como executar os testes

```bash
# 1. Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar os testes
pytest

✅ Funcionalidades Implementadas

Criar tarefa (com título obrigatório e sem duplicidade)

Listar tarefas

Concluir tarefa

Remover tarefa

🔄 Ciclo TDD Seguido

RED → Criação de um teste que falha.

GREEN → Implementação do código mínimo para o teste passar.

REFACTOR → Melhoria do código mantendo todos os testes passando.

Cada commit representa uma etapa do ciclo TDD.