from slackclient import SlackClient
from settings import SLACK_TOKEN, SLACK_CHANNEL, CLUSTER_NAME, CLUSTER_API_URL

sc = SlackClient(SLACK_TOKEN)

NORMAL_COLOR = '#36a64f'
WARNING_COLOR = '#FFFF00'
ERROR_COLOR = '#FF0000'

ALERTS_COLORS = {
    'Normal': NORMAL_COLOR,
    'Warning': WARNING_COLOR,
}


def get_slack_msg_color(event_type):
    return ALERTS_COLORS.get(event_type, ERROR_COLOR)


def send_alert(host, event_type, event_text, event_time, event_uri, involved_object):
    event_timestamp = event_time.strftime('%s')
    title_link = '{api_url}{event_uri}'.format(api_url=CLUSTER_API_URL, event_uri=event_uri)

    attachment = {
        "fallback": event_text,
        "color": get_slack_msg_color(event_type),
        "title": event_text,
        "title_link": title_link,
        "fields": [
            {
                "title": involved_object.kind,
                "value": involved_object.name
            }
        ],
        "footer": CLUSTER_NAME,
        "ts": event_timestamp
    }

    if involved_object.namespace:
        attachment['fields'].append({
            "title": "Namespace",
            "value": involved_object.namespace,
            "short": True
        })

    if host:
        attachment['fields'].append({
            "title": "Host",
            "value": host,
            "short": True
        })

    sc.api_call(
        "chat.postMessage",
        channel=SLACK_CHANNEL,
        attachments=[attachment]
    )
