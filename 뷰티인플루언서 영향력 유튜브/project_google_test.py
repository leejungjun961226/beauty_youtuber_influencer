from Kotube import get_info
from Youtube_URL import get_url
import pandas as pd
import numpy as np
import API_CLASS
import googletrend
import datetime
import json
from socialblade2 import socialblade1


def youtube_url_main(keyword, howmany):
    videolist = get_url(keyword,howmany)
    print(videolist)

df_raw = pd.read_pickle('glowpick_nodupl.pkl')
df = df_raw.copy()

result = pd.DataFrame(index=range(0,61))

for i, row in df.iterrows():
    keyword = row['상품명']
    # print(keyword)
    # print(type(keyword))
    url_list = get_url(keyword,3)
    for i in url_list:
        # print(i)
        # print(type(i))
        try:
            social_list = socialblade1(i)
        except:
            continue
        print(social_list)
        upload_date, sub = social_list[-2],social_list[-1][-1] # upload_date, sub
        #시간설정
        today = API_CLASS.convert_strtime(upload_date)
        start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
        #네이버api
        print('123123123123123123')
        try:
            na = googletrend.googletrend([keyword],start_date , enddate)
        except:
            continue
        print('456456456456456456456456')
        googletrend.table_sub(na,sub)
        result[keyword]=na.reset_index(drop=True)
        print(result)
        
#        
result.to_csv('beauti_result1.csv',encoding='utf-8-sig')