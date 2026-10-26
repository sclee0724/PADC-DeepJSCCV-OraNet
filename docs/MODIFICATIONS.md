# Modifications relative to the authors' upstream implementation

> **Scope and provenance.** The actual `Encoder`, `Decoder`, residual/attention blocks, GDN and `OracleNet` modules are derived from / imported from the [authors' upstream source](https://github.com/wyzhang-ustb/Predictive-and-Adaptive-Deep-Coding-for-Wireless-Image-Transmission-in-Semantic-Communication), reference commit `2b5fae05f1194189a97e478be21be1e2ae6d4c18`. This document describes *Colab pipeline adaptations* and implementation differences. Do not mistake a rewritten wrapper for an author's released experimental artifact.

| Component | Adaptation / reason | Reproduction implication |
|---|---|---|
| Execution environment | Google Colab + Google Drive persistence, dynamic upstream fetch, dependency setup | Environment differs from original author's machine; record package versions |
| Model architectures | Use the upstream Encoder / Decoder / GDN / OraNet architectures; do **not** publish duplicate vendored files here | Network blocks retain author provenance |
| Attention tensor handling | Adjust shape/batch-1 compatibility where needed | Numerical behavior should be tested against upstream for normal batch sizes |
| Channel simulation | AWGN sampling uses per-image independent noise; repository-style fading is exposed as `repo_fading` | **Not byte-exact** to upstream noise draws, and `repo_fading` is not independently verified as the original paper's slow Rayleigh law |
| CR / mask semantics | Explicit physical CR `R=K/(3HW)` vs upstream code's internal `cr` argument, including 48-channel quantization | Interpret nominal rates and realized effective CR separately, especially at Kodak resolutions |
| ImageNet | Support Hugging Face `validation-*.parquet` shards; crop RGB128, deterministic 45k/5k split, local/Drive cache | Data source format differs; confirm selection and crop order in metadata |
| Kodak image loading | Recognize `kodim01..24.png`; optional validation/recovery | Avoid accidental partial 23-image evaluation |
| OraNet training | Support online teacher supervision using trained DeepJSCC-V, separate checkpoints | Teacher labels depend on channel draws, selected JSCC checkpoint and sampling seed |
| Checkpoints | Save `last` / `best` files and training histories per dataset and channel | `last` for resume, `best` for evaluation; do not mix JSCC and OraNet pairs |
| Evaluation | CSV grids and plots for CIFAR100/Kodak24, CR selectors and reproducibility metadata | Some older CIFAR grid caches may not track OraNet SHA; refresh after weights change |
| Additional figures | PADC-only reproductions / diagnostics of the paper's plots | Excluding external baselines changes experimental claims; label *-like* figures honestly |
| Oracle output initialization | Bias/initialization adjustment in notebook if present | Initialization differs from default upstream; does not alter RFCB topology |

## Why this matters

1. A trained OraNet is **specific** to the DeepJSCC-V model, dataset training stage and channel mode used to generate its supervised PSNR labels. Do not mix those checkpoints.
2. The original paper used ImageNet 128×128 training for Kodak24; the CIFAR-only model should not be presented as its Kodak result.
3. The paper's data-level optimizer and the supplementary *instance-level* optimizer solve different decision problems; do not conflate Fig. 5-style curves with per-image CR predictions.
4. PSNR prediction MSE/MAE is distinct from feasible-target success; reporting a low prediction error alone does not prove a quality guarantee.
5. `repo_fading` is the **notebook's implementation-mode label**. Paper-level Rayleigh equivalence needs a separate channel-law check, including gain distribution, normalization and receiver assumptions.

## Pending or not fully audited

- Bit-exact numerical equivalence of the edited AWGN/fading forward pass to the authors' PyTorch implementation.
- Checkpoint-to-CSV provenance for all previously cached CIFAR OraNet predictions (some older cache keys do not include OraNet checkpoint SHA).
- The one-channel Kodak analysis in Fig. 9, which differs from paper PSNR values.
- Exact fixed-CR ADJSCC and BPG+LDPC comparative results from the paper.

See [`LIMITATIONS.md`](LIMITATIONS.md) for more detail.
