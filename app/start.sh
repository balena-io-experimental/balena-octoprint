#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

# During a restart any data that is not stored in /data will be lost.
if [ -f /usr/src/app/config.yaml ]; then
  mv --no-clobber --verbose /usr/src/app/config.yaml /data
fi

# start Octoprint
octoprint --verbose --config /data/config.yaml serve --iknowwhatimdoing --basedir /data --port=80
