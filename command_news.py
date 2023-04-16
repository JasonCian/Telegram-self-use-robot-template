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
#   功能指令(每日新闻功能)
########################################################################################################################################################################################################
newscommand_logger = logging.getLogger(__name__)
newsurl = 'http://excerpt.rubaoo.com/toolman/getMiniNews'

@only_public_at
async def news_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with aiohttp.ClientSession() as sesssion:
        url = newsurl
        async with sesssion.get(url) as resp:
            res = await resp.text()
            jsondata = json.loads(res)
            data = jsondata['data']
            info = data['image']
            print(info)
            ['image']
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo = info, parse_mode="HTML")
            SaveUserMessage(update,  info)
    newscommand_logger.debug("机器人处理了一条'/news'命令")