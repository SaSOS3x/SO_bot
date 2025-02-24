async def default_post_text(user_name, user_login, message_text):
    
    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>"

    return text

async def second_post_text(user_name, user_login, message_text, link):
    
    text  = f"Обращение от: <b>{user_name}</b>\n\n{message_text}\n\n<b>@{user_login}</b>\n\nОтветить на обращение:\n{link}"

    return text