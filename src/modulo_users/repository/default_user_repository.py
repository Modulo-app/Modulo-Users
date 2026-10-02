from modulo_users.repository.user_repository import UserRepository
from modulo_users.entity.user_entity import UserEntity
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timezone

class DefaultUserRepository(UserRepository):
    
    def __init__(self, database: Session):
        self.database = database
    
    def get_by_provider(self, provider: str, provider_id: str):
        return self.database.scalars(
            select(UserEntity)
                .where(UserEntity.provider == provider)
                .where(UserEntity.provider_id == provider_id)
        ).first()
    
    def create(self, email: str, first_name: str, provider: str, provider_id: str) -> UserEntity:
        user = UserEntity()
        user.email = email
        user.first_name = first_name
        user.provider = provider
        user.provider_id = provider_id
        user.created_at = datetime.now(timezone.utc)
        
        self.database.add(user)
        self.database.commit()
        self.database.refresh(user)
        
        return user