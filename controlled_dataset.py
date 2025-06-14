from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

(x_train_orig, y_train_orig), (x_test_orig, y_test_orig) = mnist.load_data()

x_all_digits = np.concatenate((x_train_orig, x_test_orig), axis=0)
y_all_digits = np.concatenate((y_train_orig, y_test_orig), axis=0)

digit1 = 5
digit2 = 9
num_images_per_digit = 2000

mask_digit1 = (y_all_digits == digit1)
mask_digit2 = (y_all_digits == digit2)
combined_mask = np.logical_or(mask_digit1, mask_digit2)

x_selected_digits = x_all_digits[combined_mask]
y_selected_digits = y_all_digits[combined_mask]

output_dir = "mnist_digits"
os.makedirs(output_dir, exist_ok=True)

digit1_dir = os.path.join(output_dir, f"digit_{digit1}")
digit2_dir = os.path.join(output_dir, f"digit_{digit2}")

os.makedirs(digit1_dir, exist_ok=True)
os.makedirs(digit2_dir, exist_ok=True)

def save_digit_images(digit, save_dir):
    indices = np.where(y_all_digits == digit)[0][:num_images_per_digit]
    for i, idx in enumerate(indices):
        img_array = x_all_digits[idx]
        img = Image.fromarray(img_array)
        img.save(os.path.join(save_dir, f"{digit}_{i+1}.png"))

save_digit_images(digit1, digit1_dir)
save_digit_images(digit2, digit2_dir)

# print("\nDisplaying some of the selected '5's and '9's:")
# num_to_display = 10  
# plt.figure(figsize=(15, 3)) 

# random_indices = np.random.choice(len(x_selected_digits), num_to_display, replace=False)

# for i, idx in enumerate(random_indices):
#     ax = plt.subplot(1, num_to_display, i + 1)

#     plt.imshow(x_selected_digits[idx], cmap='gray')
#     plt.title(f"Label: {y_selected_digits[idx]}")
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
# plt.tight_layout()
# plt.show()