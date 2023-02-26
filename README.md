# Gesture-volume-controler-OpenCV-
Gesture volume controller using OpenCV is a computer vision-based system that uses hand gestures to control the volume of an audio or video player. It involves the use of a camera to capture live video input of the user's hand gestures and OpenCV library to analyze and recognize the gestures.

Here are the steps involved in building a gesture volume controller using OpenCV:

1. Capture video input: Use a camera to capture live video input of the user's hand gestures.

2. Preprocessing: Preprocess the video input to remove background noise and improve the quality of the image.

3. Hand detection: Use OpenCV to detect and track the user's hand in the video input. This can be achieved by using techniques such as thresholding, contour detection, and convex hull.

4. Gesture recognition: Implement a gesture recognition algorithm using OpenCV to recognize the user's hand gestures. Commonly used techniques for gesture recognition include template matching, machine learning, and deep learning.

5. Volume control: Use the recognized gesture to control the volume of an audio or video player. This can be done by mapping the gesture to a specific volume level or by using a continuous gesture to increase or decrease the volume.

6. Display the output: Display the current volume level or the recognized gesture on the screen.

WORKING CONTROLS:

1. AS DISTANCE BETWEEN TIP OF MIDDLE FINGER AND TIP OF THUMB INCREASES , VOLUME INCREASES GRADUALLY
2. IF CERTAIN PERCENTAGE OF VOLUME NEED TO BE LOCKED THEN INCREASE THE DISTANCE BETWEEN TIP OF RING FINGER AND LITTLE FINGER , NOW THIS PERCENTAGE WILL BE LOCKED
3.  INORDER TO RESET THE PERCENTAGE CLSE ALL FINGERS THEN IT WILL BE RESET
4.  AGAIN LOCK AT FAVOURABLE PERCENTAGE

Overall, the gesture volume controller using OpenCV is an interesting and useful application of computer vision and can be extended to control other features of a media player, such as playback speed, mute, and skip.


![profile-min](https://user-images.githubusercontent.com/73246457/221417036-f7760eb1-d862-4f85-b93c-a9763fc20b31.jpg)
