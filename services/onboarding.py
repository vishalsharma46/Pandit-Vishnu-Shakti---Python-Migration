from datetime import datetime
from db import db

ONBOARDING_STEPS = {
    "name",
    "date_of_birth",
    "time_of_birth",
    "place_of_birth",
    "complete"
}

async def handle_onboarding(wa_id: str, message:str):
    user = await db.user.find_first(where={"waId" : wa_id})
    if not user:
        user = await db.user.create(data= {"waId" : wa_id, "isOnboarded" : False})
    
    if message.strip().upper()=="START":
        user = await db.user.update(
            where={"id" : user.id},
            data = {"name": None, "dateOfBirth": None, "timeOfBirth": None, "placeOfBirth": None, "isOnboarded" : False},
        )

        return "🙏 Namaste! Main Pandit Vishnu Shakti hoon.\nKripya apna naam batayein. 🌸", "name"
    
    if not user.name:
        await db.user.update(
            where={"id" : user.id}, 
            data= {"name": message.strip()}
        )
        return f"🙏 Dhanyavaad {message.strip()} ji!\nAb apni date of birth likhiye (DD/MM/YYYY).", "date_of_birth"
    
    if not user.dateOfBirth:
        try:
            dob = datetime.strptime(message.strip(), "%d/%m/%Y")
            await db.user.update(
                where={"id" : user.id},
                data={"dateOfBirth":dob},
            )
            return "🙏 Bahut achha! Ab apna birth time likhiye (HH:MM).", "time_of_birth"
        except:
            return "⚠️ Kripya sahi format mein likhiye. Example: 15/08/1990", "date_of_birth"
        
    if not user.timeOfBirth:
        if ":" in message:
            await db.user.update(
                where={"id": user.id},
                data={"timeOfBirth" : message.strip()},
            )
            return "🙏 Shukriya! Ab apna birth place batayein.", "place_of_birth"
        return "⚠️ Format galat hai. Example: 14:30", "time_of_birth"
    
    if not user.placeOfBirth:
        await db.user.update(
            where={"id" : user.id},
            data={"placeOfBirth": message.strip(), "isOnboarded": True},
        )
        return f"🎉 Jai Shree Ram {user.name} ji! Onboarding process complete hua.\nAb 'DAILY' likhkar apna rashifal paaiye.", "complete"
    return "🙏 Aap pehle hi onboarded ho chuke hain!", "complete"

        