# 只导入我们 100% 确定存在的模块
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.core.config.astrbot_config import AstrBotConfig
# 从 astrbot.api 导入 logger，这是正确的日志记录方式
from astrbot.api import logger

@register(
    "astrbot_plugin_silent_interceptor",
    "YourName",
    "一个根据特定关键词拦截消息的插件",
    "7.1.0 (Logging Fixed)",
    "https://github.com/Huanghun542/astrbot_plugin_silent_interceptor"
)
class SilentInterceptorPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        # 这部分逻辑是正确的，保持不变
        self.config = config
        self.keywords = self.config.get("intercept_keywords", [])

    # 使用一个能匹配所有文本消息的通用正则表达式
    # 这样可以确保插件能被加载，并且函数能被触发
    @filter.regex(r".*")
    async def intercept_handler(self, event: AstrMessageEvent):
        """
        监听所有消息，并在函数内部进行精确的逻辑判断。
        """
        # 1. 判断消息是否是发给机器人的（这部分逻辑是正确的）
        is_for_bot = event.is_private_chat() or event.is_at_or_wake_command
        if not is_for_bot:
            return

        # 2. 获取纯文本消息
        message_text = event.get_message_str().strip()

        # 3. 检查消息是否在我们从配置中读取的动态关键词列表里
        if message_text in self.keywords:
            # 4. 如果匹配，就调用正确的终止方法
            event.stop_event()
            # 使用正确的 logger.info() 来记录日志
            logger.info(f"成功拦截关键词: '{message_text}'")
