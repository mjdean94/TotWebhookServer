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

    log_entry = f"[{date}] EventType={eventType}, EventCategory={eventCategory} Actor={charName}, Params=[{params}]"

    webhook = SyncWebhook.from_url(config.audit_log_url)
    webhook.send(log_entry)
    return "OK"

@app.get("/chat")
async def receive_tot_chat_logs(message, sender, character, radius, location, channel):
    if sender != character:
        actor = f"{sender} ({character})"
    else:
        actor = sender

    log_entry = f"[{channel}][{radius}] {actor}: {message}"

    webhook = SyncWebhook.from_url(config.chat_url)
    webhook.send(log_entry)
    return "OK"