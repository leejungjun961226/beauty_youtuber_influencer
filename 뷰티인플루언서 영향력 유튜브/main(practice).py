import pandas as pd
import youtube_url_main as youtube

"""
1. 품명
2. 품명> 유튜브 검색
2.1 유튜브 검색> 상위 n개의 영상 확보
    영상확보 : 제목, 채널이름, 채널주소
3. Naver & Google(google & youtube)
4. '파급력(영향력)' 연산
"""

df = pd.read_excel('dedupl_brand_name.xlsx', sheet_name='Sheet1')
print(df.head())
# 경로 지정을 안해서? 한글이 있어서? 띄어쓰기가 있어서? : ../ 에서 저장.읽기가 수행됨
print(df['상품명'][0])

# for i in range(0,len(df)):
for i in range(0,5):
    youtube.youtube_url_main(df['상품명'][i],3)

# 진행 중 입니다. 
    
