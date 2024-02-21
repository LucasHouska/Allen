# Allen
My First Chatbot

## Setup

1. Create a virtual environment

**MacOS/Linux**:

```
python3 -m venv env
```

**Windows**:

```
python -m venv env
```

2. Activate the virtual environment

```
source env/bin/activate
```

3. Install the requirements

```
pip3 install -r requirements.txt
pip3 install streamlit
```

4. Get and set an API key as an environment variable

.env file:

```
OPENAI_API_KEY=sk-brHeh...A39v5iXsM2
```

5. Start the app

`streamlit run main.py`

### In case of self-signed certificate errors due to security
```
python -c "import certifi; print(certifi.where())"
```
and then
```
cat /path/to/cert >> /path/generated/from/line/above
```