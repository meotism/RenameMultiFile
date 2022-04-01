#import pandas as pd
import os
import re
import glob
pathen = r"C:\Users\trann\Downloads\App_Data\test\\"
path = pathen + "*.txt"

result = glob.glob(path)
print(result)
count = 1
for i in result:
    old_name = i
    new_name = str(count)+'c.txt'
    os.rename(old_name, new_name)
    count = count+1
print(result)
