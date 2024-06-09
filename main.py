from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# load chess files
df = pd.read_csv("generated_data_last_500.csv")
df = df[["moves", "explanation"]]

# print explanation
print(df.iloc[0]["explanation"])

# selenium
driver.get("https://www.chess.com/analysis?tab=analysis")
# input box
input_box = driver.find_element(By.CLASS_NAME, "load-from-pgn-textarea")
input_box.send_keys(df.iloc[0]["moves"])
# add game
driver.find_element(By.XPATH, "//button[contains(., 'Add Game(s)')]").click()

# dont close
try:
    while True:
        driver.title
except KeyboardInterrupt:
    print("Script interrupted. Closing the browser.")
finally:
    driver.quit()
