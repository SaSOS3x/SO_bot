async def default_post_text(user_name, user_login, message_text):
    """Сборщик данных для поста по умолчанию"""
    
    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>"

    return text

async def second_post_text(user_name, user_login, message_text, link):
    """Сборщик данных для поста в вспомогательный канал"""

    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>\n\nОтветить на обращение:\n{link}"

    return text

async def create_link(MAIN_CHANNEL_ID, message_from_chat_id:int):

    public_channel_id = abs(MAIN_CHANNEL_ID) - 1000000000000
    link = f"https://t.me/c/{public_channel_id}/{message_from_chat_id}"

    return link