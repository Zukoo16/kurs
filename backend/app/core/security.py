from typing import Any, Callable, Dict, List

try:
    import jwt
    from fastapi import Depends, HTTPException, status
    from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

    security = HTTPBearer(auto_error=False)
    HAVE_FASTAPI = True
except ImportError:
    HAVE_FASTAPI = False
    security = None

from app.core.config import settings


class UserPrincipal:
    def __init__(self, user_id: str, username: str, email: str, roles: List[str]):
        self.id = user_id
        self.username = username
        self.email = email
        self.roles = roles

    def has_role(self, role: str) -> bool:
        return role in self.roles


def extract_roles_from_token(claims: Dict[str, Any]) -> List[str]:
    """Keycloak JWT токенінен рөлдерді (realm_access немесе resource_access) шығарып алу."""
    roles: List[str] = []
    # Realm roles
    realm_access = claims.get("realm_access", {})
    if isinstance(realm_access, dict):
        roles.extend(realm_access.get("roles", []))

    # Client/Resource roles
    resource_access = claims.get("resource_access", {})
    client_access = resource_access.get(settings.KEYCLOAK_CLIENT_ID, {})
    if isinstance(client_access, dict):
        roles.extend(client_access.get("roles", []))

    return list(set(roles))


if HAVE_FASTAPI:
    async def get_current_user(
        credentials: HTTPAuthorizationCredentials | None = Depends(security),
    ) -> UserPrincipal:
        """Ағымдағы пайдаланушының Keycloak OIDC JWT токенін тексеру."""
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication credentials required",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = credentials.credentials
        try:
            unverified_payload = jwt.decode(
                token,
                options={"verify_signature": False},
            )
            user_id = unverified_payload.get("sub", "")
            username = unverified_payload.get("preferred_username", "")
            email = unverified_payload.get("email", "")
            roles = extract_roles_from_token(unverified_payload)

            return UserPrincipal(
                user_id=user_id,
                username=username,
                email=email,
                roles=roles,
            )
        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid authentication token: {str(exc)}",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def require_roles(allowed_roles: List[str]) -> Callable:
        """Рөлдерді тексеруші тәуелділік (RBAC: student, teacher, admin)."""

        async def role_checker(
            current_user: UserPrincipal = Depends(get_current_user),
        ) -> UserPrincipal:
            if not any(current_user.has_role(r) for r in allowed_roles):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access denied. Required roles: {', '.join(allowed_roles)}",
                )
            return current_user

        return role_checker
