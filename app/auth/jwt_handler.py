from datetime import datetime, timedelta
from jose import jwt

def create_access_token(data: dict, secret_key: str, algorithm: str, expires_delta: timedelta = None):
    to_encode=data.copy()
    expire=datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt
