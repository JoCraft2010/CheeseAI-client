import configparser

parser = configparser.ConfigParser()
parser.read("config.ini")

general__use_CUDA = bool(int(parser.get("general", "use_CUDA")))

patches__GTX1660_patch = bool(int(parser.get("patches", "GTX1660_patch")))
