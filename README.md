```
# Classification Bot

This bot classifies entities (Human, Animal, or Alien) by collecting structured information through a guided conversation. The collected data is sent to a specified Telegram group and saved to Google Sheets for record-keeping.

---

## Features

- **Classification Types**: Human, Animal, Alien.
- **Data Collection**: Guided conversation flow for collecting specific attributes based on the entity type.
- **Telegram Group Integration**: Posts formatted classification data to a Telegram group.
- **Google Sheets Integration**: Saves the data into dedicated Google Sheets worksheets for each entity type.
- **Error Handling**: Validates user inputs and provides feedback for incorrect or missing data.
- **Sequential Numbering**: Generates unique 5-digit numbers for each classification entry.

---

## Requirements

### Python Version

- Python 3.10+

### Python Libraries

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```plaintext
aiogram==3.x
gspread
google-auth
google-auth-oauthlib
python-dotenv
```

### External Services

1. **Telegram Bot**:
   - Obtain a bot token from [BotFather](https://core.telegram.org/bots#botfather).
   - Add the bot to the target group and promote it as an admin.

2. **Google Sheets API**:
   - Create a project on [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Sheets API.
   - Download the `credentials.json` file and place it in the `classification_bot/` folder.

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/alishermutalov/classification.git
cd classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the `classification_bot/` directory with the following content:

```plaintext
BOT_TOKEN=your_bot_token
TELEGRAM_GROUP_ID=your_group_id
```

Replace `your_bot_token` with your bot's token and `your_group_id` with the Telegram group's ID.

### Google Sheets Setup

1. Place the downloaded `credentials.json` file in the `classification_bot/` directory.
2. Share the target Google Sheets file with the service account email from the `credentials.json` file.

---

## Running the Bot

Start the bot using:

```bash
python classification_bot/main.py
```

---

## Project Structure

```plaintext
classification/
├── classification_bot/
│   ├── __init__.py
│   ├── main.py                # Entry point of the bot
│   ├── handlers/              # Handlers for different entity types
│   │   ├── __init__.py
│   │   ├── human.py
│   │   ├── animal.py
│   │   ├── alien.py
│   ├── utils/                 # Utility files
│   │   ├── __init__.py
│   │   ├── last_used_number.txt
│   │   ├── credentials.json
│   ├── data/                  # Data storage
│   │   ├── __init__.py
│   │   ├── google_sheets.py
│   ├── .env                   # Environment variables
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore file
├── LICENSE                    # License file
```

---

## Data Collection Workflow

### Human

- **Gender**: Male/Female.
- **Age**: Positive numeric value.
- **Nationality**: Text.
- **Education**: Higher/School.
- **Eye Color**: Text.
- **Hair Color**: Text.
- **Height**: Positive numeric value in cm.

### Animal

- **Species**: Text.
- **Mammal**: Yes/No.
- **Predator**: Yes/No.
- **Color**: Text.
- **Weight**: Positive numeric value in kg.
- **Age**: Positive numeric value in months.

### Alien

- **Humanoid**: Yes/No.
  - If Yes:
    - **Race**: X/Y/Z.
    - **Skin Color**: Text.
    - **Dangerous**: Yes/No.
    - **Has Reason**: Yes/No.
    - **Weight**: Positive numeric value in kg.

