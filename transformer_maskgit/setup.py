from setuptools import setup, find_packages

setup(
  name = 'transformer_maskgit',
  version='0.1.0',  # Required
  packages=find_packages(),
  install_requires=[
    'accelerate',
    'beartype',
    'einops>=0.6',
    'ema-pytorch>=0.2.2',
    'opencv-python',
    'pillow',
    'numpy',
    'sentencepiece',
    #'torch==2.0.1',
    'torchtyping',
    'torchvision',
    #'transformers==4.30.1',
    'tqdm',
    'vector-quantize-pytorch==1.1.2',
    'nibabel',
    'openpyxl',
  ],
)
