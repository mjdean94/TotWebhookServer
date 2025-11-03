from fastapi import FastAPI
from discord import SyncWebhook
import json

from . import config

app = FastAPI()

@app.get("/")
async def root():
    return "Tot Webhook Server is up and running."

@app.get("/tot")
async def receive_tot_webhook(date, steamId, charName, actName, eventId, eventCategory, eventType, params):

    log_entry = f"[{date}] Event={eventId}, Actor={charName}, Params=[{params}]"

    webhook = SyncWebhook.from_url(config.webhook_url)
    webhook.send(log_entry)
    return {"message": "NYI"}

