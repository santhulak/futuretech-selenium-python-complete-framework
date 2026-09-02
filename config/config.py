from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BASE_URL = (ROOT_DIR / "demo_app" / "login.html").as_uri()
DEFAULT_TIMEOUT = 10
HEADLESS = False
