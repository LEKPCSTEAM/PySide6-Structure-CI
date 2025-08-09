from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "src" / "app" / "assets"
STYLES = ASSETS / "styles"
FONTS = ASSETS / "fonts"
ICONS = ASSETS / "icons"

load_dotenv()


class Settings(BaseModel):
    app_title: str = os.getenv("APP_TITLE", "structure Ui UI")
    theme_file: str = os.getenv("THEME_FILE", str(STYLES / "app.qss"))


settings = Settings()
