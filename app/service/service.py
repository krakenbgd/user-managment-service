from fastapi.responses import JSONResponse
from sqlalchemy.exc import NoResultFound
from app.db.db import DBConn


class UserManagmentService:
    def __init__(self):
        self.db = DBConn()

    def get_all_users(self):
        try:
            result = self.db.get_all_users()

            return JSONResponse(content=result, status_code=200)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})

    def get_user_by_id(self, user_id):
        try:
            result = self.db.get_user_by_id(user_id)

            return JSONResponse(content=result, status_code=200)
        except NoResultFound as e:
            return JSONResponse(status_code=404, content={"message": str(e)})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})

    def create_user(self, user):
        try:
            status = self.db.create_user(user)

            return JSONResponse(content=status, status_code=200)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})

    def update_user(self, user_id, user):
        try:
            status = self.db.update_user(user_id, user)

            return JSONResponse(content=status, status_code=200)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})

    def delete_user(self, user_id):
        try:
            status = self.db.delete_user(user_id)

            return JSONResponse(content=status, status_code=200)
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": str(e)})
