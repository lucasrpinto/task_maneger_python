import json
import os
from src.services.list_task import carregar_tarefas
from src.data.local_data import TAREFAS_JSON

# Criar a pasta `data/` se não existir
if not os.path.exists("projeto/services/data"):
    os.makedirs("projeto/services/data")

# Criar o arquivo JSON se não existir ou se estiver vazio
if not os.path.exists(TAREFAS_JSON):
    with open(TAREFAS_JSON, "w", encoding="utf-8") as arquivo:
        json.dump([], arquivo)  # Cria um JSON vazio apenas se não existir

# Função para salvar tarefas no JSON
def salvar_tarefas(tarefas):
    with open(TAREFAS_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

# Função para adicionar uma nova tarefa ao JSON
def adicionar_tarefa(nome_tarefa): 
    tarefas = carregar_tarefas()  # Carrega as tarefas do JSON
    nova_tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)  # Salva no JSON
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
