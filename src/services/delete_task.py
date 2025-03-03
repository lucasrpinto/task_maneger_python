import json
import os
from src.services.list_task import carregar_tarefas
from src.data.local_data import TAREFAS_JSON

def salvar_tarefas(tarefas):
  with open(TAREFAS_JSON, "w", encoding="utf-8") as arquivo:
    json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def excluir_tarefas( indice_tarefa ):
  tarefas = carregar_tarefas()
  
  if 0 <= indice_tarefa < len(tarefas):
    tarefa_removida = tarefas.pop(indice_tarefa)
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa '{tarefa_removida['tarefa']}' foi deletada com sucesso!")
  else:
    print("❌ Índice inválido! A tarefa não existe.")
