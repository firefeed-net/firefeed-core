# models/translation_models.py - Translation data models
from typing import Optional, Dict
from pydantic import BaseModel


class PreparedRSSItem(BaseModel):
    """Model for storing prepared RSS item."""
    original_data: Dict[str, str]
    translations: Dict[str, Dict[str, str]]
    image_filename: Optional[str] = None
    video_filename: Optional[str] = None
    feed_id: int


__all__ = [
    'PreparedRSSItem',
]