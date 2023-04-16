########################################################################################################################################################################################################
#   导入阶段
########################################################################################################################################################################################################
from utils import *  # 导入项目共用库
from mod_mdb import *  # 导入数据库模块中的指令
from mod_config import *  # 导入配置模块中加载的全局变量
from mod_warp import *  # 导入装饰器函数
from telegram import (Update,  # tg机器人更新相关，用于更新机器人收到的消息
                      InlineKeyboardButton,  # 内联键盘
                      InlineKeyboardMarkup,  # 内联键盘markdown格式
                      )
from telegram.ext import (ContextTypes,  # 文本格式相关，大小写
                          ConversationHandler,  # 对话相关
                          BasePersistence,  # 持久化存储相关，使用第三方存储
                          )
########################################################################################################################################################################################################
#   机器人基础指令机制
########################################################################################################################################################################################################
basecommand_logger = logging.getLogger(__name__)


# /start指令,注册用户
@only_public_at
async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    basecommand_logger.info("用户 %s (%s) 使用了'/start'命令." %
                            (update.message.from_user.full_name, update.message.from_user.id))
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="你好%s (%s)，欢迎使用jason的自用机器人" %
        (update.message.from_user.full_name, update.message.from_user.id)
    )
    SaveUserMessage(update,  "你好%s (%s)，欢迎使用jason的自用机器人" %
                    (update.message.from_user.full_name,
                     update.message.from_user.id)
                    )
    basecommand_logger.debug("机器人处理了一条'/start'命令")


# /caps命令，它将一些文本作为参数并在回复时给出这些参数的大写形式
@only_public_at
async def caps_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    SaveUserMessage(update,  text_caps)
    basecommand_logger.debug("机器人处理了一条'/caps'命令")


# 指令识别，会在接受到无法识别的指令输入时回复"抱歉，您输入的指令并非本机器人可识别的指令"
async def unknown_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="抱歉，您输入的不是本机器人可识别的指令！")
    basecommand_logger.debug("机器人处理了一条无法识别的命令")
