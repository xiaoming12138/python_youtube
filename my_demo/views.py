# -*- coding=utf-8 -*-
# Create your views here.
from django.views import View
import json
from django.http import JsonResponse


import pandas as pd
xslx_file = pd.ExcelFile('./my_demo/test.xlsx')
youtube = xslx_file.parse('YouTube数据')

#处理四舍五入问题
def round_up(number,power=0):
    digit = 10 ** power
    num2 = float(int(number * digit))
    # 处理正数，power不为0的情况
    if number>=0 and power !=0:
        tag = number * digit - num2 + 1 / (digit * 10)
        if tag>=0.5:
            return (num2+1)/digit
        else:
            return num2/digit
    # 处理正数，power为0取整的情况
    elif  number>=0 and power==0 :
        tag = number * digit - int(number)
        if tag >= 0.5:
            return (num2 + 1) / digit
        else:
            return num2 / digit
    # 处理负数，power为0取整的情况
    elif power==0 and number<0:
        tag = number * digit - int(number)
        if tag <= -0.5:
            return (num2 - 1) / digit
        else:
            return num2 / digit
    # 处理负数，power不为0的情况
    else:
        tag = number * digit - num2 - 1 / (digit * 10)
        if tag <= -0.5:
            return (num2-1)/digit
        else:
            return num2/digit

test_data=[]
api_one = []
api_two = []
api_three = []
api_four = []

print(youtube.index.values)
for i in youtube.index.values:  # 获取行号的索引，并对其进行遍历：
    # 根据i来获取每一行指定的数据
    if (int(youtube.iloc[i, 5] != 0)):
        like_rate_num = round_up(100 - round_up(int(youtube.iloc[i, 6]) / int(youtube.iloc[i, 5]) * 100, 2), 2)
    else:
        like_rate_num = 0.00

    row_data = {
        '_id': youtube.iloc[i, 0],
        'name': youtube.iloc[i, 8],
        'index': i,
        'look_num': youtube.iloc[i, 4],
        'like_num': youtube.iloc[i, 5],
        'dis_like_num': youtube.iloc[i, 6],
        'like_rate': like_rate_num
    }
    # 第一个接口数据
    api_one_data = {
        '_id': youtube.iloc[i, 0],
        'index': float(i),
        'name': youtube.iloc[i, 8],
        'like_rate': like_rate_num
    }
    # 第二个接口数据
    if (like_rate_num >= 95):
        api_two_data = {
            '_id': youtube.iloc[i, 0],
            'index': float(i),
            'name': youtube.iloc[i, 8],
            'like_rate': like_rate_num
        }
        api_two.append(api_two_data)
    # 第三个接口数据
    if (like_rate_num < 95):
        api_three_data = {
            '_id': youtube.iloc[i, 0],
            'index': float(i),
            'name': youtube.iloc[i, 8],
            'like_rate': like_rate_num
        }
        api_three.append(api_three_data)
    # 第四个接口数据
    if (youtube.iloc[i, 5] >= 100000):
        api_four_data = {
            '_id': youtube.iloc[i, 0],
            'index': float(i),
            'name': youtube.iloc[i, 8],
            'like_num': float(youtube.iloc[i, 5]),
            'like_rate': like_rate_num
        }
        api_four.append(api_four_data)

    test_data.append(row_data)
    api_one.append(api_one_data)


class GetLikeRateAPIView(View):
    def get(self,request):
        req = request.GET and request.GET['rate'] or False
        print(req)
        """查询所有视频喜欢不喜欢的比率  GET     /get_rate"""
        if req == 'above':
            data_dict = {
                "data": api_two,
                "status": 200,
                "msg": "success"
            }
        elif req == 'below':
            data_dict = {
                "data": api_three,
                "status": 200,
                "msg": "success"
            }
        elif req == 'likes':
            data_dict = {
                "data": api_four,
                "status": 200,
                "msg": "success"
            }
        else:
            data_dict = {
                "data": api_one,
                "status": 200,
                "msg": "success"
            }

        # JsonResponse 可以把字典、列表转换为json.但是转换列表时需要指定，safe=False
        return JsonResponse(data_dict,status=200)




