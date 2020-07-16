def googletrend(keywords, startdate, enddate):
    '''
    입력값 keywords는 리스트 ex.['Python', 'R']
    startdate 스트링 ex. '2016-12-14'
    enddate 스트링 ex. '2017-01-25'
    리턴값은 데이터프레임
    '''
    import pandas as pd
    from pytrends.request import TrendReq
    
    pytrend = TrendReq(hl='en-US', tz=360)
    time = startdate+' '+enddate
    pytrend.build_payload(
         kw_list=keywords,
         cat=0,
         timeframe=time,
         geo='KR',
         gprop='')
    data = pytrend.interest_over_time()
    data= data.drop(labels=['isPartial'],axis='columns')
#     image = data.plot(title = 'Python V.S. R in last 3 months on Google Trends ')
#     fig = image.get_figure()
#     fig.savefig('figure.png')
#    data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')
    return data

def table_sub(df, sub):
    '''
    입력값 data 는 데이터프레임, sub은 구독자수
    리턴값은 데이터프레임(마지막 행이 [sub, 구독자수])
    '''
    import pandas as pd
    df.loc['sub']=[sub]
    return df

    
    

if __name__=='__main__':
    keywords = ['asdfqwe']
    startdate= '2016-12-14'
    enddate = '2017-01-25'
    data = googletrend(keywords, startdate, enddate)
    data = table_sub(data, 30000)
    print(data)
    