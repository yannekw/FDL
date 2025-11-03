"""Definition of Dataloader"""
import math
import random

import numpy as np


class DataLoader:
    """
    Dataloader Class
    Defines an iterable batch-sampler over a given dataset
    """
    def __init__(self, dataset, batch_size=1, shuffle=False, drop_last=False):
        """
        :param dataset: dataset from which to load the data
        :param batch_size: how many samples per batch to load
        :param shuffle: set to True to have the data reshuffled at every epoch
        :param drop_last: set to True to drop the last incomplete batch,
            if the dataset size is not divisible by the batch size.
            If False and the size of dataset is not divisible by the batch
            size, then the last batch will be smaller.
        """
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.drop_last = drop_last

    def __iter__(self):
        ########################################################################
        # TODO:                                                                #
        # Define an iterable function that samples batches from the dataset.   #
        # Each batch should be a dict containing numpy arrays of length        #
        # batch_size (except for the last batch if drop_last=True)             #
        # Hints:                                                               #
        #   - np.random.permutation(n) can be used to get a list of all        #
        #     numbers from 0 to n-1 in a random order                          #
        #   - To load data efficiently, you should try to load only those      #
        #     samples from the dataset that are needed for the current batch.  #
        #     An easy way to do this is to build a generator with the yield    #
        #     keyword, see https://wiki.python.org/moin/Generators             #
        #   - Have a look at the "DataLoader" notebook first. This function is #
        #     supposed to combine the functions:                               #
        #       - combine_batch_dicts                                          #
        #       - batch_to_numpy                                               #
        #       - build_batch_iterator                                         #
        #     in section 1 of the notebook.                                    #
        ########################################################################

        # TODO: Get the number of samples in the dataset
        sample_number = len(self.dataset)

        # TODO: Create an array of indices to sample from the dataset
        indices = [i for i in range(0, sample_number)]
        # TODO: Shuffle the indices if self.shuffle is True

        if self.shuffle:
            random.shuffle(indices)

        # TODO: Calculate the number of full batches
        batches = len(self)

        # TODO: If self.drop_last is False and there are leftover samples,
        #       add one more batch to account for the last smaller batch

        # TODO: Iterate over the number of batches
        for i in range(0, batches):

            # TODO: Calcuate the start and end index of the batch
            start = i * self.batch_size
            end = start + self.batch_size
            # TODO: Get the indices for the current batch
            indices_for_batch = iter(indices[start:end])
            # TODO: Create a list to store the samples of the current batch
            samples = []
            # TODO: Iterate over the indices of the current batch
            for j in indices_for_batch:
                samples.append(self.dataset[j]["data"])
            # TODO: Convert the list to numpy arrays
            samples = np.array(samples)
            # TODO: Yield the batch
            yield {"data": samples}

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################

    def __len__(self):
        ########################################################################
        # TODO:                                                                #
        # Return the length of the dataloader                                  #
        # Hint: this is the number of batches you can sample from the dataset. #
        # Don't forget to check for drop last (self.drop_last)!                #
        ########################################################################
        

        if self.drop_last:
            length = len(self.dataset) // self.batch_size
        else:
            length = math.ceil((len(self.dataset) / self.batch_size))


            ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return length
