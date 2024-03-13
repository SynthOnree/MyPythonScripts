import os 
import slackclient 

# conversations.history
# parse messages
# search for string

# worksapce id T01EHLSMU94
# app id    A06PM2T00RF
# channel id api_test_channel
# bot user 0auth

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

if not SLACK_BOT_TOKEN:
    raise ValueError("Missing environment variable: SLACK_BOT_TOKEN")

client = slackclient.SlackClient(SLACK_BOT_TOKEN)

channel_id = "C06PXBSHP0Q"

oldest = None # optional, defaults to latest

try: 
    result = client.channels_history(channel=channel_id, oldest=oldest)
except slackclient.SlackApiError as e:
    print(f"Error getting message history: {e}")
    exit(1)

    