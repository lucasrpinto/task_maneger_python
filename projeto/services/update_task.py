from services.list_task import carregar_tarefas

import json
import os

TAREFAS_JSON = "projeto/services/data/task.json"



def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
  print(f"Tarefa {indice_tarefa} atualizada para {novo_nome}")
  return