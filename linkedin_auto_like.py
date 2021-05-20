import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


links = [
    "https://www.linkedin.com/posts/sidd-oo_100daysofcode-devsnestday21-devsnest6monthschallenge-activity-6789459261542973440-x7FX/",
    "https://www.linkedin.com/posts/ross-nelson-32493684_devsnest6monthschallenge-devsnestday21-slowandsteady-activity-6788661474186338304-Dx0z"
]

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")

while "1" != input("press 1 when signed in: "):
    pass
for link in links:
    try:
        print("accessing link ", link)
        driver.get(link)
        sleep(2)
        el = driver.find_element_by_class_name("react-button__trigger")
        if "false" == el.get_attribute("aria-pressed"):
            print("liking")
            el.click()
            print("liked")
            sleep(1)
        else:
            print("already processed link ", link)
    except Exception as e:
        print("error processing link\nlink: ", link, "\nerror",  e)

driver.close()