# Filter_Options
Filter Project
### Install Filter_Options from PyPi.
```bash
pip install Filter_Options
```

#### Example of code execution
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
from filters import Filters

#Important: Have your desired image to test, add the file to your program.
# Read the image file (valstrax is an example image)
img = mpimg.imread("valstrax.png")

#Initialize
filters = Filters(img)

# Apply desired filter
filtered_img = filters.color_inversion()

# Display the filtered image using Matplotlib
plt.imshow(filtered_img)
plt.show()
```

