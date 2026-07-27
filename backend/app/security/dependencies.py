from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.security.jwt_handler import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return payload


def admin_required(current_user=Depends(get_current_user)):
    if current_user.get("role") != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return current_user


def coach_required(current_user=Depends(get_current_user)):
    if current_user.get("role") not in ["Admin", "Coach"]:
        raise HTTPException(
            status_code=403,
            detail="Coach access required"
        )
    return current_user


def player_required(current_user=Depends(get_current_user)):
    if current_user.get("role") not in ["Admin", "Player"]:
        raise HTTPException(
            status_code=403,
            detail="Player access required"
        )
    return current_user