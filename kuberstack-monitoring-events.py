import os
import time
import datetime
from kubernetes import client, config
from alerts.slack import send_alert as slack_send_alert
from settings import UPDATE_INTERVAL, ALERTS_LEVELS_EXCLUDE

# Kubernetes API init
if os.environ.get('DEVELOPMENT_MODE'):
    config.load_kube_config()
else:
    config.load_incluster_config()

kubeapi = client.CoreV1Api()


def get_sorted_events():
    events = kubeapi.list_event_for_all_namespaces().items
    return sorted(events, key=lambda k: k.metadata.creation_timestamp)


def get_timestamp(text):
    return datetime.datetime.strptime(text, '%Y-%m-%dT%H:%M:%SZ')


def main():
    last_event = get_sorted_events()[-1]
    events_last_name = last_event.metadata.name
    events_last_timestamp = get_timestamp(last_event.metadata.creation_timestamp)

    try:
        while not time.sleep(UPDATE_INTERVAL):
            for event in get_sorted_events():
                event_name = event.metadata.name
                event_time = get_timestamp(event.metadata.creation_timestamp)

                if event_time <= events_last_timestamp or event_name == events_last_name:
                    continue

                if event.type in ALERTS_LEVELS_EXCLUDE:
                    continue

                slack_send_alert(event.source.host, event.type, event.message,
                                 event_time, event.metadata.self_link, event.involved_object)

                events_last_name = event_name
                events_last_timestamp = event_time

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
