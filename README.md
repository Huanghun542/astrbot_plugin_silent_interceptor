🤫 Silent Interceptor 插件
![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)

![alt text](https://img.shields.io/badge/Python-3.8+-green.svg)

![alt text](https://img.shields.io/badge/AstrBot-v4.0+-purple.svg)
一个简单的AstrBot插件，当机器人被艾特并收到特定关键词时，会拦截消息并保持沉默，不会进行LLM（大语言模型）回复。
✨ 功能特色
消息拦截: 在LLM响应前捕获并拦截指定消息，从根源上阻止机器人回应。
静默处理: 成功拦截后，机器人不会做出任何回应，完美实现“闭嘴”、“安静”等效果。
网页配置: 无需修改代码，可直接在AstrBot的网页设置界面动态添加或删除拦截关键词。
精准触发: 只在机器人被私聊或在群聊中被明确艾特（@）时生效，避免误伤其他群成员的正常对话。
🖼️ 插件配置
本插件的核心功能通过网页UI进行配置。您可以在 AstrBot后台 -> 插件市场 -> 已安装 -> astrbot_plugin_silent_interceptor 配置 中找到设置界面。
![alt text](./docs/config_ui.png)
在“拦截关键词列表”中，您可以自由添加、编辑或删除需要拦截的词语。每次修改后，点击“保存并关闭”即可立即生效（无需重启机器人）。
📦 安装步骤
系统要求
Python 3.8 或更高版本
AstrBot v4.0 或更高版本
安装指南
将插件放入AstrBot插件目录
下载本插件的所有文件。
将整个插件文件夹放入 AstrBot/data/plugins/ 目录下。
重启AstrBot
重启您的AstrBot程序或在后台热重载插件。
插件没有外部依赖，无需安装 requirements.txt。
🎮 使用方法
本插件没有复杂的指令，使用方式非常直观：
群聊中: 艾特（@） 您的机器人，然后单独发送您在后台配置的任意一个关键词（例如：闭嘴）。
私聊中: 直接向您的机器人发送配置好的关键词即可。
效果: 机器人接收到消息后，会识别到关键词并终止后续所有响应流程，表现为“已读不回”。
📄 开源许可
本项目采用 MIT 开源许可证。
