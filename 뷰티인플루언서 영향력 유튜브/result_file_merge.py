import pandas as pd
### 변경할 변수
folder_file_name='result_beauty_brand_product_name_0625_'
start_file_number=0 #시작하는 파일번호
end_file_number=15 #끝나는 파일번호+1



df=pd.DataFrame()
for i in range(start_file_number,end_file_number):
    
    df1=pd.read_csv(folder_file_name+str(i)+'.csv', index_col=0)
    df =pd.merge(df,df1, how='outer', left_index=True, right_index=True)
df.to_csv(folder_file_name+'.csv',encoding='utf-8-sig')