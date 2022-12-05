import time
from selenium.webdriver.common.by import By
from appium import webdriver

desired_cap ={
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:platformVersion": "9",
    "appium:deviceName": "Android Emulator",
    "appium:app": "E:\\Appium\\PraavaAppium\\PraavaAppPractise\\Apk\\Praava Health_1.19_Apkpure.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(10)
time.sleep(3)

driver.find_element(By.ID, "com.praava.patientportal:id/signup_link").click()
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/mobile").send_keys("01852821994")
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/username").send_keys("kibria sarawar")
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/password").send_keys("12345678")
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/re_password").send_keys("12345678")
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/emailId").send_keys("kibriasarawar.qups@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "com.praava.patientportal:id/sign_up_button").click()
time.sleep(3)
driver.find_element(By.ID, "android:id/button1").click()
time.sleep(3)




