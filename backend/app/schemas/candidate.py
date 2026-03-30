from pydantic import BaseModel
from datetime import datetime

class CandidateBase(BaseModel):
    filename: str

class CandidateCreate(CandidateBase):
    file_path: str
    raw_text: str | None = None

class CandidateResponse(CandidateBase):
    id: int
    file_path: str
    raw_text: str | None
    created_at: datetime

    class Config:
        from_attributes = True