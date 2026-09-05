import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Tarefa: ")
        socket.send_string(f"ADD {tarefa}")

    elif op == "2":
        indice = input("Número da tarefa: ")
        socket.send_string(f"REMOVE {indice}")

    elif op == "3":
        socket.send_string("LIST")

    elif op == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
        continue

    resposta = socket.recv_string()
    print("\nResposta do servidor:")
    print(resposta)
