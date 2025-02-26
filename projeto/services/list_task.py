import json
import os

TAREFAS_JSON = "projeto/services/data/task.json"

# Função para carregar tarefas do JSON
def carregar_tarefas():
    if not os.path.exists(TAREFAS_JSON):  # Verifica se o arquivo existe
        return []
    
    with open(TAREFAS_JSON, "r", encoding="utf-8") as arquivo:
        try:
            tarefas = json.load(arquivo)  # Carrega os dados do JSON
            if not isinstance(tarefas, list):
                return []
            return tarefas
        except json.JSONDecodeError:
            return []  # Retorna uma lista vazia se houver erro no JSON

# Função para listar as tarefas carregadas do JSON
def ver_tarefas():  # Removido o argumento 'tarefas'
    tarefas = carregar_tarefas()  # Carrega as tarefas do arquivo JSON
    if not tarefas:
        print("\n📌 Nenhuma tarefa cadastrada!")
        return

    print("\n📋 Lista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
