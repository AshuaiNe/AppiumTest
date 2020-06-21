import yaml
import json
import time
import os
# path = "appium_xueqiu/app/data/search.yml"
# with open(path, encoding="utf-8") as f:
#     steps = yaml.safe_load(f)['add']
# raw = json.dumps(steps)
# _params = {'name': '阿里巴巴'}
# for key, value in _params.items():
#     raw = raw.replace(f'${{{key}}}', value)


def screenshot(file_path: str = None):
    if file_path is None:
        project_path = os.getcwd()
        file_path = project_path + "/image/"
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        image_name = int(time.time())
        file_path = file_path + str(image_name) + '.png'


print(screenshot())