"""
transformations.py

Module containing predefined sets of torchvision transformations 
for creating PyTorch datasets.
"""

from torchvision import transforms
import torch

simple_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

transform_28x28 = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

binary_transform_28x28 = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: (x>0).to(x.dtype))
])

binary_transform_affine = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.RandomAffine(degrees=(-45, 45), scale=(0.7, 1.5), translate=(0.2, 0.2), shear=(-5, 5)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: (x>0).to(x.dtype))
])

binary_transform_affine_64x64 = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.RandomAffine(degrees=(-45, 45), scale=(0.7, 1.5), translate=(0.2, 0.2), shear=(-5, 5)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: (x>0).to(x.dtype))
])

trivial_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.TrivialAugmentWide(num_magnitude_bins=31),
    transforms.ToTensor()
    ])

auto_augment_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.AutoAugment(),
    transforms.ToTensor()
    ])


mix_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.RandomResizedCrop(size=(64, 64), scale=(0.7, 1.05)),
    transforms.RandomRotation(degrees=(-20, 20)),
    transforms.ToTensor()
    ])