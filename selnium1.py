from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import os 
import time
import warnings
warnings.filterwarnings("ignore")
class EduTest():
    def test(self):
        df=pd.read_excel(r"poshmark.xlsx")
        driver = webdriver.Firefox(executable_path=r"geckodriver")
        driver.maximize_window()
        driver.get("https://poshmark.com/create-listing")
        log=driver.find_element_by_xpath("//input[@id='login_form_username_email']")
        log.send_keys("nirajtoughguy@gmail.com")
        pas=driver.find_element_by_xpath("//input[@id='login_form_password']")
        pas.send_keys("Posh@123")
        for i in range(3):
            print(i)
            if i!=0:
                time.sleep(4)
                driver.find_element_by_xpath("//div[@class='header--scrollable__nav']").click()
                print("yes")
                time.sleep(4)
                pass
            else:
                pass
            title=str(df.ix[i,0])
            description=str(df.ix[i,1])
            choice=str(df.ix[i,2])
            category=str(df.ix[i,3])
            subcategory=str(df.ix[i,4])
            size=str(df.ix[i,5])
            print(size)
            brand=str(df.ix[i,6])
            color=str(df.ix[i,7])
            originalprice=str(df.ix[i,8])
            listingprice=str(df.ix[i,9])
            sku=str(df.ix[i,10])
            costprice=str(df.ix[i,11])
            otherinfo=str(df.ix[i,12])
            
            
            time.sleep(40)
            #time.sleep(120)
            driver.find_element_by_xpath("//textarea[@placeholder='Describe it! (required)']").send_keys(description)
            element=driver.find_element_by_xpath("//input[@placeholder='What are you selling? (required)']")
            element.send_keys(title)
            time.sleep(5)
            driver.find_element_by_xpath("//div[@class='dropdown d--b']//div[@class='dropdown__selector dropdown__selector--select-tag dropdown__selector--select-tag--large']").click()
            time.sleep(5)
            choice_="//a[contains(text(),'{0}')]"
            choice_locator=choice_.format(choice)
            s=driver.find_element(By.XPATH,choice_locator)
            time.sleep(3)
            s.click()
            time.sleep(5)
            category_="//a[contains(text(),'{0}')]"
            category_locator=category_.format(category)
            s1=driver.find_element_by_xpath(category_locator)
            time.sleep(3)
            s1.click()
            lista=driver.find_elements(By.XPATH,"//ul[@class='dropdown__menu']//li//a")
            for ele in lista:
                    #//ul[@class="dropdown__menu ws--nowrap"]//nav//ul//li[@class="dropdown__menu__item--selected dropdown__menu__item"]
                    #//li[@class='dropdown__menu__item--selected dropdown__menu__item']
                    print(ele.get_attribute("innerHTML"))
                
            for e in lista:
                e1=e.get_attribute("innerHTML")
                if e1==subcategory:
                    e.click()
            driver.find_element_by_xpath("//div[@class='dropdown listing-editor__input--half']//div[@class='dropdown__selector dropdown__selector--select-tag dropdown__selector--select-tag--large']").click()
            
            #time.sleep(2)
            driver.find_element_by_xpath("//a[contains(text(),'Custom')]").click()
            
            #time.sleep(2)
            driver.find_element_by_xpath("//input[@class='form__text d--ib bg--white']").send_keys(size)
            driver.find_element_by_xpath("//button[@class='btn btn--secondary m--l--3']").click()
            driver.find_element_by_xpath("//input[@placeholder='Enter the Brand/Designer']").send_keys(brand)
            driver.find_element_by_xpath("//div[@class='dropdown listing-editor__input--half col-x24 col-l20']//div[@class='dropdown__selector dropdown__selector--select-tag dropdown__selector--select-tag--large']").click()
            time.sleep(2)
            color_1="//li[contains(text(),'{0}')]"
            color_1_locator=color_1.format(color)
            driver.find_element_by_xpath(color_1_locator).click()
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='p--3 dropdown__menu dropdown__menu--dark dropdown__menu--top']//button[@class='btn btn--primary'][contains(text(),'Done')]").click()
            driver.find_element_by_xpath("//body/div[@id='app']/main/div[@id='content']/div[@class='view']/div/div[@class='card card--large']/section[@class='listing-editor__section']/div[@class='listing-editor__subsection']/div/div[@class='col-x24 col-l20']/input[1]").send_keys(originalprice)
            driver.find_element_by_xpath("//div[@class='d--fl ai--c']//input[@placeholder='*Required']").send_keys(listingprice)
            driver.find_element_by_xpath("//a[@class='listing-editor-toggle-link']").click()
            driver.find_element_by_xpath("//div[@class='listing-editor__toggle']//input[1]").send_keys(sku)
            driver.find_element_by_xpath("//div[@class='listing-editor__toggle']//input[2]").send_keys(costprice)
            driver.find_element_by_xpath("//textarea[@placeholder='optional']").send_keys(otherinfo)
            driver.find_element_by_id("img-file-input").send_keys(r"C:\Users\RAHUL TIWARI\PycharmProjects\Ebay Crowling\shoes.jpg")
            time.sleep(5)
            driver.find_element_by_xpath("//button[contains(text(),'Apply')]").click()
            time.sleep(2)
            #driver.find_element_by_xpath("//body//div[@class='col-x24 col-l20']//div//div[1]//div[1]//label[1]//div[1]//div[1]").send_keys(r"C:\Users\rahul\Desktop\PY4E\flower.jpeg")
            driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
            time.sleep(3)
            parenthandle= driver.current_window_handle
            driver.find_element_by_xpath("//button[contains(text(),'List This Item')]").click()
            time.sleep(8)
            parenthandle= driver.current_window_handle
            handles=driver.window_handles
            for handle in handles:
                print(handles)
            

cr=EduTest()
cr.test()