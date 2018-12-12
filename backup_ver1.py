import os
import sys
import time
# 1.指定需要备份的文件目录
source = ['C:\\python']
# 2.备份文件夹地址
target_dir = 'C:\\backup'

# 3.备份文件压缩成zip
# 4.压缩文件名为当前的日期和时间
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录不存在，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.zip命令打包文件
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
