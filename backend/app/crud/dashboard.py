from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.models import Player, Fee, Academy


def dashboard_stats(db: Session):

    total_academies = db.query(Academy).count()

    total_players = db.query(Player).count()

    total_revenue = (
        db.query(func.sum(Fee.amount))
        .filter(Fee.status == "Paid")
        .scalar()
    ) or 0

    paid_fees = (
        db.query(Fee)
        .filter(Fee.status == "Paid")
        .count()
    )

    unpaid_fees = (
        db.query(Fee)
        .filter(Fee.status == "Unpaid")
        .count()
    )

    return {
        "total_academies": total_academies,
        "total_players": total_players,
        "total_revenue": total_revenue,
        "paid_fees": paid_fees,
        "unpaid_fees": unpaid_fees
    }


def monthly_revenue(db: Session):

    revenue = (
        db.query(
            Fee.month,
            func.sum(Fee.amount).label("total")
        )
        .filter(Fee.status == "Paid")
        .group_by(Fee.month)
        .all()
    )

    return [
        {
            "month": r.month,
            "revenue": r.total
        }
        for r in revenue
    ]

def recent_payments(db: Session):

    payments = (
        db.query(Fee)
        .filter(Fee.status == "Paid")
        .order_by(Fee.id.desc())
        .limit(5)
        .all()
    )

    return [
        {
            "player": payment.player.full_name,
            "month": payment.month,
            "amount": payment.amount,
            "voucher": payment.voucher_no
        }
        for payment in payments
    ]

def recent_players(db: Session):

    players = (
        db.query(Player)
        .order_by(Player.id.desc())
        .limit(5)
        .all()
    )

    return [
        {
            "id": player.id,
            "name": player.full_name,
            "position": player.position,
            "age": player.age
        }
        for player in players
    ]