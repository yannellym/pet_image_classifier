#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """        
    # Create a dict to store dognames
    dognames_dic = dict()

    # Read names from file, 1 name per line & automatically close the file
    with open(dogfile, "r") as infile:
        # Iterate through each line in the file
        for line in infile:
            # Strip any whitespace from the line
            line = line.strip()
            # Add the name to dognames_dic if it doesn't exist
            dognames_dic.setdefault(line, 1)

    # Iterate through results_dic to determine if labels are dogs
    for key in results_dic:
        # Check if the Pet Image Label is a dog
        is_pet_dog = results_dic[key][0] in dognames_dic
        # Check if the Classifier Label is a dog
        is_classifier_dog = results_dic[key][1] in dognames_dic
        # Append the results to the end of the value list in results_dic
        results_dic[key].extend([int(is_pet_dog), int(is_classifier_dog)])