# Importacao das funcoes
from src.services.display_menu import exibir_menu
from src.services.add_task import adicionar_tarefa
from src.services.list_task import ver_tarefas
from src.services.update_task import atualizar_nome_tarefa
from src.services.update_task import completar_tarefa
from src.services.delete_task import excluir_tarefas

# Lista que armazena as tarefas
tarefas = []

# Definindo a primeira execucao
primeira_execucao = True

while True:
  if primeira_execucao:
    exibir_menu()
    primeira_execucao = False

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefa(nome_tarefa)

  elif escolha == "2":
    ver_tarefas()
  
  elif escolha == "3":
    ver_tarefas()  # Mostrar as tarefas antes da atualização
    try:
      indice = int(input("Qual tarefa deseja atualizar: ")) - 1
      novo_nome = input("Digite o novo nome da tarefa: ").strip()

      if indice < 0:
        print("❌ Índice inválido! Digite um número válido.")
      else:
        atualizar_nome_tarefa(indice, novo_nome)
    
    except ValueError:
      print("Entrada inválida! Digite um número.")

  elif escolha == "4":
    ver_tarefas()
    try:
      indice = int(input("Qual tarefa deseja completar: ")) - 1
      completar_tarefa(indice)
    except ValueError:
      print("Entrada inválida! Digite um número.")

  elif escolha == "5":
    ver_tarefas()
    try:
      indice = int(input("Digite a tarefa que deseja remover: ")) -1
      excluir_tarefas(indice)
    except ValueError:
      print("❌ Entrada inválida! Digite um número válido.")

  elif escolha == "6":
    break

  opcao = input("\nDeseja voltar ao menu inicial? (s/n): ").strip().lower()

  if opcao == "s":
    exibir_menu()
  elif opcao == "n":
    print("Programa finalizado.")
    break
  else:
    print("Opção inválida! Programa encerrado.")
    break



