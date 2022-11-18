from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name="username"]").send_keys("ADMIN")
#driver.find_element(By.NAME("Username")).send_keys("ADMIN")
#driver.find_element(By.NAME("Password")).send_keys("admin123")
#driver.find_element(By.TAG_NAME("Login")).click()



