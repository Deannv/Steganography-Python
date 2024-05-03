
# Python Steganography

Put secret messages in an image without actualy changing the image!


## Installation

Before you start, install all this package to encode and retrieve files from local.

```bash
  pip install encode
  pip install pillow
```


## Usage

Replace the source\input with the image source or directory.

```python
import encode, decode, time, os
from PIL import Image

in_path, out_path= ("source\input","source\out")
```
And source\out is the target location to save the copy of the image 
after putting a secret message.


## FAQ

#### How long is the message limit?

well depends on the image resolution

#### Which image format is accepted?

The code is using rgba and rgb formats for fetching the pixel, .PNG would be the best option

