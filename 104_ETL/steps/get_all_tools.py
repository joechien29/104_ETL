# 取得資料夾內每個工作所提到的工具，並計算提到的次數

import json
import os


def get_filename(fold):
    list_dir = os.listdir(fold)
    return list_dir


def get_all_tools(path, filename_list):
    all_tools = []
    for filename in filename_list:
        with open(path + filename, 'r', encoding='utf8') as f:
            data = json.load(f)
            list1 = data['工作內容']
            list2 = data['條件要求']
            list3 = list1 + list2
            tools = ''
            for s in list3:
                for char in s:
                    if (ord(char) >= 65) and ord(char) <= 90:
                        tools += char
                    elif (ord(char) >= 97) and ord(char) <= 122:
                        tools += char
                    else:
                        tools += ' '
            fixed_list = [x for x in tools.strip(' ').split(' ') if x != '']
            all_tools.append(fixed_list)
    return all_tools


filepath = '../downloads/jobs/'
list_dir = [x for x in get_filename(filepath) if '.json' in x]
all_tools = get_all_tools(filepath, list_dir)
flat_list = [item for sublist in all_tools for item in sublist]

tools_count = {}
for tools in flat_list:
    if tools not in tools_count:
        tools_count[tools] = 1
    else:
        tools_count[tools] += 1
sorted_tools = {k: v for k, v in sorted(tools_count.items(), key=lambda item: item[1])}
more_needed = {k: v for k, v in sorted_tools.items() if v >= 8}
print(sorted_tools)
print(more_needed)
