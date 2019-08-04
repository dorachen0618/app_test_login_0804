import os, yaml


def get_file_data(yaml_file):
    with open("./data" + os.sep + yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(stream=f)
        return data
