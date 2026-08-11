# DCANet: Deep Context Attention Network for Automatic Polyp Segmentation

This repository provides an implementation of **DCANet (Deep Context Attention Network)** for automatic polyp segmentation, based on the following paper:

> Zaka-Ud-Din Muhammad, Zhangjin Huang, Naijie Gu, and Usman Muhammad,
> **"DCANet: deep context attention network for automatic polyp segmentation."**
> *The Visual Computer*, 39(11), 5513–5525, 2023.

## 📌 Overview

Automatic polyp segmentation is an important task in computer-aided colorectal cancer diagnosis. Accurate segmentation of polyps from colonoscopy images can assist clinicians in identifying and analyzing potentially abnormal regions.

**DCANet** is a deep-learning-based segmentation network designed to improve polyp segmentation by effectively capturing and combining contextual information at different levels of the network.

The network incorporates **deep context information and attention mechanisms** to better distinguish polyp regions from the surrounding background, particularly in challenging cases involving variations in:

* Polyp size and shape
* Appearance and texture
* Illumination
* Background complexity
* Boundary ambiguity

This repository contains the implementation, training and evaluation scripts, and supporting utilities required to reproduce the experiments.

---

## 🏗️ Network Architecture

DCANet is designed around a context-aware attention-based segmentation framework. The architecture aims to enhance feature representation by combining information from different levels of the encoder-decoder network.

Key ideas include:

* **Deep contextual feature extraction**
* **Attention-based feature refinement**
* **Multi-level feature fusion**
* **Encoder-decoder segmentation architecture**
* **Improved localization of polyp boundaries**

### Architecture Overview

```text
                    Input Image
                         │
                         ▼
                ┌─────────────────┐
                │     Encoder     │
                │ Feature Extract │
                └────────┬────────┘
                         │
             Multi-level Features
                         │
                         ▼
                ┌─────────────────┐
                │ Deep Context    │
                │ Representation  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Attention       │
                │ Mechanism       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Feature Fusion  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Decoder     │
                └────────┬────────┘
                         │
                         ▼
                  Polyp Mask
```

> **Note:** Replace the schematic above with the official DCANet architecture figure if your repository contains one.

---

## 📂 Repository Structure

A recommended project structure is:

```text
DCANet/
│
├── datasets/
│   ├── train/
│   │   ├── images/
│   │   └── masks/
│   ├── val/
│   │   ├── images/
│   │   └── masks/
│   └── test/
│       ├── images/
│       └── masks/
│
├── models/
│   └── dcanet.py
│
├── utils/
│   ├── dataset.py
│   ├── losses.py
│   └── metrics.py
│
├── train.py
├── test.py
├── inference.py
├── requirements.txt
├── README.md
└── LICENSE
```

The exact structure may differ depending on the implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n dcanet python=3.10
conda activate dcanet
```

Or using Python virtual environments:

```bash
python -m venv dcanet
source dcanet/bin/activate
```

On Windows:

```bash
dcanet\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Datasets

DCANet can be evaluated on commonly used public polyp segmentation datasets.

Depending on the experimental setup, supported datasets may include:

* **Kvasir-SEG**
* **CVC-ClinicDB**
* **CVC-ColonDB**
* **ETIS-LaribPolypDB**
* **CVC-300**

Please download the datasets from their respective official sources and organize them according to the directory structure expected by the implementation.

### Dataset Organization

For example:

```text
datasets/
└── Kvasir-SEG/
    ├── images/
    └── masks/
```

Update the dataset paths in the configuration or training script before starting training.

---

## 🚀 Training

To train DCANet from scratch:

```bash
python train.py
```

If the implementation supports configuration files:

```bash
python train.py --config configs/dcanet.yaml
```

Example options:

```bash
python train.py \
    --dataset Kvasir-SEG \
    --epochs 100 \
    --batch_size 16 \
    --lr 1e-4
```

> Adjust these commands according to the actual arguments implemented in your code.

---

## 🔍 Testing

After training, evaluate the model using:

```bash
python test.py --checkpoint path/to/checkpoint.pth
```

For a specific dataset:

```bash
python test.py \
    --dataset Kvasir-SEG \
    --checkpoint checkpoints/dcanet_best.pth
```

---

## 🖼️ Inference

To generate a segmentation mask for an individual image:

```bash
python inference.py \
    --image path/to/image.jpg \
    --checkpoint checkpoints/dcanet_best.pth
```

