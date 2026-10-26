# Reproduction notes

## Dependencies and runtime

The supplied run manifests reported **Python 3.13.16**, **PyTorch 2.11.0+cu130** and **NVIDIA RTX PRO 6000 Blackwell Server Edition**. This is provenance, not a guarantee that every later runtime will have identical package versions or hardware.

The notebook installs missing components including `pyarrow` where necessary, and uses NumPy, pandas, torchvision, matplotlib, tqdm and PIL. It clones the original author's repository pinned to commit `2b5fae05f1194189a97e478be21be1e2ae6d4c18`.

## Data expected in Colab

```
/content/drive/MyDrive/datasets/             # owned folder or shared shortcut
  cifar-10-batches-py/                        # or cifar-10-python.tar.gz
  cifar-100-python/                          # or cifar-100-python.tar.gz
  kodak24/kodim01.png ... kodim24.png
  imagenet-1k/data/validation-00000-of-00014.parquet ... validation-00013-of-00014.parquet
```

ImageNet's validation split is repartitioned 45,000/5,000 for transfer learning in the paper-style experiment. Labels are unused. The actual split seed, hashes and channel configurations are preserved in `results/<channel>/metrics_summary.json`.

## Training and evaluation

- `CHANNEL='awgn'` and `CHANNEL='repo_fading'` are **separate full training runs** with different weight checksums.
- CIFAR10 DeepJSCC-V: 400 epochs; CIFAR10 OraNet: 150 epochs; high-resolution transfer: 50 epochs; high-resolution OraNet: 150 epochs.
- Run `PROFILE='smoke'` only for functional testing; `PROFILE='paper'` is the long-run configuration.
- Preserve the mapping of each OraNet to the **specific JSCC weight hash and channel type** used for its PSNR labels. Do not cross-load an AWGN OraNet against a fading JSCC model.
- The current notebook's built-in ImageNet path calls training/resume; a best-only model release does **not** automatically make that stage evaluation-only.
- Reproduction figures for Fig. 8 BPG+LDPC and ADJSCC comparisons require additional actual baseline implementations, and not just labels copied from the paper.

## Model files from the Colab run

Each channel has these inference checkpoint names under `MyDrive/<RUN_FOLDER>/paper/<channel>/checkpoints/`:

```
jscc_v_<channel>_cifar10_best.pt
oracle_<channel>_cifar10_best.pt
jscc_v_<channel>_imagenet128_best.pt
oracle_<channel>_imagenet128_best.pt
```

Each source checkpoint contains a PyTorch `state_dict` plus training metadata and optimizer state. The original notebook's load functions check `channel` and/or `teacher_sha` to guard mismatches. See `checkpoints/README.md` for release instructions and SHA verification.

## Raw results

The original AWGN results archive is about 70.8 MiB compressed and contains ~397 MB uncompressed; `repo_fading` is about 64.3 MiB compressed and contains ~412 MB uncompressed. Large per-image CSV files are **deliberately not tracked** in the GitHub starter pack. Distribute the original archives as Release assets with the same names; this repository contains representative figures and the summary JSON only.
