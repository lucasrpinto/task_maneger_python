from src.services.list_task import carregar_tarefas
from src.data.local_data import TAREFAS_JSON

import json
import os

def salvar_tarefas(tarefas):
  with open(TAREFAS_JSON, "w", encoding="utf-8") as arquivo:
    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def atualizar_nome_tarefa( indice_tarefa, novo_nome):
  tarefas = carregar_tarefas()

  if 0 <= indice_tarefa < len(tarefas):
    tarefas[indice_tarefa]["tarefa"] = novo_nome
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa {indice_tarefa + 1} atualizada para '{novo_nome}' com sucesso!")
  else:
    print("❌ Índice inválido! A tarefa não existe.")