from fastapi import FastAPI

from .schemas import RequestId, RequestIndex



app = FastAPI()


#  ---- Index ----
@app.get('/')
def index(request: RequestIndex):
    print(request)
    if request.tool == 'owasp':
        return {'data': {'tool': f'{request.tool} - available'}}
    else:
        return {'data': {'tool': f'{request.tool} - not_available'}}


#  ---- Status ----
@app.get('/status/')
def status(request: RequestId):
    return {'data': request.id}


# ---- Stop ----
@app.post('/stop_all_scaner/')
def stop_all_scaner(requests: RequestIndex):
    return {'data': {'scanner': 'stop_all'}}


@app.post('/stop/')
def stop_id(request: RequestId):
    return {'data': request.id}


'''
Realizar un escaneo de vulnerabilidades sobre un set de urls usando Active Scan de Zaproxy.
Poder consultar el estado de un escaneo y los resultados una vez terminado el mismo.

Consideraciones:
En los datos que devuelve la API construida tienen que persistir tanto los escaneos realizados como sus resultados más allá de lo que puede guardar Zaproxy. 

También es parte del desafío el diseño de la API REST (los recursos, paths y métodos utilizados para cada acción).

Entregables:
● Código funcionando en repositorio privado de GitHub.
● Documentación mínima para correr el proyecto.
● Explicación del diseño y las decisiones tomadas

Extras:
● Mecanismo para realizar escaneos programados.
● Diseño adaptable a distintos scanners, ejemplo Burp o Acunetix.
● Test unitarios y de integración.
● Propuesta de diseño para una aplicación escalable que pueda realizar N escaneos
en paralelo, teniendo en cuenta cuestiones de performance y resiliencia.



'''
