import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

tarefas = []

print("Servidor iniciado.", flush=True)

while True:

    mensagem = socket.recv_string()

    partes = mensagem.split(" ", 1)
    comando = partes[0].upper()

    if comando == "ADD":

        if len(partes) < 2 or not partes[1].strip():
            resposta = "Erro: informe uma tarefa."
        else:
            tarefas.append(partes[1])
            resposta = f"Tarefa adicionada: {partes[1]}"

    elif comando == "LIST":

        if not tarefas:
            resposta = "Neca de pitibiriba"
        else:
            resposta = "\n".join(
                f"{i + 1}. {t}"
                for i, t in enumerate(tarefas)
            )

    elif comando == "REMOVE":

        if len(partes) < 2:
            resposta = "Erro: informe o número da tarefa."

        else:
            try:
                indice = int(partes[1]) - 1

                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    resposta = f"Removida: {removida}"
                else:
                    resposta = "Índice inválido."

            except ValueError:
                resposta = "Digite um número."

    else:

        resposta = "Comando inválido."

    print(f"Recebido: {mensagem}", flush=True)

    socket.send_string(resposta)