# This is a GEO Location Detailed service taking Longitude and Latitude as an Input and provides detailed Address/Location using MaxMind Services.


# aws-hack-genai-llm

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n aws-hack-genai-llm python=3.11.7 -y
```

```bash
conda activate aws-hack-genai-llm
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- Finally run the following command

```bash
#python maxmind.py

python3 -m uvicorn maxmindservice.app:app --reload

```
### STEP 05- Curl Commands 

```bash

#Example 
curl http://127.0.0.1:8000/location?lat=37.7749&lon=-122.4194

curl https://fly.io/apps/aws-hack-genai-llm/location?lat=37.7749&lon=-122.4194

curl https://aws-hack-genai-llm.fly.dev/location?lat=37.7749&lon=-122.4194

curl https://aws-hack-genai-llm.fly.dev/location?lat\=37.7749\&lon\=-122.4194

ngrok config add-authtoken YOUR_AUTHTOKEN

curl  https://b1b9-12-94-132-170.ngrok-free.app/location?lat\=37.7749\&lon\=-122.4194

zip -r lambda_function.zip .

```


