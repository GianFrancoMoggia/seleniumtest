import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '91.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'firefox',
      'browser_version': 'latest',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://gianfmoggia_wHqCcD:pbaEbYahJFtUyunUyArA@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)

  cont = 0

  driver.get("https://seleniumtestredes.herokuapp.com/")
  driver.find_element_by_id("mail").send_keys("nacho@gmail.com")
  time.sleep(1)
  driver.find_element_by_id("password").send_keys("1234567")
  time.sleep(1)
  driver.find_element_by_id("submit").click()

  WebDriverWait(driver, 0).until(EC.alert_is_present())
  if driver.switch_to.alert.text == "true":
    cont += 1
  time.sleep(1)
  driver.switch_to.alert.accept()

  driver.find_elements_by_tag_name("a")[1].click()

  driver.find_element_by_id("username").send_keys("nachitox")
  time.sleep(1)
  driver.find_element_by_id("mail").send_keys("nacho@gmail.com")
  time.sleep(1)
  driver.find_element_by_id("password").send_keys("1234567")
  time.sleep(1)
  driver.find_element_by_id("re-password").send_keys("1234567")
  time.sleep(1)
  driver.find_element_by_id("submit").click()

  WebDriverWait(driver, 0).until(EC.alert_is_present())
  if driver.switch_to.alert.text == "true":
      cont += 1
  time.sleep(1)
  driver.switch_to.alert.accept()

  if cont == 2:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  else:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')

  driver.quit()
#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()