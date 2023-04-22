from datetime import datetime
from pytz import timezone

from fastapi import FastAPI

app = FastAPI()


@app.get('/fusos/{fuso_horario:path}/fusos2/{fuso_horario2:path}')
def hora_fuso_horario(fuso_horario: str, fuso_horario2: str):
    return \
        [{fuso_horario: datetime.now().astimezone(timezone(fuso_horario)).strftime('%Z %H:%M')},
         {fuso_horario2: datetime.now().astimezone(timezone(fuso_horario2)).strftime('%Z %H:%M')}]

#  http://127.0.0.1:8000/fusos/Brazil/Acre/fusos2/Brazil/east
