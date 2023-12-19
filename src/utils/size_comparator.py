import os

def get_file_size(file_path):
    ''' Returns the file size in bytes '''
    return os.path.getsize(file_path)

def compare_tensor_sizes(original_file, compressed_file):
    ''' Compares the size of the original and compressed tensors '''
    original_size = get_file_size(original_file)
    compressed_size = get_file_size(compressed_file)

    reduction = ((original_size - compressed_size) / original_size) * 100

    return {
        'original_size': original_size,
        'compressed_size': compressed_size,
        'reduction_percentage': reduction
    }