The predicted segmentation mask will be saved to the configured output directory.

Example:

```text
results/
├── input.jpg
└── input_mask.png
```

---

## 📈 Evaluation Metrics

Polyp segmentation performance is commonly evaluated using metrics such as:

### Dice Similarity Coefficient

$$
Dice = \frac{2|P \cap G|}{|P| + |G|}
$$

where:

* $P$ is the predicted segmentation
* $G$ is the ground-truth segmentation

### Intersection over Union

$$
IoU = \frac{|P \cap G|}{|P \cup G|}
$$

Other metrics that may be reported include:

* Mean Dice (mDice)
* Mean IoU (mIoU)
* Precision
* Recall
* Accuracy
* F-measure
* MAE

---

## 📊 Results

Add the experimental results obtained from your implementation here.

| Dataset           | Dice (%) | IoU (%) | Precision (%) | Recall (%) |
| ----------------- | -------- | ------- | ------------- | ---------- |
| Kvasir-SEG        | XX.XX    | XX.XX   | XX.XX         | XX.XX      |
| CVC-ClinicDB      | XX.XX    | XX.XX   | XX.XX         | XX.XX      |
| CVC-ColonDB       | XX.XX    | XX.XX   | XX.XX         | XX.XX      |
| ETIS-LaribPolypDB | XX.XX    | XX.XX   | XX.XX         | XX.XX      |
| CVC-300           | XX.XX    | XX.XX   | XX.XX         | XX.XX      |

> **Important:** Replace the placeholder values with results produced by your implementation. Do not report values from the paper unless your implementation reproduces the corresponding experimental protocol.

---

## 🖼️ Qualitative Results

You can include qualitative segmentation examples here.

```text
Input Image        Ground Truth        DCANet Prediction
     │                  │                    │
     ▼                  ▼                    ▼

  [image]            [mask]               [mask]
```

For example:

![Qualitative Results](results/qualitative_results.png)

If you have several examples, consider creating a figure containing:

1. Original colonoscopy image
2. Ground-truth mask
3. DCANet prediction
4. Overlay of prediction and ground truth

---

## 💾 Pretrained Models

Pretrained weights can be provided here:

| Model  | Dataset      | Download  |
| ------ | ------------ | --------- |
| DCANet | Kvasir-SEG   | [Link](#) |
| DCANet | CVC-ClinicDB | [Link](#) |

If pretrained weights are not currently available, remove this section or replace it with:

> Pretrained model weights will be released soon.

---

## 🧪 Reproducibility

For reproducible experiments, we recommend recording:

* Python version
* PyTorch version
* CUDA version
* GPU model
* Dataset split
* Input resolution
* Batch size
* Learning rate
* Number of epochs
* Optimizer
* Learning-rate scheduler
* Random seed

Example environment:

```text
Python: 3.10
PyTorch: X.X.X
CUDA: XX.X
GPU: NVIDIA XXXXX
Input Size: XXX × XXX
Batch Size: XX
Learning Rate: X.Xe-X
Epochs: XXX
```

---

## 📚 Citation

If you use this implementation in your research, please cite the original DCANet paper:

```bibtex
@article{muhammad2023dcanet,
  title={DCANet: deep context attention network for automatic polyp segmentation},
  author={Muhammad, Zaka-Ud-Din and Huang, Zhangjin and Gu, Naijie and Muhammad, Usman},
  journal={The Visual Computer},
  volume={39},
  number={11},
  pages={5513--5525},
  year={2023},
  publisher={Springer}
}
```

### Paper

**Muhammad, Z.-U.-D., Huang, Z., Gu, N., & Muhammad, U. (2023).**
*DCANet: deep context attention network for automatic polyp segmentation.*
The Visual Computer, 39(11), 5513–5525.

---

## 🙏 Acknowledgements

We thank the authors of the original DCANet paper and the researchers who developed and publicly released the datasets used for automatic polyp segmentation research.

This repository is intended for **research and educational purposes**.

---

## 📄 License

Please specify the license under which this implementation is released.

For example:

```text
MIT License
```

See `LICENSE` for more information.

---

## ⚠️ Disclaimer

This project is intended for research purposes only. It is **not a medical device** and should not be used for clinical diagnosis or treatment decisions.

---

## 📬 Contact

If you have questions, suggestions, or issues regarding this implementation, please open a GitHub issue or contact the repository maintainer.


