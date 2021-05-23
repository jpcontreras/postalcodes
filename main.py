import uvicorn
from fastapi import FastAPI
from config.database import connection
from application import file_uploads_controller, postal_codes_controller

app = FastAPI(title='Postal Codes Service',
              description='This service use some flat file with csv format to save and send to another service to process data.',
              version='0.0.1')

app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

app.get('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


app.include_router(file_uploads_controller.router)
app.include_router(postal_codes_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)