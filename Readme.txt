You need the folowing to run this project

1) OpenCV
2) Dlib

Using DLIB's object detection and tracking we will implemnt a project to track faces in subsequent frames from a web cam feed.

Using object detection in every frame is not a good practice, as object detection uses up a lot of effeciency in searching for object Over the entire imagespace, we only need to check for the object inthe nearby regions, hence a tracker whoul dincrease the performance of the algorithm

This peoject uses the simple theory mentioned above to implement a system that tracks the face in the web cam feed.
