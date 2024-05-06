from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

options = webdriver.ChromeOptions()

options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PATH = "/Users/113990/src/Python/WebScraper/chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)

driver = webdriver.Chrome(PATH)

driver.get("https://conjuguemos.com/auth/login")

dataFrame = pd.read_csv ('VocabList.csv')

vocabList = {
  "affection" : "la ternura", 
  "annoyed" : "molesta", 
  "apron" : "el delantal", 
  "boo-boo" : "la nana", 
  "bottle" : "el frasco", 
  "boyfriend" : "el pololo", 
  "burning" : "picando", 
  "calves" : "las pantorrillas", 
  "carefully" : "detenidamente", 
  "commoner" : "el plebeyo", 
  "complexion" : "la tez", 
  "cops and robbers" : "el paco-ladrón", 
  "country estates" : "los fundos", 
  "disapproving" : "reporobatoria", 
  "do not enter" : "No se meta", 
  "except" : "salvo", 
  "exit" : "el mutis", 
  "face" : "el rostro", 
  "fight" : "la riña", 
  "First Aid Station" : "la posta", 
  "foolishness" : "Tonterías", 
  "frames" : "los cuadros", 
  "gentleman" : "el caballero", 
  "He’s just like his father" : "Salió al padre", 
  "hideous" : "espantosa", 
  "kick" : "la patada", 
  "lack of enthusiasm" : "con displicencia", 
  "low class swine" : "rota cochina", 
  "man belonging to the poor class" : "el roto", 
  "mistress" : "la patrona", 
  "not even" : "ni siquiera", 
  "outfit" : "la tenida", 
  "perhaps" : "acaso", 
  "petrol" : "la bencina", 
  "pigsty" : "la pocilga", 
  "Prince Charmings" : "los príncipes azules", 
  "quarrelsome" : "peleador", 
  "rear end" : "el traste", 
  "reluctantly" : "con desgano", 
  "room" : "la pieza", 
  "sedative" : "el sedante", 
  "shore" : "la orilla", 
  "small land parcel" : "la cuadra", 
  "sunstroke" : "la insolación", 
  "tent/ canopy" : "la carpa", 
  "they have left (over)" : "les sobra", 
  "this is the limit" : "esto es el colmo", 
  "to address as tú" : "tutear", 
  "to become rude" : "insolentarse", 
  "to begin" : "principiar", 
  "to burst out laughing" : "lanzar una carcajada", 
  "to dare to" : "atreverse a", 
  "to destroy" : "botar", 
  "to go forward" : "adelantarse", 
  "to head towards" : "dirigirse a", 
  "to kidnap" : "raptar", 
  "to leaf through, to skim" : "hojear", 
  "to lend" : "prestar", 
  "to look down" : "bajar la vista", 
  "to make a mistake" : "equivocarse", 
  "to move away" : "retirarse", 
  "to prepare oneself" : "aprontarse", 
  "to pull off" : "tirar", 
  "to rent" : "arrendar", 
  "to ruin" : "deshacer", 
  "to sit up" : "incorporarse", 
  "to sniffle" : "sorberse los mocos", 
  "to spend the summer" : "veranear", 
  "to stay stretched out" : "permanecer tendida", 
  "to stop" : "detenerse", 
  "to struggle" : "forcejear", 
  "to take advantage of" : "aprovechar", 
  "to take off" : "sacarse", 
  "to think over" : "recapacitar", 
  "to unbutton" : "desabrocharse", 
  "to weave" : "tejer", 
  "underwear" : "los calzones", 
  "veins" : "las venas", 
  "well restrained/subdued" : "bien sujeta", 
  "worked up" : "acalorada"
}

def login():
  #My Login
  # username = '3230360'
  # password = 'glenbard'
  
  #Jainie Login
  username = '3230434@glenbard.org'
  password = 'Shah2004!'

  usernameField = driver.find_element(by=By.ID, value= 'identity')
  usernameField.send_keys(username)
  passwordField = driver.find_element(by=By.ID, value='password')
  passwordField.send_keys(password)
  loginButton = driver.find_element(by= By.ID, value='login_btn')
  loginButton.click()

def selectList():
  #driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3)")
  
  #This needs to change per list
  listButton = driver.find_element(by=By.XPATH, value = '//*[@id="activities"]/div[1]/span/a')
  listButton.click()
  practiceButton = driver.find_element(by=By.XPATH, value='//*[@id="practice"]')
  practiceButton.click()
  timeInput = driver.find_element(by=By.ID, value= 'set_time_input')
  time.sleep(1)
  timeInput.send_keys(Keys.BACK_SPACE)
  timeInput.send_keys("15")
  startButton = driver.find_element(by=By.XPATH, value='//*[@id="timerModal"]/div/div[3]/button')
  startButton.click()

def getAnswer(word:str):
  return vocabList.get(word)

time.sleep(1)
login()
time.sleep(1)
selectList()
time.sleep(1)

for i in range(103):
  time.sleep(1)
  englishWordElement = driver.find_element(by=By.ID, value='question-input')
  englishWord = englishWordElement.get_attribute("innerHTML")
  answer = getAnswer(englishWord)
  print(f"{englishWord}, {answer}")
  answerField = driver.find_element(by=By.ID, value='answer-input')
  answerField.send_keys(answer)
  answerField.send_keys(Keys.RETURN)
  time.sleep(.5)

time.sleep(900)

driver.close()



