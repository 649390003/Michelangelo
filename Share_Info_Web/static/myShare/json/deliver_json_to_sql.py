import sys
import os
project = 'Share_Info_Web'  # 工作项目根目录
sys.path.append(os.getcwd().split(project)[0] + project)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Share_Info_Web.settings")# project_name 项目名称
django.setup()
import json

from myShare.models import ColsingPrice



filename = "btc_close_2017.json"
# 将json文件中的数据村给了btc_data
with open(filename) as f:
    btc_data = json.load(f)

for btc_dict in btc_data:
    share = ColsingPrice(sclose=btc_dict["close"],sdate=btc_dict["date"],smonth=int(btc_dict["month"]),
                               sweek=int(btc_dict["week"]),sweekday=btc_dict["weekday"])
    share.save()