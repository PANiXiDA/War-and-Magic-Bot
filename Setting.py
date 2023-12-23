import configparser

class Settings:
    config = configparser.ConfigParser()
    config.read("settings.ini", "utf-8")

    countHeroes = config["Settings"]["countHeroes"]
    countAllianceMines = config["Settings"]["countAllianceMines"]