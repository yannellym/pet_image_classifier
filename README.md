
# Pet Image Classifier

This repository contains code for a pet image classifier. Given an input image, the classifier aims to identify whether the image contains a dog or not. The classifier is built using deep learning techniques and utilizes a convolutional neural network (CNN) model.

## About

This image classifier has been trained on a dataset of labeled dog and cat images. It has been designed to accurately classify pet images, providing insights into whether the image contains a dog or not.

### Example Results

Here are the example results from the pet image classifier:

#### Resnet Model
![Screenshot 2023-07-12 at 5 11 04 PM](https://github.com/yannellym/pet_image_classifier/assets/91508647/b289dcaa-97c4-4463-91da-b9e6732e7500)

#### VVG Model
![Screenshot 2023-07-12 at 5 11 19 PM](https://github.com/yannellym/pet_image_classifier/assets/91508647/8a387664-a445-4000-9625-2de1242b9dcc)

#### Alexnet Model
![Screenshot 2023-07-12 at 5 10 47 PM](https://github.com/yannellym/pet_image_classifier/assets/91508647/7a71ff2e-ff7a-4e60-9360-75789a8127f9)


Results Table

Project Results

Given our results, the "best" model architecture is VGG. It outperformed both of the other architectures when considering both objectives 1 and 2. 
ResNet did classify dog breeds better than AlexNet, but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. 
The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification 
with 93.3% accuracy.

### Training Data

The model was trained using a diverse dataset of dog images. Here is an example of a dog image used during the training:

![Screenshot 2023-07-12 at 5 12 36 PM](https://github.com/yannellym/pet_image_classifier/assets/91508647/daa08e31-3a16-494a-9b86-84ad3fb1211a)


### Testing the Classifier

You can test the classifier by providing your own images. Here is an example of an uploaded NOT A dog image:

![Screenshot 2023-07-12 at 5 12 57 PM](https://github.com/yannellym/pet_image_classifier/assets/91508647/b661e8f4-992e-4c5e-8ffc-5d120acf4e9b)



## Installation

To use this pet image classifier, follow the steps below:

1. Clone the repository:

   ```shell
   git clone https://github.com/yannellym/pet_image_classifier.git

2. Install the required dependencies. The classifier requires Python 3 and the following libraries:

 - TensorFlow
 - Keras
 - OpenCV
 - Matplotlib

    2. a. You can install the dependencies using pip:

      - shell
      - Copy code
      - pip install tensorflow keras opencv-python matplotlib

## Usage

To use the pet image classifier, follow the steps below:

    1. Ensure you have downloaded and saved the trained model weights. The trained weights file (model_weights.h5) should be placed in the models directory.
    
    2. Prepare the image you want to classify. The image should be in JPEG or PNG format.
    
    3. Run the classify_image.py script and provide the path to the input image as a command-line argument:
    
      -  python classify_image.py --image path/to/your/image.jpg

* The script will load the trained model, process the image, and provide the classification result.

## Model Training
If you are interested in training the pet image classifier from scratch or fine-tuning the existing model, you can use the provided Jupyter Notebook (model_training.ipynb) in the notebooks directory. The notebook provides step-by-step instructions on data preparation, model architecture, training, and evaluation.

## Dataset
The pet image classifier was trained on a dataset of labeled dog and cat images. The dataset used for training is not included in this repository. However, you can obtain similar datasets from various online sources or use your own labeled dataset.

## License
This project is licensed under the MIT License.

Acknowledgements
The pet image classifier is based on the work of several researchers and contributors in the field of deep learning and computer vision. It is also an original assignment by the Udacity Nanodegree Program.

Contributions
Contributions to this project are welcome. If you find any issues, have suggestions, or want to contribute improvements, please feel free to submit a pull request or open an issue.

Contact
For any questions or inquiries about this project, please contact me at yannellym@gmail.com

## Enjoy classifying pet images!
