# !/usr/lib/python3
import itchat
import requests
from itchat.content import *
def get_reply(msg):
    api_tuling = "http://www.tuling123.com/openapi/api"
    KEY = "201279773c324b8d97b0f78a1728ab0c"
    UID = 177234
    data = {
        'key': KEY,
        'info': msg,
        'userid': UID
    }
    ret = requests.post(api_tuling, data=data).json()
    return ret.get('text');
@itchat.msg_register('Text') #监听文本消息 调用以下第一个方法
def text_reply(msg):
    return get_reply(msg['Text'])
@itchat.msg_register('File') #监听文件消息 调用以下第一个方法
def file_reply(msg):
    return "收到，谢谢"
@itchat.msg_register([TEXT,MAP,CARD,NOTE],isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        return  text_reply(msg)

itchat.auto_login(hotReload=True);# hotReload 不用频繁扫码
itchat.run() # 等待消息到来