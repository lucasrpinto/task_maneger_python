# Importacao das funcoes
from services.display_menu import exibir_menu
from services.add_task import adicionar_tarefa
from services.list_task import ver_tarefas

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



