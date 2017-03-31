Kubernetes Events monitoring with alerting

Light. Simple. Fast.

h3. Notification transports support

* Slack

h3. Install

h4. Clone repo

  git clone https://github.com/kuberstack/kuberstack-monitoring-events.git

h4. Create Slack bot

[Create Slack bot](https://my.slack.com/services/new/bot) and getting *token* for next step

h4. Edit env section in controller file

  vim kuberstack-monitoring-events/manifestos/controller.yaml
  
h4. Deploy events monitoring

  kubectl create -f kuberstack-monitoring-events/manifestos/