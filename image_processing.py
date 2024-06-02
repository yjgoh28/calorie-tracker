import base64

def encode_image(image):
    # Read the bytes of the image directly from the file-like object
    bytes = image.read()
    return base64.b64encode(bytes).decode("utf-8")

def encode_multiple_images(images):
    # Encode each image in the list
    return [encode_image(image) for image in images]