# bbalena-octoprint
remotely control your 3d-printer with [octoprint](https://github.com/foosel/OctoPrint) and Balena !

**octoprint is exposed on port 80 which can be remotely accessible via Balena [public URL](https://www.balena.io/docs/learn/manage/actions/#enable-public-device-url) feature**

## Features

- Latest version of Octoprint
- The following Octoprint plugins are added:
  - [TouchUI](https://plugins.octoprint.org/plugins/touchui/)
  - [Preheat](https://plugins.octoprint.org/plugins/preheat/)
  - [DisplayProgress](https://plugins.octoprint.org/plugins/displayprogress/)
  - [BedLevelVisualizer](https://plugins.octoprint.org/plugins/bedlevelvisualizer/)
  - [Floating Navbar](https://plugins.octoprint.org/plugins/floatingnavbar/)
  - [Navbar Temperature](https://plugins.octoprint.org/plugins/navbartemp/)
  - [Emergency Stop Button](https://plugins.octoprint.org/plugins/estop/)
  - [Cancel Object](https://plugins.octoprint.org/plugins/cancelobject/)
  - [Octolapse](https://plugins.octoprint.org/plugins/octolapse/) (version 0.3.4)
- A MJPG streamer that is accessible via http://<public-url>/webcam/

## Getting started

- Sign up on [balena-cloud.io](https://dashboard.balena-cloud.com/signup)
- go through the [getting started guide](https://www.balena.io/docs/learn/getting-started/raspberry-pi/nodejs/) and create a new application
- clone this repository to your local workspace
- add the _balena remote_ to your local workspace using the useful shortcut in the dashboard UI
- `git push balena master`
- see the magic happening, your device is getting updated Over-The-Air!

## Configure via [environment variables](https://docs.resin.io/management/env-vars/)
Variable Name | Value | Description | Device-specific
------------ | ------------- | ------------- | -------------
**`RESIN_HOST_CONFIG_gpu_mem`** | `128` | the amount of RAM dedicated to the GPU | Raspberry Pi (all revs) - only required if you plan camera streaming
**`RESIN_HOST_CONFIG_start_x`** | `1` | required to enable the Raspberry Pi Camera Module | Raspberry Pi (all revs) - only required if you plan camera streaming

Apply the above settings in the "Fleet Configuration" panel (if applying it for the all devices withing your application), or "Device Configuration" panel (if applying it for a single device).

## License

Copyright 2016-2019 Balena Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
