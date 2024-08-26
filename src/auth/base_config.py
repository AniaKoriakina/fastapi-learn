from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from .manager import get_user_manager
from src.config import SECRET_COOKIE
from src.database import User

cookie_transport = CookieTransport(cookie_name="books", cookie_max_age=3600)

SECRET_COOKIE = SECRET_COOKIE


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_COOKIE, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
