from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio

@bot.on_inline_query(filters.regex("^سەرچاوە$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("⚡️ کەناڵی سەرچاوە ⚡️",url="https://t.me/MGIMT"),
             ],
             [
             InlineKeyboardButton("⚡️ بۆ بەژداربوون ⚡️",url="https://t.me/IQ7amo"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - سەرچاوەی زیرەك",
                input_message_content=InputTextMessageContent(
                    "╭──── • ◈ • ────╮\n么 [⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 ⚡️](https://t.me/MGIMT)\n么 [𝘿𝞝𝙑𝙇𝙊𝙋𝞝𝙍 ⚡️](https://t.me/IQ7amo)\n么 [کەناڵی وتە ⚡️](https://t.me/xv7amo)\n╰──── • ◈ • ────╯\n⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼"
                ),
                url="https://t.me/MGIMT",
                description=" SOURCE",
                thumb_url="https://telegra.ph/file/02293319c1eca481884f2.jpg",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )








