import os
from translationinline

@Bot.on_message(filters.private & filters.media)
async def _main(_, message):
    await message.reply_text(
        "Where you want to Upload?",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Upload to GoFile.io", callback_data="uptogofile"),
                 InlineKeyboardButton("Upload to Streamtape", callback_data="")]
            ]
        ),
