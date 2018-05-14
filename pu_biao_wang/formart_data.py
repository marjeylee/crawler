# -*- coding: utf-8 -*-
"""
进行数据清洗、格式化
"""
import json
import os
import re
from collections import defaultdict

from framework.utility.word_process import is_chinese_character, remove_bracket


def get_original_list():
    """
    从文件中读取所有json数据并转换
    :return:
    """
    original_list = []
    for root, dirs, files in os.walk("./detail_content", topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            with open(file_path, mode='r', encoding='utf8') as file:
                text = file.readlines()[0]
                json_obj = json.loads(text)
                original_list.append(json_obj)
                # return original_list
    return original_list


def split_str_to_content_obj(result, content_str):
    """
    把str转变成obj
    :param result:
    :param content_str
    :return:
    """
    content = {}
    for title in result:
        re_str = title + '[\s\S\w\W]*?【'
        pattern = re.compile(re_str)
        match_obj = pattern.search(content_str)
        match_str = match_obj.group(0)
        match_str = match_str.replace(title, '').replace('【', '').replace('】', '')
        title = title.replace('【', '')
        title = title.replace('】', '')
        content[title] = match_str
    return content


def format_prescription(content):
    """
    格式化处方
    :param content:
    :return:
    """
    prescription_str = content['处方']
    prescription_str = remove_bracket(prescription_str)
    prescription_list = []
    tmp_str = ''
    for i in range(len(prescription_str)):
        ch = prescription_str[i]
        if is_chinese_character(ch):
            tmp_str = tmp_str + ch
        else:
            if len(tmp_str) > 0:
                prescription_list.append(tmp_str)
                tmp_str = ''
    content['处方+'] = prescription_list


def format_usage(content):
    """
    格式化主治和功效
    :param content:
    :return:
    """
    s = content['功能与主治'].strip()
    if s.find('用于'):
        str_list = s.split('用于')
        usage_str = str_list[0]
        treatment_str = str_list[1]
        usage_list = []
        treatment_list = []
        tmp_usage_str = ''
        tmp_treatment_str = ''
        for i in range(len(treatment_str)):
            ch = treatment_str[i]
            if is_chinese_character(ch):
                tmp_usage_str = tmp_usage_str + ch
            else:
                if len(tmp_usage_str) > 0:
                    usage_list.append(tmp_usage_str)
                    tmp_usage_str = ''
        """疗效"""
        for i in range(len(usage_str)):
            ch = usage_str[i]
            if is_chinese_character(ch):
                tmp_treatment_str = tmp_treatment_str + ch
            else:
                if len(tmp_treatment_str) > 0:
                    treatment_list.append(tmp_treatment_str)
                    tmp_treatment_str = ''
        content['功能'] = usage_list
        content['主治'] = treatment_list


def format_content(detail_obj):
    """
    用于格式化数据
    :param detail_obj:
    :return:
    """
    content_str = detail_obj['content'] + '【'
    pattern = re.compile('【\S*】')
    result = pattern.findall(content_str)
    content = split_str_to_content_obj(result, content_str)
    try:
        format_prescription(content)
        format_usage(content)
        detail_obj['content'] = content
        return detail_obj
    except Exception as e:
        return None


if __name__ == '__main__':
    o_list = get_original_list()

    f_list = []
    for obj in o_list:
        f_list.append(format_content(obj))
    c_dict = defaultdict(int)
    for obj in f_list:
        try:
            c = obj['content']['功能']
            for name in c:
                c_dict[name] = c_dict[name] + 1
        except Exception as e:
            pass
    c_dict = sorted(c_dict.items(), key=lambda d: d[1], reverse=True)
    for f in f_list:
        try:
            strs = f['content']['功能与主治']
            if str(strs).index('急') > 0:
                print(str(strs).index('急、'))
                print(strs)
                print(f['content']['功能和主治'])
        except Exception:
            pass
