from pathlib import Path
from datetime import datetime

SCREENSHOT_DIR = Path(__file__).resolve().parent.parent / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

def capture_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOT_DIR / f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(path))
    return path
