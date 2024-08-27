# coding=utf-8

# 异步函数

import asyncio
import aiohttp
import aiofiles
import time

def get_params():
    code = input('the code method:')
    name = input('the name of the object you need search:')
    pages = int(input('the page you want to search:'))

    params = {
        'ie': code,
        'pn': pages*50,
        'kw': name
    }

    return params, code, name, pages


async def aio_download(url, params, name, page, session):
    async with session.get(url=url, params=params) as res:
        async with aiofiles.open(f'test/{name}_{page}.html', 'wb') as f:
            await f.write(await res.content.read())



async def page_extraction(pages):
    for page in range(1, pages + 1):
        yield page


async def download_task(url, params, name, pages):
    tasks = []
    async with aiohttp.ClientSession() as session:
        if pages == 0:
            raise ValueError('pages should greater than 0')
        else:
            ait = aiter(page_extraction(pages))
            async for page in ait:
                task = asyncio.create_task(aio_download(url, params, name, page, session))
                tasks.append(task)

            await asyncio.wait(tasks)


def main(url):
    params, code, name, pages = get_params()
    asyncio.run(download_task(url, params, name, pages))


if __name__ == '__main__':
    t1 = time.time()
    url = 'http://tieba.baidu.com/f'
    main(url)
    t2 = time.time()
    print(t2-t1)
