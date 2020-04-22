#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

mkdir -p /data/octoprint-data

if [ ! -f /data/octoprint-data/config.yaml ]; then
  touch /data/octoprint-data/config.yaml

  octoprint --config /data/octoprint-data/config.yaml \
    config set --bool server.firstRun true

  octoprint --config /data/octoprint-data/config.yaml \
    config set --int server.port 80

  octoprint --config /data/octoprint-data/config.yaml \
    config set server.commands.serverRestartCommand "/usr/src/app/balenactl.py reboot"

  octoprint --config /data/octoprint-data/config.yaml \
    config set server.commands.systemRestartCommand "/usr/src/app/balenactl.py reboot"

  octoprint --config /data/octoprint-data/config.yaml \
    config set server.commands.systemShutdownCommand "/usr/src/app/balenactl.py shutdown"

  octoprint --config /data/octoprint-data/config.yaml \
    config set webcam.ffmpeg /usr/bin/ffmpeg
fi

# Start OctoPrint
octoprint \
  --basedir /data/octoprint-data \
  --config /data/octoprint-data/config.yaml \
  --verbose \
  serve --iknowwhatimdoing --port 80
