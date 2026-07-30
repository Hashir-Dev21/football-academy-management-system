from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.fees import FeeCreate
from app.crud.fees import create_fee, get_fees, mark_fee_paid
from app.database.models import Fee
from app.utils.pdf_generator import generate_fee_receipt

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


@router.get("/{fee_id}/receipt")
def download_receipt(fee_id: int, db: Session = Depends(get_db)):
    fee = db.query(Fee).filter(Fee.id == fee_id).first()

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee not found"
        )

    pdf_path = f"receipt_{fee.id}.pdf"

    generate_fee_receipt(fee, pdf_path)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"{fee.voucher_no}.pdf"
    )