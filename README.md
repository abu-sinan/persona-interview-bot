# Automated Persona Interview Bot

This Python project automates generating interview-style answers using AI (Google Gemini API) and stores the results in Google Sheets. It can simulate thousands of customer interviews and save responses for further analysis.

---

## 🚀 Get the Code

```bash
git clone https://github.com/abu-sinan/persona-interview-bot.git
cd persona-interview-bot
```

## 📌 Features

- Calls Gemini 2.0 Flash API to generate human-like responses.

- Handles rate limits (429) and overload errors (503) automatically.

- Stores results directly in Google Sheets using the Sheets API.

- Designed to work in Termux, Linux, or any Python environment.

- Simple, single-threaded for stability (optional multi-threading possible).

---

## 📦 Requirements

- Python 3.8+

- Google Cloud service account with Sheets API access.

- A Google Sheet shared with your service account.

- Dependencies:

```bash
pip install requests google-api-python-client google-auth google-auth-oauthlib
```

---

## 🔑 Setup

### 1. Gemini API Key

- Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

- Replace in `main.py`:

`GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'`

### 2. Google Sheets Setup

- Create a Google Sheet and get its ID from the URL:

`https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit`

- Replace in `main.py`:

```python
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
SHEET_NAME = 'Sheet1'
```

### 3. Service Account

- Create a service account JSON via Google Cloud Console.

- Enable Google Sheets API for your project.

- Place the JSON file as `service_account.json` in your project folder.

- Share the Google Sheet with the service account’s email (`e.g. xxxx@xxxx.iam.gserviceaccount.com`).

---

## 🚀 How to Run

```bash
python main.py
```

The script will:

- Generate personas (or marketing answers).

- Handle errors gracefully.

- Write results to your Google Sheet.

---

## 🛠 Configuration

Edit `main.py` for:

```python
TOTAL_PERSONAS = 20  # Adjust the number of personas as needed
```

---

## 📝 Example Output (Google Sheet)

**Interview Responses**

Measuring ROI of our campaigns and proving their effectiveness.
Getting consistent leads and engaging potential customers.
Understanding customer pain points accurately.

---

⚙️ File Structure

```
project/
├── main.py
├── service_account.json
└── README.md
```

---

## 📊 Use Cases

- Customer persona research

- Simulated interview generation

- AI-driven survey simulations

- Automated marketing data collection

---

## 📢 Notes

- **Rate Limits:** Free Gemini API allows ~15 requests/minute.

- **Error Handling:** Automatically waits and retries for 429 (rate limit) and 503 (overload) errors.

- **Format:** Responses are saved as clean, plain text rows.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📮 Support

If you need help, please open an issue or contact me.


Happy automating! 🚀