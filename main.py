from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# load chess files
df = pd.read_csv("generated_data_last_500.csv")
df = df[["moves", "explanation"]]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

for i in range(5):

    # print explanation
    print()
    print(f"===================================== Game {i} ====================================")
    print(df.iloc[i]["explanation"])

    # selenium
    driver.get("https://www.chess.com/analysis?tab=analysis")
    # input box
    input_box = driver.find_element(By.CLASS_NAME, "load-from-pgn-textarea")
    input_box.send_keys(df.iloc[i]["moves"])
    # add game
    driver.find_element(By.XPATH, "//button[contains(., 'Add Game(s)')]").click()
    
    # wait for key press to go to next iteration
    input("Press Enter to continue...")

driver.quit()
