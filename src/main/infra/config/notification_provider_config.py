from src.main.infra.environment.environment_consts import NotificationProviderConsts
from src.main.business.notification.registry.notification_provider_registry import NotificationProviderRegistry
from src.main.business.notification.provider.whatsapp_notification_provider_impl import WhatsappNotificationProviderImpl
from src.main.business.notification.provider.google_calendar_notification_provider_impl import GoogleCalendarNotificationProviderImpl


def create_notification_providers() -> NotificationProviderRegistry:
    """
    Creates and records the notification providers available in the application.
    """
    return NotificationProviderRegistry() \
        .register(NotificationProviderConsts.WHATSAPP, WhatsappNotificationProviderImpl()) \
        .register(NotificationProviderConsts.GOOGLE_CALENDAR, GoogleCalendarNotificationProviderImpl())
