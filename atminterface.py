# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:48:47 2019

@author: Inchel
"""
#银行存储机

#定义一个余额
balance = 5000

#定义一个余额查看函数
def showbal(balance):
    '''
    余额信息的输出
    '''
    print('-'*15,'余额','-'*15)
    print(balance)
    print('-'*35)
    
while True:
    #输出初始界面
    print('='*12,'银行自动存储机','='*12)
    print('{:1}{:15}{}'.format('','1.查看余额信息','2.存款'))
    print('{:1}{:15}{}'.format('','3.取款','   4.退卡'))
    print('='*38)
    key = input('请输入对应的选择：')
    #根据键盘值，判断并执行对应的操作
    if key == '1':
        showbal(balance)
        input('按回车继续：')
    elif key == '2':
        num = input('请输入你要存款的金额：')
        balance += int(num) 
        showbal(balance)
        input('按回车继续：')
    elif key == '3':
        num = input('请输入你要取款的金额：')
        balance -= int(num)
        showbal(balance)
        input('按回车继续：')
    elif key == '4':
        print('='*12,'再见','='*14)
        break
    else:
        print('='*7,"无效的键盘输入！",'='*7)
    
        