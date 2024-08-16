#kfc店面位置前十页爬取
#第一页
#http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#post
#负载
# cname:北京
# pid:
# pageIndex:1
# pageSize:10

#第二页
#http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#post
#负载
# cname:北京
# pid:
# pageIndex:2
# pageSize:10


import urllib.request

def create_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    date = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(date).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('kfc'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = input("请输入起始页：")
    end_page = input("请输入结束页：")

    for page in range(int(start_page),int(end_page)+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)
