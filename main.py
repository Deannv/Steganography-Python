import encode, decode, time, os
from PIL import Image

# BEFORE STARTING THIS PROGRAM, MAKE SURE TO INSERT AN IMAGE TO "INPUT" DIRECTORY (lossless-compression)
in_path, out_path= ("source\input","source\out")

def enc():
    print('---Encoding---')
    file                    = input('File name : ')
    file                    += ".png"
    img                     = Image.open(f'{in_path}\{file}')
    message                 = input('Message : ')
    result                  = encode.run(image=img, message=message)
    if result is None:
        enc()
    img_save                = result.save(f'{out_path}\{file}-result.png')
    print("encoded!\n")
    time.sleep(1.5)
    for i in range(4):
        os.system('cls')
        print(f"loading to decoding the image {i*'. '}")
        time.sleep(1)
    imgs = Image.open(f'{out_path}\{file}-result.png')
    print(f"{30*'-'}\nDecoded text : {decode.run(image=imgs)}")

def dec():
    print('---Decoding---')
    file = input('File name : ')
    try:
        imgs = Image.open(f'{out_path}\{file}.png')
        for i in range(3):
            os.system('cls')
            print(f"loading to decoding the image {(i+1)*'. '}")
            time.sleep(1)
        print(f"{30*'-'}\nDecoded text from {file}.png : {decode.run(image=imgs)}")
    except:
        print('ERROR ! This can be caused when the file doesn\'t exist or corrupted.\n')
        dec()
    
def start():
    options = [enc,dec]
    print(f'this steganography only works for .png\nbuild by Kmz.\n{40*"_"}\nMenu : \n1. Encode\n2. Decode\n{40*"_"}')
    option = input('What do you want to do ? (1-2) : ')
    option = int(option)
    if option in [1, 2]:
        exe = options[option-1]
        exe()
    else:
        os.system('cls')
        print('Invalid choice, please input from 1 to 2!')
        start()
    return None
    
if __name__ == "__main__":
    start()