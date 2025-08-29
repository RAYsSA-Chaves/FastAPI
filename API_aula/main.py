from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import PersonagensOnePiece
from typing import Any
from routes import curso_router, usuario_router
import requests

app = FastAPI()

app.include_router(curso_router.router, tags=["Cursos"])
app.include_router(usuario_router.router, tags=["Usuários"])

@app.get("/personagem/{personagem_id}")
def get_ponei(personagem_id: int):
    response = requests.get(f"http://ponyapi.net/v1/character/{personagem_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"Mensagem": "Ponei não encontrado"}


# def fake_db():
#     try:
#         print("Abrindo conexão com o banco de dados")
#     finally:
#         print("Conexão concluída, fechando conexão com o banco")

# personagens = {
#     1:
#         {
#             "nome": "Monkey D. Luffy",
#             "fruta": "Gomu Gomu no Mi",
#             "resompensa": 300000000,
#             "funcao": "Capitão",
#             "foto": "https://preview.redd.it/what-makes-luffy-such-an-attractive-personality-v0-zggpeewz13se1.jpeg?width=640&crop=smart&auto=webp&s=09968bb9cab9d491cd14d399077d66d491fd8d6a"
#          },
#     2: {
#         "nome": "Trafalgar D. Water Law",
#         "fruta": "Ope Ope no Mi",
#         "recompensa": 300000000,
#         "funcao": "Capitão",
#         "foto": "https://i.pinimg.com/736x/21/71/cb/2171cb69cef931e2b227c6e71f6f33d6.jpg"
#     }      
# }

# @app.get("/")
# def teste():
#     return { "Mensagem": "Deu certo"}

# @app.get("/personagens")
# async def get_personagens(db: Any = Depends(fake_db)):
#     return personagens

# @app.get("/personagens/{personagem_id}", description="Retorna um personagem com um ID específico ou retorna o erro 404", summary="Retorna um personagem específico")
# async def get_personagem(personagem_id: int):
#     try:
#         personagem = personagens[personagem_id]
#         return personagem
#     except KeyError:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail="Personagem não encontrado")
    
# @app.post("/personagens", status_code=status.HTTP_201_CREATED)
# async def post_personagem(personagem: PersonagensOnePiece):
#     next_id = len(personagens) + 1

#     personagens[next_id] = personagem

#     del personagem.id

#     return personagem

# @app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
# async def put_personagem(personagem_id: int, personagem: PersonagensOnePiece):
#     if personagem_id in personagens:
#         personagens[personagem_id] = personagem
#         personagem.id = personagem_id
#         del personagem.id
#         return personagem
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail="Personagem não encontrado")
        
# @app.delete("/personagens/[personagem_id]", status_code=status.HTTP_204_NO_CONTENT)
# async def deletar_personagem(personagem_id: int):
#   if personagem_id in personagens:
#     del personagens[personagem_id]
#     return Response(status_code=HTTP_204_NO_CONTENT)
#   else:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# @app.get("/calculadora")
# async def calcular(a: int, b: int):
#     soma = a + b
#     return {"Resultado = ": soma}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="info", reload=True)