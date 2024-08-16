""""
这里有个表格，说明JSONPath语法元素和对应XPath元素的对比。
XPath	                JSONPath	                Description
  /	                    $	                        表示根元素
  .	                    @	                        当前元素
  /	                    . or []	                    子元素
  ..	                n/a	                        父元素
  //	                ..	                        递归下降，JSONPath是从E4X借鉴的。
  *	                    *                           通配符，表示所有的元素
  @	                    n/a	                        属性访问字符
  []	                []                          子元素操作符
  |	                    [,]                         连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。
  n/a	                [start:end:step]            数组分割操作从ES4借鉴。
  []	                ?()                         应用过滤表示式
  n/a	                ()                          脚本表达式，使用在脚本引擎下面。
  ()	                n/a	                        Xpath分组操作符

[]在xpath表达式总是从前面的路径来操作数组，索引是从1开始。
使用JOSNPath的[]操作符操作一个对象或者数组，索引是从0开始。

"""
import jsonpath
import json

obj = json.load(open('package.json', 'r', encoding='utf-8'))

# 书点所有书的作者
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj, '$..author')
# print(author_list)

# store的所有元素。所有的bookst和bicycle
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# store里面所有东西的price
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj, '$..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book)

# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# print(book_list)

# 过滤出所有的包含isbn的书。
#条件过滤要在（）前加？
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 过滤出价格低于10的书。
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
# print(book_list)

