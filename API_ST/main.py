from fastapi import FastAPI, HTTPException, status, Response
from models import StrangerThingsCharacters, StrangerThingsCharactersPatch

app = FastAPI(
    title= "Stranger Things API",
    description= "API dos personagens da melhor série!",
    version= "1.0.0",
)

# Criando os personagens
characters = {
    1:
        {
            "nome": "Jane Ives (Eleven)",
            "status": "Viva",
            "ocupaçao": "Estudante/Ex-experimento do Hawkins Lab",
            "habilidades": "Telecinese",
            "familia": "Terry ives (mãe), Jim Hopper (pai adotivo)",
            "foto": "https://i.pinimg.com/736x/03/1d/d2/031dd24bec9f0dc5a64db8289f2836f2.jpg"
        },
        
    2: 
        {
            "nome": "Mike Wheeler",
            "status": "Vivo",
            "ocupaçao": "Estudante",
            "habilidades": "Liderança",
            "familia": "Karen Wheeler (mãe), Ted Wheeler (pai), Nancy Wheeler (irmã), Holly Wheeler (irmã)",
            "foto": "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/An_image_of_the_character_Mike_Wheeler_%28portrayed_by_Finn_Wolfhard%29_from_season_3_of_the_Netflix_series_%22Stranger_Things%22.png/250px-An_image_of_the_character_Mike_Wheeler_%28portrayed_by_Finn_Wolfhard%29_from_season_3_of_the_Netflix_series_%22Stranger_Things%22.png"
        },  
        
    3: 
        {
            "nome": "Jim Hopper",
            "status": "Vivo",
            "ocupaçao": "Chefe da Polícia de Hawkins",
            "habilidades": "Investigação, Combate",
            "familia": "Sara Hopper (filha falecida), Eleven (filha adotiva)",
            "foto": "https://i.redd.it/favorite-jim-hopper-v0-sf2py21vdsod1.jpg?width=3353&format=pjpg&auto=webp&s=58ed0497345c40e30090c7188b2c76b415edaeb0" 
        },  
        
    4:
        {
            "nome": "Max Mayfield",
            "status": "Vivo",
            "ocupaçao": "Estudante",
            "habilidades": "Skate, Competição de videogame, Coragem",
            "familia": "Sam Mayfield (pai), Neil Hargrove (padastro), Susan Mayfield (mãe), Billy Hargrove (meio-irmão)",
            "foto": "https://i.pinimg.com/736x/e5/a3/3b/e5a33b5fec259cc8fba761c9dae82ddd.jpg" 
        },
        
    5: 
        {
            "nome": "Joyce Byers",
            "status": "Vivo",
            "ocupaçao": "Caixa/Balconista na loja de departamentos de Hawkins",
            "habilidades": "Detetive amadora, Coragem, Persistência",
            "familia": "Will Byers (filho), Jonathan Byers (filho)",
            "foto": "https://i.pinimg.com/custom_covers/222x/760545524512209798_1626962300.jpg" 
        },
        
    6: 
        {
            "nome": "Vecna",
            "status": "Vivo",
            "ocupaçao": "Criatura do Mundo Invertido",
            "habilidades": "Telecinese, Controle mental, Criação de ilusões",
            "familia": "Victor Creel (pai), Virginia Creel (mãe), Alice Creel (irmã)",
            "foto": "https://www.usmagazine.com/wp-content/uploads/2022/05/Stranger-Things-Newest-Villain-What-to-Know-About-Season-Four-Introduction-to-Vecna-04.jpg?quality=86&strip=all"
        },
        
    7:
        {
            "nome": "Dustin Henderson",
            "status": "Vivo",
            "ocupaçao": "Estudante",
            "habilidades": "Ciência, Inteligência, Canto",
            "familia": "Claudia Henderson (mãe)",
            "foto": "https://pbs.twimg.com/media/EXnUHw1XYAQ9eY2.jpg"
        },
        
    8: 
        {
            "nome": "Kali Prasad (Eight)",
            "status": "Vivo",
            "ocupaçao": "Ex-experiemnto do Hawkins Lab",
            "habilidades": "Criação de ilusões",
            "familia": "Eleven (irmã)",
            "foto": "https://static.wikia.nocookie.net/strangerthings/images/9/9e/Kali.png/revision/latest?cb=20171106213307&path-prefix=pt-br"
        },
        
    9: 
        {
            "nome": "Lucas Sinclair",
            "status": "Vivo",
            "ocupaçao": "Estudante",
            "habilidades": "Tiro com estilingue, Coragem",
            "familia": "Charles Sinclair (pai), Sue Sinclair (mãe), Erica Sinclair (irmã)",
            "foto": "https://static.wikia.nocookie.net/herois/images/b/b0/Lucasseason2.jpg/revision/latest?cb=20221009131115&path-prefix=pt-br"
        },
        
    10:
        {
            "nome": "Murray Bauman",
            "status": "Vivo",
            "ocupaçao": "Jornalista/Investigador",
            "habilidades": "Alta inteligência, Fluência em russo, Investigação",
            "familia": "Não detalhada",
            "foto": "https://hips.hearstapps.com/hmg-prod/images/murray-bauman-stranger-things-4-protagonista-1583308680.jpg?crop=0.498xw:1.00xh;0.204xw,0&resize=1200:*"
        },
        
    11:
        {
            "nome": "Demogorgon",
            "status": "Vivo",
            "ocupaçao": "Criatura do Mundo Invertido",
            "habilidades": "Força, Agilidade, Caça",
            "familia": "Não aplicável",
            "foto": "https://i.pinimg.com/474x/86/b3/53/86b353c2d53a1858720a670ae3248468.jpg"
        },
        
    12:
        {
            "nome": "Billy Hargrove",
            "status": "Morto",
            "ocupaçao": "Estudante e Salva-vidas na Piscina Comunitária de Hawkins",
            "habilidades": "Força, Intimidação",
            "familia": "Neil Hargrove (pai), Susan Mayfield (madrasta), Max Mayfield (meia-irmã)",
            "foto": "https://miro.medium.com/v2/resize:fit:382/1*Mgm1hZuxoctTuQcQZ1r3GA.png"
        },
        
    13:
        {
            "nome": "Eddie Munson",
            "status": "Morto",
            "ocupaçao": "Estudante e Líder do Hellfire Club",
            "habilidades": "Guitarrista, Coragem, Estratégia",
            "familia": "Wayne Munson (tio e tutor legal), Alan Munson (pai)",
            "foto": "https://preview.redd.it/your-opinions-about-eddie-munson-v0-fd3buyuodnyc1.jpeg?width=1080&crop=smart&auto=webp&s=3edd960786811abe358287768d3e8366fd2b0fc8"
        },
        
    14:
        {
            "nome": "Nancy Wheeler",
            "status": "Viva",
            "ocupaçao": "Estudante e Jornalista amadora",
            "habilidades": "Investigação, Determinação, Mira",
            "familia": "Karen Wheeler (mãe), Ted Wheeler (pai), Mike Wheeler (irmão), Holly Wheeler (irmã)",
            "foto": "https://preview.redd.it/what-season-do-you-like-nancy-wheeler-the-best-v0-b2ugvntn3ydb1.jpg?width=564&format=pjpg&auto=webp&s=1062e1e073451e2b2034e827a9deaa6b3b050e0f"
        },
        
    15:
        {
            "nome": "Jonathan Byers",
            "status": "Vivo",
            "ocupaçao": "Fotógrafo",
            "habilidades": "Fotografia",
            "familia": "Will Byers (irmão), Joyce Byers (mãe), Lonnie Byers (pai)",
            "foto": "https://static.wikia.nocookie.net/strangerthings/images/d/d7/Jonathan_Byers_001.jpg/revision/latest?cb=20160818153946&path-prefix=pt-br"
        },
        
    16:
        {
            "nome": "Steve Harrington",
            "status": "Vivo",
            "ocupaçao": "Estudante, Babá, Atendente na sorveteria Scoops Ahoy/Atendente locadora Family Video",
            "habilidades": "Cuidados com criaças, Combate, Liderança, Capacidade atlética",
            "familia": "Não detalhada",
            "foto": "https://hips.hearstapps.com/hmg-prod/images/mh-steve-stranger-things-legend-1561499047-1-1561561628.jpg?crop=0.668xw:1.00xh;0.182xw,0&resize=640:*"
        },
        
    17: 
        {
            "nome": "Will Byers",
            "status": "Vivo",
            "ocupaçao": "Estudante",
            "habilidades": "Sobrevivência, Sensibilidade ao Devorador de Mentes",
            "familia": "Joyce Byers (mãe), Lonnie Byers (pai), Jonathan Byers (irmão)",
            "foto": "https://people.com/thmb/QQX9HmtACKsAswbpf8jUkJa1mmk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2)/m07_promo_stills_022519.0007_r-1-2000-7e55b34306eb48159fd7c46f5bb9170f.jpg"
        },
        
    18:
        {
            "nome": "Robin Buckley",
            "status": "Viva",
            "ocupaçao": "Atendente na sorveteria Scoops Ahoy/Atendente locadora Family Video",
            "habilidades": "Inteligência",
            "familia": "Melissa Buckley (mãe) e Richard Buckley (pai)",
            "foto": "https://i0.wp.com/bloody-disgusting.com/wp-content/uploads/2019/12/Stranger-Things-season-3-screenshots-Chapter-2-The-Mall-Rats-017-e1575303475500.jpg?resize=1000%2C597&ssl=1"
        },
        
    19:
        {
            "nome": "Bob Newby",
            "status": "Morto",
            "ocupaçao": "Gerente da Radio Shack local",
            "habilidades": "Inteligência, Informática, Tecnologia",
            "familia": "Joyce Byers (parceiro falecido)",
            "foto": "https://static.wikia.nocookie.net/herois/images/0/05/Bob_Newby.webp/revision/latest?cb=20220618145805&path-prefix=pt-br"
        },
        
    20: 
        {
            "nome": "Erica Sinclair",
            "status": "Viva",
            "ocupaçao": "Estudante",
            "habilidades": "Inteligência, Raciocínio lógico e matemático, Perspicácia",
            "familia": "Charles Sinclair (pai), Sue Sinclair (mãe), Lucas Sinclair (irmão)",
            "foto": "https://static.wikia.nocookie.net/strangerthings8338/images/8/8d/Erica_Sinclair_S3.png/revision/latest?cb=20190706021540"
        }
}

