from selenium import webdriver
import argparse as ap
from selenium.webdriver.common.keys import Keys
import time

parser = ap.ArgumentParser(description='Enter your email ID, Password, username')
parser.add_argument("email", help="Enter your email")
parser.add_argument("password", help="Enter your password")
parser.add_argument("username", help="Enter your twitter username")
args = parser.parse_args()

path = r"C:\Users\shria\Desktop\Selenium\geckodriver\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)

driver.maximize_window()
driver.get("https://www.twitter.com/")

time.sleep(3)

emailID = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input')
emailID.send_keys(args.email)

passw = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input')
passw.send_keys(args.password)

loginBtn1=driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div')
loginBtn1.click()

#The below block is in case you get an additional login prompt, that sometimes happens if you are working with twitter automation.

#time.sleep(3)

#scam1 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
#scam1.send_keys(args.username)

#scam2 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
#scam2.send_keys(args.password)
#loginBtn2=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
#loginBtn2.click()

time.sleep(3)

firstTrend = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div[3]/div/div/div[1]/div[1]/div[1]/span").text
secondTrend = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div[3]/div/div/div[1]/div[2]/span").text


bigResultBtn=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div[3]/div')
bigResultBtn.click()

time.sleep(3)

majorNewsMatter = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div[3]/div/span").text

with open("Twitterdata.txt", "w+") as f:
    f.write("2nd Test" + "\n" + firstTrend + "\n" + secondTrend + "\n" + majorNewsMatter )

time.sleep(5)

search = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
search.send_keys("COVID", Keys.ENTER)

time.sleep(15)
driver.close()
