import os
import gzip
import numpy as np
from urllib.request import urlretrieve
from PIL import Image

def download_and_process_fashion_mnist():
    """
    Downloads the FashionMNIST dataset if not already downloaded,
    processes it into individual image files, and organizes them
    into train/test folders by label.
    """
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths relative to the script's location
    source_dir = os.path.join(script_dir, "tmp/mnist-source")
    output_dir = os.path.join(script_dir, "tmp/mnist")
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Fashion-MNIST URLs
    base_url = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"
    files = {
        "train_images": "train-images-idx3-ubyte.gz",
        "train_labels": "train-labels-idx1-ubyte.gz",
        "test_images": "t10k-images-idx3-ubyte.gz",
        "test_labels": "t10k-labels-idx1-ubyte.gz",
    }

    # Download files if not already present
    for file_name in files.values():
        file_path = os.path.join(source_dir, file_name)
        if not os.path.exists(file_path):
            print(f"Downloading {file_name}...")
            urlretrieve(base_url + file_name, file_path)

    # Extract and process files
    print("Processing dataset...")
    data = {}
    for key, file_name in files.items():
        file_path = os.path.join(source_dir, file_name)
        with gzip.open(file_path, "rb") as f:
            data[key] = np.frombuffer(f.read(), dtype=np.uint8)

    # Parse IDX data
    train_images = data["train_images"][16:].reshape(-1, 28, 28)
    train_labels = data["train_labels"][8:]
    test_images = data["test_images"][16:].reshape(-1, 28, 28)
    test_labels = data["test_labels"][8:]

    datasets = [
        (train_images, train_labels, "train"),
        (test_images, test_labels, "test"),
    ]

    # Reprocess and save images
    for images, labels, split in datasets:
        split_dir = os.path.join(output_dir, split)
        # Clear previous files
        if os.path.exists(split_dir):
            for root, _, files in os.walk(split_dir):
                for file in files:
                    os.remove(os.path.join(root, file))
        os.makedirs(split_dir, exist_ok=True)

        for idx, (image, label) in enumerate(zip(images, labels)):
            label_dir = os.path.join(split_dir, str(label))
            os.makedirs(label_dir, exist_ok=True)

            image_path = os.path.join(label_dir, f"{idx}.png")
            Image.fromarray(image).save(image_path)

    print("Dataset processing completed. Images saved to './tmp/mnist/'.")

def iterate_processed_fashion_mnist(data_dir="./tmp/mnist"):
    """
    Iterates through the processed FashionMNIST dataset and yields images and their metadata.

    Args:
        data_dir (str): Directory containing the processed FashionMNIST dataset.

    Yields:
        tuple: A tuple (image, label, relative_path), where:
            - image: PIL.Image object of the image.
            - label: Integer label of the image.
            - relative_path: String path to the image file relative to `data_dir`.
    """
    for split in ["train", "test"]:
        split_dir = os.path.join(data_dir, split)
        if not os.path.exists(split_dir):
            raise FileNotFoundError(f"Split directory '{split_dir}' does not exist. Run the processing script first.")

        for label in os.listdir(split_dir):
            label_dir = os.path.join(split_dir, label)
            if not os.path.isdir(label_dir):
                continue

            for image_file in os.listdir(label_dir):
                image_path = os.path.join(label_dir, image_file)
                relative_path = os.path.join(split, label, image_file)  # Relative path
                yield split, int(label), relative_path, image_path

# Example usage
if __name__ == "__main__":
    download_and_process_fashion_mnist()