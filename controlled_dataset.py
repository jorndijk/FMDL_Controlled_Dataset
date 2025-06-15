import os
import numpy as np
from PIL import Image
from keras.datasets import mnist

def generate_base_dataset(digits_to_save, num_images, output_base_dir):
    (x_train_orig, y_train_orig), (x_test_orig, y_test_orig) = mnist.load_data()

    x_all_digits = np.concatenate((x_train_orig, x_test_orig), axis=0)
    y_all_digits = np.concatenate((y_train_orig, y_test_orig), axis=0)
    
    os.makedirs(output_base_dir, exist_ok=True)

    for digit in digits_to_save:
        digit_dir = os.path.join(output_base_dir, f"digit_{digit}")
        os.makedirs(digit_dir, exist_ok=True)

        indices = np.where(y_all_digits == digit)[0][:num_images]

        if len(indices) < num_images:
            print(f"Warning: Found only {len(indices)} images for digit {digit}, which is less than the requested {num_images}.")

        for i, idx in enumerate(indices):
            img_array = x_all_digits[idx]
            img = Image.fromarray(img_array)
            img.save(os.path.join(digit_dir, f"{digit}_{i+1}.png"))
        
        print(f"Saved {len(indices)} images for digit {digit} in '{digit_dir}'.")


if __name__ == "__main__":
    DIGITS_TO_PROCESS = [5, 9]
    IMAGES_PER_DIGIT = 2000
    OUTPUT_DIRECTORY = "mnist_digits"
    random_seed = 42
    np.random.seed(random_seed)
    
    generate_base_dataset(
        digits_to_save=DIGITS_TO_PROCESS,
        num_images=IMAGES_PER_DIGIT,
        output_base_dir=OUTPUT_DIRECTORY
    )
    print("\nDataset generation complete.")