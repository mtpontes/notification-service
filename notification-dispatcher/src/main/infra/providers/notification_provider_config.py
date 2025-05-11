from src.main.infra.providers.notification_provider_enum import NotificationProviderEnum
from src.main.infra.providers.notification_provider_registry import NotificationProviderRegistry
from src.main.business.provider.whatsapp_notification_provider_impl import WhatsappNotificationProviderImpl
from src.main.business.provider.google_calendar_notification_provider_impl import GoogleCalendarNotificationProviderImpl


def load_notification_provider_registry() -> NotificationProviderRegistry:
    """
    Creates and records the notification providers available in the application.
    """
    
    return NotificationProviderRegistry() \
        .register(NotificationProviderEnum.WHATSAPP, WhatsappNotificationProviderImpl()) \
        .register(NotificationProviderEnum.GOOGLE_CALENDAR, GoogleCalendarNotificationProviderImpl())
