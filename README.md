# Desafio 2 - API Fuso Horário
Criação de uma API em FastAPI com um endpoint que retorna o horário atual dos fusos horários (GMT - 3) e (GMT - 5).
O fuso horário é passado como um parâmetro da API.

## Comandos necessários para execução:

### É necessário realizar as seguintes instalações (no terminal):
`pip install fastapi`
`pip install unicorn`
`pip install pytz`

O pytz é uma biblioteca criada pela comunidade Python para facilitar a manipulação de timezones.

### Comando para iniciar a API (no terminal):
`uvicorn main:app --reload`

### Link para acessar no navegador:
[http://127.0.0.1:8000/fusos/Brazil/Acre/fusos2/Brazil/east](http://127.0.0.1:8000/fusos/Brazil/Acre/fusos2/Brazil/east)

### Resultado esperado:
![image](https://user-images.githubusercontent.com/109490199/233717506-d3fa97b6-a2b0-4db0-84ef-455acf8c64b3.png)
