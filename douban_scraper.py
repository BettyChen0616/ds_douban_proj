#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:14:51 2020

@author: chenjiayu
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def login_douban(path):
    """固定功能,登录豆瓣"""
    global driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options) #打开浏览器
    driver.set_window_size(1120, 1000)
    # 进入登录页面
    login_page_url = 'https://accounts.douban.com/passport/login?source=movie'

    driver.get(login_page_url)

    # 点击密码登录
    driver.find_element_by_class_name("account-tab-account").click()

    # 输入账号和密码
    username = driver.find_element_by_id('username')

    username.send_keys('17611313631')

    password = driver.find_element_by_id("password")

    password.send_keys('a123456789')

    driver.find_element_by_class_name('btn-account').click()
    # 完成登录
    time.sleep(10)
# 采集一页
def get_one_page_short(url):
    """采集一页豆瓣短评内容"""
    
    global driver
    driver.get(url)
    short = [i.text for i in driver.find_elements_by_class_name('short')]
    username = [i.find_element_by_tag_name('a').text for i in driver.find_elements_by_class_name('comment-info')]
    time = [i.text for i in driver.find_elements_by_class_name('comment-time')]
    
    
    rating = [i.get_attribute('title') for i in driver.find_elements_by_class_name('rating')]
    #
    return short,username,time,rating



# 翻页采集
def get_comments(movie_id,n,path,slp_time):
    #"/Users/chenjiayu/github/ds_douban_proj/chromedriver"
    #Initializing the webdriver
    
    df = pd.DataFrame()
    empty_short = []
    empty_username = []
    empty_time = []
    empty_score = []
    
    for i in range(n):

        #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
        url = "https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P".format(movie_id,i*20)
        driver.get(url)
    
        #print(url)
        
        short,username,comment_time,rating = get_one_page_short(url)
    
        empty_short.extend(short)
        empty_username.extend(username)
        empty_time.extend(comment_time)
        empty_score.extend(rating)
            
        time.sleep(slp_time)
        #driver.close()     #关闭浏览器
        print("page",i)
        
    df['短评']  = empty_short
    df['用户名']  = empty_username
    df['评论时间']  = empty_time
    df['评分'] = empty_score
    return df

    









