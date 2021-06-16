from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Haiya'}

@app.get('/users')
async def get_users():
    return {'message': 'Get User'}