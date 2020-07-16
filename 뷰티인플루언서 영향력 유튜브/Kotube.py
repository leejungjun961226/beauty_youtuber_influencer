from pytube import YouTube
import re

def get_info(video_url):

    yt = YouTube(video_url)
    # 동영상 링크를 이용해 YouTube 객체 생성
    info = {
        'title' : yt.title,
        'length' : yt.length,
        'rating' : yt.rating,
        'thumbnail' : yt.thumbnail_url,
        'views' : yt.views,
        'description' : yt.description
    }
    return info

def get_ko_sub(video_url):
    yt = YouTube(video_url)
    all_caption = yt.captions.all() # 모든 자막

    all_sub = ' '

    for i in range(0, len(all_caption)):
        if all_caption[i].code == 'ko':
            ko_sub = all_caption[i].generate_srt_captions()
            ko_sub = re.sub('\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+', ' ', ko_sub)
            ko_sub = re.sub("\[박수\]",'',ko_sub)
            ko_sub = re.sub('\[음악\]', '', ko_sub)
            ko_sub = re.sub('\d{1,2}', '', ko_sub).strip()

            all_sub += ko_sub.strip()


        else:
            print('Korean Sub does not exist')
    return all_sub

with open('test.txt','w') as f:
    f.write(get_ko_sub('https://www.youtube.com/watch?v=LKJjaJXDJqE'))

























