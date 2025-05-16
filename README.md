# Chatbot Alura com Gemini

Este repositório contém o código para um chatbot desenvolvido como parte de um projeto na Alura, utilizando a API Gemini do Google AI Studio. O chatbot é configurado para responder perguntas de forma útil, mas com um toque de humor (mesmo que as piadas não sejam as melhores!).

## Pré-requisitos

* Python 3.6 ou superior
* Uma chave de API do Google AI Studio (obtida no [Google AI Studio](https://makersuite.google.com/app/home))
* A biblioteca `python-dotenv` para carregar variáveis de ambiente.
* A biblioteca `google-generativeai` para interagir com a API Gemini.

## Instalação

1.  Clone este repositório:

    ```bash
    git clone [https://github.com/LucasRaimundo/chatbot-alura-gemini.git](https://github.com/LucasRaimundo/chatbot-alura-gemini.git)
    cd chatbot-alura-gemini
    ```

2.  Crie um ambiente virtual (recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # No Linux/macOS
    env\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install python-dotenv google-generativeai
    ```

4.  Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:

    ```
    GOOGLE_API_KEY=SUA_CHAVE_DE_API
    ```

    Substitua `SUA_CHAVE_DE_API` pela sua chave real do Google AI Studio.

## Estrutura do Projeto

chatbot-alura-gemini/
├── main.py          # Arquivo principal para executar o chatbot
├── configs/
│   └── config.py    # Configuração do modelo Gemini e do objeto chat
└── .env           # Arquivo com a chave de API (não versionar!)


## Rodando o projeto

1. Execute o arquivo main.py:

    - Bash

    - python main.py

- O chatbot responderá às suas perguntas, tentando ser engraçado (ou não).

## Próximos Passos

- Adicionar mais funcionalidades ao chatbot (acesso a outras APIs, etc.).
- Melhorar o "humor" do chatbot (se possível!).

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


- Lembre-se de substituir `"SUA_CHAVE_DE_API"` pela sua chave real do Google AI Studio no