import tkinter
import easygui as g
from tkinter import *
# 导入表格模块
from openpyxl import Workbook
from openpyxl.descriptors.base import DateTime
from openpyxl.styles import Font, colors, Alignment
# 网络模块导入
import requests
# json模块导入
import demjson
# 正则模块导入
import re
import time
import linecache

if __name__ == "__main__":
    UpPath = g.enterbox(msg="请输入UP主名称文件路径", title="UID捕捉")
    print(UpPath)
    Cookie = g.enterbox(msg="请输入你的cookie", title="UID捕捉") #这里使用的B站cookie只需要复制SSEDATA那一栏
    timeS = g.enterbox(msg="请输入每10人间断秒数", title="UID捕捉") #建议1秒
    UpPath = open(UpPath, "r",encoding='utf-8').read()
    UpPath = UpPath.replace(' ', '')
    print(UpPath)



    UpPath = UpPath.split(",")
    # 爬虫头设置
    headers = {
        'referer':'https://search.bilibili.com/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
        'Cookie': Cookie
    }
    count = len(UpPath)
    # count = len(open(UpPath, 'r', encoding='utf-8').readlines())
    # 初始化循环值
    i = 0
    h = 2 #行数
    c = 0 #断点频率
    User = ""
    while i < count:
        #if c == 10:
            #time.sleep(int(timeS))
            #c = 0
        UpName = UpPath[i]
        if UpName != "":
            So_str = requests.get("http://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword="+str(UpName)+"&order=fans",headers=headers)
            #UpName = linecache.getline(UpPath, i)
            So_str.encoding = 'utf-8'
            So_str = So_str.text
            So_strJson = demjson.decode(So_str)
            if So_strJson['code'] == 0:
                if So_strJson['data']['numResults'] != 0:
                    Mid = So_strJson['data']['result'][0]['mid']
                    print(Mid)
                    # Name = So_strJson['data']['result'][0]['uname']
                    # Fans = So_strJson['data']['result'][0]['fans']
                    # sheet.cell(count, 1, arr['title']) 传入的3个值 行数 列数 值 如果单元格为空则创建写入这些内容
                    # 即代表第一行横着依次写入分P的CID
                    h = h + 1
                    User = User + "UID："+str(Mid)+"\n"
                else:
                    i = i + 1
            c = c + 1
            i = i + 1
        else:
            i = i + 1
    UpMid = open("白名单id.txt", "w+",encoding='utf-8').write(User)
    print("需要采集UP主"+str(count)+"人\n成功采集"+str(h-2)+"人")
            

