########################################################################################################################################################################################################
#   导入阶段
########################################################################################################################################################################################################
from utils import *  # 导入项目共用库
from functools import wraps # 导入装饰器函数
from mod_config import *  # 导入配置模块中加载的全局变量
from mod_mdb import *  # 导入数据库模块中的指令
########################################################################################################################################################################################################
#   常用的函数
########################################################################################################################################################################################################
warp_logger = logging.getLogger(__name__)
# 禁止命令
async def invalid_command(update, context):
    text = "您无法使用这个命令"
    await update.message.reply_text(text=text, quote=True)

# 不回复命令
def checkValidCommand(text, BOT_NAME):
    text = text.split()[0]
    try:
        at = text.index('@')+1
        if text[at:] == BOT_NAME:
            return True
        else:
            return False
    except ValueError:
        return False

# 管理员指令装饰器
def only_admin(func):
    @wraps(func)
    async def wrapped(update, context, *args, **kwargs):
        if update.message.from_user.id not in admins:
            await invalid_command(update, context, *args, **kwargs)
            SaveUserMessage(update,  "权限不足")
            warp_logger.debug("权限不足")
            return
        return await func(update, context, *args, **kwargs)
    return wrapped

#在非私有聊天中必须@机器人才能执行指令
def only_public_at(func):
    @wraps(func)
    async def wrapped(update, context, *args, **kwargs):
        SetUser(update)
        SetChat(update)
        if update.message.chat.type != "private":
            if checkValidCommand(update.message.text, BOT_NAME) == False:
                SaveUserMessage(update,  "发出指令时未指定本机器人")
                warp_logger.debug("发出指令时未指定本机器人")
                return
        return await func(update, context, *args, **kwargs)
    return wrapped

