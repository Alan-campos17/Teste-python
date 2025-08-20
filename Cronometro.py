from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool

from Cronometro import cronometro

# 1. Modelo LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 2. Registrar o cronômetro como ferramenta
tools = [
    Tool(
        name="Cronometro",
        func=lambda segundos: cronometro(int(segundos)),  # garante que entra como int
        description="Use esta ferramenta para iniciar um cronômetro em segundos. Exemplo: 'inicie um cronômetro de 10 segundos'."
    )
]

# 3. Inicializar agente
agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True
)

# 4. Teste interativo
while True:
    comando = input("📝 Você: ")
    if comando.lower() in ["sair", "exit", "quit"]:
        break
    resposta = agent.run(comando)
    print("🤖 IA:", resposta)
