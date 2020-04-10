import os
import urllib.request
from time import sleep
from selenium import webdriver


def scroll_to_end(webdriver):
    webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)


DIR = "picture/"
query = input("query : ")
url = "https://www.google.co.in/search?q=음식점+"+query+"&source=lnms&tbm=isch"
browser = webdriver.Chrome('./api/crawling/chromedriver.exe')
browser.get(url)
scroll_to_end(browser)
thumbnail_results = browser.find_elements_by_css_selector("img.rg_i")
# thumbnail_results.click()
number_results = len(thumbnail_results)

img_urls = set()
for img in thumbnail_results:
    if img.get_attribute('src'):
        img_urls.add(img.get_attribute('src'))

if not os.path.exists(DIR):
    os.mkdir(DIR)

DIR = os.path.join(DIR, query + "/")

if not os.path.exists(DIR):
    os.mkdir(DIR)

for i, img_url in enumerate(img_urls):
    saveName = DIR + '%03d' % i + ".jpg"
    urllib.request.urlretrieve(img_url, saveName)

browser.close()

# for img in thumbnail_results[:number_results]:
#     try:
#         img.click()
#         sleep(0.5)
#     except Exception:
#         continue


# os.mkdir(DIR)
# print(os.path.join(DIR, ""))
