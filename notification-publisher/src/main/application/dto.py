from typing import TypedDict


class EventDispatcherDTO(TypedDict):
    title: str
    description: str
    dt_init: str
    dt_end: str


class UserDispatcherDTO(TypedDict):
    full_name: str
    email: str
    phone: str