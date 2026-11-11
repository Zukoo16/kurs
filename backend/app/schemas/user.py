from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str
    role: str = "student"


class UserProfileResponse(UserBase):
    id: int
    keycloak_id: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CurrentUserResponse(BaseModel):
    id: str
    username: str
    email: str
    roles: list[str]

