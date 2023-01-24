import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @am_robots")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5931646626:AAGWH3AYL-qIx7GkQhmWeyp0p5DT3tDwlk8') #BOT Token Add
API_ID = int(os.environ.get('API_ID', '16734393')) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', 'e49a46ce63b238c429d618c4aa37f52e')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', '5543917190')
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://mirror:mirror@cluster0.fuouswc.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", "-1001787652537")
BOT_NAME = os.environ.get('BOT_NAME', 'Video_Compressor_AmRoBot')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @Am_Robots || Telegram @Amrobots_Bots ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
