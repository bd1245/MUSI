import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنج"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("جاري حساب سرعه البنج ⚡️ ")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>-›  بنج</b> `{delta_ping * 1000:.3f} ms` \n<b>-›  الوقت</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["تحديث"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**-عزيزي المطور تم التحديث بنجاح  ⚡️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>  نورت يخويا ❤️ {m.from_user.mention}!

🛠 هذه هي قائمـة اوامر سـورس ويلسون و الدوله
- أوامر المستخدمين: 
• !شغل [عنوان المطقع | رابط يوتيوب | الرد على ملف مقطع صوتي] - لتشغيل مقطع صوتي في المكالمه

• !فيديو [عنوان الفيديو | رابط يوتيوب | الرد على الفيديو] - لتشغيل فيديو في المكالمة
• !القائمة  - لعرض قائمة التشغيل الحالية

• !بنج - لعرض سرعه النت للبوت

• !الاوامر - لعرض اوامر سورس ميوزك ويلسون و الدوله

- أوامر المشرفين  : 
• !كمل - لمواصلة تشغيل المقطع الصوتي أو الفيديو المتوقف

• !وقف - لإيقاف تشغيل المقطع الصوتي أو مقطع فيديو مؤقتًا

• !غير - لتخطي المقطع الصوتي أو الفيديو الحالي وتشغيل ما بعده

• !انهاء - لإنهاء التشغيل</b>
"By: @kyany_el5as
DEV: @WEIS0N
DEV: @EL_D_A_W_L_A"""
    await m.reply(HELP)
