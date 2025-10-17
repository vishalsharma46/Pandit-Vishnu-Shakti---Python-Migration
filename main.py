from turtle import back
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import Form, BackgroundTasks
from db import db
from services.onboarding import handle_onboarding


load_dotenv()

app = FastAPI(title ="Pandit Vishnu Shakti API")

@app.on_event("startup")
async def connect_db():
    await db.connect()
    logger.info("Connected to Prisma Database")

@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()
    logger.info("Disconnected from Prisma Database")

@app.get("/readyz")
async def readyz():
    return{"status": "ok"}
    
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pandit-vishnu-shakti")

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(
    background_tasks: BackgroundTasks,
    From: str = Form(...),
    Body: str = Form(...),
):
    
    logger.info(f"Recieved from {From}: {Body}")
    background_tasks.add_task(process_message, From, Body)
    return {"ok": True}


async def process_message(sender: str, message: str):
    wa_id = sender.replace("whatsapp:", "")
    logger.info(f"Processing message from {wa_id}: {message}")

    response, step = await handle_onboarding(wa_id, message)

    logger.info(f"Reply to {wa_id} (step: {step}): {response}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3100)