# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:49:33 2020
@author: LARRY PRATO
"""
from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path = r'C:/Users/LARRY/Desktop/Selenium/chromedriver.exe',  chrome_options=options)
driver.implicitly_wait(5)
driver.get('https://transparencia.registrocivil.org.br/registros')
time.sleep(10)

radio = driver.find_element_by_xpath("//input[@type='radio' and @value='death']")
driver.execute_script("arguments[0].click();", radio)
time.sleep(2)

y_2015 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[6]/span/span'
y_2016 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[5]/span/span'
y_2017 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[4]/span/span'
y_2018 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[3]/span/span'
y_2019 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[2]/span/span'
y_2020 = '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[1]/span/span'

m_Janeiro =       '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[2]/span/span'
m_Fevereiro =     '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[3]/span/span'
m_Março =         '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[4]/span/span'   
m_Abril =         '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[5]/span/span'
m_Maio =          '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[6]/span/span'
m_Junho =         '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[7]/span/span'
m_Julho =         '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[8]/span/span'
m_Agosto =        '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[9]/span/span'
m_Setembro =      '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[10]/span/span'
m_Outubro =       '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[11]/span/span'
m_Novembro =      '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[12]/span/span'
m_Dezembro =      '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[13]/span/span'

YEARS = [y_2015, y_2016, y_2017, y_2018, y_2019]
MONTHS =[m_Janeiro, m_Fevereiro, m_Março, m_Abril, m_Maio, m_Junho, m_Julho, m_Agosto, m_Setembro, m_Outubro, m_Novembro, m_Dezembro]

DATOS = pd.DataFrame([])
for ano in YEARS:
    try:    
        for mes in MONTHS:
            ##########################
            if mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[2]/span/span':
                n_mes = "Janeiro"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[3]/span/span':
                n_mes = "Fevereiro"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[4]/span/span':
                n_mes = "Março"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[5]/span/span':
                n_mes = "Abril"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[6]/span/span':
                n_mes = "Maio"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[7]/span/span':
                n_mes = "Junho"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[8]/span/span':
                n_mes = "Julho"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[9]/span/span':
                n_mes = "Agosto"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[10]/span/span':
                n_mes = "Setembro"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[11]/span/span':
                n_mes = "Outubro"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[12]/span/span':
                n_mes = "Novembro"
            elif mes == '//*[@id="__BVID__62"]/div/div/div[3]/ul/li[13]/span/span':
                n_mes = "Dezembro"            
            #######################
            if ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[6]/span/span':
                n_year = '2015'
            elif ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[5]/span/span':
                n_year = '2016'
            elif ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[4]/span/span':
                n_year = '2017'
            elif ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[3]/span/span':
                n_year = '2018'
            elif ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[2]/span/span':
                n_year = '2019'
            elif ano == '//*[@id="datePickrGroup"]/div/div/div[3]/ul/li[1]/span/span':
                n_year = '2020'
            ######################
            year = driver.find_element_by_class_name('multiselect__single')
            year.click()
            time.sleep(3)
            year_in= driver.find_element_by_xpath(ano)
            year_in.click()
            
            month = driver.find_element_by_xpath('//*[@id="__BVID__62"]/div/div/div[2]/span')
            month.click()
            month_in =driver.find_element_by_xpath(mes) 
            time.sleep(3)
            month_in.click()
            time.sleep(3)           
    
            pesquisar = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/button')
            time.sleep(2)
            pesquisar.click()
            time.sleep(2)
             
            ######
            noOfRows = len(driver.find_elements_by_xpath("//tr")) -1
            	# get number of columns
            noOfColumns = len(driver.find_elements_by_xpath("//tr[2]/td"))
            
            r1 = []
            r2 = []
            	# iterate over the rows, to ignore the headers we have started the i with '1'
            for i in range(1, noOfRows+1):
            	# reset the row data every time
            	# iterate over columns
                for j in range(1, noOfColumns) :
                    # get text from the i th row and j th column
                    r1.append(driver.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text)
                
                for j in range(2, noOfColumns+1) :
                    # get text from the i th row and j th column
                    r2.append(driver.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text)
            
            ######
            dato_dict = dict(zip(r1,r2))
            dato_mes = pd.DataFrame(r2, index=r1)
            temp = n_year+'_'+n_mes
            DATOS[temp] = r2
            print(temp)
    except Exception:
         pass

DATOS['estados'] = r1
DATOS.set_index('estados', inplace=True)      
print('finalizado')

arquivo= 'Datos_Covid.xlsx'
file='C:/Users/your_file_path/WebScraping/'+arquivo
DATOS.to_excel(file)