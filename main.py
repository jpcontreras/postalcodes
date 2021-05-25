import uvicorn
from fastapi import FastAPI
from config.database import connection
from fastapi.middleware.cors import CORSMiddleware
from infraestructure.controllers import file_uploads_controller, postal_codes_controller

app = FastAPI(title='Postal Codes Service',
              description='This service use some flat file with csv format to save and send to another service to process data.',
              version='0.0.1')

origins = [
    "processor_web_1:3000",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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