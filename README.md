# WG-Mail 🏡

WG-Mail automates the apartment-hunting process in Trier by fetching private agency/landlord details from the [Studibu](https://www.studibu.de/cms?_sprache=de&_template_variant=&_bereich=artikel&_aktion=detail&idartikel=230937) website and sending personalized emails.

## 📝 Problem Statement
Finding student accommodation in Trier can be a time-consuming process, requiring repeated visits to the [Studibu](https://www.studibu.de/cms?_sprache=de&_template_variant=&_bereich=artikel&_aktion=detail&idartikel=230937) website and manually drafting emails to landlords. This repetitive task reduces efficiency and often delays opportunities. <b>WG-Mail</b> solves this problem by automating the workflow — fetching landlord details directly from the [Studibu](https://www.studibu.de/cms?_sprache=de&_template_variant=&_bereich=artikel&_aktion=detail&idartikel=230937) platform and sending personalized emails, saving time and effort for students searching for housing.

## ✨ Features
- Scrape landlord/property details from Studibu Trier website
- Automate personalized email generation and sending
- Configurable templates for email messages
- Logging and error handling for reliability
- Extendable for other accommodation platforms

## 🛠 Tech Stack
- **Python 3.9+**
- `requests` (for fetching landlord details)
- `smtplib` (for email automation)
- `pandas` (for data handling)
- `dotenv` (for environment variable management)
- `openpyxl` (for Writing to Excel)

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or above installed
- A valid email account (e.g., Gmail/Outlook) for sending automated emails
- Access to Studienwerk Trier accommodation listings

### Installation
```bash
# Clone this repository
git clone https://github.com/mohammedOwaiskh/wg-mail.git
cd wg-mail

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:
```
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_password_or_app_password
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```

### Usage
```bash
python main.py
```

This will:
- Fetch the latest landlord details from Studienwerk Trier
- Save data in a `.xlsx` (Excel) file
- Generate personalized email messages
- Send them automatically using your configured email account

## 📂 Project Structure
```
wg-mail/
│-- main.py          # Entry point of the application
│-- fetcher.py       # Fetches data from Studienwerk website
│-- mailer.py        # Handles email sending
│-- templates/       # Email templates
│-- requirements.txt # Python dependencies
│-- README.md        # Project documentation
|-- LICENSE          # MIT License
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to open a PR or an issue.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

---
_Developed with ❤️ by Mohammed Owais Khan_
