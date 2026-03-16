# SpamSys 🛡️

A machine learning web app that detects whether a message is spam or not — instantly.

🔗 **Live Demo:** https://web-production-23158.up.railway.app

---

## What it does
Paste any SMS message and SpamSys will predict in real time whether it's **Spam** or **Not Spam**.

---

## Tech Stack
| Layer | Tool |
|---|---|
| Model | Naive Bayes |
| Vectorizer | TF-IDF |
| Backend | Flask |
| Frontend | HTML + CSS |
| Deployment | Railway |
| Language | Python 3.11 |

---

## Model Performance
- **Accuracy:** 96.2%
- **Dataset:** SMS Spam Collection (5,169 messages) from Kaggle
- **False Positives:** 0 (never marks real messages as spam)

---

## Project Structure
```
spamsys/
├── app.py              ← Flask server
├── model.pkl           ← Trained Naive Bayes model
├── vectorizer.pkl      ← TF-IDF vectorizer
├── Procfile            ← Railway deployment config
├── requirements.txt    ← Dependencies
├── templates/
│   └── index.html      ← Web interface
├── static/
│   └── style.css       ← Styling
└── notebook/
    └── train.ipynb     ← Model training notebook
```

---

## Run Locally
```bash
git clone https://github.com/akshat316-12/spamsys.git
cd spamsys
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000

---

## How it works
1. User pastes a message into the web form
2. Flask receives the message
3. TF-IDF vectorizer converts text to numbers
4. Naive Bayes model predicts spam or not
5. Result is displayed instantly
