import mod_reader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    yaml_data_dict = mod_reader.read_yaml("pyanywhere.yaml")
    print()
    print(mod_reader.read_config("default_config.cfg"))
    mod_reader.write_to_json(yaml_data_dict, "pyanywhere.json")
