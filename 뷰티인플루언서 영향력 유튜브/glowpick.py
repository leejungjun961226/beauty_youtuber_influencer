from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 한번은 열어줘야 함수에서 실행됨

brand_result = [] # 브랜드명 가져오기
name_result = [] # 상품명 가져오기
key_result = [] # 브랜드명, 상품명 합치기


def cos_f(br):
    a="시작"
    h=0
    for j in range(2,1000):
        
        if a=="끝":
            break
        else:
            for i in range(1,1000):
                br.get("https://www.glowpick.com/beauty/ranking?id="+str(i)+"&level="+str(j))

                try:
                    elem = WebDriverWait(br,100).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#gp-default-top > header > div > nav > ul > li.gp-header__menu-list-item--beauty-ranking > a > span')))
                except:
                    if h!=j: 
                        a = "끝"
                        break
                    else:
                        print(1)
                        break

                h=j
                html = br.page_source
                soup = BeautifulSoup(html, 'html.parser')

                for k in range(1,6):
                    # 브랜드 이름 가져오기
                    brand_value = soup.select_one('#gp-list > div > section.section-list > ul > li:nth-child('+str(k)+') > div > div > div.product-item__info > div.product-item__info__details.details.details--ranking > div.details__labels > p.details__labels__brand').getText().strip()

                    # 브랜드 이름에 공백 제거
                    # ex) 더랩 바이 블랑두 -> 더랩바이블랑두
                    brand_sub = re.sub(r'\s+','',brand_value)

                    # 브랜드 이름에서 한글만 가져오기
                    # ex) 코스알엑스(cosrx) -> 코스알엑스
                    brand_find = re.findall(r'[가-힣]+', brand_sub)

                    # 최종 brand_result의 리스트에 추가
                    brand_result.append(brand_find)


                    # 상품 이름 가져오기
                    name_value = soup.select_one('#gp-list > div > section.section-list > ul > li:nth-child('+str(k)+') > div > div > div.product-item__info > div.product-item__info__details.details.details--ranking > div.details__labels > p.details__labels__name').getText()

                    # 상품 이름에 공백 제거
                    name_sub = re.sub(r'\s+','',name_value)
                    name_split = name_sub.split('\n')
                    # 상품 이름에서 한글만 가져오기
                    #name_find = re.findall(r'[가-힣]+', name_sub)

                    # 상품 결과값에 추가
                    name_result.append(name_split)


                #br.close()
                for i in range(0,len(brand_result)):
                    key_result.append(brand_result[i]+name_result[i])
    return key_result
    
    
# 돌리기만 해보기

br = webdriver.Chrome("C:/Users/tjoeun/Documents/GitHub/Team_Projects/Bigdata_Project/Bigdata_Project/Naver_Api/chromedriver.exe")
a=cos_f(br)