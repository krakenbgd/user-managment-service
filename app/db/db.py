from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError, NoResultFound


from app.db.conn import users_table, engine


class DBConn:
    def __init__(self):
        self.db_engine = engine
        self.db_users_table = users_table

    def get_all_users(self):
        try:
            with self.db_engine.connect() as connection:
                query = select(users_table)
                result = connection.execute(query)
                users = [dict(zip(result.keys(), row)) for row in result.fetchall()]

                return users
        except Exception as e:
            print(str(e))

            raise Exception(
                f"Server encountered unexpected error! Try again later or contact the administrator."
            )

    def get_user_by_id(self, user_id):
        try:
            with engine.connect() as connection:
                query = select(users_table).where(users_table.c.id == user_id)
                result = connection.execute(query)
                user = result.fetchone()
                if user is None:
                    raise NoResultFound("User does not exist!")

                return dict(user._mapping)
        except NoResultFound as e:
            print(str(e))

            raise NoResultFound(str(e))
        except SQLAlchemyError as e:
            print(str(e))

            raise Exception(
                f"Server encountered unexpected error! Try again later or contact the administrator."
            )

    def create_user(self, user):
        try:
            with engine.connect() as connection:
                query = insert(users_table).values(user.dict())
                result = connection.execute(query)
                connection.commit()
                user_id = result.inserted_primary_key[0]

                return {"message": f"User created successfully! User ID is: {user_id}"}
        except SQLAlchemyError as e:
            print(str(e))

            raise ValueError(
                f"Server encountered unexpected error! Try again later or contact the administrator."
            )

    def update_user(self, user_id, user):
        try:
            with engine.connect() as connection:
                update_stmt = (
                    update(users_table)
                    .where(users_table.c.id == user_id)
                    .values(user.dict())
                )
                connection.execute(update_stmt)
                connection.commit()

                return {
                    "message": f"User associated with {user_id} updated successfully!"
                }
        except SQLAlchemyError as e:
            print(str(e))

            raise ValueError(
                f"Server encountered unexpected error! Try again later or contact the administrator."
            )

    def delete_user(self, user_id):
        try:
            with engine.connect() as connection:
                delete_stmt = delete(users_table).where(users_table.c.id == user_id)
                connection.execute(delete_stmt)
                connection.commit()

                return {
                    "message": f"User associated with {user_id} deleted successfully!"
                }
        except Exception as e:
            print(str(e))

            raise ValueError(
                f"Server encountered unexpected error! Try again later or contact the administrator."
            )
