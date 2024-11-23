"""Endpoints module."""

from typing import Optional, List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide

from services import MyService
from containers import Container


class Response(BaseModel):
    who: str

router = APIRouter()

@router.get("/", response_model=Response)
@inject
async def index(
        my_service: MyService = Depends(Provide[Container.my_service]),
):
    res = await my_service.name()
    print(res)
    return {
        "who": res,
    }