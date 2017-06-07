# Cognitive Services Hackfest

## Background
I create the code in preparation for Azure Cognitive Services hackfest held by __Microsoft Indonesia Developer eXperience (DX)__ Team.
The idea was to create an advertising player app in which the displayed ads depend on who watched the ads.
## Scenario
Remember if you in an elevator or in a waiting room and see a TV displaying ads?
What if the TV can "see" the person around it and decide which ads to play that fit best? Cool isn't it?
## Ingredients
1. [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) subscription, I'm using the Computer Vision API.
2. [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/ "Raspberry Pi 3").
3. [Raspberry Pi Camera Module V2](https://www.raspberrypi.org/products/camera-module-v2/).

I'm using the official [Raspbian Jessie](https://www.raspberrypi.org/downloads/raspbian/). All the required tools and libraries already included with this distro (such as [PiCamera](https://picamera.readthedocs.io/en/release-1.13/) Python module, or [OMXPlayer](https://github.com/popcornmix/omxplayer)).
## Codes
[hackfest-cognitive-ads.py](https://github.com/The-RainMaker/Hackfest/blob/master/hackfest-cognitive-ads.py)
