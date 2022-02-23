# Balena OctoPrint
**Remotely control your 3d-printer with [OctoPrint](https://github.com/foosel/OctoPrint) and balenaCloud!** Octoprint is exposed on port 80 which can be remotely accessible via the balenaCloud [public URL](https://www.balena.io/docs/learn/develop/runtime/#public-device-urls) feature.

This is a very simple implementation of OctoPrint designed to get you up and running with the basics. Once you have it running you can browse and install any [OctoPrint plugins](https://plugins.octoprint.org/) from within OctoPrint itself. Any that you install will be persisted to a volume, which means they will still be there if the service or device restarts AND they will be installed into any other devices running OctoPrint in your fleet. You now have a fleet-capable Octoprint system! :) 

## Software setup

Running this project is as simple as deploying it to a balenaCloud application, then downloading the OS image from the dashboard and flashing your SD card.

[![](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy)

We recommend this button as the de-facto method for deploying new apps on balenaCloud, but as an alternative, you can set this project up with the repo and balenaCLI if you choose. Get the code from this repo, and set up [balenaCLI](https://github.com/balena-io/balena-cli) on your computer to push the code to balenaCloud and your devices. [Read more](https://www.balena.io/docs/learn/deploy/deployment/).

