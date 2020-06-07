import falcon
import requests
import json



class Qi_tech(object):
    
    def on_get(self, req, resp, doc):
        resp.status = falcon.HTTP_200
        dados = json.loads(requests.get('http://www.mocky.io/v2/5ed926833100006900c4eb93').text)
        resp.body = json.dumps(dados)
    


app = falcon.API()


empresa = Qi_tech()


app.add_route('/documento/{doc}', empresa)


# em um terminal rode:
# waitress-serve --port=8080 things:app

# em um outro terminal rode:
# http localhost:8080/documento/123

# depois rode o notebook para analisar o json