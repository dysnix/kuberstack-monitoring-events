import telegram
from settings import CLUSTER_NAME, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

bot = telegram.Bot(token=TELEGRAM_TOKEN)


def send_alert(host, event_type, event_text, event_time, event_uri, involved_object):
    text = "*{event_type}*: `{cluster}`\n" \
           "{involved_object_kind}: ```{involved_object_name}```\n" \
           "Namespace: ```{namespace}```\n" \
           "Host: ```{host}```\n" \
           "`{event_text}`".format(involved_object_kind=involved_object.kind,
                                   involved_object_name=involved_object.name,
                                   namespace=involved_object.namespace, cluster=CLUSTER_NAME, host=host,
                                   event_type=event_type, event_text=event_text)

    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
