#from Kotube import get_info
from youtube_url_project import get_url
import pandas as pd
import numpy as np
import API_CLASS
import googletrend
import datetime
import json
#from socialblade2 import socialblade1
#from datetime import datetime
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

##파일마다 변경해야 하는 변수
default_folder='뷰티인플루언서 영향력 유튜브/'
folder_file_name='beauty_brand_product_name_0625'
column_name='브랜상품'
# '브랜상품(beauty_brand_product_name)'', '상품명(beauty_product_name)', '상품명(beauty_brand_category)'
start_file_number=31 #시작하는 파일번호
end_file_number=33 #끝나는 파일번호
####################################



for i in range(start_file_number,end_file_number):
    print('※',i,'번째 파일 작업 시작')
    now = datetime.datetime.now()
    nowDate = str(now.strftime('%Y-%m-%d'))
    def youtube_url_main(keyword):
        videolist = get_url(keyword,3)
        print(videolist)

    num = i #파일번호
    num=str(num)
    df_raw = pd.read_csv(default_folder+folder_file_name+'/'+folder_file_name+'_'+num+'.csv')

    df = df_raw.copy()
    print(df)
    result_na = pd.DataFrame(index=range(0,62))
    result_goo = pd.DataFrame(index=range(0,62))
    
    for i, row in df.iterrows():
        print('[[첫번째 for문]]')
        print(i,'번 idx',row,'진행')
        keyword = row[column_name]
        # print(keyword)
        # print(type(keyword))
        url_list = get_url(keyword,10)
        if url_list==1:
            continue
        iter_n = 0
        for i in tqdm(url_list):
            # print('[[두번째 for문]]')
            # print(i,'진행')
            # # print(i)
            # # print(type(i))
            # try:
            #     print('소셜 시작')
            #     social_list = socialblade1(i)
            #     print('소셜 끝+')
            # except:
            #     print('EXCEPT - in url_list')
            #     continue
            #print(social_list)
            upload_date, sub = i[0],i[1] # upload_date, sub
            
            upload_date = str(datetime.datetime.strptime(upload_date,'%Y-%m-%d').date())
            print(upload_date, sub)
            
            #시간설정
            today = API_CLASS.convert_strtime(upload_date)
            start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
            print(start_date, enddate)
            if enddate>=nowDate or start_date<'2016-01-01':
                print('CONTINUE - enddata >= nowDate')
                continue

            #네이버api
            print('[[#네이버 api" 진입]]')
            print(keyword,start_date , enddate)
            na = API_CLASS.NaverApi(keyword,start_date , enddate).to_dataframe()
            na = googletrend.table_sub(na,sub)
            print(na)
            result_na[keyword+'_'+str(iter_n)]=na.reset_index(drop=True)
            result_na.to_csv('result_'+folder_file_name+'_'+num+'.csv',encoding='utf-8-sig')
            #print(result)

            #구글트렌드
            # try:
            #     goo = googletrend.googletrend(keyword,start_date , enddate)
            #     goo = googletrend.table_sub(goo,sub)
            #     result_goo[keyword]=goo.reset_index(drop=True)
            #     result_goo.to_csv('result_'+folder_file_name+'_'+num+'.csv',encoding='utf-8-sig')
            # except:
            #     goo = googletrend.googletrend(keyword,start_date , enddate)
            #     goo = googletrend.table_sub(goo,sub)
            #     result_goo[keyword]=goo.reset_index(drop=True)
            #     result_goo.to_csv('result_'+folder_file_name+'_'+num+'.csv',encoding='utf-8-sig')
            #print(result)

            iter_n +=1
            if iter_n>=2:
                print('BREAK - iter_n이 3이상')
                break
    print(str(num)+'번 파일 완료')            
    #result.to_csv('beauti_result1.csv',encoding='utf-8-sig')
    #print('완료')