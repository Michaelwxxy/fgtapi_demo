import yaml

class YamlUtil:
    def __init__(self):
        pass

    #读取yaml文件
    def read_yaml(self, yaml_file):
        """
        读取yaml，对yaml反序列化，即把yaml格式转换成dict格式
        :return:
        """
        with open(yaml_file, encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)