# object_identification
Computer vision project aiming to train a model to identify people within live video inputs

Source of the dataset used in my project: https://www.kaggle.com/datasets/fareselmenshawii/human-dataset

Within main directory of project - create two folders: one for images, one for labels. Within each of those create two additional folders: one for training files, one for validation files.

Download you dataset, split between training and validation sets, annotate, and save in the appropriate folders.

pip install the Ultralytics library in a venv to eliminate any compatability issues with previously installed libraries.

Change paths in functions to match where your data is located.

Specify the source to "0" within the prediction scripts to make predictions on live video from default webcam in your system.
