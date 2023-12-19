def rle_compress(tensor):
    ''' Run-Length Encoding for compressing a tensor '''
    if not tensor.size:
        return []

    compressed = []
    prev_value = tensor[0]
    count = 1

    for item in tensor[1:]:
        if item == prev_value:
            count += 1
        else:
            compressed.append((prev_value, count))
            prev_value = item
            count = 1

    compressed.append((prev_value, count))
    return compressed
