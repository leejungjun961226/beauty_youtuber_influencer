from Kotube import get_info
from Youtube_URL import get_url


def youtube_url_main(keyword, howmany):
    videolist = get_url(keyword,howmany)
    print(videolist)

"""
videolist = get_url('파이썬',3)
print(videolist)
"""
