#!/usr/bin/env python3
import numpy as np

# Function to generate a 3D tensor and save it to a file
def create_test_tensor():
    # Generate a 3D tensor with random data
    tensor = np.random.rand(4, 4, 4)  # Example size: 4x4x4

    # Save the tensor to a file
    file_path = '../data/test_tensor.npy'
    np.save(file_path, tensor)

    return file_path

# Create the tensor and get the file path
tensor_file_path = create_test_tensor()
tensor_file_path
