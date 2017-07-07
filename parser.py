# -*- coding: utf-8 -*-
import os
import re
import traceback
from pprint import pprint

    
# ファイルをパース
def parse_log_files():
    for target in os.listdir('target_dir'):
        filename = 'dir/%s'%target
        fp = open(filename, 'r')
        for line in fp:
            if re.search('search_word', line):
               print(line)
   
        fp.close()

    
print('File parse process')
try:
    parse_log_files()
except:
    traceback.print_exc()
    exit()
print('End local process')
