class script(object):   
    HELP_TXT = """𝙷𝙴𝚈 {}\n𝖧𝖾𝗋𝖾 𝗂𝗌 𝗆𝗒 𝖧𝖤𝖫𝖯 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌."""

    ABOUT_TXT = """𒊹︎︎︎ 𝖬𝗒 𝖭𝖺𝗆𝖾 : {}
✯ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=https://t.me/k_ASTRA1>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</a>
𒊹︎︎︎ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆
𒊹︎︎︎ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝖳𝗁𝗋𝖾𝖾
𒊹︎︎︎ 𝖣𝖺𝗍𝖺 𝖡𝖺𝗌𝖾 : 𝖬𝖮𝖭𝖦𝖮-𝖣𝖡
𒊹︎︎︎ 𝖡𝗈𝗍 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝖶𝗁𝖾𝗋𝖾
𒊹︎︎︎ 𝖡𝗎𝗂𝗅𝖽 𝖵𝖾𝗋𝗌𝗂𝗈𝗇 : 𝖴𝖪𝖭𝖮𝖶𝖭"""

    SOURCE_TXT = """<b>NOTE:</b>
- 𝖥𝗈𝗋 𝖤𝗇𝗊𝗎𝗂𝗋𝖾𝗌 :<a href=https://t.me/k_ASTRA1>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</a>

<b>𝖣𝖤𝖵𝖲:</b>
- 𝖨 𝖶𝖺𝗌 𝖬𝖺𝖽𝖾 𝖡𝗒<a href=https://t.me/k_ASTRA1>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</a>
𝖲𝗉𝖾𝖼𝗂𝖺𝗅 𝖳𝗁𝖺𝗇𝗄𝗌 𝖳𝗈 𝖤𝗏𝖺 𝖬𝖺𝗋𝗂𝖺 𝖣𝖤𝖵𝖲 𝖺𝗇𝖽 𝖢𝗅𝗈𝗇𝖾𝗋𝗌 𝖥𝖮𝖱 𝗍𝗁𝖾 𝖢𝖮𝖣𝖤𝖲"""

    FILE_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐞../

<b>𝖡𝖸 𝖴𝗌𝗂𝗇𝗀 𝖳𝖧𝖨𝖲 𝖬𝗈𝖽𝗎𝗅𝖾 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖲𝗍𝗈𝗋𝖾 𝖥𝖨𝖫𝖤𝖲 𝖨𝖭 𝖬𝗒 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 𝖠𝖭𝖣 𝖨 𝗐𝗂𝗅𝗅 𝖦𝗂𝗏𝖾 𝖸𝗈𝗎 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖠𝖼𝖼𝖾𝗌𝗌 𝖳𝗁𝖾 𝖲𝖠𝖵𝖤𝖣 𝖥𝗂𝗅𝖾𝗌. 𝖨𝖿 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖳𝗈 𝖠𝖽𝖽 𝖥𝗂𝗅𝖾𝗌 𝖥𝗋𝗈𝗆 𝖠 𝖯𝗎𝖻𝗅𝗂𝖼 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖲𝖾𝗇𝖽 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾 𝖫𝖨𝖭𝖪 𝖮𝗇𝗅𝗒 𝖮𝗋 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖳𝗈 𝖠𝖽𝖽 𝖥𝗂𝗅𝖾𝗌 𝖥𝗋𝗈𝗆 𝖠 𝖯𝗋𝗂𝗏𝖺𝗍𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖸𝗈𝗎 𝖬𝗎𝗌𝗍 𝖬𝖺𝗄𝖾 𝖬𝖤 𝖠𝖣𝖬𝖨𝖭 𝖮𝗇 𝖳𝗁𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖠𝖼𝖼𝖾𝗌𝗌 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌...//</b>

𒊹︎︎︎ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾 ›

➪ /plink ›› <b>𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠𝗇𝗒 𝖬𝖾𝖽𝗂𝖺 𝖳𝗈 𝖦𝖤𝖳 𝖳𝗁𝖾 𝖫𝗂𝗇𝗄.</b>
➪ /pbatch ›› <b>𝖴𝗌𝖾 𝖸𝗈𝗎𝗋 𝖬𝖤𝖣𝖨𝖠 𝖫𝗂𝗇𝗄 𝖶𝗂𝗍𝗁 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.</b>
➪ /batch ›› <b>𝖳𝗈 𝖢𝗋𝖾𝖺𝗍𝖾 𝖫𝗂𝗇𝗄 𝖥𝗈𝗋 𝖬𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖥𝗂𝗅𝖾𝗌.</b>

