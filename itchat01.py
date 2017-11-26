# !/usr/lib/python3
import itchat
itchat.auto_login(hotReload=True);# hotReload 不用频繁扫码
#给文件助手发消息
itchat.send("hello ",toUserName='filehelper')
#给好友发消息
print(itchat.get_friends()[1])#最近聊天的第一个用户，第0个用户表示自己
print(itchat.get_friends()[1]["NickName"])#昵称
username=itchat.get_friends()[1]["UserName"]
itchat.send("聊天",toUserName=username)
#print(itchat.search_friends(name="源小宝"))#查找用户
print(itchat.search_friends(remarkName='五矿霍少龙'))#查找用户