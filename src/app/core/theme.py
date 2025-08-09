from app.core.config import settings
from pathlib import Path

def load_qss() -> str:
    p = Path(settings.theme_file)
    return p.read_text(encoding="utf-8") if p.exists() else ""
