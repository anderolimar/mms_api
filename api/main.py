
from fastapi import FastAPI
from api.handlers import mms
from shared.data import setup
import logging


description = """
API de Médias Móveis Simples (MMS) fornece MMS 20, MMS 50 and MMS 200 para os pares BRLBTC e BRLETH.

## MMS 

Retorna MMS para os pares BRLBTC E BRLETH.

"""

tags_metadata = [
    {
        "name": "mms",
        "description": "Retorna as media moveis referentes ao par informado e o tipo de media movel.",
    },
]

# Configure logging 
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler("load_data.log"),
#         logging.StreamHandler()
#     ]
# )

# Initialize FastAPI app    
app = FastAPI(
    title="API de Médias Móveis Simples",
    description=description,
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


@app.get("/", tags=["home"])
async def home():
    return {"status": "ok"}

app.include_router(mms.router)