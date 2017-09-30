from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
time.sleep(10)
dotButton = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/button')
dotButton.click()
time.sleep(1)
groupButton = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
groupButton.click()
time.sleep(2)
target1 = 'Mom'
target2 = 'Dad'
#searchBoxPath = '//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[1]/div/div/input'
#searchInput = wait.until(EC.presence_of_all_elements_located((By.XPATH, searchBoxPath)))
#searchInput.send_keys(target1 + Keys.ENTER)
#searchInput.send_keys(target2 + Keys.ENTER)
searchBox = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[1]/div/div/input')
searchBox.send_keys(target1)
result = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[2]/div/div/div/div[1]')
result.click()
time.sleep(2)
searchBox.send_keys(target2)
result = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[2]/div/div/div/div[1]')
result.click()
time.sleep(2)
nextButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/span/div')
nextButton.click()
groupNameBox = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[2]/div/div[2]/div[1]/div')
groupNameBox.send_keys('Sample group')
time.sleep(2)
avatarOverlay = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/div[1]/div/div/span/div')
avatarOverlay.click()
time.sleep(1)
uploadButton = driver.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/li[2]/div')
#driver.find_element_by_css_selector('input[type="file"]').clear()
#driver.find_element_by_css_selector('input[type="file"]').send_keys('G:\Pictures\Batman-and-Heath-Ledger-Joker.jpg')
driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("G:\\Pictures\\Batman-and-Heath-Ledger-Joker.jpg")
time.sleep(8)
adjustButton = driver.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div')
adjustButton.click()
time.sleep(2)
finalButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div/span/div/div')
finalButton.click()
time.sleep(4)
