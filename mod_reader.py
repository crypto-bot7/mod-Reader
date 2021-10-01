import yaml
import configparser
import json


def read_yaml(file):
    """This function reads the yaml file supplied and returns dictionary"""

    with open(file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    return data

def read_config(file):
    """This function reads the config file supplied and returns dictionary"""

    parser = configparser.ConfigParser()
    data = parser.read(file)
    data_dict = dict(parser)
    dict1 = {}
    for key, value in data_dict.items():
        # for key2, value2 in dict(value).items():
        dict1[key] = dict(value)
    return dict1

# def write_env(data,full_filename):
#     with open(full_filename, 'w') as f:
#         for key

def write_to_json(data_dict, file):
    """This function accepts a flat dictionary and an output file name/file
     path. Then converts the dict to JSON and writes it to file"""
    with open(file, 'w') as outfile:
        json.dump(data_dict, outfile)
