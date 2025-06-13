# Sentiment Analysis Flask API

This is a simple REST API for **sentiment analysis** using a pre-trained Hugging Face model (`distilbert-base-uncased-finetuned-sst-2-english`).  
You can send text data to the API and get back a structured prediction of the sentiment (POSITIVE/NEGATIVE).

## Features

- Easy-to-use `/predict-text` endpoint
- Returns JSON structured response
- Uses state-of-the-art transformer model

## Setup

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**  
   ```bash
   python app.py
   ```

3. **API will be available at**  
   `http://localhost:5000/`

## API Usage

### Endpoint

`POST /predict-text`

**Content-Type:** `application/json`

#### Request Body

```json
{
  "text": "I love using this API!"
}
```

#### Sample Response

```json
{
  "input": "I love using this API!",
  "prediction": {
    "label": "POSITIVE",
    "score": 0.9998
  }
}
```

#### Error Response

```json
{
  "error": "Missing 'text' field in JSON"
}
```

## Model Information

- **Model:** distilbert-base-uncased-finetuned-sst-2-english
- **Source:** [Hugging Face Model Card](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- **Task:** Sentiment Analysis (binary: Positive / Negative)

## Sample Test Input

See [`sample_input.json`](./sample_input.json).

---

## Example curl command

```bash
curl -X POST http://localhost:5000/predict-text \
     -H "Content-Type: application/json" \
     -d '{"text": "This product is great!"}'
```
