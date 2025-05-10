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