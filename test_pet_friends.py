import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_petfriends(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open PetFriends base page:
    selenium.get("https://petfriends.skillfactory.ru/login")

    # Wait for the page to load and elements to be present
    WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]"))
    )

    # Find the field for search text input:
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element(By.ID, "email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("shik2@mail.ru")

    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("Innasamos1978!")

    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    # Save cookies of the browser after the login
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(selenium.get_cookies(), cookies)

    # Make the screenshot of browser window:
    selenium.save_screenshot('result_petfriends.png')