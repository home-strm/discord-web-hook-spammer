from discord_webhook import DiscordWebhook

print("Enter text or image url you want to spam.")
yes1 = input()

while True:
    webhook = DiscordWebhook(url='insert webhook url here.', content=yes1)
    response = webhook.execute()