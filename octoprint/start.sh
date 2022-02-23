curl -X PATCH --header "Content-Type:application/json" \
    --data '{"network": {"hostname": "octoprint"}}' \
    "$BALENA_SUPERVISOR_ADDRESS/v1/device/host-config?apikey=$BALENA_SUPERVISOR_API_KEY"

exec octoprint serve --iknowwhatimdoing --host 0.0.0.0 --basedir "/data"