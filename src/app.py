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

    log_entry = f"`[{date}] EventType={eventId}, Actor={charName}, Params=[{params}]`"

    webhook = SyncWebhook.from_url(config.audit_log_url)
    webhook.send(log_entry)
    return "OK"

@app.get("/chat")
async def receive_tot_chat_logs(message, sender, character, radius, location, channel):
    if sender != character:
        actor = f"{sender} ({character})"
    else:
        actor = sender

    channel_shortname = channel
    if channel == 1:
        channel_shortname = "Global"
    if channel == 2:
        channel_shortname = "Local"
    if channel == 3:
        channel_shortname = "Clan"

    if channel == 2:
        log_entry = f"`[{channel_shortname}][{radius}] {actor}: {message}`"
    else:
        log_entry = f"`[{channel_shortname}] {actor}: {message}`"

    webhook = SyncWebhook.from_url(config.chat_url)
    webhook.send(log_entry)
    return "OK"