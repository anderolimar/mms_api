import fastapi
from fastapi import Query, Path
from typing import Annotated, Literal
from api.models.params.filter_param import FilterParams
from api.services.mms import MMSService
from shared.repositories.mms import MMSRepository

router = fastapi.APIRouter()

repository = MMSRepository()
service = MMSService(repo= repository)

@router.get("/{pair}/mms", tags=["mms"])
async def get_mms(pair: Annotated[Literal["BRLBTC", "BRLETH"], Path(title="pair to query mms")], filter_query: Annotated[FilterParams, Query()]):
    try:
        return service.get_mms(fromTms= filter_query.fromTms, toTms= filter_query.toTms, pair= pair, range= filter_query.range)
    except Exception as e:
        raise fastapi.HTTPException(status_code=500, detail="Internal Server Error")