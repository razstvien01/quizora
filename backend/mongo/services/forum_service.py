from mongo.services.mongo import thread_collection, comments_collection
from mongo.models.thread import create_thread
from mongo.models.comment import create_comment
from pymongo.errors import PyMongoError


async def create_new_thread(mock_exam_id, title, created_by):
    try:
        data = create_thread(mock_exam_id, title, created_by)
        result = await thread_collection.insert_one(data)
        
        return str(result.inserted_id)
    except PyMongoError as e:
        print(f"[MongoError] Failed to insert thread: {e}")
        return {"error": "Could not create thread. Please try again later."}

async def get_thread_with_comments(thread_id):
    thread = await thread_collection.find_one({"_id": thread_id})
    comments_cursor = comments_collection.find({"thread_id": thread_id})
    comments = await comments_cursor.to_list(length=100)
    
    return {**thread, "comments": comments}