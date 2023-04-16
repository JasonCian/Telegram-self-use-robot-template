########################################################################################################################################################################################################
#   导入阶段
########################################################################################################################################################################################################
from utils import *  # 导入项目共用库
from mod_config import *  # 导入配置模块中加载的全局变量
from command_base import *  #导入基础指令模块
from command_sgk import *  #导入社工库指令模块
from command_news import *  #导入新闻指令模块
from command_news import *  #导入新闻指令模块
from mod_calback import * # 导入消息处理模块
from mod_log import Logger  # 导入日志模块
from telegram.ext import (Application,  # 机器人初始化相关，任务处理也会用到
                          CommandHandler,  # 命令注册处理相关
                          MessageHandler, filters,  # 信息处理相关，过滤信息
                          )
########################################################################################################################################################################################################
#   启动日志模块
########################################################################################################################################################################################################
if not os.path.exists("./logs"):
    os.mkdir("./logs")
ConsoleLog = Logger()
main_logger = logging.getLogger(__name__)

########################################################################################################################################################################################################
#   主函数
########################################################################################################################################################################################################


def main():
    # 初始化
    application = (Application.builder()
                   .token(BOT_TOKEN)
                   .build()
                   )
    main_logger.debug("机器人初始化完成")

    # 注册命令规则
    start_handler = CommandHandler('start', start_callback)
    caps_handler = CommandHandler('caps', caps_callback)


    qqcphone_handler = CommandHandler('qqcphone', qqcphone_callback)
    phonecqq_handler = CommandHandler('phonecqq', phonecqq_callback)
    qqclol_handler = CommandHandler('qqclol', qqclol_callback)
    lolcqq_handler = CommandHandler('lolcqq', lolcqq_callback)
    phonecwb_handler = CommandHandler('phonecwb', phonecwb_callback)
    wbcphone_handler = CommandHandler('wbcphone', wbcphone_callback)


    news_handler = CommandHandler('news', news_callback)

    unknown_handler = MessageHandler(filters.COMMAND, unknown_callback)

    Message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message_callback)
    Message_handler = MessageHandler(filters.PHOTO & (~filters.COMMAND), photo_callback)


    main_logger.debug("命令注册完成")

    # 挂载命令
    application.add_handler(start_handler)
    application.add_handler(caps_handler)


    application.add_handler(qqcphone_handler)
    application.add_handler(phonecqq_handler)
    application.add_handler(qqclol_handler)
    application.add_handler(lolcqq_handler)
    application.add_handler(phonecwb_handler)
    application.add_handler(wbcphone_handler)


    application.add_handler(news_handler)


    application.add_handler(unknown_handler)


    application.add_handler(Message_handler)

    main_logger.debug("命令挂载完成")

    # 保持运行
    application.run_polling()


########################################################################################################################################################################################################
#   执行本程序
########################################################################################################################################################################################################
if __name__ == '__main__':
    main()
