# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 01:19:21 2022

@author: okmen
"""

from  selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://twitter.com/login")
#üye girisi

input("giriş yaptıktan sonra enter tuşuna basınız")


#bitti

#online çalışma
driver.get("https://twitter.com/search?q=online%20%C3%A7al%C4%B1%C5%9Fma&src=typed_query&f=live")


time.sleep(5)
input("Okunan değer sayısı istenilene ulaştığında durmazsa ctrl+c ile durdurabilirsiniz")

dosya=open("onlinecalisma.txt", 'a')




ekle=[]
sayac=0
while 1:
       
    for i in range(1,16):    
        try:
            
            if sayac==25000:
                dosya.close()
                break
            else:
                
                sayac=sayac+1
            
            
            xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div['+str(i)+']'                                
            a=driver.find_elements_by_xpath(xpath)[0].text
            
            if a in ekle:
                pass
            else:
                dosya.write(a)
                ekle.append(a)
            print("adet twit eklendi: "+str(len(ekle)))
        except Exception as e:
            print("hata",str(e))
    driver.execute_script("scrollBy(0,+2000);")
    
    if sayac==25000:
        dosya.close()
        break
    
    
dosya.close()


#veri temizleme


