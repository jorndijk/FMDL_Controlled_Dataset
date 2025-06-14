import os
from PIL import Image
import matplotlib.pyplot as plt

def show_mnist_images(digit, num_images, base_dir="mnist_digits"):
    digit_dir = os.path.join(base_dir, f"digit_{digit}")
    if not os.path.exists(digit_dir):
        print(f"Directory {digit_dir} does not exist.")
        return

    image_files = sorted([f for f in os.listdir(digit_dir) if f.endswith('.png')])[:num_images]
    if len(image_files) == 0:
        print(f"No images found for digit {digit} in {digit_dir}.")
        return

    cols = 5
    rows = (num_images + cols - 1) // cols

    plt.figure(figsize=(cols * 2, rows * 2))
    for i, img_file in enumerate(image_files):
        img_path = os.path.join(digit_dir, img_file)
        img = Image.open(img_path)

        plt.subplot(rows, cols, i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(f"{digit} - {i+1}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

digit_to_show = 5
images_to_show = 10
show_mnist_images(digit_to_show, images_to_show)
