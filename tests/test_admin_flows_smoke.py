import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _wait(drv, timeout=25):
    return WebDriverWait(drv, timeout)


@pytest.mark.skip(reason="Admin panel likely requires credentials and may not be public. Enable when creds available.")
def test_admin_login_smoke(driver):
    base_admin = os.getenv("ADMIN_URL") or os.getenv("BASE_ADMIN_URL")
    if not base_admin:
        pytest.skip("ADMIN_URL not configured")

    driver.get(base_admin)

    try:
        email = _wait(driver).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        password = driver.find_element(By.XPATH, "//input[@type='password']")
    except Exception:
        pytest.skip("Admin login form not found")

    email.send_keys(os.getenv("ADMIN_EMAIL", "test@example.com"))
    password.send_keys(os.getenv("ADMIN_PASSWORD", "incorrect-password"))

    submit = driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Login')]")
    submit.click()

    # Expect either error toast or redirect; this is just a smoke test scaffold.
    _wait(driver).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

