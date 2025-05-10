# API Hosted on
[https://sympliqueapi-production.up.railway.app](https://sympliqueapi-production.up.railway.app)

## Add Reminder:
[https://sympliqueapi-production.up.railway.app/reminders/](https://sympliqueapi-production.up.railway.app/reminders/)

## JSON for adding reminder on POSTMAN
```bash
{
    "userid": "abc123",
    "date": "2025-05-10", 
    "time": "19:30:00", 
    "message": "Dental appointment", 
    "reminder_type": "sms"
}
```
For uploading reminder to database:
```bash
curl -X POST "https://sympliqueapi-production.up.railway.app/reminders/" `
    -H "Content-Type: application/json" `
    -d '{"userid": "abc123", "date": "2025-05-10", "time": "14:30:00", "message": "Doctor appointment", "reminder_type": "email"}'
```

## Check all user's reminders:
```bash
https://sympliqueapi-production.up.railway.app/get_reminders/users/{userid}
```
For Example

[https://sympliqueapi-production.up.railway.app/get_reminders/users/abc123](https://sympliqueapi-production.up.railway.app/get_reminders/users/abc123)

## Check all reminders in database:

[https://sympliqueapi-production.up.railway.app/get_reminders/all/](https://sympliqueapi-production.up.railway.app/get_reminders/all/)

## Delete all user's reminder:
```bash
https://sympliqueapi-production.up.railway.app/remove_reminders/users/{userid}
```
For Example

[https://sympliqueapi-production.up.railway.app/remove_reminders/users/abc123](https://sympliqueapi-production.up.railway.app/remove_reminders/users/abc123)

# To Run Locally
## Install requirements.txt
## Make sure to run the FastAPI app before sending any requests. Open a terminal and run:

```bash
uvicorn main:app --reload
```

This will start your FastAPI app locally at http://127.0.0.1:8000

## Check if the API is running (GET /)

```bash
curl -X GET "http://127.0.0.1:8000/
```

Response:
```bash
{
  "Test Route"
}
```

For uploading reminder to database:

```bash
curl -X POST "http://127.0.0.1:8000/reminders/" `
    -H "Content-Type: application/json" `
    -d '{"userid": "abc123", "date": "2025-05-10", "time": "14:30:00", "message": "Doctor appointment", "reminder_type": "email"}'
```

For getting reminders for a particular user:
```bash
curl -X GET "http://127.0.0.1:8000/get_reminders/users/{userid}"
```
For example
```bash
curl -X GET "http://127.0.0.1:8000/get_reminders/users/abc123"
```

Check all user's reminders:
```bash
http://127.0.0.1:8000/get_reminders/users/{userid}
```
For Example
```bash
http://127.0.0.1:8000/get_reminders/users/abc123
```

## Check all reminders in database:

```bash
http://127.0.0.1:8000/get_reminders/all/
```

## Delete all user's reminder:
```bash
http://127.0.0.1:8000/remove_reminders/users/{userid}
```
For Example

http://127.0.0.1:8000/remove_reminders/users/abc123
