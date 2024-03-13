import os 
import slackclient 

# conversations.history
# parse messages
# search for string

# worksapce id T01EHLSMU94
# app id    A06PM2T00RF

# bot user 0auth

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

if not SLACK_BOT_TOKEN:
    raise ValueError("Missing environment variable: SLACK_BOT_TOKEN")

