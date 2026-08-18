from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

tarefas = list()

counter = 0

class Pessoa(BaseModel):
    nome: str
    sobrenome: str
    idade: int

class Tarefa(BaseModel):
    tarefa: str
    prioridade: int
    feito: bool

@app.get("/")
def root():
    return tarefas

@app.get("/tarefa/{pos}")
def get_tarefa(pos: int):
    return tarefas[pos]

@app.post("/adicionar/")
def criar_tarefa(tarefa: Tarefa):
    tarefa.feito = False
    tarefas.append(tarefa)
    return len(tarefas)

@app.put("/feito/{pos}")
def marcar_feito(pos: int):
    tarefas[pos].feito = True
    return tarefas[pos]

@app.delete("/deletar/{pos}")
def deletar_tarefa(pos: int):
    tarefa = tarefas.pop(pos)
    return tarefa

@app.get("/")
def root():
    return {"message": "hello world"}

# 1. após executar algumas vezes na página FastAPI o contador vai acrescentando
#alguns números (Exemplo: primeira execução 0, segunda execução 1, terceira execução 3.... assim por diante) 
# 2. Quando declaramos counter como global, estamos dizendo, para o counter não criar uma varíavel counter local MAS 
#que eu quero utilizar um counter fora dessa função
# 3. Por conta do "counter += 1", ele apenas não consulta mas modifica o estado da aplicação
@app.get("/count")
def get_count():
    global counter
    counter += 1
    return counter

#Este exibe apenas o "Hello, world!"
@app.get("/hello")
def hello_world():
    return "Hello, world"

#Este requisita uma string ao final para prosseguir 
#"Hello, world!" ou "Hello, Usuário!" ou "Hello, ...!"
#Assim por diante
@app.get("/hello/{name}")
def hello(name):
    return f"Hello, {name}"

#Este requisita uma string ao final para prosseguir 
#"Hello, world!" ou "Hello, Usuário!" ou "Hello, ...!"
#Assim por diante
@app.get("/hello/")
def hello(parameter = "World"):
    return f"Hello, {parameter}"

@app.post("/pessoa/")
def criar_pessoa(pessoa: Pessoa):
    return pessoa

@app.post("/pessoa/")
def criar_pessoa(pessoa: Pessoa):
    return pessoa