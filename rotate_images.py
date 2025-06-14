import os
from PIL import Image
import random

def rotate_images(digit, input_base="mnist_digits", output_base="mnist_digits_rotated", min_angle=0, max_angle=20):
    input_dir = os.path.join(input_base, f"digit_{digit}")
    output_dir = os.path.join(output_base, f"digit_{digit}")
    os.makedirs(output_dir, exist_ok=True)

    image_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]

    for img_file in image_files:
        img_path = os.path.join(input_dir, img_file)
        img = Image.open(img_path)

        angle = random.uniform(min_angle, max_angle)
        if random.random() < 0.5:
            angle = -angle
        rotated_img = img.rotate(angle, resample=Image.BILINEAR)

        rotated_img.save(os.path.join(output_dir, f"rotated_{img_file}"))

    print(f"Rotated {len(image_files)} images for digit {digit} and saved them in '{output_dir}'.")

if __name__ == "__main__":
    digit_to_rotate = 9
    rotate_images(digit_to_rotate)
    digit_to_rotate = 5
    rotate_images(digit_to_rotate)
