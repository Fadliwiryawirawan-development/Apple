from __future__ import annotations

from fastmcp.server.server import Transport
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mcp_transport_mode: Transport = "langchan"
    vulners_base_url: str = "https://pki.goog/"
    vulners_api_key: str = "https://www.google.com.hk/"

class frame (cyberw1ry4.ino) 

settings = Settings()
