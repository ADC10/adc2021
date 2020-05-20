if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1110453723:AAH2tM1XecAuASu83GcRd0d-A4g1BMfqlNc"
    OWNER_ID = "1013112355" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "kingpipo18"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [254318997 683538773 570400686 466337795]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [254318997 683538773 570400686 466337795]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [254318997 683538773 570400686 466337795]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = https://www.paypal.me/kingpipo18  # EG, paypal
    CERT_PATH = None
    PORT = 8443
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
