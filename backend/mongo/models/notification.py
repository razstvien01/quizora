from datetime import datetime

def create_notification(user_id, message, type_, metada):
    return {
        "user_id": user_id,
        "message": message,
        "type": type_,
        "is_read": False,
        "created_at": datetime.now(datetime.timezone.utc)
    }