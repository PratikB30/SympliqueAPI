from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime
from class_reminder import Reminder

app = FastAPI()

# from dotenv import load_dotenv
# load_dotenv()

# .env has my personal account URI for database connection
MONGODB_URI = os.getenv('MONGODB_URI')
mongo_client = AsyncIOMotorClient(MONGODB_URI)

db = mongo_client['Reminder']
col = db["Reminder_Collection"]  

# It is just to check if the API is working 
@app.api_route('/')
def index():
    return {"Test Route"}

# Main route
# run these 3 lines in powershell altogether to enter a reminder ->
# curl -X POST "http://127.0.0.1:8000/reminders/" `
#     -H "Content-Type: application/json" ` 
#     -d '{"userid": "abc123", "date": "2025-05-10", "time": "14:30:00", "message": "Doctor appointment", "reminder_type": "email"}'

@app.post('/reminders/')
async def create_reminder(
    reminder: Reminder
):
    try:
        reminder_date_time = datetime.combine(reminder.date, reminder.time)
        
        # to check if entered date and time is greater than current time
        if reminder_date_time < datetime.now():
            raise HTTPException(
                status_code=400,
                detail="Reminder must be greater than the current date and time"
            )
        
        reminder_data = {
            "userid": reminder.userid,
            "message": reminder.message,
            "reminder type": reminder.reminder_type,
            "time": reminder_date_time.isoformat()
        }
        
        # Uploads document to database (mongodb)
        result = await col.insert_one(reminder_data)
        return {"id": str(result.inserted_id), "message": f"Created reminder - {reminder.message} at {reminder_date_time} for {reminder.userid}"}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")
      
    
    
# Get a user's reminders stored in the database  
# To get records ->     
@app.get('/get_reminders/users/{userid}')
async def get_all_reminder_for_user(
    userid: str
):
    try:
        reminders = await col.find({"userid": userid}, {"_id": 0}).to_list(length=100)
        if not reminders:
            print(f"No reminder for {userid}")
        return reminders
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")
    

# Gets all reminders stored in the database
# To get records -> curl -X GET "http://127.0.0.1:8000/get_reminders/all/"
@app.get('/get_reminders/all/')
async def all_reminders():
    try:
        reminders = await col.find({}, {"_id": 0}).to_list(length=100)
        if not reminders:
            print(f"No reminders found")
        return reminders
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")