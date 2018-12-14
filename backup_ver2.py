import os
import time
# 1.指定需要备份的文件目录
source = ['C:\\python']
# 2.备份文件夹地址
target_dir = 'C:\\backup'

# 如果目标目录不存在，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3.备份文件压缩成zip
# 4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')

# zip文件名称格式
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory')

# 5.zip命令打包文件
zip_command = 'zip -qr {0} {1}'.format(target, ''.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
