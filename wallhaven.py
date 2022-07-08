#获取网站内容
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from io import BytesIO
from operator import index
import os
import request
import requests


def get_html(url):
    import requests
    r = requests.get(url)
    return r.text
#text转json
def text_to_json(text):
    import json
    return json.loads(text)
#调用def get_html(url)
def get_json(url):
    return text_to_json(get_html(url))
#获取图片URL，列表list的索引必须是整数或者切片，而不能是字符串类型
def get_image_url(json):
    #索引
    index = 0
    #列表
    url_list = []
    #获取图片的url
    for i in json['data']:
        url_list.append(i['url'])
        index += 1
    return url_list
#获取图片的id
def get_image_id(json):
    #索引
    index = 0
    #列表
    id_list = ''
    #获取图片的id
    for i in json['data']:
        id_list = id_list + str(i['id']) + ','
        index += 1
    return id_list
#获取图片的浏览数
def get_image_views(json):
    #索引
    index = 0
    #列表
    views_list = ''
    #获取图片的浏览数
    for i in json['data']:
        views_list = views_list + str(i['views']) + ','
        index += 1
    return views_list
#获取图片的类型
def get_image_type(json):
    #索引
    index = 0
    #列表
    type_list = ''
    #获取图片的类型
    for i in json['data']:
        type_list = type_list + str(i['file_type']) + ','
        index += 1
    return type_list
#获取图片的颜色配置
def get_image_color_config(json):
    #索引
    index = 0
    #列表
    color_config_list = ''
    #获取图片的颜色配置
    for i in json['data']:
        color_config_list = color_config_list + str(i['colors']) + '\n'
        index += 1
    return color_config_list
#获取图片的分辨率
def get_image_resolution(json): 
    #索引   
    index = 0
    #列表
    resolution_list = ''
    #获取图片的分辨率
    for i in json['data']:
        resolution_list = resolution_list + str(i['resolution']) + ','
        index += 1
    return resolution_list
#获取图片的尺寸
def get_image_size(json):
    #索引
    index = 0
    #列表
    size_list = ''
    #获取图片的尺寸
    for i in json['data']:
        size_list = size_list + str(i['file_size']/1048576) + 'MiB\n'
        index += 1
    return size_list
#获取图片的收藏数
def get_image_favorites(json):
    #索引
    index = 0
    #列表
    favorites_list = ''
    #获取图片的收藏数
    for i in json['data']:
        favorites_list = favorites_list + str(i['favorites']) + ','
        index += 1
    return favorites_list
#获取预览图片的下载链接
def get_image_downloads(json):
    #索引
    index = 0
    #列表
    downloads_list = ''
    #获取图片的下载链接
    for i in json['data']:
        #索引
        index2 = 0
        #列表
        downloads_list2 = ''
        for key,value in i['thumbs'].items():
            downloads_list2 = downloads_list2 + str(key) + ':' + str(value) + '\n'
            index2 += 1
        downloads_list = downloads_list + downloads_list2
        index += 1
    return downloads_list
#获取图片的创建时间
def get_image_created_at(json):
    #索引
    index = 0
    #列表
    created_at_list = ''
    #获取图片的创建时间
    for i in json['data']:
        created_at_list = created_at_list + str(i['created_at']) + '\n'
        index += 1
    return created_at_list

#获取图片原比例下载链接
def get_image_original_url(json):
    #索引
    index = 0
    #列表
    original_url_list = ''
    #获取图片的原比例下载链接
    for i in json['data']:
        original_url_list = original_url_list + str(i['path']) + '\n'
        index += 1
    return original_url_list

#下载图片
def download_image(url,path):
    #创建文件夹
    if not os.path.exists(path):
        os.makedirs(path)
    #文件名
    filename = url.split('/')[-1]
    #文件路径
    filepath = path + '/' + filename
    #浏览器头部信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    #下载图片
    response = requests.get(url,headers=headers)
    #保存图片
    with open(filepath,'wb') as f:
        f.write(response.content)
        f.close()
        print('下载完成')
    #打开图片
    img = Image.open(filepath)
    #绘制图片
    img.show()

