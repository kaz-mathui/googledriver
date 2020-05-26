from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_csv('/Users/kaz/Downloads/python_lesson/noun_data1.csv', encoding='UTF-8',dtype='object',names=['a'])
print(df.iat[0,0])
#
# driver = webdriver.Chrome("/Users/kaz/Downloads/chromedriver")
# # driver.get("http://www.related-keywords.com/")
print(len(df.index))
list =[]
for i in range(len(df.index)):
    driver = webdriver.Chrome("/Users/kaz/Downloads/chromedriver")
    driver.get("http://www.related-keywords.com/")
    word = df.iat[i,0]
    driver.find_element_by_name('keyword').send_keys(word)
    driver.find_element_by_css_selector("input[type='submit'][value='取得開始']").click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'meta')))

    print(driver.find_element_by_tag_name('textarea').get_attribute('value'))
    list.append(driver.find_element_by_tag_name('textarea').get_attribute('value'))
    driver.close()
    driver.quit()
filename = "scraping.tsv"
pd.DataFrame(list).to_csv(filename,sep='\t',index =False)


#
# driver = webdriver.Chrome("/Users/kaz/Downloads/chromedriver")
# driver.get("http://www.related-keywords.com/")
#
#
# driver.find_element_by_name('keyword').send_keys("Anytype")
# driver.find_element_by_css_selector("input[type='submit'][value='取得開始']").click()
#
# WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'meta')))
#
# print(driver.find_element_by_tag_name('textarea').get_attribute('value'))

# driver.close()
# driver.quit()
