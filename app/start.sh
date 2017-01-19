#!/bin/bash

# Enable Camera
modprobe bcm2835-v4l2 >/dev/null 2>&1 || true

# Start haproxy
service haproxy start >/dev/null 2>&1 || true

# start picam stream
cd /usr/src/app/mjpg-streamer/mjpg-streamer-experimental/ \
  && ./mjpg_streamer -i "./input_uvc.so -y" -o "./output_http.so"  &

# start Octoprint
octoprint --iknowwhatimdoing --port=5000 --basedir /data
