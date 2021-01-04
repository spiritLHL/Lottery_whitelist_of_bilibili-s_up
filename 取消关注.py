from selenium import webdriver
from bs4 import BeautifulSoup
import time,re,os,requests,lxml



'''单账号查询有自动回复的up（可重复多次，结果续写在有自动回复的up.txt中，最后去重(注释转代码后)生成白名单.txt）'''
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
#driver.maximize_window()
#登陆
driver.get('https://passport.bilibili.com/login')
time.sleep(15)
comment = input('True or False:')
while comment:
    if comment == False:
        pass
    else:
        comment = input('True or False:')
#driver.minimize_window()
#消息页面操作
driver.get('https://message.bilibili.com/#/whisper')
time.sleep(3)
c = 0
while c < 400:  # 私信页面下拉次数
    c += 1
    draft = driver.find_elements_by_class_name('list-item')
    draft[len(draft)-1].click()
    time.sleep(0.7)
    print(c)
print('下拉结束,正在获取up列表')
auto_reply_up = driver.find_elements_by_class_name('name')
time.sleep(1)
list_name = []
for up in auto_reply_up:
    try:
        list_name.append(up.get_attribute('title'))
        time.sleep(0.7)
    except:
        passa
list_name = [i for i in list_name if i !='']
print(list_name)
fp = open('./有自动回复的up.txt','a',encoding='utf-8')
for t in list_name:
    fp.write(t+',')
print("存储完毕")


'''多次统计后up名字去重'''
'''
with open("有自动回复的up.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    list_name = data.split(',')
    list_name = [i for i in list_name if i != '']
    list_real = list(set(list_name))
    print(len(list_real))

fp = open('./白名单.txt','w',encoding='utf-8')
for r in list_real:
    fp.writelines(r+',\n')
print("存储完毕")
'''


'''查询去重后的up对应id(破千访问会报错)(注释掉前面的代码，下面注释转换成代码运行)'''
'''
with open("白名单.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    list_name = data.split(',')
    list_name = [i for i in list_name if i != '']
    print(list_name)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
url = 'https://search.bilibili.com/upuser?'
UP_id=[]
for i in data:
    param = {
        'keyword':i
    }
    res = requests.get(url=url,  params=param, headers=headers)
    page_text = res.text
    soup = BeautifulSoup(page_text, 'lxml')
    try:
        UP_sp_u = soup.find_all('a',class_='title')[0]['href']
    except:
        pass
    UP_ID = re.findall('//space.bilibili.com/(.*?)?from=search&.*?',UP_sp_u,re.S)
    UP_id.append(UP_ID)
    time.sleep(0.5)
fp_id = open('./对应的up的id.txt','w',encoding='utf-8')
for u in UP_id:
    fp_id.writelines(u+',')
print("存储完毕")
'''