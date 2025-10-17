# 🕉️ Pandit Vishnu Shakti AI Bot (FastAPI Edition)

An AI-powered WhatsApp astrologer bot that provides personalized Vedic astrology guidance in Hinglish (Hindi mixed with English), now rebuilt using **FastAPI**, **Prisma (Python)**, and **PostgreSQL**.

---

## 🌟 Features

### Core Capabilities
- 🤖 **AI-Powered Responses** — ready for Replicate Llama 3.1 integration  
- 📱 **WhatsApp Integration** via Twilio Webhook endpoint  
- 🔄 **Automatic Onboarding Flow** (Name → DOB → TOB → Place of Birth)  
- 🧪 **Background Message Processing** using FastAPI `BackgroundTasks`  
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

## 🗁 Project Structure

```
Pandit_Vishnu_Shakti/
│
├── main.py               # FastAPI entry point
├── db.py                 # Prisma DB connector
├── .env                  # Environment variables
├── prisma/
│   └── schema.prisma     # Prisma schema definition
└── services/
    ├── onboarding.py     # Step-based onboarding logic
    └── __init__.py
```

---

## ⚡ Quick Start

### 1️⃣ Clone and Install
```bash
git clone https://github.com/<your-username>/pandit-vishnu-shakti-fastapi.git
cd pandit-vishnu-shakti-fastapi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Environment Setup
Copy `.env.example` to `.env` and configure:
```env
DATABASE_URL="postgresql://mystic:secret@localhost:5432/mystic_sage"
PORT=3100
```

### 3️⃣ Database Setup
```bash
prisma generate
prisma db push
```

### 4️⃣ Run Services
```bash
uvicorn main:app --reload --port 3100
```

✅ Visit:
- http://127.0.0.1:3100/readyz → Health Check  
- `/webhook/whatsapp` → POST endpoint for messages

---

## 🧬 Testing (Postman)

**POST** → `http://127.0.0.1:3100/webhook/whatsapp`  
**Body type:** `x-www-form-urlencoded`

| Key | Value |
|------|-------|
| From | whatsapp:+919999999999 |
| Body | START |

✅ Response:
```json
{"ok": true, "message": "Received 🙏"}
```

Console log:
```
INFO: Received from whatsapp:+919999999999: START
INFO: Reply → 🙏 Namaste! Main Pandit Vishnu Shakti hoon...
```

---

## 🦭 Onboarding Flow

1️⃣ **START** → Bot greets the user  
2️⃣ **Name** → Requests Date of Birth  
3️⃣ **DOB** → Requests Time of Birth  
4️⃣ **TOB** → Requests Place of Birth  
5️⃣ **POB** → Marks onboarding complete 🎉  

Each message updates the DB record and advances the flow automatically.

---

## 🧩 AI Model Configuration (Future Integration)

The system supports Meta Llama 3.1 (405B Instruct) via Replicate.  
Add these to your `.env` when integrating:

```env
REPLICATE_API_TOKEN="your_replicate_api_token"
REPLICATE_MODEL="meta/meta-llama-3.1-405b-instruct"
REPLICATE_MAX_TOKENS=1024
REPLICATE_TEMPERATURE=0.6
REPLICATE_TOP_P=0.9
REPLICATE_TOP_K=50
```

You can adjust:
- **Temperature:** controls creativity  
- **Top_P / Top_K:** control response diversity  
- **Max Tokens:** controls message length  

---

## 🧠 User Experience Enhancements (Planned)

- 🌅 Personalized daily horoscopes  
- 🗓️ Festival & planetary alerts  
- 🧬 User preference tracking (language, horoscope type, frequency)  
- 📈 Conversation analytics dashboard  
- 🧘 Mood-aware conversational tone  

---

## 🗾 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| **GET** | `/readyz` | Health check endpoint |
| **POST** | `/webhook/whatsapp` | Receives incoming WhatsApp messages |
| *(future)* | `/stats` | Returns usage and analytics summary |

---

## 🔒 Environment Variables Reference

| Variable | Description |
|-----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `PORT` | Server port (default 3100) |
| `REPLICATE_API_TOKEN` | API token for Replicate (AI model) |
| `REPLICATE_MODEL` | Model ID for AI responses |
| `TWILIO_TOKEN` | WhatsApp business API token (future) |

---

## 🧭 Roadmap

- [x] FastAPI base webhook  
- [x] Onboarding logic with DB  
- [ ] AI response via Replicate  
- [ ] WhatsApp send via Twilio mock  
- [ ] Admin analytics routes  
- [ ] Deployment (Render / Railway)

---

## 📊 Analytics (Future CLI Commands)
```bash
python scripts/analytics.py
```

Will display:
- User count & onboarding completion rate  
- Model response stats  
- Average response time  
- Daily active users  

---

## 🧮 Development Commands

| Command | Description |
|----------|-------------|
| `uvicorn main:app --reload` | Start dev server |
| `prisma db push` | Sync DB schema |
| `prisma generate` | Generate Prisma client |
| `docker compose up -d` | Start PostgreSQL via Docker |
| `pytest` | Run tests (if added) |

---

## 🧱 Database Schema (Prisma)
```prisma
model User {
  id            Int       @id @default(autoincrement())
  waId          String    @unique
  name          String?
  dateOfBirth   DateTime?
  timeOfBirth   String?
  placeOfBirth  String?
  isOnboarded   Boolean   @default(false)
  createdAt     DateTime  @default(now())
}

model Message {
  id        Int       @id @default(autoincrement())
  userId    Int
  sender    String
  content   String
  createdAt DateTime  @default(now())
}
```

---

## 🤝 Contributing

1️⃣ Fork this repo  
2️⃣ Create a new branch (`feature/new-module`)  
3️⃣ Commit and push changes  
4️⃣ Submit a PR  

---

## 🦶 License

Licensed under the **MIT License**.  
Feel free to use, modify, and learn from it.

---

## 🙏 Credits

Built by **Vishal Sharma** during development of the Pandit Vishnu Shakti AI system at Zephico.  
Inspired by the original **Mystic Sage (Node.js)** version.  

**Jai Shree Ram!** ✨  
_– Pandit Vishnu Shakti AI Bot (FastAPI Edition)_

