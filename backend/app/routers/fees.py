from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.fees import FeeCreate
from app.crud.fees import create_fee, get_fees,mark_fee_paid

router = APIRouter(
    prefix="/fees",
    tags=["Fees"]
)


@router.post("/")
def add_fee(fee: FeeCreate, db: Session = Depends(get_db)):
    return create_fee(db, fee)


@router.get("/")
def all_fees(db: Session = Depends(get_db)):
    return get_fees(db)

@router.put("/{fee_id}/pay")
def pay_fee(fee_id: int, db: Session = Depends(get_db)):
    fee = mark_fee_paid(db, fee_id)

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee not found"
        )

    return fee