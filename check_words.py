# clomedriverインストール済み
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import pandas as pd

# HTMLを読み取る
from bs4 import BeautifulSoup
# データを指定のURLから収集する
import urllib.request as req

# # アクセス情報指定
EMAIL = 'admin@admin.com'
PASS = 'adminadmin'

def check_content_words():
    url = "http://54.248.84.199/"
    response = req.urlopen(url)
    parse_html = BeautifulSoup(response, 'html.parser')
    # print(parse_html)

    # 以下取得する値を指定
    table = parse_html.find_all("table")[1]
    latest_td = table.find_all('td')[2]
    td_string = latest_td.string
    # print(string)

    # 条件式（不適切な場合は自動的に管理者が削除する）
    search_words = ["殺", "死", "刺す"]
    for i in search_words:
        if i in td_string:
            # 削除処理実行
            print('削除処理を実行します')
            # time.sleep(3)
            
            # 処理内容
            # chromブラウザー起動
            browser = webdriver.Chrome()
            # 暗黙的な待機指定（javascriptを使用しているため）
            browser.implicitly_wait(3)

            # サイトログイン
            admin_login = "http://54.248.84.199/admin/sign_in"
            browser.get(admin_login)
            # time.sleep(3)
            # print('サイトを表示しました')

            # ログイン情報入力処理
            element = browser.find_element("id", "admin_email")
            element.clear()
            element.send_keys(EMAIL)
            element = browser.find_element("id", "admin_password")
            element.clear()
            element.send_keys(PASS)
            # time.sleep(3)
            # print("テキストに値を入力しました")

            # ログイン処理
            browser_from = browser.find_element("name", "commit")
            # time.sleep(3)
            browser_from.click()
            print("ログインに成功しました")
            time.sleep(3)
            
            # 削除処理実行
            post_index_url = "http://54.248.84.199/admin/posts"
            browser.get(post_index_url)
            time.sleep(2)
            # index_html = browser.page_source
            # soup = BeautifulSoup(index_html, 'html.parser')
            # post_table = soup.find("table")
            # table_body = post_table.find_all("tbody")[0]
            # first_tr = table_body.find_all("tr")[0]
            # third_td = first_tr.find_all("td")[2]
            # a_tag = third_td.find("a")
            index_element = browser.find_element(by=By.XPATH, value="/html/body/main/div/div[3]/table/tbody/tr[1]/td[3]/a")
            index_element.click()
            time.sleep(2)
            print('不適切な投稿を自動的に削除しました')       
        else:
            print('正常です')


while(True):
    print('投稿内容をチェック')
    check_content_words()
    time.sleep(60 * 10) #10分間隔
        
    