𒊹︎︎︎ 𝖥𝗈𝗋 𝖠𝗇 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 ›

<code>/batch https://t.me/mkn_bots_updates https://t.me/Movie_Genie SUPPORT</code>

𝖢𝗋𝖾𝖽𝗂𝗍𝗌 ☞︎︎︎ <a href=https://t.me/Movie_Genie SUPPORT><b>𝖬𝗈𝗏𝗂𝖾 𝖦𝖾𝗇𝗂𝖾</b></a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭  will respond whenever a keyword is found the message

<b>𝖭𝖮𝖳𝖤:</b>
1. 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖲𝗁𝗈𝗎𝗅𝖽 𝖧𝖺𝗏𝖾 𝖠𝖽𝗆𝗂𝗇 𝖯𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
2. 𝖮𝗇𝗅𝗒 𝖠𝖽𝗆𝗂𝗇𝗌 𝖢𝖺𝗇 𝖠𝖽𝖽 𝖥𝗂𝗅𝗍𝖾𝗋𝗌 𝖮𝗇 𝖠 𝖢𝗁𝖺𝗍
3. 𝖠𝗅𝖾𝗋𝗍 𝖡𝗎𝗍𝗍𝗈𝗇 𝖧𝖺𝗏𝖾 𝖠 𝖫𝗂𝗆𝗂𝗍 𝖮𝖿 𝖲𝗂𝗑𝗍𝗒 𝖥𝗈𝗎𝗋 𝖢𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>

• <code>/g_filter off</code> use this commoand + on/off in your group to control global filter in your group"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙾𝙽/𝙾𝙵𝙵 𝙼𝙾𝙳𝚄𝙻𝙴..
<u>USE THIS COMMAND ON YOUR GROUP</u>

• /autofilter on - autofilter enable in yor chat
• /autofilter off - autofilter disable in your chat 

𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖨𝗌 𝗍𝗁𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾 𝖳𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖠𝖭𝖣 𝖲𝖺𝗏𝖾 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 𝖠𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖥𝗋𝗈𝗆 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖦𝗋𝗈𝗎𝗉. 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖳𝗁𝖾 𝖥𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌  𝖳𝗈 𝖮𝖭 𝖠𝗇𝖽 𝖮𝖥𝖥 𝖳𝗁𝖾 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉../

𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :-
›› /set_template - 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖨𝖬𝖣𝖡 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖥𝗈𝗋 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋. 
›› /get_template - 𝖦𝖤𝖳 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖨𝖬𝖣𝖡 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖮𝖿 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋.

𝖢𝗋𝖾𝖽𝗂𝗍𝗌 :- <a href=https://t.me/k_ASTRA</a>**"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>𝖭𝖮𝖳𝖤:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔋 <u><b>Basic Command</b></u>
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>

🗂️ <u><b>Database & Server Command</b></u>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀᴛʙᴀꜱᴇ ꜱᴛᴀᴛᴜꜱ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>"""

    US_CHAT_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

📯 <u><b>Chat & User</b></u>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /restart - <code>Tᴏ Rᴇsᴛᴀʀᴛ ᴀ Bᴏᴛ</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>

• /clear_junk - clear all delete account & blocked account in database 
• /clear_junk_group - clear add removed group or deactivated groups on db"""

    G_FIL_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔥 <u><b>Adv Global Filter </b></u>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ</code>
"""

    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>
<b>᚛› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>𝖦𝗋𝗈𝗎𝗉 ☞︎︎︎ {a}(<code>{b}</code>)</b>
<b>𝖦 𝖨𝖣 ☞︎︎︎ @{c}
<b>𝖳𝖮𝖳𝖠𝖫 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 ☞︎︎︎ {d}</b>
<b>𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 ☞︎︎︎ {e}</b>

By {f}
"""
    LOG_TEXT_P = """𝖶𝖤 𝖦𝗈𝗍 𝖠 𝖭𝖤𝖶 𝖴𝖲𝖤𝖱!
    
<b>• 𝖴𝗌𝖾𝗋'𝗌 𝖨𝖣 - <code>{}</code></b>
<b>• 𝖴𝗌𝖾𝗋'𝗌 𝖭𝖠𝖬𝖤 - {}</b>
<b>• 𝖴𝖭 - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """𝖧𝖤𝖫𝖯 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗂𝖼𝗄 𝖴𝖲𝖤𝖱𝖲

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝖧𝖤𝖫𝖯 𝖨𝗆𝖺𝗀𝖾

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

