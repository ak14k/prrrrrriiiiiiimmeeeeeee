class script(object):
   
    START_TXT = """<b>{} {}, ɪ ᴀᴍ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ</b>"""

#<spoiler>➪ ʟᴀᴛᴇsᴛ ɴᴇᴡ ʀᴇʟᴇᴀsᴇs /list</spoiler>
    
    HELP_TXT = """<b>ʜᴇʀᴇ ɪs ᴀ ʙʀɪᴇғ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ sᴏᴍᴇ ᴏғ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴍɪɴᴇ</b>"""
    
    FSUB_TXT = """<b>➜ <u>ʀᴇǫᴜᴇsᴛ ғᴏʀᴄᴇsᴜʙ ᴍᴏᴅ:</u>
    
➥ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴ

/setchat : ᴀᴅᴅ ғᴏʀᴄᴇsᴜʙ / ʀᴇǫᴜᴇsᴛ ᴄʜᴀɴɴᴇʟ ɪᴅ
/delchat : ᴅᴇʟᴇᴛᴇᴅ ғᴏʀᴄᴇsᴜʙ ᴄʜᴀɴɴᴇʟ
/viewchat : ɢᴇᴛ sᴀᴠᴇᴅ ғᴏʀᴄᴇsᴜʙ ᴄʜᴀɴɴᴇʟ ᴅᴇᴛᴀɪʟ
/totalrequests : ɢᴇᴛ ᴛᴏᴛᴀʟ ʀᴇǫᴜᴇsᴛ ᴄᴏᴜɴᴛs ᴏɴ ᴄᴜʀʀᴇɴᴛ ғsᴜʙ ᴄʜᴀɴɴᴇʟ
/purgerequests : ᴄʟᴇᴀʀ ʀᴇǫᴜᴇsᴛs ᴏɴ ᴄᴜʀʀᴇɴᴛ ғsᴜʙ ᴄʜᴀɴɴᴇʟ</b>"""
   
    ADMIN_CMD_TXT = """<b>• /set_muc - sᴇᴛ ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀᴛ ɪᴅ.
• /del_muc - ᴅᴇʟᴇᴛᴇ ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀᴛ ɪᴅ.
• /movie_update_on - ᴇɴᴀʙʟᴇ ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs.
• /movie_update_off - ᴅɪsᴀʙʟᴇ ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs.
• /pm_search_on - ᴇɴᴀʙʟᴇ ᴘᴍ sᴇᴀʀᴄʜ.
• /pm_search_off - ᴅɪsᴀʙʟᴇ ᴘᴍ sᴇᴀʀᴄʜ.
• /postfile - ᴍᴀɴᴜᴀʟ ᴘᴏsᴛ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʟɪɴᴋs.
• /file_text - sᴇᴛ ᴛᴏ ɴᴇᴡ ʀᴇʟᴇᴀsᴇs ɴᴀᴍᴇs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʟɪɴᴋs.
• /index - ɪɴᴅᴇx ᴀʟʟ ғɪʟᴇs.
• /leave - ʟᴇᴀᴠᴇ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢʀᴏᴜᴘ.
• /broadcast - ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs.
• /grp_broadcast - ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.
• /pin_broadcast - ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀs ᴘɪɴ ᴛᴏ ᴀʟʟ ʙᴏᴛ.
• /pin_grp_broadcast - ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀs ᴘɪɴ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs.
• /restart - ᴛᴏ ʀᴇsᴛᴀʀᴛ ʙᴏᴛ.</b>"""   

    ABOUT_TEXT = """<b>‣ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/TGFilmsProvider">Hello</a> 
‣ ʜᴏsᴛᴇᴅ ᴏɴ : <a href="https://www.heroku.com/">ʜᴇʀᴏᴋᴜ</a>
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 𝟹</a>
‣ ʟɪʙʀᴀʀʏ : <a href="https://t.me/TGFilmsProvider">ᴘʏʀᴏғᴏʀᴋ</a></b>"""
   
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    OWNER_INFO = """@TGFilmsProvider"""    

    EXTRAMOD_TXT = """<b>➜ <u>ᴇxᴛʀᴀ ᴍᴏᴅs ᴄᴏᴍᴍᴀɴᴅs:</u>

• /id - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
• /imdb - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ.
• /upload - ᴛᴏ ɢᴇᴛ ʜᴏsᴛ ᴄʟᴏᴜᴅ ʟɪɴᴋ.</b>"""
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    SPELL_TEXT = """<b>🙋🏻‍♂ Hey {}, Something Is Wrong 🫣
    
➪ Check Your Spelling Of Movie Check Correct Spelling <u>Google</u> Button Below Will Help You..
<blockquote expandable>➪ If You Ask For A Movie Released In Theaters, You Will Not Get It, Movie Is Only Available When OTT & DVD Is Released. We Are Not Promote Theatre Prints, Leaked HD
➲ New OTT Files Channel Link Button Below 👇</blockquote>
⚠️ Movie Is Not Available in My Database. You Report To Admin @MlReportrobot 🙅‍♂ Don't Ask Theater Print 📵</b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  
    
    IMDB_TEMPLATE_TXT = """<b>📻 ᴛɪᴛʟᴇ - {title}
