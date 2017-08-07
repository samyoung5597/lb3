from core import db_handler
from conf import settings
import json


def account_load(user_id):

    db_path = db_handler.db_handler(settings.DATABASE)
    new_user_file = "%s\%s.json" % (db_path, user_id)
    with open(new_user_file, "r") as f:
        user_data = json.load(f)
        return user_data

def account_dump(new_accounts):
    db_path = db_handler.db_handler(settings.DATABASE)
    new_user_file = "%s\%s.json" % (db_path, new_accounts['id'])
    with open(new_user_file, "w") as f:
        json.dump(new_accounts, f)
    return True