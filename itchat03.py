# !/usr/lib/python3
"""
图灵API 调用
"""
import itchat
import requests

api_tuling="http://www.tuling123.com/openapi/api"
KEY="201279773c324b8d97b0f78a1728ab0c"
UID=177234
msg='您好'
data={
    'key':KEY,
    'info':msg,
    'userid':UID
}
ret=requests.post(api_tuling,data=data).json()
print(ret.get('text'))

@itchat.msg_register('Text') #监听文本消息 调用以下第一个方法
def text_reply(msg):
    if msg['Text']=='您好':
        return '您好，很好的'
    else:
        return '自动回复，我现在不在稍后回复您'
@itchat.msg_register('File') #监听文件消息 调用以下第一个方法
def file_reply(msg):
    return "收到，谢谢"
itchat.auto_login(hotReload=True);# hotReload 不用频繁扫码
itchat.run() # 等待消息到来