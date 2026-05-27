# Project Galaxy

A Python package scaffold for computer vision and natural language processing research. Provides a structured starting point for ML projects using PyTorch, Transformers, and OpenCV.

## Intended Scope

This repository serves as a foundation for building ML pipelines that combine:

- **Computer Vision**: Image preprocessing, object detection, and visual feature extraction via OpenCV and torchvision
- **Natural Language Processing**: Text tokenisation, embeddings, and sequence modelling via NLTK and Hugging Face Transformers
- **Deep Learning**: Model training and evaluation using PyTorch, with support for GPU acceleration

## Tech Stack

| Component | Library |
|---|---|
| Deep Learning | PyTorch, torchvision, torchaudio |
| Transformers / LLMs | Hugging Face Transformers |
| Computer Vision | OpenCV (`opencv-python`) |
| NLP Utilities | NLTK |
| Numerics | NumPy |
| Visualisation | matplotlib |

## Installation

```bash
pip install -e .
```

Or install dependencies directly:

```bash
pip install -r requirements.txt
```

## Package Setup

The project uses `setuptools` for packaging. Update `setup.py` with the project description and entry points before publishing:

```python
setup(
    name='Galaxy',
    version='0.1.0',
    description='<project description>',
    packages=find_packages(),
    install_requires=<requirements>,
)
```

## License

MIT
