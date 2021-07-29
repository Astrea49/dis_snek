from typing import Optional

from dis_snek.models.enums import UserFlags, PremiumTypes


class BaseUser:
    __slots__ = "id", "username", "discriminator", "avatar"

    def __init__(self, data: dict):
        self.id: int = data["id"]
        self.username: str = data["username"]
        self.discriminator: int = data["discriminator"]
        self.avatar = data["avatar"]  # todo convert to asset

    def __str__(self):
        return f"{self.username}#{self.discriminator}"

    @property
    def mention(self):
        return f"<@{self.id}>"


class User(BaseUser):
    __slots__ = (
        "is_bot",
        "is_system",
        "mfa_enabled",
        "locale",
        "verified",
        "email",
        "flags",
        "premium_type",
        "public_flags",
        "banner",
        "banner_color",
        "accent_color",
    )

    def __init__(self, data: dict):
        super().__init__(data)
        self.is_bot: bool = data.get("bot", False)
        self.is_system: bool = data.get("system", False)
        self.mfa_enabled: bool = data.get("mfa_enabled", False)
        self.locale: Optional[str] = data.get("locale")
        self.verified: Optional[bool] = data.get("verified")
        self.email: Optional[str] = data.get("email")
        self.flags: UserFlags = UserFlags(data.get("flags", 0))
        self.premium_type: PremiumTypes = PremiumTypes(data.get("premium_type", 0))
        self.public_flags: UserFlags = UserFlags(data.get("public_flags", 0))
        self.banner = data.get("banner")  # todo convert to asset
        self.banner_color = data.get("banner_color")  # todo convert to color objects
        self.accent_color = data.get("accent_color")