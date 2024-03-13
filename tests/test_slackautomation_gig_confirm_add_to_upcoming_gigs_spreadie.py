import pytest
import sys

""" TESTS """


""" test bot token messaging works """
@pytest.mark.usefixtures("slack_bot_token")
def test_bot_token():
    if not SLACK_BOT_TOKEN:
        raise ValueError("Missing environment variable: SLACK_BOT_TOKEN")

print(sys.path)
