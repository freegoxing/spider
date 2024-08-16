#适用场景：绕过登录，获取登录后的页面内容
#个人信息页面用utf-8编码，但其跳转到登录页面
#登录页面不用utf-8编码，需要用其他编码
#需要登录的网站，需要使用cookie登录
#需要先使用登录的网站，使用cookie（包含了登录信息）登录
#referer  判断是否从登录页面跳转过来    一般用于图片防盗链


import urllib.request

url = 'http://weibo.cn/6451491586/info'

headers = {
    #冒号开头的要注释掉
    # ':authority':'assport.weibo.com',
    # ':method':'GET',
    # ':path':'/sso/signin?entry=wapsso&source=wapssowb&url=https%3A%2F%2Fweibo.cn',
    # ':scheme':'https',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #encoding要注释掉
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'max-age=0',
    'Cookie':'PC_TOKEN=ec7992b202; SRT=D.QqHBTrsNKdkzSdRtOeYoWrSNUdRnPQYGQ-W8UqPu5cWgMdbbN-uoV%21EFNbHi5mYNUCsuPDbhVdkBSeMNAZSLUb9-OPPtMdkdK49ZJeYq5cM9KmAsdEyTIQW%21isbTTX77%2AB.vAflW-P9Rc0lR-ykKDvnJqiQVbiRVPBtS%21r3J8sQVqbgVdWiMZ4siOzu4DbmKPWfWd4l4OEKTQWG5%219wAqB3Jc%21-54sO; SRF=1722470121; SCF=AvmyoeTtc6ZB5EXQGFBSXoyO-RF5UO3HGZHbeKGh3R8tsCzlDBbayhgVg0indh76bNv3J8WJpTRVQsCeK4RBYR0.; SUB=_2A25LrqBODeRhGeFJ71cR9C_Kyj6IHXVoxb2GrDV8PUNbmtANLWTMkW9Nf8dIkzerdTCSkS2LiaoHC2RAuAHDYUyl; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFb3fq1UrA7H9IqhfIJZzvl5NHD95QNS0BfehBpSo2EWs4Dqcjqi--fi-iFi-i8i--fiKyhi-zReo57So5R; ALC=ALC-8s9p80-1722470430-1-1508552284-ppR67pcRY0Yg8YW5litXC602HO8=-2; ALF=02_1725062430; X-CSRF-TOKEN=CK-YcoeZc7EmN7e9JXmmEHCMcH49bXvwcWwPNXmzcHxKga4-xa0=',
    'Priority':'u=0, i',
    'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as f:
    f.write(content)