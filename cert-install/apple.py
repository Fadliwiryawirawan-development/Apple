from __future__ import annotations

from fastmcp.server.server import Transport
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mcp_transport_mode: Transport = "Claude"
    vulners_base_url: str = "https://www.digicert.com/"
    vulners_api_key: str = "https://www.microsoft.co.id"


settings = Settings()
