"""
data_setup.py

Module for setting up data loading for PyTorch models.

Provides a DataManager class that:
- Loads training and testing datasets from directories
- Applies image transformations
- Creates and returns DataLoaders for training and evaluation

Intended for modular deep learning workflows.
"""

import os
import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from PIL import Image
from typing import Tuple, List, Dict
from .paths import train_dir, test_dir
from .image_transforms import simple_transform


# def for get class and dictionary
def get_classes(PATH: int) -> Tuple[List[str], Dict[str, int]]:
    
    classes = sorted(entry.name for entry in os.scandir(PATH))
    if not classes:
        raise FileNotFoundError(f"Couldn't find classes in {PATH}")
    
    class_to_idx = {class_name: i for i, class_name in enumerate(classes)}
    return classes, class_to_idx


# custom class
class CustomDataSet(torch.utils.data.Dataset):
    def __init__(self, root, transform):
        self.root_dir = root,
        self.transform = transform
        self.paths = list(root.glob('*/*.png'))
        self.classes, self.class_to_idx = get_classes(root)
    
    def load_image(self, index: int):
        'Return PIL image'
        image_path = self.paths[index]
        img = Image.open(image_path)
        img = img.convert('RGBA')
        r, g, b, a = img.split()
        return a
    
    def __len__(self):
        'Return len of the dataset'
        return len(self.paths)
    
    def __getitem__(self, index: int) -> Tuple[torch.tensor, int]:
        'Return image and class'
        img = self.load_image(index)
        class_name = self.paths[index].parent.name
        class_idx = self.class_to_idx[class_name]
        
        if self.transform:
            return self.transform(img), class_idx
        else:
            return img, class_idx


class DataManager():
    """
    A class for managing PyTorch datasets and creating DataLoaders.

    It takes training and testing directories along with image transformations,
    and converts them into PyTorch Datasets and DataLoaders.

    This makes the data handling process easier and more modular.

    Args:
        train_dir (str): Path to the training images directory.
        test_dir (str): Path to the testing images directory.
        transform (transforms.Compose): Transformations to apply to the training images.
        test_transform (transforms.Compose, optional): Transformations for test images.
            If None, the same transformations as 'transform' will be applied to the test set.
    """
    
    
    def __init__(self, 
                 train_dir: str = train_dir,
                 test_dir: str = test_dir,
                 transform: transforms.Compose = simple_transform,
                 test_transform: transforms.Compose = None):

        self.train_dir = train_dir
        self.test_dir = test_dir
        self.transform = transform
        self.test_transform = transform if test_transform is None else test_transform
        self.batch_size = None
        self.num_workers = None

        #self.train_dataset = ImageFolder(root=self.train_dir, transform=self.transform)
        #self.test_dataset = ImageFolder(root=self.test_dir, transform=self.test_transform)
        self.train_dataset = CustomDataSet(root=self.train_dir, transform=self.transform)
        self.test_dataset = CustomDataSet(root=self.test_dir, transform=self.test_transform)
        self.classes = self.test_dataset.classes

    
    def create_dataloaders(self,
                           batch_size: int = 32,
                           num_workers: int = os.cpu_count() - 1,
                           shuffle_train: bool = True,
                           shuffle_test: bool = False):
        """
        Creates DataLoaders for the training and testing datasets.

        Args:
            batch_size (int): Number of samples per batch (default: 32).
            num_workers (int): Number of CPU cores used for data loading (default: available CPU cores - 1).
            shuffle_train (bool): Whether to shuffle the training dataset (default: True).
            shuffle_test (bool): Whether to shuffle the testing dataset (default: False).

        Returns:
            Tuple[DataLoader, DataLoader, List[str]]: 
                A tuple containing (train_loader, test_loader, class_names).
        """
        
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.shuffle_train = shuffle_train
        self.shuffle_test = shuffle_test
    
        train_loader = DataLoader(dataset=self.train_dataset,
                                  batch_size=self.batch_size,
                                  shuffle=self.shuffle_train,
                                  num_workers=self.num_workers)
    
        test_loader = DataLoader(dataset=self.test_dataset,
                                 batch_size=self.batch_size,
                                 shuffle=self.shuffle_test,
                                 num_workers=self.num_workers)
    
        return train_loader, test_loader, self.classes
