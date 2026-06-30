from src.crawler.browser import Browser


browser = Browser()

browser.start()

browser.open("https://www.youtube.com")

print(browser.title())

input("\nPress ENTER to close...")

browser.close()