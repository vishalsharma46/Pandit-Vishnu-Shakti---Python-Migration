# 🕉️ Pandit Vishnu Shakti AI Bot (FastAPI Edition)

An AI-powered WhatsApp astrologer bot that provides personalized Vedic astrology guidance in Hinglish (Hindi mixed with English), now rebuilt using **FastAPI**, **Prisma (Python)**, and **PostgreSQL**.

---

## 🌟 Features

### Core Capabilities
- 🤖 **AI-Powered Responses** — ready for Replicate Llama 3.1 integration  
- 📱 **WhatsApp Integration** via Twilio Webhook endpoint  
- 🔄 **Automatic Onboarding Flow** (Name → DOB → TOB → Place of Birth)  
- 🪄 **Background Message Processing** using FastAPI `BackgroundTasks`  
- 🧹 **Smart Input Cleaning** — accepts various date/time formats  
- 🧠 **Stateful User Tracking** — remembers where users left off  
- 📊 **Database Layer** powered by Prisma ORM and PostgreSQL  
- 🧘 **Hinglish Conversations** for natural user experience  

---

## ⚙️ Tech Stack

| Layer | Technology |
|--------|-------------|
| Backend | **FastAPI (Python 3.13)** |
| Database | **PostgreSQL 16** |
| ORM | **Prisma Python Client** |
| Queue / Worker | **FastAPI BackgroundTasks** |
| AI Integration | **Replicate (Meta Llama 3.1 405B Instruct)** |
| Messaging | **Twilio WhatsApp Business API** |
| Config | **dotenv (.env)** |
| Deployment | **Docker Compose / Render / Railway** |

---

## 📁 Project Structure

Pandit_Vishnu_Shakti/
│
├── main.py # FastAPI entry point
├── db.py # Prisma DB connector
├── .env # Environment variables
├── prisma/
│ └── schema.prisma # Prisma schema definition
└── services/
├── onboarding.py # Step-based onboarding logic
└── init.py

## ⚡ Quick Start

### 1️⃣ Clone and Install
git clone https://github.com/<your-username>/pandit-vishnu-shakti-fastapi.git
cd pandit-vishnu-shakti-fastapi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

###2️⃣ Environment Setup
Copy .env.example to .env and configure:

DATABASE_URL="postgresql://mystic:secret@localhost:5432/mystic_sage"
PORT=3100

###3️⃣ Database Setup
prisma generate
prisma db push

###4️⃣ Run Services
uvicorn main:app --reload --port 3100


##✅ Visit:

http://127.0.0.1:3100/readyz
 → Health Check

/webhook/whatsapp → POST endpoint for messages

##🧪 Testing (Postman)

POST → http://127.0.0.1:3100/webhook/whatsapp
Body type: x-www-form-urlencoded

Key	    Value
From	   whatsapp:+919999999999
Body	   START

✅ Response:

{"ok": true, "message": "Received 🙏"}


Console log:
INFO: Received from whatsapp:+919999999999: START
INFO: Reply → 🙏 Namaste! Main Pandit Vishnu Shakti hoon...

##🧭 Onboarding Flow
1️⃣ START → Bot greets the user
2️⃣ Name → Requests Date of Birth
3️⃣ DOB → Requests Time of Birth
4️⃣ TOB → Requests Place of Birth
5️⃣ POB → Marks onboarding complete 🎉

Each message updates the DB record and advances the flow automatically.
