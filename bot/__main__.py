from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task
from pyrogram import types

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
    message.reply_text(f"Hey {message.from_user.mention()} This is Not Public BOT. Ask Permission From My Master @HC_CARTOONS", quote=True)

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
def encode_video(app, message):
    message
    if message.document:
      if not message.document.mime_type in video_mimetype:
        message.reply_text("Invalid Video Format !\nMake Sure Its a Supported Video File 🐭", quote=True)
        return
    message.reply_text("Added To Queue Prem Sir 🙇🏼‍♂️", quote=True) 
    data.append(message)
    if len(data) == 1:
      add_task(message)

app.run()
