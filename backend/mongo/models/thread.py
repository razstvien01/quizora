from datetime import datetime

def create_thread(mock_exam_id, title, created_by):
    return {
        "mock_exam_id": mock_exam_id,
        "title": title,
        "created_by": created_by,
        "created_at": datetime.now(datetime.timezone.utc),
        "updated_at": None
    }