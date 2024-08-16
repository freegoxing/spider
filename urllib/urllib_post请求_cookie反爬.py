import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/ai/smartSug'

headers = {
    'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':'keep-alive',
    # 'Content-Length':'253',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'BIDUPSID=C6C9D0D736FD72A5AD660B9069EAE37E; PSTM=1719999261; BAIDUID=C6C9D0D736FD72A5E46EABB4DCE8EE7A:FG=1; BDUSS=1RocVdNNzI5a29TZFhYU2EzZExxdnpaZDhpeGtiSkQzTFcyYnVyNklWeGZMYTVtSVFBQUFBJCQAAAAAAQAAAAEAAACijK4mAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-ghmZfoIZmY; BDUSS_BFESS=1RocVdNNzI5a29TZFhYU2EzZExxdnpaZDhpeGtiSkQzTFcyYnVyNklWeGZMYTVtSVFBQUFBJCQAAAAAAQAAAAEAAACijK4mAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-ghmZfoIZmY; newlogin=1; H_PS_PSSID=60275_60359_60454_60468_60491_60500_60473; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_WISE_SIDS=60275_60359_60454_60468_60491_60500_60473; BAIDUID_BFESS=C6C9D0D736FD72A5E46EABB4DCE8EE7A:FG=1; BA_HECTOR=0gah0100842g010l2h2h2124880gvq1jajaka1v; ZFY=WrHRq:BkerROVyvEUWR107:BEU:ATuqEJm9hMsUgOTiJoI:C; H_WISE_SIDS_BFESS=60275_60359_60454_60468_60491_60500_60473; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1722395921; RT="z=1&dm=baidu.com&si=199679a9-f009-4963-837f-b85031c49242&ss=lz9hu2ub&sl=5&tt=5lj&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=jg1"',
    'Host':'fanyi.baidu.com',
    'Origin':'https://fanyi.baidu.com',
    # 'Referer:https':'//fanyi.baidu.com/mtpe-individual/multimodal?query=spider&lang=en2zh',
    'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

data = {
    'aiType': '2',
    'from': 'en',
    'select': 'all',
    'sentence': '[{"id":"zg10kxk62e","paraIdx":0,"src":"spider\n","dst":"蜘蛛\n","metadata":"","metaData":[]}]',
    'to': 'zh',
    'type': '1',
    'typeID': 'lblq3zkB1d'
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)
