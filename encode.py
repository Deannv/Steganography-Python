from PIL import Image
def run(image, message):
    encoded_image = image.copy()
    width, height = image.size

    binary_message = [format(ord(i), '08b') for i in message]
    binary_message = ''.join(binary_message)


    if len(binary_message) > width * height:
        print("Message is too long")
        return None

    index = 0
    for x in range(width):
        for y in range(height):
            try:
                r, g, b, a = image.getpixel((x, y))
            except:
                r, g, b = image.getpixel((x, y))
            if index <= len(binary_message) - 1:
                new_r = (r & ~1) | int(binary_message[index])
        encoded_image.putpixel((x, y), (new_r, g, b))
        index += 1

    return encoded_image