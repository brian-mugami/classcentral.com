from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from englisttohindi.englisttohindi import EngtoHindi

service = Service(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
driver = webdriver.Chrome(service=service)

driver.get("https://brian-mugami.github.io/classcentral.com/")
links = driver.find_elements(by=By.TAG_NAME, value="a")

actual_links = [li.text for li in links if len(li.text) > 0]

for link in actual_links:
    link_to_click = driver.find_element(by=By.LINK_TEXT, value=link)
    link_to_click.click()

    driver.implicitly_wait(5)

    p_tags = driver.find_elements(by=By.TAG_NAME, value="p")
    h1_tags = driver.find_elements(by=By.TAG_NAME, value="h1")
    h2_tags = driver.find_elements(by=By.TAG_NAME, value="h2")
    a_tags = driver.find_elements(by=By.TAG_NAME, value="a")
    article_tags = driver.find_elements(by=By.TAG_NAME, value="article")

    actualp = [p.text for p in p_tags if len(p.text) > 0]
    actualh1 = [h1.text for h1 in h1_tags if len(h1.text) > 0]
    actualh2 = [h2.text for h2 in h2_tags if len(h2.text) > 0]
    actuala = [a.text for a in a_tags if len(a.text) > 0]
    actualarticle = [article.text for article in article_tags if len(article.text) > 0]


    driver.implicitly_wait(30)

    if actualp:
        for p in actualp:
            hindu = EngtoHindi(p).convert
            text = f"'{hindu}';"
            replacement = "var elements = document.getElementsByTagName('p'); for (var i = 0; i < elements.length; i++) { if (elements[i].textContent === '"+ p +"' ) {elements[i].textContent =" + text +";}}"
            driver.execute_script(replacement)

    if actualh1:
        for h1 in actualh1:
            hindu = EngtoHindi(h1).convert
            text = f"'{hindu}';"
            replacement = "var elements = document.getElementsByTagName('h1'); for (var i = 0; i < elements.length; i++) {if (elements[i].textContent=== '" + h1 +"') {elements[i].textContent =" + text + "}}"
            driver.execute_script(replacement)


    if actuala:
        for a in actuala:
            hindu = EngtoHindi(a).convert
            text = f"'{hindu}';"
            replacement = "var elements = document.getElementsByTagName('a'); for (var i = 0; i < elements.length; i++) { if (elements[i].textContent === '"+ a +"' ) {elements[i].textContent =" + text +";}}"
            driver.execute_script(replacement)




    driver.implicitly_wait(30)
    driver.back()




driver.close()



#for link in actual_links:
 #   to_click = driver.find_element(by=By.LINK_TEXT, value=link)
  #  to_click.click()
   # if p_tags:
    #    driver.execute_script(f"var element = document.getElementsByClassName('head-2 medium-up-head-1 margin-bottom-xsmall')[0]; element.innerHTML = '{hindi_title}'")
    #page = driver.page_source
#print(page)

    #if len(title) > 0:
     #   new_title = EngtoHindi(title).convert

      #  #driver.execute_script(f"var element = document.getElementsByClassName('head-2 medium-up-head-1 margin-bottom-xsmall')[0]; element.innerHTML = '{hindi_title}'")
       # time.sleep(1)
        #driver.back()

#driver.close()

#new_title = EngtoHindi(title)
#hindi_title = new_title.convert
#print(hindi_title)
#print(driver.current_url)
#driver.execute_script(f"var element = document.getElementsByClassName('head-2 medium-up-head-1 margin-bottom-xsmall')[0]; element.innerHTML = '{hindi_title}'")
