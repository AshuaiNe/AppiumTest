import yaml
print(yaml.safe_load(open("app/data/data.yml", encoding='utf-8'))['data'])
