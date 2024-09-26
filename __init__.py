from typing import Tuple, Any
from nonebot import on_regex
from nonebot.params import RegexGroup
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from utils.message_builder import image
from services.log import logger
from utils.manager import withdraw_message_manager
from configs.config import Config

from typing import Tuple
from nonebot.plugin import PluginMetadata
from zhenxun.configs.config import Config
from zhenxun.configs.path_config import TEMP_PATH
from zhenxun.configs.utils import PluginExtraData, RegisterConfig
from zhenxun.services.log import logger
from zhenxun.utils.http_utils import AsyncHttpx
from zhenxun.utils.message import MessageUtils
from zhenxun.utils.withdraw_manage import WithdrawManager

__zx_plugin_name__ = "lap"
__plugin_usage__ = """
usage：
    我与赌毒不共戴天！！！色图虽好但不要冲太多哦！！！
    指令：
        lap/腿/sn[1-5]/skll/ll/cos2/jz1/jz2
    示例：5连  lap|leg|指令 （单次请求张数小于9）
""".strip()
__plugin_des__ = "看看漂亮妹妹？"
__plugin_cmd__ = ["lap/腿/sn[1-5]/skll/ll/cos2/jz1/jz2"]
__plugin_version__ = 0.1
__plugin_author__ = "Shouzi"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["lap", "LAP", "腿", "sn[1-5]", "sll", "ll", "cos2", "jz1", "jz2"],
}
__plugin_configs__ = {
    "WITHDRAW_LAP_MESSAGE": {
        "value": (30, 1),
        "help": "自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
        "default_value": (0, 1),
    },
    "WITHDRAW_XJJ_MESSAGE": {
        "value": (30, 1),
        "help": "自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
        "default_value": (0, 1),
    },
    "WITHDRAW_LSP_MESSAGE": {
        "value": (30, 1),
        "help": "自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
        "default_value": (0, 1),
    },
}


__plugin_meta__ = PluginMetadata(
    name="lap",
    description="我与赌毒不共戴天！！！色图虽好但不要冲太多哦！！！",
    usage="""
    lap/腿/sn[1-5]/skll/ll/cos2/jz1/jz2
    示例: lap/腿/sn[1-5]/skll/ll/cos2/jz1/jz2
    """.strip(),
    extra=PluginExtraData(
        author="shouzi",
        version="0.1",
        configs=[
            RegisterConfig(
                key="WITHDRAW_LAP_MESSAGE",
                value=(30, 1),
                help="自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
                default_value=(30, 1),
                type=Tuple[int, int],
            ),
            RegisterConfig(
                key="WITHDRAW_XJJ_MESSAGE",
                value=(30, 1),
                help="自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
                default_value=(30, 1),
                type=Tuple[int, int],
            ),
            RegisterConfig(
                key="WITHDRAW_LSP_MESSAGE",
                value=(30, 1),
                help="自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
                default_value=(30, 1),
                type=Tuple[int, int],
            ),
        ],
    ).dict(),
)

lap = on_regex("^(\d?)连?(lap|LAP|腿)$", priority=5, block=True)


# url = "https://api.jrsgslb.cn/cos/url.php?return=img"
url = "http://api.qemao.com/api/pic/?type=ad"


@lap.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await lap.send(image(url))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"lap 发送了未知错误 {type(e)}：{e}")


xjj = on_regex("^(\d?)连?(学习|xjj)$", priority=5, block=True)


# xjjurl = "https://img.moehu.org/pic.php?id=xjj"
xjjurl = "https://img.moehu.org/pic.php?id=xjj"


