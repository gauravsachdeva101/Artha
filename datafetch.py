import time
import os 

def dailydatafirst(month,year,driver,path):
    time.sleep(3)
    daybutton = driver.find_element_by_id('nav-profile-tab')
    driver.execute_script("arguments[0].click()", daybutton)
    #opening calendar and selecting the required month
    time.sleep(3)
    calendar = driver.find_element_by_css_selector("button[aria-label='Open calendar']")
    driver.execute_script("arguments[0].click()",calendar)

    time.sleep(3)
    clickyear = driver.find_element_by_css_selector("td[aria-label = '{}']".format(year))
    driver.execute_script("arguments[0].click()", clickyear)
    
    time.sleep(5)
    clickmonth = driver.find_element_by_css_selector("td[aria-label = '{}']".format(month + ' ' + year))
    driver.execute_script("arguments[0].click()", clickmonth)

    time.sleep(10)
    driver.find_element_by_class_name("highcharts-exporting-group").click() 
    #downloading the report
    time.sleep(5)
    download = driver.find_element_by_xpath("//*[contains(text(), 'Download CSV')]")
    driver.execute_script("arguments[0].click()", download)
    time.sleep(5)
    #renaming downloaded file
    name= month+year+'.csv'
    os.rename(path+'\\chart.csv',path+'\\'+name) 
    return name

def dailydata(month,year,driver,path):
    time.sleep(3)
    #opening calendar and selecting the required month
    calendar = driver.find_element_by_css_selector("button[aria-label='Open calendar']")
    driver.execute_script("arguments[0].click();",calendar)

    time.sleep(3)
    year_picker = driver.find_element_by_css_selector("td[aria-label = '{}']".format(year))
    driver.execute_script("arguments[0].click()", year_picker)

    time.sleep(3)
    month_picker = driver.find_element_by_css_selector("td[aria-label = '{}']".format(month + ' ' + year))
    driver.execute_script("arguments[0].click();", month_picker)
    #selecting and downloading file
    time.sleep(10)
    driver.find_element_by_class_name("highcharts-exporting-group").click() 

    download = driver.find_element_by_xpath("//*[contains(text(), 'Download CSV')]")
    driver.execute_script("arguments[0].click();", download)
    time.sleep(5)
    #renaming the downloaded file
    name= month+year+'.csv'
    os.rename(path+'\\chart.csv',path+'\\'+name) 
    return name

def errorlogs(driver,start_date,end_date,alarms,url,path):
    time.sleep(5)
    #going to the error log url
    driver.get(url)
    time.sleep(5)
    #selecting the required months  
    driver.find_element_by_id("nav-home-tab").click()
    time.sleep(3)
    driver.find_element_by_css_selector("input[formcontrolname='clearStart_dt']").send_keys(start_date)
    time.sleep(3) 
    driver.find_element_by_css_selector("input[formcontrolname='clearEnd_dt']").send_keys(end_date)
    time.sleep(3)
    #downloading the file
    driver.find_element_by_xpath("//button[contains(text(), ' Download')]").click()
    time.sleep(5)
    #renaming the downloaded file
    name= 'errorlogs.csv'
    os.rename(path+'\\Download_CSV.csv',path+'\\'+name) 
    return name

    
    
