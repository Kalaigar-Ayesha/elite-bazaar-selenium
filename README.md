## Selenium test suite

This folder contains end-to-end smoke tests for Elite Bazaar using Selenium + pytest.

- Default base URL: `https://elite-bazaar-front.vercel.app/`.
- You can override via the `BASE_URL` env var.

### Prerequisites
- Python 3.10+
- Google Chrome installed

### Setup (Windows PowerShell)
```powershell
cd testing
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# optional: copy defaults
Copy-Item .env.example .env

# set base URL (if you want to override)
$env:BASE_URL="https://elite-bazaar-front.vercel.app/"

# headless off for visible browser (default is headless on)
$env:HEADLESS="0"
```

### Run tests
```powershell
pytest -v
```

### Environment variables
- `BASE_URL`: target site (defaults to `https://elite-bazaar-front.vercel.app/`)
- `HEADLESS`: `1` to run headless (default), `0` to show the browser

### Notes
- WebDriver binaries are auto-managed via `webdriver-manager`.
- Tests are written to be resilient. If a selector is not found (e.g., page layout differs), that test will be `skipped` rather than fail hard.

### Reference
- Deployed frontend: [Elite Bazaar frontend](https://elite-bazaar-front.vercel.app/)

