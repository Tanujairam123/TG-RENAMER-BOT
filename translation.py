from sample_config import Config

class Translation(object):
    START_TEXT = """Hello {name}ᎪᎷ ҒᎪՏͲᎬՏͲ ᎷᏦ 🗡️ ᎡᎬΝᎪᎷᎬᎡ ᏴϴͲ 🖊️.
Ꮖ ᏟᎪΝ ᎡᎬΝᎪᎷᎬ ᎽϴႮᎡ ҒᏆᏞᎬՏ ҒᎪՏͲᎬᎡ🖊️
ՏᎬΝᎠ ᎷᎬ ᎪΝᎽ ҒᏆᏞᎬՏ Ͳϴ ᎡᎬΝᎪᎷᎬ 🖊️
ՏᎬΝᎠ ᎷᎬ ᎪΝᎽ ᏢᎻϴͲϴՏ Ͳϴ ՏᎪᏙᎬ ͲᎻႮᎷᏴΝᎪᏆᏞ 🖊️
ᏟᎪΝ ᎡᎬΝᎪᎷᎬ ✍ ᏔᏆͲᎻ ᏟႮՏͲϴᎷ ͲᎻႮᎷᏴΝᎪᏆᏞ ᎪΝᎠ ႮᏢᏞϴᎪᎠ ᎪՏ ᏙᏆᎠᎬϴ/ҒᏆᏞᎬ

   



Type /help for more details."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "ᎠϴᏔΝᏞϴᎪᎠᏆΝᏀ Ͳϴ ᎷᎽ ՏᎬᎡᏙᎬᎡ ᏢᏞՏ ᏔᎪᏆͲ..🎁"
    DOWNLOAD_START = "ᎠϴᏔΝᏞϴᎪᎠᏆΝᏀ Ͳϴ ᎷᎽ ՏᎬᎡᏙᎬᎡ ᏢᏞՏ ᏔᎪᏆͲ..🎁"
    UPLOAD_START_VIDEO = "ႮᏢᏞϴᎪᎠᏆΝᏀ ᎪՏ ᏙᏆᎠᎬϴ.. 📸"
    UPLOAD_START = "ႮᏢᏞϴᎪᎠᏆΝᏀ ᎪՏ ҒᏆᏞᎬ...✉️"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "ͲᎻᎪΝᏦ ᎽϴႮ ҒϴᎡ ႮՏᏆΝᏀ ᎷᎬ🗡️ ՏͲᎪᎽ ͲႮΝᎬᎠ"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "ᏢᏞᎬᎪՏᎬ /ႮᏢᏀᎡᎪᎠᎬ ᎽϴႮᎡ ՏႮᏴՏᏟᎡᏆᏢͲᏆϴΝ."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/Ns_Bot_supporters'>Ns Bot Supporters</a>"
    SAVED_CUSTOM_THUMB_NAIL = "ͲᎻᎬ ᏟႮՏͲϴᎷ ҒᏆᏞᎬ ՏႮᏟᏟᎬՏՏҒႮᏞ ՏᎪᏙᎬᎠ🗡️"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ͲᎻᎬ ᏟႮՏͲϴᎷ ҒᏆᏞᎬ ᎠᎬᏞᎬͲᎬᎠ ՏႮᏟᏟᎬՏՏҒႮᏞᎽ"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "💘ᎷᎬᎠᏆᎪ ᏟᏞᎬᎪᎡᎬᎠ ՏႮᏟᏟᎬՏՏҒႮᏞᏞᎽ"
    SAVED_RECVD_DOC_FILE = "ᎠϴᏟႮᎷᎬΝͲ ᎠϴᏔΝᏞϴᎪᎠᎬᎠ ՏႮᏟᏟᎬՏՏҒႮᏞᏞᎽ✉️"
    CUSTOM_CAPTION_UL_FILE = "@renamer_Ns_bot"
    NO_CUSTOM_THUMB_NAIL_FOUND = ".ᏟႮՏͲϴᎷ ͲᎻႮᎷᏴΝᎪᏆᏞ ΝϴͲ ҒϴႮΝᎠ🧐."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
 
   


"Support Group : @MK_PROJECTS"""
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

**👨‍💻 Developer:** [Anonymous](https://t.me/Ns_AnoNymouS)

**📮 Channel:** [MK PROJECTS](https://t.me/MKPROJECTS)

**👥 Group:** [MK SUPPOTERS](https://t.me/MK_SUPPORT1)
