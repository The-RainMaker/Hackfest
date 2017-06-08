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
## Flow
  * Get video duration, we need this to get the proper time to capture the viewer (in this code, it's 15s before video end).
  * Spawn video player
  * Before video end, capture image, analyze it and decide which ads should be played next.
  * Wait for video end, and play the ads.
## Codes
[hackfest-cognitive-ads.py](https://github.com/The-RainMaker/Hackfest/blob/master/hackfest-cognitive-ads.py)

Just change the Ocp-Apim-Subscription-Key with your API key.
## Nice Features
  * Handle interrupt signal and exit gracefully, otherwise you will face an out of resource error when you try to initialize the camera again.
  * No external tools nor libraries, because you might found that to get video duration, one can use MediaInfo or ffmpeg. Well, I don't use it because OMXPlayer already have that information, just need a little bit effort :)
## Special Thanks
To my wife and kids, as they helped me to test the code. If there's a GenY person in the picture, then absolutely playing [XBox One S](http://www.xbox.com/en-US/xbox-one-s) ads, and if there's a female present then play [Surface Laptop](https://www.microsoft.com/en-us/surface) commercial :)
