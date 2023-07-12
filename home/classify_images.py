#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py


                                                                           
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
import os.path

def classify_images(images_dir, results_dic, model):
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    # Defining lists to populate dictionary
   # Process all files in the results_dic - use images_dir to give the full path
    # that indicates the folder and the filename (key) to be used in the classifier function
        # Process all files in the results_dic - use images_dir to give full path
    # that indicates the folder and the filename (key) to be used in the classifier function
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    # look through the results dictionary
     for key in results_dic:
        # get the directory, the key, and the model.
        direct = os.path.join(images_dir, key)
        model_label = classifier(direct, model)
        # turn everything into lowercase and strip it from white spaces
        model_label = model_label.lower().strip()
        
        truth = results_dic[key][0]
        # add the classifier label and the value of the model
        match = int(truth in model_label)
        results_dic[key].extend([model_label, match])
            