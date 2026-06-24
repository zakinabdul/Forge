from pydantic import BaseModel, EmailStr
from typing import List, Dict

class ExperienceItem(BaseModel):
    id: str
    company: str
    role_title: str
    duration: str
    bullets: List[str]

class ProjectItem(BaseModel):
    id: str
    title: str
    description: str
    bullets: List[str]

class MasterProfile(BaseModel):
    user_id: str
    name: str
    email: EmailStr
    skills_inventory: List[str]
    experiences: List[ExperienceItem]
    projects: List[ProjectItem]

class ResumeVariant(BaseModel):
    variant_id: str
    master_profile_id: str
    target_job_title: str
    ai_optimized_summary: str
    visible_experience_bullets: Dict[str, List[bool]]
    visible_project_bullets: Dict[str, List[bool]]
    selected_skills: List[str]
