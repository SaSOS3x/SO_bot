async def default_post_text(user_name, user_login, message_text):
    """Сборщик данных для поста по умолчанию"""
    
    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>"

    return text

async def second_post_text(user_name, user_login, message_text, link):
    """Сборщик данных для поста в вспомогательный канал"""

    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>\n\nОтветить на обращение:\n{link}"

    return text