#预览图片
def preview_image(url):
    #浏览器头部信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    #下载图片
    response = requests.get(url,headers=headers)
    #打开图片
    img = Image.open(BytesIO(response.content))
    #绘制图片
    img.show()



#显示图片信息
def show_image_info(json):
    #索引
    index = 0
    #列表
    info_list = ''
    #获取图片的信息
    for i in json['data']:
        info_list = info_list + '图片的id:' + str(i['id']) + '\n'
        info_list = info_list + '图片的url:' + str(i['url']) + '\n'
        info_list = info_list + '图片的浏览数:' + str(i['views']) + '\n'
        info_list = info_list + '图片的类型:' + str(i['file_type']) + '\n'
        info_list = info_list + '图片的颜色配置:' + str(i['colors']) + '\n'
        info_list = info_list + '图片的分辨率:' + str(i['resolution']) + '\n'
        info_list = info_list + '图片的大小:' + str(i['file_size']/1048576) + 'MiB\n'
        info_list = info_list + '图片的收藏数:' + str(i['favorites']) + '\n'
        info_list = info_list + '图片的创建时间:' + str(i['created_at']) + '\n'
        info_list = info_list + '预览图片的下载链接:\n' + str(i['thumbs']) + '\n'
        info_list = info_list + '图片的原比例下载链接:' + str(i['path']) + '\n\n'
        index += 1
    return info_list




#定义变量
def set_var(url):
    #定义字符串变量n
    n = ''
    #输入变量n
    n = input('请输入要搜索的关键字：')
    url = 'https://wallhaven.cc/api/v1/search?q='+ n +'&categories=111&purity=100&sorting=relevance&order=desc'
    json = get_json(url)
    print('一共有' + str(json['meta']['last_page']) + '页')
    #定义变量page
    page = 0
    #输入页数
    page = input('请输入要搜索的页数：')
    url = 'https://wallhaven.cc/api/v1/search?q='+ n +'&categories=111&purity=100&sorting=relevance&order=desc&page=' + page
    print(url)
    return url
    


#运行主程序
if __name__ == '__main__':
    url = set_var('')
    json = get_json(url)
#换行
    print('\n')
#输出结果
    #print('一共' + get_image_url(json).__len__().__str__() + '张图片')
    #print('图片的id：\n' + get_image_id(json))
    #print('图片的浏览数：\n' + get_image_views(json))
    #print('图片的类型：\n' + get_image_type(json))
    #print('图片的颜色配置：\n' + get_image_color_config(json))
    #print('图片的分辨率：\n' + get_image_resolution(json))
    #print('图片的大小：\n' + get_image_size(json))
    #print('图片的收藏数：\n' + get_image_favorites(json))
    #print('预览图片的下载链接：\n' + get_image_downloads(json))
    #print('图片的原比例下载链接：\n' + get_image_original_url(json))
    #print('图片的创建时间：\n' + get_image_created_at(json)) 

    print('图片的信息：\n' + show_image_info(json))
#创建文件并写入内容
    f = open('C:\\Users\\L\\Desktop\\image_info.txt', 'w')
    f.write(show_image_info(json))
    f.close()
#打开文件
    f = open('C:\\Users\\L\\Desktop\\image_info.txt', 'r')
    if f.read() == '':
        print('文件为空')
    else:
        print('写入完成')
    f.close()
#输入要下载图片的链接
    #死循环
    while True:
        down_url = input('请输入要下载的图片的链接：')
        #预览图片
        preview_image(down_url)
        #确认是否下载
        down_sure = input('是否下载？（y/n）')
        if down_sure == 'y':
        #下载图片
            download_image(down_url, 'C:\\Users\\L\\Desktop\\image')
        else:
            print('取消下载')