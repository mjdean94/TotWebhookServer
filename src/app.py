from fastapi import FastAPI
from discord import SyncWebhook

from . import config

app = FastAPI()

@app.get("/")
async def root():
    return "Tot Webhook Server is up and running."

@app.post("/tot")
async def receive_tot_webhook(payload):
    webhook = SyncWebhook.from_url(config.webhook_url)
    webhook.send(payload)
    return {"message": "NYI"}

