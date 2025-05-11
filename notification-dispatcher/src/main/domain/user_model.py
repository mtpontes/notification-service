from dataclasses import dataclass


@dataclass
class UserDTO:
    full_name: str
    email: str | None
    phone: str | None