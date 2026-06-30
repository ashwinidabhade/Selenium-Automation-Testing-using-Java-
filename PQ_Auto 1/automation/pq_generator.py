from playwright.sync_api import sync_playwright
import os

def capture_screenshots():
    os.makedirs("automation/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:3000")  # Replace with actual URL
        page.screenshot(path="automation/screenshots/landing_page.png")
        print("✅ Screenshot taken.")
        browser.close()
