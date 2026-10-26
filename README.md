# PADC: DeepJSCC-V & OraNet Reproduction

Unofficial PyTorch reproduction of **"Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication"** (*IEEE Transactions on Wireless Communications*, 2023).

This repository contains training and evaluation notebooks for **DeepJSCC-V** and **OraNet**, covering PSNR prediction and adaptive compression-ratio (CR) selection under AWGN and fading channels.

[**Paper**](https://doi.org/10.1109/TWC.2023.3234408) · [**Original implementation**](https://github.com/wyzhang-ustb/Predictive-and-Adaptive-Deep-Coding-for-Wireless-Image-Transmission-in-Semantic-Communication) · [**Pretrained weights**](https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction) · [**한국어 README**](README_KO.md)

## Structure of this repository

The following notebooks provide the main experiments:

- **[`01_PADC_AWGN_Colab.ipynb`](notebooks/01_PADC_AWGN_Colab.ipynb)** — DeepJSCC-V and OraNet training and evaluation over **AWGN**, including CIFAR, ImageNet fine-tuning, and Kodak24 experiments.
- **[`02_PADC_Fading_Colab.ipynb`](notebooks/02_PADC_Fading_Colab.ipynb)** — The corresponding experiments under the **`repo_fading`** channel implementation, using separate models and checkpoints.
- **[`03_CIFAR_Reaudit.ipynb`](notebooks/03_CIFAR_Reaudit.ipynb)** — CIFAR100 OraNet prediction and CR-selection analysis using saved evaluation results; **no retraining required**.

Additional resources:

- **[`results/`](results/)** — Experimental figures and evaluation summaries for AWGN and fading.
- **[`checkpoints/`](checkpoints/README.md)** — Pretrained-weight links and checkpoint descriptions.
- **[`docs/MODIFICATIONS.md`](docs/MODIFICATIONS.md)** — Changes relative to the authors' implementation.
- **[`docs/REPRODUCTION.md`](docs/REPRODUCTION.md)** — Dataset preparation and experiment settings.
- **[`docs/FIGURE_STATUS.md`](docs/FIGURE_STATUS.md)** — Correspondence between the reported figures and the original paper.

The original model architectures (`models.py`, `GDN.py`, and `OracleNet.py`) are loaded from the authors' repository by the notebooks rather than duplicated here.

## Experimental results

OraNet PSNR prediction errors from the saved experiments:

| Dataset / metric | AWGN | `repo_fading` |
|:--|--:|--:|
| CIFAR100 MAE (dB) | 0.550 | 0.612 |
| CIFAR100 MSE (dB²) | 0.586 | 0.688 |
| Kodak24 MAE (dB) | 0.377 | 0.288 |
| Kodak24 MSE (dB²) | 0.245 | 0.132 |

**CIFAR100 — OraNet prediction MSE (AWGN)**

![OraNet prediction MSE on CIFAR100](results/awgn/figures/CIFAR100_test_oranet_mse.png)

**Kodak24 — Actual vs. predicted PSNR (AWGN)**

![Actual and predicted Kodak24 PSNR](results/awgn/figures/Kodak24_test_psnr_vs_snr.png)

More plots are available in [`results/`](results/).

## Datasets

- **CIFAR-10 / CIFAR-100:** [Toronto dataset page](https://www.cs.toronto.edu/~kriz/cifar.html)
- **ImageNet-1K:** [ImageNet on Hugging Face](https://huggingface.co/datasets/ILSVRC/imagenet-1k)
- **Kodak24:** [Kodak Lossless True Color Image Suite](https://r0k.us/graphics/kodak/)

Dataset files are **not redistributed** in this repository. Obtain them from their respective sources and follow the applicable terms of use.

## Reproduction

1. Open the AWGN or fading notebook in a GPU-enabled Jupyter environment (Google Colab is supported).
2. Configure the dataset paths and choose `PROFILE='paper'` for the full training schedule.
3. Use a new `RUN_FOLDER` to train from scratch, or reuse an existing run folder to resume from its checkpoints.

See [`docs/REPRODUCTION.md`](docs/REPRODUCTION.md) for detailed instructions.

**Pretrained checkpoints:** [Hugging Face](https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction) · [Checkpoint guide](checkpoints/README.md)

## Notes

This reproduction is based on the authors' implementation, with adaptations for data loading, channel simulation, checkpoint management, and evaluation. See [`MODIFICATIONS.md`](docs/MODIFICATIONS.md) for details.

The repository focuses on the core PADC models and experiments; it does not include every comparison baseline from the paper. The `repo_fading` mode should not be assumed to be an independently verified exact slow-Rayleigh implementation. See [`FIGURE_STATUS.md`](docs/FIGURE_STATUS.md) and [`LIMITATIONS.md`](docs/LIMITATIONS.md).

## Reference

W. Zhang *et al.*, "Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication," *IEEE Transactions on Wireless Communications*, vol. 22, no. 8, 2023. [DOI: 10.1109/TWC.2023.3234408](https://doi.org/10.1109/TWC.2023.3234408).

This is an **unofficial reproduction**. Please cite the original paper and credit the [authors' implementation](https://github.com/wyzhang-ustb/Predictive-and-Adaptive-Deep-Coding-for-Wireless-Image-Transmission-in-Semantic-Communication).
