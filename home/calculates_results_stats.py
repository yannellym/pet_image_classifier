#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    results_stats_dic = {}
    
  # how many images in the result dic
    n_images = len(results_dic)
    # variables to keep counts
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    
    # let's look at each key in our dic
    for key in results_dic:
        # if the value of the key at index 3 = 1(true), add 1 to the count of dogs_img
        if results_dic[key][3] == 1:
            n_dogs_img += 1
        else:
            # else, it's not a dog, the value is 0, so add 1 to notdogs_img
            n_notdogs_img += 1

            # same logic as above, but for the match variable
        if results_dic[key][2] == 1:
            n_match += 1
        
        # if we get the values at index 2 and index 3 to be true,
        # # we have the correct breed
        if results_dic[key][2] == 1 and results_dic[key][3] == 1:
            n_correct_breed += 1
        # if we get the values at index 3 and index 4 to be true,
        # # we have correctly identified dogs
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            n_correct_dogs += 1
        # if we get the values at index 3 and index 4 to be false,
        # # we have NOT correctly identified dogs
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            n_correct_notdogs += 1

    # Calculate percentages
    pct_match = (n_match / n_images) * 100 if n_images > 0 else 0.0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100 if n_dogs_img > 0 else 0.0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100 if n_dogs_img > 0 else 0.0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100 if n_notdogs_img > 0 else 0.0

    # adds the results of our counts to the results dic
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['pct_match'] = pct_match
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs

    return results_stats_dic