@xjj.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await xjj.send(image(xjjurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_XJJ_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"xjj 发送了未知错误 {type(e)}：{e}")


lsp = on_regex("^(\d?)连?(lsp|LSP)$", priority=5, block=True)


lspurl = "https://api.jrsgslb.cn/cos/url.php?return=img"


@lsp.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await lsp.send(image(lspurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LSP_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"lap 发送了未知错误 {type(e)}：{e}")


leg = on_regex("^(\d?)连?(leg|足控)$", priority=5, block=True)


# url = "https://api.jrsgslb.cn/cos/url.php?return=img"
tpmturl = "https://ovooa.com/API/meizi/api.php?type=image"


@leg.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await leg.send(image(tpmturl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"leg 发送了未知错误 {type(e)}：{e}")


pc = on_regex("^(\d?)连?(pc|胖次)$", priority=5, block=True)


# url = "https://api.jrsgslb.cn/cos/url.php?return=img"
pcurl = "https://api.uomg.com/api/rand.img3?sort=胖次猫&format=images"


@pc.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await pc.send(image(pcurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"pc 发送了未知错误 {type(e)}：{e}")


qlgs = on_regex("^(\d?)连?(qlgs|七了个三)$", priority=5, block=True)


# url = "https://api.jrsgslb.cn/cos/url.php?return=img"
qlgsurl = "https://api.uomg.com/api/rand.img3?sort=七了个三&format=img"


@qlgs.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await qlgs.send(image(qlgsurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
            )
        except Exception as e:
            logger.error(f"qlgs 发送了未知错误 {type(e)}：{e}")


cos2 = on_regex("^(\d?)连?(cos2|jpcos)$", priority=5, block=True)


cos2url = "https://ovooa.com/API/cosplay/api.php?type=image"


@cos2.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await cos2.send(image(cos2url))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await cos2.send("色图虽好但不要冲太多哦")
            )
        except Exception as e:
            logger.error(f"cos2 发送了未知错误 {type(e)}：{e}")


ll = on_regex("^(\d?)连?(ll|萝莉1)$", priority=5, block=True)


llurl = "https://api.r10086.com/img-api.php?type=萝莉"


@ll.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await ll.send(image(llurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await ll.send("色图虽好但不要冲太多哦")
            )
        except Exception as e:
            logger.error(f"ll 发送了未知错误 {type(e)}：{e}")


jz1 = on_regex("^(\d?)连?(jz1|橘子1)$", priority=5, block=True)


jz1url = "https://api.r10086.com/img-api.php?type=橘里橘气横屏系列1"


@jz1.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await jz1.send(image(jz1url))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await jz1.send("色图虽好但不要冲太多哦")
            )
        except Exception as e:
            logger.error(f"jz1 发送了未知错误 {type(e)}：{e}")


ys1 = on_regex("^(\d?)连?(yst1|原神1)$", priority=5, block=True)


ys1url = "https://api.r10086.com/img-api.php?type=原神竖屏系列1"


@ys1.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await ys1.send(image(ys1url))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await ys1.send("二次元真不错嘿嘿(●´∀｀●)")
            )
        except Exception as e:
            logger.error(f"ys1 发送了未知错误 {type(e)}：{e}")


ys2 = on_regex("^(\d?)连?(yst2|原神2)$", priority=5, block=True)


ys2url = "https://api.r10086.com/img-api.php?type=原神横屏系列1"


@ys2.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await ys2.send(image(ys2url))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await ys2.send("二次元真不错嘿嘿(●´∀｀●)")
            )
        except Exception as e:
            logger.error(f"ys2 发送了未知错误 {type(e)}：{e}")


tb = on_regex("^(\d?)连?(tb|淘宝)$", priority=5, block=True)


tburl = "https://api.ghser.com/tao"


@tb.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await tb.send(image(tburl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await tb.send("漂亮妹妹真不错嘿嘿(●´∀｀●)")
            )
        except Exception as e:
            logger.error(f"tb 发送了未知错误 {type(e)}：{e}")


tk = on_regex("^(\d?)连?(tk|腿控)$", priority=5, block=True)


tkurl = "http://jintia.jintias.cn/api/tk.php"


@tk.handle()
async def _(bot: Bot, event: MessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    num = reg_group[0] or 1
    for _ in range(int(num)):
        try:
            msg_id = await tk.send(image(tkurl))
            withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("lap", "WITHDRAW_LAP_MESSAGE"),
                await tk.send("漂亮妹妹真不错嘿嘿(●´∀｀●)")
            )
        except Exception as e:
            logger.error(f"tk 发送了未知错误 {type(e)}：{e}")
