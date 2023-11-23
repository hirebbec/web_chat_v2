# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from starlette import status
# from starlette.responses import JSONResponse
# from routes.users import create_user
# from schemas.schemas import Login
# from utils.utils import create_access_token, hash_password_sha256, verify_pass
#
#
# def register(form_data: Login, db: Session):
#     username = form_data.username
#     password = form_data.password
#
#     hashed_password = hash_password_sha256(password)
#     new_user = create_user(db, username, hashed_password)
#
#     access_token = create_access_token(data={"sub": new_user.username})
#     response = JSONResponse(
#         content={"access_token": access_token, "token_type": "bearer"}
#     )
#     response.set_cookie(key="access_token", value=access_token)
#
#     return response
#
#
# def login(username: str, password: str, db: Session):
#     user = get_user_by_username(db, username)
#     if not user or not verify_pass(password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
#         )
#
#     access_token = create_access_token(data={"sub": user.username})
#
#     return JSONResponse(
#         content={
#             "access_token": access_token,
#             "username": user.username,
#             "redirect_url": "/OpenChat/chat",
#         }
#     )
