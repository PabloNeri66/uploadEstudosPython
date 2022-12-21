from fastapi import FastAPI

app = FastAPI()

# rotas: 
    #app.get() --> Imagino que para get

#vendas = [
    #{
    #    'id' : 1,
     #   'preço' : (2.54),
      #  'produto' : "Ruffles"
    #},
    #{
    #    'id': 2,
    #    'preço' : 5,
    #   'produto' : "Veja"
    #},
    #{
    #    'id' : 3,
    #    'preço' : 49,
    #    'produto' : "bola"
    #}
#]
vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}
 #no FastAPI o jsonfy ja esta estruturado na rota /docs, apenas executar o deploy.
@app.get('/')
def home():
    return{"vendas" : len(vendas)}

@app.get('/vendas/{id_venda}')#id_venda == <int:id>
def pegar_venda(id_venda : int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return('Não foi encontrado!')

        
#http://127.0.0.1:8000/docs
# O fastapi é bom pelo fato da facilidade, já o Postman aparenta ser mais otimizado.
