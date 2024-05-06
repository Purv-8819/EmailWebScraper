from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PATH = "/Users/113990/src/Python/WebScraper/chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)

driver = webdriver.Chrome(PATH)

linkList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

driver.get("https://www.glenbardnorthhs.org/staff-directory/")
print(driver.title)

list = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "staff-listing-items"))
    )
listText = list.text

while("Wit" not in listText):
  list = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "staff-listing-items"))
    )
  listText = list.text
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(3)

#print("this is: ")
#print(list.text)

listMedial = listText.splitlines()
#print(listFinal)
emailText = "@"
teacherText = "Teacher"
chairText = "Chair"
listFinal = []

print(listText)
print()
print(listMedial)
print()

for item in listMedial:
  if emailText in item:
    index = listMedial.index(item)
    titleIndex = index -3
    if teacherText in listMedial[titleIndex] or chairText in listMedial[titleIndex]:
      listFinal.append(item)


print()
print(listFinal)

file = open('TeacherEmailList.txt', 'w')
for email in listFinal:
  file.write(email+"\n")

file.close()
driver.close()


