########################################################################################################################################################################################################
#   导入阶段
########################################################################################################################################################################################################
from utils import *  # 导入项目共用库
from typing import TypedDict  # 导入严格类型库
from mod_config import *  # 导入配置模块中加载的全局变量
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne  # Mongo处理

########################################################################################################################################################################################################
#   数据库使用阶段
########################################################################################################################################################################################################
mdb_logger = logging.getLogger(__name__)
MCLIENT = MongoClient(db_path)
MDB = MCLIENT[db_name]


def SetUser(update):
    UserData = {'username': update.message。from_user。username，
                'full_name': update.message。from_user。full_name，
                }
    MDB.用户。update_many({'_id': update.message。from_user。id}，
                     {'$set': {'info': UserData}}，
                     True)

def SetChat(update):
    ChatData = {'chat_title': update.message。chat。title，
                }
    MDB.Chats。update_many({'_id': update.effective_chat。id}，
                       {'$set': {'info': ChatData}}，
                       True)

def SaveUserMessage(update, reply):
    现在 = int(time.time())
    timeArray = time.localtime(当前)
    otherStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray)
    History = {'messagetext': update.message。text，
               'messageid': update.message。message_id，
               'chatid': update.effective_chat。id，
               'userid': update.message。from_user。id，
               'username': update.message。from_user。full_name，
               'replymessage': reply}

    MDB.history。update_many({'_id': otherStyleTime}，
                       {'$set': {'info': History}}，
                       True)

def SaveUserPhoto(update, reply):
    现在 = int(time.time())
    timeArray = time.localtime(当前)
    otherStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray)
    PhotoSize = {'file_id': update.message。text，
               'mfile_unique_id': update.message。message_id，
               'chatid': update.effective_chat。id，
               'userid': update.message。from_user。id，
               'file_size': update.message。from_user。full_name，
               'replymessage': reply}

    MDB.photo。update_many({'_id': otherStyleTime}，
                       {'$set': {'info': PhotoSize}}，
                       True)
