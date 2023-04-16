
########################################################################################################################################################################################################
#   导入需要的库
########################################################################################################################################################################################################
import logging  # 日志记录相关
from logging import handlers  # 日志记录处理器相关
from datetime import datetime  # 日期时间相关，用于命名日志文件
from utils import *  # 导入项目共用库
########################################################################################################################################################################################################
#   日志模块
########################################################################################################################################################################################################


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename="./logs/Log-" + datetime.now().date().strftime('%Y-%m-%d') + ".log", when="D", level='debug', fmt='%(asctime)s - %(levelname)s - %(module)s[line:%(lineno)d] : %(message)s'):
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        self.format_str = logging.Formatter(fmt)  # 设置日志格式
        console_handler = logging.StreamHandler()  # 往屏幕上输出
        console_handler.setFormatter(self.format_str)  # 设置屏幕上显示的格式
        File_handler = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        File_handler.setFormatter(self.format_str)  # 设置文件里写入的格式
        self.logger.addHandler(console_handler)  # 把对象加到logger里
        self.logger.addHandler(File_handler)  # 把对象加到logger里
