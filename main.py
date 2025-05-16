from configs.config import chat

def main():
    loop_chatbot()

def loop_chatbot():
    prompt = input("Digite sua pergunta: ")
    while prompt != "sair":
        response = chat.send_message(prompt)
        print("Resposta: ",response.text , "\n\n")
        prompt = input("Digite sua pergunta ou fim para encerrar chat: ")

if __name__ == "__main__":
    main()