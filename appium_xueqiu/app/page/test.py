import yaml
import json
path = "appium_xueqiu/app/data/search.yml"
with open(path, encoding="utf-8") as f:
    steps = yaml.safe_load(f)['add']
raw = json.dumps(steps)
_params = {'name': '阿里巴巴'}
for key, value in _params.items():
    raw = raw.replace(f'${{{key}}}', value)
