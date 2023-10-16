from __future__ import annotations

from typing import Annotated, TypedDict

from fastapi import (
    Body,
    Depends,
)

from diracx.routers.auth import UserInfo, verify_dirac_token
from diracx.routers.fastapi_classes import DiracxRouter
from mydiracx.db.dss.db import DSSDB

LAST_MODIFIED_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"

router = DiracxRouter()
# router = DiracxRouter(require_auth=False) #also comment user_info for local tests


class CustomObject(TypedDict):
    PathValueAsString: str
    IntegerValue: int