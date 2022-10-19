from fastapi import APIRouter

# from fastapi.responses import JSONResponse

router = APIRouter()


# @router.get("", response_class=JSONResponse)
@router.get("")
def upload_http() -> int:
    """Upload video."""
    return "ASD"
