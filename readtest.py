import xlrd
import json
import os
import re

exl_src = "C:/Users/Ovenus/Desktop/辰安/文本分析/code/422条突发事件初步处理.xlsx"
seg_path = "C:/Users/Ovenus/Desktop/辰安/文本分析/code/422_seg.txt"
label_path = "C:/Users/Ovenus/Desktop/辰安/文本分析/code/422_label.txt"
stop_path = "C:/Users/Ovenus/Desktop/辰安/文本分析/corpus/stopword.txt"
json_file = "C:/Users/Ovenus/Desktop/辰安/文本分析/code/colliery_data.json"


class Read_file:

    # 读excel文件，提取事件描述 + 训练集Label
    def readexl(self, excel_path):
        ##########################
        ## excel_path: 文件路径 ##
        #########################
        try:
            train_list = []
            train_label = []
            exe_sheet = xlrd.open_workbook(excel_path)
            work_sheet = exe_sheet.sheet_by_name("emergency_event_data")

            for num in range (work_sheet.nrows):
                train_tem = str(work_sheet.cell(num,1).value)
                train_lab = str(work_sheet.cell(num,7).value)
                train_tem = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",train_tem)

                train_list.append("".join(train_tem.split()))
                train_label.append("".join(train_lab.split()))

            return train_list, train_label
        except Exception as e:
            print("[Error] read excel:" + str(e))
            return None

    # 读txt文件, content.txt + Label.txt
    def read_file(self, txt_path):
        ########################
        ## txt_path: 文件路径 ##
        #######################
        try:
            text_content = []
            with open(txt_path,"r", encoding='utf-8') as fp:
                for line in fp:
                    sentence = line.strip()
                    text_content.append(sentence)
            return text_content
        except Exception as e:
            print("[Error] read from txt:" + str(e))
            return None

    # 读取json文件，提取事件描述和事件类型
    def read_json(self, json_path):
        #########################
        ## json_path: 文件路径 ##
        ########################
        try:
            event_describle = []
            event_type = []
            with open(json_path, 'r', encoding='utf-8') as json_data:
                d = json.load(json_data)
                for index in range(len(d['RECORDS'])):
                    event_describle.append(d['RECORDS'][index]['describle'])
                    event_type.append(d['RECORDS'][index]['type'])
            return event_describle, event_type
        except Exception as e:
            print("[Error] read from json:" + str(e))
            return None
