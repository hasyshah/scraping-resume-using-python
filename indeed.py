from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

list_of_links = []
title_1 = []
title_2 = []
title_3 = []
title_4 = []
title_5 = []
company_1 = []
company_2 = []
company_3 = []
company_4 = []
company_5 = []
time_1 = []
time_2 = []
time_3 = []
time_4 = []
time_5 = []
edu_1 = []
eduschool_1 = []
edu_2 = []
eduschool_2 = []

        
driver = webdriver.Chrome(executable_path="/Users/abhyudit/Desktop/blank/chromedriver")

def open_page_and_search():
    driver.get("https://resumes.indeed.com/")
    driver.find_element_by_name('q').send_keys("java")
    driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[1]/div[2]/div/form/div[3]/button").send_keys(Keys.ENTER)

    
def name():
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        link = str(elem.get_attribute("href"))
        if(link.startswith('https://resumes.indeed.com/resume/')==True):
            list_of_links.append(link)
def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  

def wait(time_in_seconds):
    time.sleep(time_in_seconds)

def work():
    try:
        for i in range(len(list_of_links)):
            driver.get(list_of_links[i])
            print("----------------------------------")
            title1 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]")
            print(title1.text)
            title_1.append(title1.text)
            company1 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/span[1]")
            print(company1.text)
            company_1.append(company1.text)
            duration1 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]")
            print(duration1.text)
            time_1.append(duration1.text)
            try:
                title2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]")
                print(title2.text)
                title_2.append(title2.text)
                company2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]")
                print(company2.text)
                company_2.append(company2.text)
                duration2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]")
                print(duration2.text)
                time_2.append(duration2.text)
                print('-----------------------------------')
                try:
                    title3 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[3]/div[1]")
                    print(title3.text)
                    title_3.append(title3.text)
                    company3 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/span[1]")
                    print(company3.text)
                    company_3.append(company3.text)
                    duration3 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]")
                    print(duration3.text)
                    time_3.append(duration3.text)
                    print('-----------------------------------')
                    try:
                        title4 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[4]/div[1]")
                        print(title4.text)
                        title_4.append(title4.text)
                        company4 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div[1]/span[1]")
                        print(company4.text)
                        company_4.append(company4.text)
                        duration4 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div[2]")
                        print(duration4.text)
                        time_4.append(duration4.text)
                        print('-----------------------------------')
                        try:
                            title5 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[5]/div[1]")
                            print(title5.text)
                            title_5.append(title5.text)
                            company5 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[1]/span[1]")
                            print(company5.text)
                            company_5.append(company5.text)
                            duration5 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]")
                            print(duration5.text)
                            time_5.append(duration5.text)
                            print('-----------------------------------')
                        except Exception:
                            title_5.append(' - ')
                            company_5.append(' - ')
                            time_5.append(' - ')
                            pass
                    except Exception:
                        title_4.append(' - ')
                        company_4.append(' - ')
                        time_4.append(' - ')
                        title_5.append(' - ')
                        company_5.append(' - ')
                        time_5.append(' - ')
                        pass
                except Exception:
                    title_3.append(' - ')
                    company_3.append(' - ')
                    time_3.append(' - ')
                    title_4.append(' - ')
                    company_4.append(' - ')
                    time_4.append(' - ')
                    title_5.append(' - ')
                    company_5.append(' - ')
                    time_5.append(' - ')
                    pass
            except Exception:
                title_2.append(' - ')
                company_2.append(' - ')
                time_2.append(' - ')
                title_3.append(' - ')
                company_3.append(' - ')
                time_3.append(' - ')
                title_4.append(' - ')
                company_4.append(' - ')
                time_4.append(' - ')
                title_5.append(' - ')
                company_5.append(' - ')
                time_5.append(' - ')
                pass
    except Exception:
                title_1.append(' - ')
                company_1.append(' - ')
                time_1.append(' - ')
                title_2.append(' - ')
                company_2.append(' - ')
                time_2.append(' - ')
                title_3.append(' - ')
                company_3.append(' - ')
                time_3.append(' - ')
                title_4.append(' - ')
                company_4.append(' - ')
                time_4.append(' - ')
                title_5.append(' - ')
                company_5.append(' - ')
                time_5.append(' - ')
                pass


def edu():
    for i in range(len(list_of_links)):
        try:
            driver.get(list_of_links[i])
            edu1 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[3]/div[2]/div/span/span[1]")
            edu_1.append(edu1.text)
            eduschool1 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[3]/div[2]/div/div/div/span[1]/span")
            eduschool_1.append(eduschool1.text)
            try:
                edu2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/span/span[1]")
                edu_2.append(edu2.text)
                eduschool2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div/span[1]/span")
                eduschool_2.append(eduschool2.text)
            except Exception:
                edu_2.append(' - ')
                eduschool_2.append('-')
        except Exception:
            edu_1.append(' - ')
            eduschool_1.append('-')
            edu_2.append(' - ')
            eduschool_2.append('-')
def save_as_csv():
    d = {'WorkTitle 1':title_1,'WorkCompany 1':company_1,'WorkDates 1':time_1,'WorkTitle 2':title_2,'WorkCompany 2':company_2,'WorkDates 2':time_2,'WorkTitle 3':title_3,'WorkCompany 3':company_3,'WorkDates 3':time_3,'WorkTitle 4':title_4,'WorkCompany 4':company_4,'WorkDates 4':time_4,'WorkTitle 5':title_5,'WorkCompany 5':company_5,'WorkDates 5':time_5,'Edu 1':edu_1,'EduSchool 1':eduschool_1,'Edu 2':edu_2,'EduSchool 2':eduschool_2}
    df = pd.DataFrame(d)
    df
    df.to_csv('Indeed_Resumes_100.csv')
    
def run_this():
    open_page_and_search()
    wait(1)
    name()
    wait(1.5)
    driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/div[5]/span[3]/span").send_keys(Keys.ENTER)
    wait(1.5)
    name()
    work()
    wait(0.5)
    edu()
    wait(0.5)
    save_as_csv()

run_this()