🎭 ɢᴇɴʀᴇs - {genres}
🎖 ʀᴀᴛɪɴɢ - {rating} / 10 
📆 ʏᴇᴀʀ - {release_date}
🌟 runtime - {runtime}
❗️ ʟᴀɴɢᴜᴀɢᴇ - {languages}</b>"""

    FILE_CAPTION = """<code> <i>📂{file_name}</i> </code>

<b>╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
♻️ 𝙅𝙊𝙄𝙉 :- @FilmsProviderBot
♻️ 𝙅𝙊𝙄𝙉 :- @TGFilmsProvider
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>"""

    RESTART_TXT = """<b>
📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """• This Is Not Your Movie Request.     
• Don't Click Others Results 🥴."""

    COMUNITY_TEXT = """<b>🎖<u>@TGFilmsProvider</u>🎖
    
➠ 𝖰𝗎𝗂𝖼𝗄𝗅𝗒 𝖩𝗈𝗂𝗇 𝖮𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 & 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌</b>"""

    OLD_ALRT_TXT = """ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇs..sᴇɴᴅ ᴀ ɴᴇᴡ ʀᴇǫᴜᴇsᴛ.."""

    NO_RESULT_TXT = """<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🙄</b>"""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗻𝗮𝗺𝗲.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 😞... 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 𝗱𝗶𝗱 𝘆𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 ?? 👇"""
    
    SOURCE_TXT = """<b>🧑‍💻 <u>𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : </u>

ᴛʜɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ
» sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ~ <spoiler>ᴘʀɪᴠᴀᴛᴇ 😜</spoiler></b>"""

    APPROVED_TEXT = """<b>🙋 Hello {mention}

◈ Your Request To Joined In ➤ <u>{title}</u> Successfully.

◈ Thank You For Joiny ❤️ {mention}
◈ <a href="https://t.me/addlist/IOm27HOynnQ5NmI8">🔞𝗔𝗱𝘂𝗹𝘁 𝗟𝗶𝗻𝗸𝘀🔞</a></b>"""

    DISCL_TXT = """<b>👨‍🏫 <u>𝗗𝗜𝗦𝗖𝗟𝗔𝗜𝗠𝗘𝗥 :</u>
    
<blockquote>𝖠𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 𝖺𝗋𝖾 𝖿𝗋𝖾𝖾𝗅𝗒 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗈𝗇 𝗍𝗁𝖾 𝗂𝗇𝗍𝖾𝗋𝗇𝖾𝗍 𝗈𝗋 𝗉𝗈𝗌𝗍𝖾𝖽 𝖻𝗒 𝗌𝗈𝗆𝖾𝖻𝗈𝖽𝗒 𝖾𝗅𝗌𝖾.
𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗂𝗌 𝗂𝗇𝖽𝖾𝗑𝗂𝗇𝗀 𝖿𝗂𝗅𝖾𝗌 𝗐𝗁𝗂𝖼𝗁 𝖺𝗋𝖾 𝖺𝗅𝗋𝖾𝖺𝖽𝗒 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗈𝗇 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖿𝗈𝗋 𝖾𝖺𝗌𝖾 𝗈𝖿 𝗌𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀,
𝖶𝖾 𝗋𝖾𝗌𝗉𝖾𝖼𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝗅𝖺𝗐𝗌 𝖺𝗇𝖽 𝗐𝗈𝗋𝗄𝗌 𝗂𝗇 𝖼𝗈𝗆𝗉𝗅𝗂𝖺𝗇𝖼𝖾 𝗐𝗂𝗍𝗁 𝖣𝖬𝖢𝖠 𝖺𝗇𝖽 𝖤𝖴𝖢𝖣.</blockquote>

