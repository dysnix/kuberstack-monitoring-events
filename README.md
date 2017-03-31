## Kubernetes Events monitoring with alerting

Light. Simple. Fast.

### Notification transports support

* Slack

### Install

#### Clone repo

    git clone https://github.com/kuberstack/kuberstack-monitoring-events.git

#### Create Slack bot

[Create Slack bot](https://my.slack.com/services/new/bot) and getting *token* for next step

#### Edit env section in controller file

    vim kuberstack-monitoring-events/manifestos/controller.yaml
  
#### Deploy events monitoring

    kubectl create -f kuberstack-monitoring-events/manifestos/