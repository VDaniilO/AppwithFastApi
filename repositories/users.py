from typing import List

from db.info import users
from core.security import hash_password
from models.user import User, UserSend
from .mainReposit import BaseRepository

class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query = query)

#for get user on id
    async def get_by_id(self, id: int) -> User:
        query = users.select().where(users.c.id==id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

#for create a new user
    async def create(self, u: UserSend) -> User:
        user = User(
            email = u.email,
            name = u.name,
            surname = u.surname,
            gender = u.gender,
            description = u.description,
            hashed_password = hash_password(u.password),
        )

        values = {**user.dict()}
        values.pop("id", None)

        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

#for auth
    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email==email).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
        return

#for update info about user
    async def update(self, id: int, u: UserSend) -> User:
        user = User(
            id = id,
            email = u.email,
            name = u.name,
            surname = u.surname,
            gender = u.gender,
            description = u.description,
            hashed_password = hash_password(u.password),
        )
        values = {**user.dict()}
        values.pop("create_at", None)
        values.pop("id", None)

        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user
