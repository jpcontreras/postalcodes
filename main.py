from fastapi import FastAPI

app = FastAPI(title='Postal Codes Service',
              description='This service use some flat file with csv format to save and send to another service to process data.',
              version='0.0.1')

@app.post('/postal_codes/upload')
async def upload():
    return 'uploading CSV flat file'

@app.post('/postal_codes/create')
async def create():
    return 'create some postal code register'