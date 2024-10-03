from llama_index.core import Settings
from langgraph.prebuilt import create_react_agent
from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv
import os

load_dotenv()

def create_dev_agent():
    llm = ChatVertexAI(model_name="gemini-1.5-pro-001", api_key=os.environ.get('API_GEMINI'))
    Settings.llm = llm
    tools = []
    return create_react_agent(model=llm, tools=tools)

programador = create_dev_agent("Programador")
testador = create_dev_agent("Testador")
revisor = create_dev_agent("Revisor de Código")

def simulate_conversation(agent, user_input):
    response = agent.invoke(user_input)
    return response

def dev_pipeline(codigo):
    
    print("Programador criando código...")
    codigo_gerado = simulate_conversation(programador, "Crie um código que resolva o problema XYZ")
    print(f"Programador: {codigo_gerado}\n")
    
    
    print("Testador verificando o código...")
    resultado_testes = simulate_conversation(testador, f"Teste o seguinte código: {codigo_gerado}")
    print(f"Testador: {resultado_testes}\n")
    
    print("Revisor de Código revisando o código...")
    revisao = simulate_conversation(revisor, f"Revise o seguinte código: {codigo_gerado}")
    print(f"Revisor de Código: {revisao}\n")

print('cheguei')
dev_pipeline("Código de exemplo")