# Teste
@app.get("/")
def teste():
    return { "Mensagem": "Funcionando!"}

# Puxar os personagens
@app.get("/characters", description="Retorna todos os personagens", summary="Retorna todos os personagens")
async def get_characters():
    return characters

# Puxar personagem específico
@app.get("/characters/{character_id}", description="Retorna um personagem com um ID específico ou retorna o erro 404", summary="Retorna um personagem específico")
async def get_character(character_id: int):
    try:
        character = characters[character_id]
        return character
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Personagem não encontrado")

# Cria um personagem novo
@app.post("/characters", status_code=status.HTTP_201_CREATED, description="Cria um novo personagem com ID válido", summary="Cria um novo personagem")
async def post_character(character: StrangerThingsCharacters):
    character_dict = character.dict()

    # Se o id passado não está sendo usado -> aceita
    if character_dict.get("id") and character_dict["id"] not in characters:
        new_id = character_dict["id"]
    else:
        # Caso contrário, gera o próximo disponível
        new_id = len(characters) + 1

    character_dict["id"] = new_id
    characters[new_id] = character_dict
    return character_dict

# Atualiza ou substitui um personagem
@app.put("/characters/{character_id}", status_code=status.HTTP_202_ACCEPTED, description="Atualiza ou substitui um personagem específico ou retorna o erro 404", summary="Atualiza um personagem")
async def put_character(character_id: int, character: StrangerThingsCharacters):
    # Verificar se o id já existe para atualizar as infos do personagem
    if character_id in characters:
        characters[character_id] = character.dict()
        characters[character_id]["id"] = character_id  # evita passar um id diferente
        return characters[character_id]
    # Caso não exista -> erro
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")

# Deleta um personagem
@app.delete("/characters/{character_id}", status_code=status.HTTP_204_NO_CONTENT, description="Deleta um personagem ou retorna o erro 404", summary="Deleta um personagem")
async def delete_character(character_id: int):
    if character_id in characters:
        del characters[character_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)  
        
# Permite atualizar apenas as infos que quiser do personagem
@app.patch("/characters/{character_id}", status_code=status.HTTP_200_OK, description="Atualiza somente as infos desejadas do personagem (não ele completo) ou retorna o erro 404", summary="Atualiza um personagem parcialmente")
async def patch_character(character_id: int, character_patch: StrangerThingsCharactersPatch):
    if character_id not in characters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")

    patch_data = character_patch.dict(exclude_unset=True)  # pega só os campos enviados

    # Atualiza apenas os campos enviados
    for key, value in patch_data.items():
        characters[character_id][key] = value

    return characters[character_id]


# Rodar o servidor quando o arquivo for rodado
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="info", reload=True)
