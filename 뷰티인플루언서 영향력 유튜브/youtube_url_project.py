from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re



def get_url(plusURL, count):
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_options.add_argument('--log-level=3')

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome('chromedriver.exe', options = chrome_options)


    

    baseURL = 'https://www.youtube.com/results?search_query='



    URL = baseURL + plusURL

    driver.get(URL)


    # 스크롤
    body = driver.find_element_by_css_selector('body')
    a = 0
    while True:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        videos = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-video-renderer')
        
        if len(videos)<=a:
            return 1

        if len(videos) >= int(count):
            break
        a = len(videos)


    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    videos = soup.find_all('a', class_ = 'yt-simple-endpoint style-scope ytd-video-renderer' )
    

    videolist = []
    baseURL = 'https://www.youtube.com'
    for i in range(0,int(count)):
        href = videos[i].attrs['href']
        # click_count = videos[i].attrs['aria-label']
        # click_count = re.sub('[^0-9]','',click_count.split()[-1])
        vidurl = baseURL+href
        videolist.append(vidurl)

    
    all_list = []
    print(videolist)
    for url in videolist:
        # 내가 수정
        one = []
        driver.get(url)
        #print('1')
        elem = WebDriverWait(driver,20).until(\
            EC.presence_of_element_located((By.CSS_SELECTOR, \
            '#date > yt-formatted-string')))
        #print('12')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select('#date > yt-formatted-string')
        upload_date = notices[0].text #동영상 올린날짜 string
        
        try:
            view_count = soup.select('#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer')
            
            # print(view_count)
            view_count = view_count[0].text
            # print(view_count)
            view_count = re.sub('[^0-9]','',view_count.split()[-1])
            upload_date = re.sub('. ','-',upload_date)[:-1]
            # print(upload_date)
            upload_date = re.findall('[0-9]+-[0-9]+-[0-9]+', upload_date)
            if upload_date == []:
                continue
            # print(upload_date)
            # print(type(upload_date))
            # print(upload_date[0])
            one.append(upload_date[0])
            one.append(view_count)
            all_list.append(one)
        except:
            continue
    return all_list
        

if __name__=='__main__':
    
    print(get_url('비욘드 [SPF50+/PA++++]',10))