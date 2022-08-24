from itertools import count
from re import S
from selenium import webdriver
from script import script
import pandas as pd

driver = webdriver.Edge(executable_path="/Users/matt/Drivers/edgedriver_mac64/msedgedriver")
driver.maximize_window()
tcount = 0
fcount = 0
count = 0 
df = pd.read_csv('top-1m.csv')
df = df['url']
exp_list = []

for url in df[:200]:
    url = "https://"+url
    try:
        driver.get(url)
        returnval = driver.execute_script(script)
        if returnval == True:
            driver.get_screenshot_as_file(f"Screenshots/TRUE/{tcount}.png")
            tcount += 1
            count+=1
        else:
            driver.get_screenshot_as_file(f"Screenshots/FALSE/{fcount}.png")
            fcount += 1
            count+=1
            
    except:
        print(f"exception: {count}")
        exp_list.append(count)
        count+=1

print(count)
print(exp_list)
driver.close()