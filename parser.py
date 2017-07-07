# -*- coding: utf-8 -*-
import os
import re
import traceback
from pprint import pprint

    
# ファイルをパース
def parse_log_files(dir_path, regexp):
    for target in os.listdir(dir_path):
        fp = open(target, 'r')
        for line in fp:
            if re.search(regexp, line):
               print(line)
   
        fp.close()

    
print('Type directory path: /target/dir/name')
target_path = input('>')

print('Type parse word regexp: /^search$/')
search_regexp = input('>')

try:
    parse_log_files(target_path, search_regexp)
except:
    traceback.print_exc()
    exit()
print('End local process')
