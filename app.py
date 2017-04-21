import os
from slackclient import SlackClient


# Create a Slack client for making Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(SLACK_BOT_TOKEN)


def send_notification(message_text):
    # Post a message to a channel
    slack_client.api_call(
        "chat.postMessage",
        channel="#general",
        text=message_text,
        as_user=True
    )


# When the app loads, it sends a basic text-only notification
send_notification("New review requested on *slackapi/example-app*")
