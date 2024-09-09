# YOLOv8-ToolKit
A repo where you can find codes for preprocessing data like splitting, combining multiple versions, and also training and streaming the predictions over a video(For YOLOv8).

These are some other scripts used to ease the process of training and development but are not needed to run the framework.

1. `extract_images.py`: Use this script to extract images from a video every *n* frames, which we can set based on the number of images required. In the script, set the path for your video, and set the skip frames based on the interval in which you wish to save the frames. In the given example, `frame_skip` is set to 25, and if the video is of 25 FPS, frames will be saved once every second.

2. `data_split.py`: A simple script to split the dataset into training, testing, and validation sets as per the format required by YOLOv8. Specify the images folder, labels folder, and also mention your test, train, and validation split ratio to get the split in the same folder as this `.py` file. **Note: The code assumes that the images are in `.jpg` format. If you have any other format, modify the same in Line 18.**

3. `data_combine.py`: This script can be used to combine datasets. Useful when there are multiple sets of data (maybe annotated by different people), and this can be used to easily combine them into a single bigger dataset.

4. `auto_annotate.py`: Manual annotation can be time-consuming; hence use this script to auto-annotate using an existing model to increase the size of your dataset. Once auto annotation is done, it can be manually verified. In the script, pass the model location and also pass the folder where the images are located. The location for labels also needs to be passed. Final annotations are in `.txt` format and can be viewed using any labeling software like *LabelImg*.

5. `stream.py`: This code lets us view the YOLO model in action on a live video. It shows us the predictions being made in real-time in the video. Specify the location of the video and model for the same.

6. `data.yaml`: This config file is used to specify parameters like the number of classes and the location of the dataset and will be required for training with YOLOv8. Refer to the [Documentation](https://docs.ultralytics.com/modes/train/) for more details.

7. `training.ipynb`: This notebook has steps to train a model, with a few hyperparameters to start with. However, refer to the [Documentation](https://docs.ultralytics.com/modes/train/) to achieve the best results by changing these parameters according to your dataset size, quality, etc.

8. `capture_coordinates.py`: This Python script allows you to manually capture coordinates from an image using mouse clicks and display them on the image. It's useful for defining regions of interest (ROIs) in an image by capturing sets of four points, typically to create rectangular regions.
