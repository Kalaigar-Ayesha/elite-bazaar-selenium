# Elite Bazaar Selenium Test Suite

Welcome to the **Elite Bazaar** end-to-end smoke testing suite! This project uses **Selenium** with **pytest** to automate critical user flows and ensure the core functionalities of the Elite Bazaar e-commerce platform are working as expected.

---

## 🚀 Overview

This test suite covers essential smoke tests designed to validate the main features of Elite Bazaar. It helps catch bugs early and maintain a high standard of quality with automated UI checks.

---

## 🌐 Default Setup

- **Base URL:** [`https://elite-bazaar-front.vercel.app/`](https://elite-bazaar-front.vercel.app/)  
  This can be overridden by setting the `BASE_URL` environment variable.

---

## ⚙️ Prerequisites

- Python 3.10 or higher  
- Google Chrome installed on your machine

---

## 🔧 Quick Setup (Windows PowerShell)

```powershell
# Navigate to your project directory
cd testing

# Create a Python virtual environment and activate it
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install the required dependencies
pip install -r requirements.txt

# (Optional) Copy environment variable template
Copy-Item .env.example .env

# Override base URL if needed (default is Elite Bazaar frontend)
$env:BASE_URL="https://elite-bazaar-front.vercel.app/"

# Run tests with visible browser (default is headless)
$env:HEADLESS="0"