𒊹︎︎︎ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾:

• 𝖩𝖴𝖲𝖳 𝖲𝖤𝖭𝖣 𝖬𝖤 𝖠𝖭 𝖨𝖬𝖠𝖦𝖤 𝖳𝖮 𝖤𝖣𝖨𝖳 ✨

𝖮𝖧𝖧 𝖨 𝗐𝖺𝗌 𝗆𝖺𝖽 𝖻𝗒 <a href=https://t.me/k_ASTRA1>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</a>"""

    RESTRIC_TXT = """𝖧𝖤𝖫𝖯: 𝖬𝖴𝖳𝖤 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

• /ban: 𝖳𝗈 𝖡𝖺𝗇 𝖠 𝖴𝗌𝖾𝗋 𝖥𝗋𝗈𝗆 𝖠 𝖦𝗋𝗈𝗎𝗉.
• /unban: 𝖳𝗈 𝖴𝗇𝖻𝖺𝗇 𝖠 𝖡𝖺𝗇𝗇𝖾𝖽 𝖴𝗌𝖾𝗋.
• /tban: 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖡𝖺𝗇 𝖠 𝖴𝗌𝖾𝗋.
• /mute: 𝖳𝗈 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 𝖨𝗇 𝖠 𝖦𝗋𝗈𝗎𝗉.
• /unmute: 𝖳𝗈 𝖴𝗇𝗆𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 𝖨𝗇 𝖠 𝖦𝗋𝗈𝗎𝗉.
• /tmute: 𝖳𝗈 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋.

• 𝖮𝖧𝖧 𝖠𝗇𝖽 𝖭𝖮𝖳𝖤:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>

<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>

<b>𒊹︎︎︎ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾</b>

𒊹︎︎︎ /pin :- 𝖳𝗈 𝖯𝗂𝗇 𝖳𝗁𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖮𝗇 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗍𝗌
𒊹︎︎︎ /unpin :- 𝖳𝗈 𝖴𝗇𝗉𝗂𝗇 𝖳𝗁𝖾 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖯𝗂𝗇𝗇𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>𒊹︎︎︎ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""

    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /ping - To get your ping.
<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me this command reply with Picture or Vide Under (5MB) 

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    CARB_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽︎
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""

    FOND_TXT = """☾𝖧𝖤𝖫𝖯 𝖥𝖮𝖱 𝖥𝖮𝖭𝖳𝖲
𝖥𝖮𝖭𝖳 𝖨𝖲 𝖠 𝖬𝖮𝖣𝖴𝖫𝖤 𝖳𝖮 𝖬𝖠𝖪𝖤 𝖸𝖮𝖴𝖱 𝖳𝖤𝖷𝖳 𝖲𝖳𝖸𝖫𝖨𝖲𝖧
𝖳𝖮 𝖴𝖲𝖤 𝖳𝖧𝖤 𝖥𝖤𝖠𝖳𝖴𝖱𝖤 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""

    SHARE_TXT = 𝖧𝖤𝖫𝖯 𝖥𝖮𝖱 𝖲𝖧𝖠𝖱𝖤 𝖳𝖤𝖷𝖳

𒊹︎︎︎ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾:
• /share - 𝚁𝚎𝚙𝚕𝚢 𝚆𝚒𝚝𝚑 𝙰𝚗𝚢 𝚃𝚎𝚡𝚝 𝚃𝚘 𝚂𝚎𝚗𝚍 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 """

    YTDL = """<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

🍁 𝖴𝖲𝖠𝖦𝖤
𝖸𝗈𝗎 𝖢𝖺𝗇 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖡𝗈𝗍𝗁 𝖵𝗂𝖽𝖾𝗈𝗌 𝖠𝗇𝖽 𝖠𝗎𝖽𝗂𝗈𝗌 𝖥𝗋𝗈𝗆 𝖸𝖳

𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾
• /song 𝖲𝗈𝗇𝗀 𝖭𝖺𝗆𝖾
• /video or /mp4 𝘈𝘯𝘥 https://youtu.be/*****

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/song kevin</code>
<code>/mp4 https://youtu.be/*******</code>
<code>/video https://youtu.be/*****</code>  """


    


    

