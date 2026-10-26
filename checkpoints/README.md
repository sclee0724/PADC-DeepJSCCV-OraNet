# Model checkpoints (upload separately)

The supplied reproduction notebooks and result archives contained **no** `.pt` weights. The author's/reproducer's separately trained checkpoint files are stored in Google Drive and can be published to Hugging Face after verifying distribution rights.

**Expected Hugging Face model repo:** [sclee0724/PADC-DeepJSCCV-OraNet-Reproduction](https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction)

The repository ID and uploaded file inventory have **not** been independently verified. Replace this link if your actual model repo differs; keep the model repo Public if public GitHub users need to access it.

## Eight `best` files to publish (four per channel)

```
awgn/
  jscc_v_awgn_cifar10_best.pt
  oracle_awgn_cifar10_best.pt
  jscc_v_awgn_imagenet128_best.pt
  oracle_awgn_imagenet128_best.pt
repo_fading/
  jscc_v_repo_fading_cifar10_best.pt
  oracle_repo_fading_cifar10_best.pt
  jscc_v_repo_fading_imagenet128_best.pt
  oracle_repo_fading_imagenet128_best.pt
```

- The **CIFAR10 OraNet** should be evaluated with its **matching CIFAR10 JSCC** and the **same channel**.
- The **ImageNet OraNet** should be paired with the **matching ImageNet transfer JSCC**, not the CIFAR10 JSCC. The embedded `teacher_sha` in the checkpoint should match the trained JSCC checkpoint's SHA-256.
- `*_best.pt` should be the evaluation weights. `*_last.pt` contains optimizer state and is needed for the **training-resume** path; distributing it is optional and often wasteful for inference users.
- In the supplied full notebook, ImageNet training/resume is executed when `RUN_IMAGENET_FINETUNE=True`, even if only the `*_best.pt` files are present. Users need a separately verified evaluation-only entrypoint or an explicit training-skip branch. Do not promise instant pretrained evaluation using only the current `Run All` path.

## Prepare files from Google Drive

Once you have the original weights, run the provided `scripts/collect_checkpoints.py` (e.g., in the Colab runtime) to copy them into an asset staging folder without modifying your originals and produce SHA-256 manifests.

```bash
python scripts/collect_checkpoints.py \
  --run-root /content/drive/MyDrive/PADC_reproduction_CIFAR_fresh_20261022_v1 \
  --out /content/PADC_release_weights
```

**Full model checkpoint safety:** `.pt` training checkpoints are serialized with PyTorch. Do not load arbitrary untrusted checkpoints; hash and verify all files before use. Your own checkpoint is safe to read when you know its provenance.

## GitHub Releases vs Hugging Face

- **GitHub Releases**: appropriate if individual assets are under GitHub's release-asset size limit and you want a single downloadable version with code. Attach models as distinct `awgn_*` and `repo_fading_*` files.
- **Hugging Face model repos**: good for larger weights, versioning and model cards. Prefer **separate model repos/variants** for AWGN vs fading and CIFAR vs ImageNet, or provide clear directories within a collection. Link each weight to its matching GitHub code revision and evaluation summary.
- **Normal Git commits**: not recommended for `.pt` binary histories or raw 80–110 MiB CSV files. GitHub blocks >100 MiB regular Git objects.

Add actual URLs to root README after uploading.

## Download weights from Hugging Face

Once these files have been uploaded under the documented folder names, download a matching pair using the Hugging Face Hub client:

```python
from huggingface_hub import hf_hub_download

repo_id = "sclee0724/PADC-DeepJSCCV-OraNet-Reproduction"  # change if needed
jscc = hf_hub_download(repo_id, "awgn/jscc_v_awgn_cifar10_best.pt")
oracle = hf_hub_download(repo_id, "awgn/oracle_awgn_cifar10_best.pt")
print(jscc, oracle)
```

This only **downloads** the checkpoint files. Loading them requires the original model architecture and the appropriate checkpoint loading code; it is not a ready-made Transformers model. Only load trusted PyTorch checkpoint files. **File locations above assume the Hugging Face upload followed this directory layout.**

AWGN and `repo_fading` need separate JSCC/OraNet pairs, and CIFAR10 and ImageNet128 stages must not be crossed. Download instructions are not verified until a separate evaluate-only notebook is tested.
