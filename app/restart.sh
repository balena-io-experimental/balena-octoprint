#!/usr/bin/env bash

generate_post_data()
{
  cat <<EOF
{
  "appId": "$BALENA_APP_ID"
}
EOF
}

curl -X POST --header "Content-Type:application/json" --data "$(generate_post_data)" "$BALENA_SUPERVISOR_ADDRESS/v1/restart?apikey=$BALENA_SUPERVISOR_API_KEY"
