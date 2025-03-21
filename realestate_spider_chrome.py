import time
import random
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select




# 解析网页内容并提取房屋信息
def parse_page(table):
    rows = table.find_elements(By.TAG_NAME, "tr")
    houses = []
    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        house = {
            "area": cols[0].text,
            "type": cols[2].text,
            "rooms": cols[3].text,
            "square": cols[4].text,
            "price": cols[5].text,
        }
        houses.append(house)
    return houses


def browser_using(browser, keys, area):
    
    input = browser.find_element(By.NAME,'ctl00$MainContent$txt_Pro')
    input.send_keys(keys)
    time.sleep(random.uniform(1, 3))

    select_element = browser.find_element(By.ID,'MainContent_ddl_qy')
    select = Select(select_element)
    select.select_by_visible_text(area)
    time.sleep(random.uniform(1, 3))

    button = browser.find_element(By.ID,'MainContent_bt_select')
    button.click()
    # wait = WebDriverWait(browser, 10)
    time.sleep(random.uniform(2, 5))


    pages_total = browser.find_element(By.ID,"MainContent_PageGridView1_PageList_0")
    page_select = Select(pages_total)

    max_page = page_select.options[-1].text
    max_page = int(max_page)
    # print(max_page)
    data = []
    for i in range(max_page):
        table = browser.find_element(By.ID, "MainContent_PageGridView1")
        houses = parse_page(table)
        for x in houses:
            print(x)
            data.append(x)
        time.sleep(random.uniform(1, 3))
        next_button = browser.find_element(By.ID, "MainContent_PageGridView1_Next_0")
        next_button.click()
    # 将data存储到df中
    df = pd.DataFrame(data)
    df.to_csv(f'data-{keys}-{time.strftime("%Y%m%d%H%M%S")}.csv', index=False)
       


if __name__ == '__main__':
    q = {
        "大悦":"相城区", 
        "江南":"相城区",
        "墨香":"相城区",
        "东望":"吴中区",
        "融悦":"吴中区",
    }
    
    browser = webdriver.Chrome()
    browser.get('http://spf.szfcweb.com/szfcweb/DataSerach/CanSaleHouseSelectIndex.aspx')
    for keys, area in q.items():
        print(f"{keys}--{area}")
        try:
            browser_using(browser, keys, area)
        except:
            continue
    browser.close()
