from fastapi import FastAPI
from mangum import Mangum

import os

stage = os.environ.get('STAGE', None)
openapi_prefix = f'/{stage}' if stage else '/'

app = FastAPI(title='API', openapi_prefix=openapi_prefix)


@app.get('/')
async def root():
    return {'message': 'Haiya'}


handler = Mangum(app)