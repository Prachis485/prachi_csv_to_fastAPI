from fastapi import APIRouter, HTTPException, Path
from services import get_all_data, get_data_by_id

router = APIRouter()

# GET all data
@router.get("/data")
def fetch_all(limit: int = 10, skip: int = 0):
    data = get_all_data()
    return data[skip: skip + limit]

# GET by ID
@router.get("/data/{id}")
def fetch_one(
    id: str = Path(
        description="Please enter a valid student ID",
        examples=["STU_1000"]
    )
):
    result = get_data_by_id(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return result