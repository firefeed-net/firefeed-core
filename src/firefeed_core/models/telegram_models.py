# models/telegram_models.py - Telegram-specific data models
from typing import Optional
from pydantic import BaseModel


class TelegramPublication(BaseModel):
    """Telegram publication tracking model."""
    translation_id: Optional[int] = None
    channel_id: int
    message_id: int


class FeedLimits(BaseModel):
    """Feed publication limits model."""
    cooldown_minutes: int = 10
    max_news_per_hour: int = 10


class UserSettings(BaseModel):
    """User settings model."""
    user_id: int
    language: str = "en"
    timezone: str = "UTC"
    notifications_enabled: bool = True
    max_articles_per_notification: int = 10
    notification_interval: int = 60


class UserStats(BaseModel):
    """User statistics model."""
    user_id: int
    subscription_count: int = 0
    notifications_sent: int = 0
    articles_read: int = 0
    last_activity: str  # ISO date-time format


class Subscription(BaseModel):
    """User subscription model."""
    user_id: int
    category_id: int
    category_name: str
    subscribed_at: str  # ISO date-time format


__all__ = [
    'TelegramPublication',
    'FeedLimits',
    'UserSettings',
    'UserStats',
    'Subscription',
]