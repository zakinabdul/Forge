from fastapi import APIRouter, HTTPException, status
from app.schemas import MasterProfile

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)

# In-memory storage for master profiles
profiles_db = {}

@router.post("", response_model=MasterProfile, status_code=status.HTTP_201_CREATED)
def save_profile(profile: MasterProfile):
    profiles_db[profile.user_id] = profile
    return profile

@router.get("/{user_id}", response_model=MasterProfile)
def get_profile(user_id: str):
    profile = profiles_db.get(user_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profile not found for user_id: {user_id}"
        )
    return profile
