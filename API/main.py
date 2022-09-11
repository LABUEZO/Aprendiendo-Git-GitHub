from fastapi import FastAPI
from schemas.users import Usuario

app = FastAPI()

lista_usuarios=[]

@app.get('/')
def home():
    return {'message':'Hello world API'}

@app.post('/user/{nombre}')      #lo que está en paréntesis es un endpoint
def crear_usuario(nombre:str, user:Usuario):
    lista_usuarios.append({'nombre':nombre, 'data':user})
    return {'msg':'usuario creado'}

@app.get('/users')
def obtener_usuarios():
    return {'usuarios':lista_usuarios}

@app.delete('/user/{nombre}')
def borrar_usuario(nombre):
    for usuario in lista_usuarios:
        if nombre == usuario['nombre']:
            lista_usuarios.remove(usuario)
    return {'msg':'usuario borrado'}

@app.put('/user/{nombre}')
def actualizar_usuario(nombre:str, user:Usuario):
    for usuario in lista_usuarios:
        if nombre==usuario['nombre']:
            usuario['data']=user
    return {'message':'datos actualizados'}
