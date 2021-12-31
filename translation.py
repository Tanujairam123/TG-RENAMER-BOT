from sample_config import Config

class Translation(object):
    START_TEXT = """Hello <i><b>{}</b></i>,

This is a Telegram Rename clone of <a href='https://t.me/renamer_Ns_bot'>Renamer NS BOT</a> by {}

I Can rename ✍ with custom thumbnail and upload as video/file

Type /help for more details."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "Downloading to my server PLS WAIT.....📥"
    DOWNLOAD_START = "Downloading to my server PLS Wait.....📥"
    UPLOAD_START_VIDEO = "Uploading as video PLS WAIT.....📤"
    UPLOAD_START = "Uploading as File PLS WAIT.....📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using ME stay tuned
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/Ns_Bot_supporters'>Ns Bot Supporters</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail  SUCCESSFUL saved ✅️ .
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail SUCCESSFUL DELETED succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai <b><i>{}</i></b>, 

Ꮖ ᎪᎷ ᎷᏦ🗡️ ᎡᎬΝᎪᎷᎬᎡ ᏴϴͲ 2.0
    
1. Ꮖ ᏟᎪΝ ᎡᎬΝᎪᎷᎬ ᎽϴႮ ҒᏆᏞᎬՏ ҒᎪՏͲᎬᎡ⭐

2. ՏᎬΝᎠ ᎷᎬ ͲᎻᎬ ҒᏆᏞᎬ Ͳϴ ᏴᎬ ᎡᎬΝᎪᎷᎬᎠ ᏆΝ ҒᎪՏͲᎬᎡ

3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

4. Reply to that message with <code>/rename_vidoe new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

--------

Support Group : @MK_PROJECT
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@renamer_Ns_bot</code>
Please short your file name and try again!"""

    About = """Hi __{}__,

**📝 Language:** Python 3

**🧰 Framework:** Pyrogram


**📮 Channel:** [MK PROJECTS ](https://t.me/MKPROJECTS)

**👥 Group:** [MK  SUPPOTERS](https://t.me/MK_SUPPORT1)
