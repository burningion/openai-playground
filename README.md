# OpenAI Playground

Does what it says on the label. You'll need an OpenAI API key, and it should be set as an environment variable named `OPENAI_API_KEY` within Gitpod.

Here's what the example prompt returns:

```bash
$ python3 playground.py 
To write a FastAPI application that accepts file uploads and stores them on Amazon S3, you need to have the following installed in your project:

1. Install FastAPI and its dependencies

```bash
pip install fastapi
```

2. Install boto3 to connect to Amazon S3

```bash
pip install boto3
```

3. Create a FastAPI application called `app.py` and paste the following code:

```python
import os
import boto3
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from botocore.exceptions import NoCredentialsError

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add your Amazon S3 credentials
ACCESS_KEY = 'your-access-key'
SECRET_KEY = 'your-secret-key'
BUCKET_NAME = 'your-bucket-name'

# Initialize a boto3 session and create the S3 client
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
s3 = session.client('s3')


def upload_file_to_s3(file, bucket, filename):
    try:
        s3.upload_fileobj(file.file, bucket, filename)
        return True
    except FileNotFoundError:
        return False
    except NoCredentialsError:
        return False


@app.post("/upload/")
async def upload_file_to_s3_route(file: UploadFile):
    if upload_file_to_s3(file, BUCKET_NAME, file.filename):
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
    else:
        return JSONResponse(status_code=400, content={"message": "Upload failed"})

# Run: `uvicorn app:app --host 0.0.0.0 --port 8000` to run the FastAPI server
```

Replace the placeholders with your access, secret keys and the bucket name.

To run the FastAPI server for the app:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

You can test the endpoint `http://localhost:8000/upload/` by sending a POST request with a file using tools like Postman or CURL. The files will be uploaded to the 
specified Amazon S3 bucket securely.
enter next prompt:
```