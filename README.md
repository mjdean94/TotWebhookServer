# Tot Webhook Server

A simple webhook server that forwards Tot Sudo webhook payloads to Discord.

## Setup
1. Create a Discord Webhook from the "Integrations" section of server settings.
2. Create a `config.py` file in `/src` that defines a variable called `webhook_url` and sets it equal to the webhook URL you just made.
```python
webhook_url = 'https://discord.com/api/webhooks/somelongstringofcharacters'
```
3. In Conan Exiles, open the Tot Sudo Admin panel. In "Configure" log under the Sudo settings, enable the webhook and past your IP address with port 8000 and a path of `/tot`. You're done.