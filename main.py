from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datafetch import dailydata,errorlogs,dailydatafirst
from storedata import dailylog,errorlog
import time
import os
import shutil  
import pymysql

#define the default download path
download_path = 'C:\\Users\\Gaurav\\Downloads'

options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=C:/Downloads")
driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.injectsolar.com/portal/')

#connecting database
mydb = pymysql.connect(host='localhost',user='root',passwd='gaurav',db='arthadb',autocommit=True,)

cursor = mydb.cursor()
cursor.execute("SET SQL_MODE='ALLOW_INVALID_DATES'")
# login begins
login_id = driver.find_element_by_id('login_id')
login_id.send_keys('triose')

password = driver.find_element_by_id('password')
password.send_keys('triose123')

login_button = driver.find_element_by_tag_name('button')
login_button.click()
# login ends


# getting daily data of Jan and Feb 
file1 = dailydatafirst('January','2020',driver,download_path)
file2 = dailydata('February','2020',driver,download_path)

# #getting error logs from Jan to Feb
errorfile = errorlogs(driver,'1/1/2020','2/29/2020','Cleared Alarms','http://www.injectsolar.com/portal/#/inject-solar/errore-log',download_path)    

#storing in database
dailylog(cursor,download_path,file1,mydb)
dailylog(cursor,download_path,file2,mydb)
errorlog(cursor,download_path,errorfile,mydb)

#close the connection to the database.
mydb.commit()
cursor.close()
driver.quit()

