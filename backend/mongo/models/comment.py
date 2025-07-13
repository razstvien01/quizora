from datetime import datetime

def create_comment(thread_id, user_id, content):
    return {
        "thread_id": thread_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.now(datetime.timezone.utc),
        "edited": False,
        "updated_at": None
    }