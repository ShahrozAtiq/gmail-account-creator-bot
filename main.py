from appium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from helper import *
from gsheets import *





def run():
    try:
        # Set up driver
        desired_cap = {}
        userName = "your_user_name"
        accessKey = "your_access_key"
        driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)
        driver.find_element_by_xpath("//*[@text='SIGN IN']").click()
        driver.find_element_by_xpath("//*[@resource-id='view_container']//android.widget.Spinner").click()
        driver.find_element_by_xpath("//android.view.View//android.view.MenuItem[1]").click()
        el=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View")
        el.click()
        sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(fName)
        actions.perform()
        sleep(2)
        el=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View")
        el.click()
        sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(lName)
        actions.perform()
        driver.find_element_by_xpath("//*[@resource-id='collectNameNext']").click()
        driver.find_element_by_xpath('//*[@resource-id="month"]').click()
        driver.find_element_by_xpath(f'//*[@text="{Bmonth}"]').click()
        driver.find_element_by_xpath('//*[@resource-id="day"]').click()
        actions = ActionChains(driver)
        actions.send_keys(Bday)
        actions.perform()
        driver.find_element_by_xpath('//*[@resource-id="year"]').click()
        actions = ActionChains(driver)
        actions.send_keys(Byear)
        actions.perform()
        driver.find_element_by_xpath('//*[@resource-id="gender"]').click()
        driver.find_element_by_xpath('//*[@text="Male"]').click()
        driver.find_element_by_xpath("//*[@resource-id='birthdaygenderNext']").click()
        rnd_email=driver.find_element_by_xpath("//*[@resource-id='selectionc0']")
        email_address=rnd_email.text
        rnd_email.click()
        driver.find_element_by_xpath("//*[@resource-id='next']").click()
        driver.find_element_by_xpath("//*[@resource-id='passwd']").click()
        sleep(2)
        actions = ActionChains(driver)
        actions.send_keys('pa$$word')
        actions.perform()
        driver.find_element_by_xpath("//*[@resource-id='confirm-passwd']").click()
        sleep(2)
        actions = ActionChains(driver)
        actions.send_keys('pa$$word')
        actions.perform()
        driver.find_element_by_xpath("//*[@resource-id='createpasswordNext']").click()
        driver.swipe(364,1843,434,460)
        driver.find_element_by_xpath("//*[@text='Skip']").click()
        driver.find_element_by_xpath("//*[@resource-id='next']").click()
        driver.swipe(364,1843,434,460)
        el=driver.find_element_by_xpath("//*[@resource-id='termsofserviceNext']")
        driver.scroll(el,driver.find_element_by_xpath('//*'))
        sleep(2)
        el.click()
        driver.find_element_by_xpath('//*[@text="More"]').click()
        driver.find_element_by_xpath('//*[@text="Accept"]').click()
        sleep(5)
        worksheet.append_row([email, 'pa$$word', dob])
        writeCred('gmailCreds.csv', [email, 'pa$$word', dob])
    except Exception as e:
        print(e)

    finally:
        driver.quit()

if __name__ == "__main__":
    run()
