import random
from sqlalchemy.orm import Session
from app.database.models import Fee
from app.schemas.fees import FeeCreate


def create_fee(db: Session, fee: FeeCreate):
    voucher = f"VCH-{random.randint(100000, 999999)}"

    db_fee = Fee(
        player_id=fee.player_id,
        month=fee.month,
        amount=fee.amount,
        due_date=fee.due_date,
        voucher_no=voucher
    )

    db.add(db_fee)
    db.commit()
    db.refresh(db_fee)

    return db_fee


def get_fees(db: Session):
    return db.query(Fee).all()

def mark_fee_paid(db: Session, fee_id: int):
    fee = db.query(Fee).filter(Fee.id == fee_id).first()

    if not fee:
        return None

    fee.status = "Paid"

    db.commit()
    db.refresh(fee)

    return fee