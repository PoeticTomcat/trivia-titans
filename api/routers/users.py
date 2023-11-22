from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from typing import List

from queries.users import (
    UserModelIn,
    UserModelOut,
    UserRepository,
    DuplicateAccountError,
)


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    user: UserModelOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/api/users", response_model=UserToken | HttpError)
async def create_user(
    info: UserModelIn,
    request: Request,
    response: Response,
    repo: UserRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        user = repo.create_user(info, hashed_password)
        print(user)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = UserForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=user, **token.dict())


@router.get("/api/users", response_model=List[UserModelOut])
async def get_all_users(repo: UserRepository = Depends()):
    return repo.get_all_users()


@router.get("/api/users/{user_id}", response_model=UserModelOut)
async def get_user(user_id: int, repo: UserRepository = Depends()):
    user = repo.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


class AccountToken(Token):
    account: UserModelOut


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: UserModelIn = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.get("/leaderboard")
def get_leaderboard_route(queries: UserRepository = Depends()):
    leaderboard = queries.get_leaderboard()
    return leaderboard
