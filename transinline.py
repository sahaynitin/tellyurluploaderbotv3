@Bot.on_message(filters.private & filters.media)
async def _main(_, message):
    await message.reply_text(
        "Choose Your Upload Form ?",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("file", callback_data="cb_string_file"),
                 InlineKeyboardButton("video", callback_data="cb_string_video")]
            ]
        ),
