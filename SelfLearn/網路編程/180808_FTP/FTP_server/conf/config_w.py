import configparser
config = configparser.ConfigParser()

config["jamie"] = {'Password': '1230',
                   'Quotation': '100'}

config["root"] = {'Password': 'root',
                  'Quotation': '100'}

with open('account.cfg', 'w') as f:
    config.write(f)
