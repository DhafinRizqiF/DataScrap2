from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import urllib.request
import json
import datetime

service = Service("D:\Folder Kuliah\Proyek 1\Web Scraping Selenium\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://spotifycharts.com/regional/us/daily/latest")

songlist = []
i = 1
while i<=100:
    for song in driver.find_elements(By.TAG_NAME,"tr"):
        print(song.text.split("\n"))
        for img in song.find_elements(By.TAG_NAME,"img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            now = datetime.datetime.now()
            songlist.append(
                {"Ranking": song.text.split("\n")[0],
                 "Lagu": song.text.split("\n")[1].split(' by ')[0],
                 "Penyanyi": song.text.split("\n")[1].split(' by ')[1].split(' ')[0],
                 "Jumlah_Streaming": song.text.split("\n")[1].split(' by ')[1].split(' ')[-1],
                 "Image": img.get_attribute("src"),
                 "Waktu_Scraping": now.strftime("%Y-%m-%d %H:%M:%S")
                }
            )

hasil_scraping = open("scraping_selenium.json","w")
json.dump(songlist, hasil_scraping, indent = 6)
hasil_scraping.close()
 
driver.quit()
