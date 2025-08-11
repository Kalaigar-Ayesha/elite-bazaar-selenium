import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv is optional; environment variables can be provided by the shell
    pass


def _get_base_url() -> str:
    return os.getenv("BASE_URL", "https://elite-bazaar-front.vercel.app/").rstrip("/")


@pytest.fixture(scope="session")
def base_url() -> str:
    return _get_base_url()


@pytest.fixture(scope="session")
def driver():
    headless = os.getenv("HEADLESS", "1") != "0"

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)

    yield drv
    drv.quit()

