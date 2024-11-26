import time

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Open browser with UI
        page = browser.new_page()
        page.goto("https://ai-interview-mockinterviewtool.vercel.app/dashboard")  # Navigate to a URL
        page.screenshot(path="screenshot.png")  # Take a screenshot
        browser.close()  # Close the browser

if __name__ == "__main__":
    run()
time.sleep(10)
 
