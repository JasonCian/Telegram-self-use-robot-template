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
#   功能指令(简单社工库)
########################################################################################################################################################################################################
sgkcommand_logger = logging.getLogger(__name__)
sgkurl = "https://zy.xywlapi.cc/"

# 查q绑


@only_public_at
@only_admin
async def qqcphone_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "qqapi?qq="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/qqcphone'命令")


# 查qq
@only_public_at
@only_admin
async def phonecqq_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "wbapi?id="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/phonecqq'命令")


# qq查lol
@only_public_at
@only_admin
async def qqclol_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "wbapi?id="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/qqclol'命令")

# lol查qq


@only_public_at
@only_admin
async def lolcqq_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "wbapi?id="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/lolcqq'命令")

# 手机查微博


@only_public_at
@only_admin
async def phonecwb_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "wbapi?id="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/phonecwb'命令")

# 微博查手机


@only_public_at
@only_admin
async def wbcphone_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api = "wbapi?id="
    async with aiohttp.ClientSession() as sesssion:
        arg = api + context.args[0]
        url = sgkurl + arg
        async with sesssion.get(url) as resp:
            res = await resp.json()
            info = str(res)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    sgkcommand_logger.debug("机器人处理了一条'/wbcphone'命令")
