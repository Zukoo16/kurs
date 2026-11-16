from fastapi import APIRouter, Depends

from app.core.security import UserPrincipal, get_current_user, require_roles
from app.schemas.user import CurrentUserResponse

router = APIRouter()


@router.get("/me", response_model=CurrentUserResponse)
async def get_me(user: UserPrincipal = Depends(get_current_user)) -> CurrentUserResponse:
    """Ағымдағы пайдаланушының мәліметтері мен Keycloak рөлдері."""
    return CurrentUserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        roles=user.roles,
    )


@router.get("/admin/dashboard")
async def admin_dashboard(user: UserPrincipal = Depends(require_roles(["admin"]))) -> dict:
    """Тек 'admin' рөлі бар пайдаланушыларға арналған аймақ."""
    return {
        "message": f"Қош келдіңіз, әкімші {user.username}!",
        "access": "granted",
        "role": "admin",
    }


@router.get("/mentor/students")
async def mentor_students(
    user: UserPrincipal = Depends(require_roles(["mentor", "admin"])),
) -> dict:
    """Менторлар мен әкімшілерге арналған аймақ (жоспарлы placeholder)."""
    return {
        "message": f"Ментор интерфейсі: {user.username}",
        "access": "granted",
    }


@router.get("/student/materials")
async def student_materials(
    user: UserPrincipal = Depends(require_roles(["student", "mentor", "admin"])),
) -> dict:
    """Студенттерге, менторларға және әкімшілерге қолжетімді аймақ."""
    return {
        "message": f"Студенттік материалдар: {user.username}",
        "access": "granted",
    }

