import logging
from conf import settings

def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LIVEL)#设置等级

    ch = logging.StreamHandler() #屏幕对象
    ch.setLevel(settings.LOG_LIVEL)

    log_file = "%s\log\%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])


    fh = logging.FileHandler(log_file)#文件对象
    fh.setLevel(settings.LOG_LIVEL)


    #日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger