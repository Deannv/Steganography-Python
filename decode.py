def run(image):
    width, height = image.size
    binary_message = []

    for x in range(width):
        for y in range(height):
            try:
                r, g, b, a = image.getpixel((x, y))
            except:
                r, g, b = image.getpixel((x, y))
        binary_message.append(r & 1)

    binary_message = ''.join(str(i) for i in binary_message)
    message = [chr(int(binary_message[i: i+8], 2)) for i in range(0, len(binary_message), 8)]
    message = ''.join(message)

    return message.split('ÿ')[0]