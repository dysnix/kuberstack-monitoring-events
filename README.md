## Kubernetes Events monitoring with alerting

Light. Simple. Fast.

### Notification transports support

* Slack

## Install

##### Clone repo

    git clone https://github.com/kuberstack/kuberstack-monitoring-events.git

##### Create Slack bot

[Create Slack bot](https://my.slack.com/services/new/bot) and getting *token* for next step

##### Edit env section in controller file

    vim kuberstack-monitoring-events/manifestos/controller.yaml
  
##### Deploy events monitoring

    kubectl create -f kuberstack-monitoring-events/manifestos/
    
## Settings

|Paramater|Description|Value|
|---|---|---|
|CLUSTER_NAME|Cluster name|```demo-cluster.example.com```|
|CLUSTER_API_URL|Base URL of Kubernetes API|```https://api.demo-cluster.example.com```|
|SLACK_TOKEN|Slack BOT tocken|```xoxb-162761768114-eO7Vt7z3ElhBxAG99B7835oj```|
|SLACK_CHANNEL|Slack channel|```#alerts```|
|UPDATE_INTERVAL|Update events interval in sec.|```60```|
|ALERTS_LEVELS_EXCLUDE|Exclude Kubernetes Events types in alerting|```Normal```|