𝖨𝖿 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗂𝗌 𝖺𝗀𝖺𝗂𝗇𝗌𝗍 𝗅𝖺𝗐 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗎𝗌 𝗌𝗈 𝗍𝗁𝖺𝗍 𝗂𝗍 𝖼𝖺𝗇 𝖻𝖾 𝗋𝖾𝗆𝗈𝗏𝖾𝖽 𝖺𝗌𝖺𝗉.</b>"""
   
    RULES_TEXT = """<b>⚠️ <u>𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖥𝗈𝗅𝗅𝗈𝗐 𝖱𝗎𝗅𝖾𝗌</u> 👇🏻

» 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀.
» 𝖬𝗎𝗌𝗍 𝖢𝗁𝖾𝖼𝗄 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗂𝗇 𝖦𝗈𝗈𝗀𝗅𝖾.
» 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 𝖨𝗇 𝖤𝗇𝗀𝗅𝗂𝗌𝗁 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖮𝗇𝗅𝗒.
» 𝖣𝗈𝗇'𝗍 𝖠𝗌𝗄 𝖥𝗈𝗋 𝖴𝗇𝗋𝖾𝗅𝖾𝖺𝗌𝖾𝖽 𝖬𝗈𝗏𝗂𝖾𝗌.
» [𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾, 𝖸𝖾𝖺𝗋, 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾] 𝖠𝗌𝗄 𝖳𝗁𝗂𝗌 𝖶𝖺𝗒.
» 𝖣𝗈 𝖭𝗈𝗍 𝖴𝗌𝖾 𝖶𝗈𝗋𝖽𝗌 𝖫𝗂𝗄𝖾 𝖣𝗎𝖻, 𝖬𝗈𝗏𝗂𝖾, 𝖫𝗂𝗇𝗄, 𝖯𝗅𝗌𝗌, 𝖲𝖾𝗇𝗍 𝖾𝗍𝖼 𝖮𝗍𝗁𝖾𝗋 𝖳𝗁𝖺𝗇 𝖳𝗁𝖾 𝖶𝖺𝗒 𝖬𝖾𝗇𝗍𝗂𝗈𝗇𝖾𝖽 𝖠𝖻𝗈𝗏𝖾.
» 𝖣𝗈𝗇'𝗍 𝖴𝗌𝖾 𝖲𝗍𝗒𝗅𝗂𝗌𝗁 𝖥𝗈𝗇𝗍 𝖶𝗁𝗂𝗅𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍.
» 𝖣𝗈𝗇'𝗍 𝖴𝗌𝖾 𝖲𝗒𝗆𝖻𝗈𝗅𝗌 𝖶𝗁𝗂𝗅𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝗅𝗂𝗄𝖾 (+:;'!-|...𝖾𝗍𝖼).

<spoiler>𝖨𝖿 𝖸𝗈𝗎 𝖣𝗈𝗇'𝗍 𝖦𝖾𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝖠𝗇𝖽 𝖲𝖾𝗋𝗂𝖾𝗌
𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖠𝖽𝗆𝗂𝗇 - @MlReportrobot</spoiler>

<blockquote expandable>» <u>𝖬𝗈𝗏𝗂𝖾𝗌 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖥𝗈𝗋𝗆𝖺𝗍</u>
𝖪𝗎𝗋𝗎𝗉 𝖬𝗈𝗏𝗂𝖾❌
𝖪𝗎𝗋𝗎𝗉 2021 ✅
𝖪𝗀𝖿: 𝖢𝗁𝖺𝗉𝗍𝖾𝗋 2❌
𝖪𝗀𝖿 𝖢𝗁𝖺𝗉𝗍𝖾𝗋 2✅</blockquote>
<blockquote expandable>» <u>𝖲𝖾𝗋𝗂𝖾𝗌 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖱𝗎𝗅𝖾𝗌</u>
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝗌𝖾𝖺𝗌𝗈𝗇 1❌
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖲01✅
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 1❌
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖲01𝖤01✅
𝖲𝗍𝖺𝗇𝗀𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌 𝖲01𝖤P01✅</blockquote>
<blockquote>𝖢𝗅𝗂𝖼𝗄 𝖡𝖾𝗅𝗈𝗐 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖠𝗇𝖽 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖬𝗈𝗏𝗂𝖾𝗌 𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖨𝗇 𝖬𝗈𝗏𝗂𝖾𝗌 𝖦𝗋𝗈𝗎𝗉.</blockquote></b>"""  
      
    MOVIES_UPDATE_TXT = """<b>#New_File_Added

📻 Title: #{title}

🌟 Rating: {rating} / 10
🎥 Quality: Proper HDRip
<blockquote>🎭 Genres: {genres}</blockquote>
@TGFilmsProvider </b>"""
