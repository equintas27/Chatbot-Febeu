## HomeOffice
- Skeelo
- Estante Mágica
- netLex
- Asaas
- QuintoAndar
- Estuda. com
- iFood
- Heineken
- Sicoob
- TOTVS

## Funcionalidades do chatbot:

1- Apresentar a FEBEU e a sua história.
2- Explicar os serviços e as áreas de actuação.
3- Responder a perguntas sobre a empresa.
4- Informar sobre contactos e oportunidades de parceria.
5- Encaminhar questões que não consiga responder para os contactos dos fundadores.

## Tecnologias
Backend: Python + FastAPI.
Base de dados: PostgreSQL.
Vector Database: ChromaDB
Pipeline RAG: LangChain
Tabela conversations: dados das conversas.
Tabela messages: mensagens trocadas.

### Responsabilidades

- **FastAPI:**  Receber e responder às mensagens
- **LangChain:** Coordenar o pipeline RAG
- **ChromaDB:**  Armazenar e recuperar embeddings
- **PostgreSQL:** Guardar conversas e mensagens

## Arquitectura do chatbot

1- Frontend — interface do chatbot.
2- Backend — processamento e gestão das conversas.
3- Sistema RAG — recuperação de informação.
4- Base de conhecimento — documentos FEBEU.
5- Modelo de IA — geração das respostas.
6- Sistema de encaminhamento — WhatsApp dos fundadores.
7- Base de dados — conversas, sessões e perguntas pendentes.


## Backend do chatbot FEBEU

1- Receber mensagens: receber as perguntas enviadas pelo visitante através do website.
2- Gerir conversas: identificar cada visitante e manter o histórico da conversa.
3- Executar o RAG: procurar informações relevantes na base de conhecimento da FEBEU.
4- Gerar respostas: utilizar o modelo de IA para formular respostas fundamentadas.
5- Encaminhar perguntas: enviar aos fundadores as questões que o chatbot não consegue responder com segurança.


### Conversação:
```text
Visitante entra no chatbot
     |
     v
Backend cria uma conversa
     |
     v
conversation_id: abc123
    	|
    	v
Visitante envia uma mensagem
    	|
    	v
Backend guarda a mensagem
    	|
    	v
Chatbot responde
    	|
    	v
Backend guarda a resposta
	      conversations
      -------------
id
created_at
status
     |
     | 1:N
     |
     v
     messages
     --------
     id
     conversation_id
     content
     role
     created_at
```

### Funcionamento das mensagens
Quando o visitante enviar uma pergunta, o backend deverá:
1. Receber a mensagem.
2. Identificar a conversa através do conversation_id.
3. Guardar a mensagem no PostgreSQL.
4. Enviar a mensagem para o sistema RAG.
5. Receber a resposta e guardá-la.
6. Devolver a resposta ao website.

### Estrutura de uma mensagem
Cada mensagem terá um campo chamado role.

Esse campo identifica quem enviou a mensagem:
role           Significado
user	          Mensagem enviada pelo visitante.
assistant	     Resposta gerada pelo chatbot.

## Sistema RAG
Agora vamos estudar como o backend vai:
1. Receber a pergunta.
2. Procurar informação nos documentos institucionais da FEBEU.
3. Seleccionar os conteúdos relevantes.
4. Entregar esses conteúdos ao modelo de IA.
5. Gerar uma resposta fundamentada, sem inventar informações.


### Opções  

1. Precisão das respostas.
2. Capacidade de compreender português.
3. Fidelidade à base de conhecimento.
4. Capacidade de reconhecer quando não sabe responder.
5. Velocidade de resposta.


```text
Website FEBEU
     |
     v
Backend Python (FastAPI)
     |
     v
Sistema RAG
     |
     +---- Base de Conhecimento
     |
     +---- Modelo de IA
     |
     v
Resposta ao visitante
```


## Estrutura do projecto
```text
febeu-chatbot/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes/
│   │       └── chat.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── models/
│   │       ├── conversation.py
│   │       └── message.py
│   │
│   ├── schemas/
│   │   └── chat.py
│   │
│   ├── services/
│   │   └── chat_service.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   ├── retriever.py
│   │   └── chain.py
│   │
│   └── llm/
│       └── provider.py
│
├── knowledge_base/
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Ordem de execução

A ordem será:
1. Criar a estrutura do projecto.
2. Configurar o ambiente Python.
3. Instalar as dependências.
4. Criar a primeira aplicação FastAPI.
5. Configurar o PostgreSQL.
6. Desenvolver o sistema RAG.
7. Integrar os modelos de IA.
8. Implementar o encaminhamento para os fundadores.