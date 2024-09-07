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

```


