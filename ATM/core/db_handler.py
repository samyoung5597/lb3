def db_path(user_data):

    user_path = "%s\%s" % (user_data['path'], user_data['name'])
    return user_path


def db_handler(user_data):
    if user_data['engine'] == "file_storage":
        return db_path(user_data)