import os
from slackclient import SlackClient


# Create a Slack client for making Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(SLACK_BOT_TOKEN)


def send_notification(message_text):
    # Message attachments are sent as a JSON array
    # See our Message Builder tool for more info
    # https://api.slack.com/docs/messages/builder
    message_attachments = [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                "author_name": "Bobby Tables",
                "author_link": "http://flickr.com/bobby/",
                "author_icon": "http://flickr.com/icons/bobby.jpg",
                "title": "Slack API Documentation",
                "title_link": "https://api.slack.com/",
                "text": "Optional text that appears within the attachment",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": False
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Slack API",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": 123456789
            }
        ]

    # Post a message to a channel
    slack_client.api_call(
        "chat.postMessage",
        channel="#general",
        text=message_text,
        attachments=message_attachments,
        as_user=True
    )


# When the app loads, it sends a basic text-only notification
send_notification("New review requested on *slackapi/example-app*")
