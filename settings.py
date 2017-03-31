import os

# Cluster info
CLUSTER_NAME = os.environ.get('CLUSTER_NAME', '')
CLUSTER_API_URL = os.environ.get('CLUSTER_API_URL', '')

# Notifications
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL', '#alerts')

# Monitoring
UPDATE_INTERVAL = int(os.environ.get('UPDATE_INTERVAL', 60))

ALERTS_LEVELS_EXCLUDE_RAW = os.environ.get('ALERTS_LEVELS_EXCLUDE', 'Normal')
ALERTS_LEVELS_EXCLUDE = [level.strip() for level in ALERTS_LEVELS_EXCLUDE_RAW.split(',')]

try:
    from local_settings import *
except ImportError:
    pass
