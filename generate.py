import os

repo = '2020-guoqing'
path = '201007'
prefix = '![](https://cdn.jsdelivr.net/gh/xieqiaokang/' + repo + '@1.0/'
final_str = '<photos>'

img_list = os.listdir(path)

for img_name in img_list:
    img_str = prefix + path + '/' + img_name + ')'
    final_str += img_str

final_str += '</photos>'

print(final_str)