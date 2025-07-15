import requests
import time
import json
import random
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ====================== CONFIGURATION ======================
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
SHEET_NAME = 'Sheet1'
SERVICE_ACCOUNT_FILE = 'service_account.json'

TOTAL_PERSONAS = 20  # Set as needed

# ====================== GOOGLE SHEETS SETUP ======================

def setup_sheets_api():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()

def write_to_google_sheets(spreadsheet_id, sheet_name, data):
    sheets = setup_sheets_api()
    body = {'values': [[text] for text in data]}  # One result per row
    sheets.values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A1",
        valueInputOption="RAW",
        body=body
    ).execute()

# ====================== GEMINI API FUNCTION ======================

def call_gemini_api(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY,
    }
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    while True:
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                candidates = result.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        text_part = parts[0].get("text", "")
                        return str(text_part).strip()
                return ""
            elif response.status_code == 429:
                print("Rate limit hit. Waiting 60 seconds...")
                time.sleep(60)
            elif response.status_code == 503:
                print("Model overloaded. Waiting 30 seconds...")
                time.sleep(30)
            else:
                print(f"API Error {response.status_code}: {response.text}")
                return ""
        except Exception as e:
            print(f"Exception calling Gemini API: {str(e)}")
            time.sleep(5)

# ====================== PERSONA GENERATION ======================

def generate_prompt():
    # Customize as needed
    return "What is your biggest challenge in marketing?"

def generate_persona_response():
    prompt = generate_prompt()
    return call_gemini_api(prompt)

# ====================== MAIN PROCESS ======================

def main():
    results = []

    for idx in range(1, TOTAL_PERSONAS + 1):
        print(f"Processing {idx}/{TOTAL_PERSONAS}...")
        response = generate_persona_response()
        if response:
            results.append(response)
        else:
            results.append("No response generated.")

    print("Writing results to Google Sheets...")
    write_to_google_sheets(SPREADSHEET_ID, SHEET_NAME, results)
    print("Done.")

# ====================== ENTRY POINT ======================

if __name__ == "__main__":
    main()