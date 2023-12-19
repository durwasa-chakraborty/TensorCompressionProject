import numpy as np
from src.algorithms.rle import rle_compress
from src.algorithms.huffman import huffman_coding
from src.utils.size_comparator import compare_tensor_sizes
import pickle

def main():
    # Load the tensor
    tensor = np.load('data/test_tensor.npy')

    # Apply RLE Compression
    rle_compressed = rle_compress(tensor.flatten())

    # Apply Huffman Coding
    huffman_codes = huffman_coding(tensor.flatten())

    # Save the compressed tensors to files for size comparison
    with open('data/rle_compressed.pkl', 'wb') as f:
        pickle.dump(rle_compressed, f)

    with open('data/huffman_compressed.pkl', 'wb') as f:
        pickle.dump(huffman_codes, f)

    # Compare and display the sizes
    original_size_info = compare_tensor_sizes('data/test_tensor.npy', 'data/rle_compressed.pkl')
    print("Original vs RLE Compressed Tensor Size:")
    print(original_size_info)

    huffman_size_info = compare_tensor_sizes('data/test_tensor.npy', 'data/huffman_compressed.pkl')
    print("\\nOriginal vs Huffman Compressed Tensor Size:")
    print(huffman_size_info)

if __name__ == '__main__':
    main()
