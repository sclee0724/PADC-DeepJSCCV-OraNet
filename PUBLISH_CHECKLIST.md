# Publishing checklist

- [ ] Read the [original PADC paper](https://doi.org/10.1109/TWC.2023.3234408) and [upstream code](https://github.com/wyzhang-ustb/Predictive-and-Adaptive-Deep-Coding-for-Wireless-Image-Transmission-in-Semantic-Communication).
- [ ] Verify your legal right to redistribute adapted upstream code and *trained model weights*. The main notebooks fetch the upstream source; original authors' network files are **not** republished here.
- [ ] Run `python scripts/verify_repository.py`; verify no tokens, credentials, private user paths or raw dataset images are committed.
- [ ] Confirm the channel mode and output directory in each notebook's first **EDIT ME** cell, especially `CHANNEL`, `RUN_FOLDER`, `PROFILE`, and data paths.
- [ ] Confirm pinned upstream SHA in the notebook's setup/metadata.
- [ ] Keep `results/*/figures/*.png` and `metrics_summary.json` in Git; exclude full `*grid.csv` files and large ZIPs from Git history.
- [ ] Optionally upload full run ZIPs to GitHub Releases, after reviewing contents and redistribution terms.
- [ ] Upload AWGN/fading × CIFAR10/ImageNet128 × JSCC/OraNet `*_best.pt` as eight identified weights to Hugging Face; verify SHA256 from `scripts/collect_checkpoints.py`.
- [ ] Insert **verified** Hugging Face model URL and GitHub repository URL into README once actually created.
- [ ] Update Model Card with provenance, source code note, and each checkpoint's associated channel and dataset.
- [ ] Before describing a download-and-evaluate workflow as working, independently verify it in a fresh Colab runtime. The provided 01/02 notebooks are full training pipelines, **not** dedicated weights-only evaluation notebooks.
- [ ] Name partial Figure results honestly (PADC-only Fig. 4/5, unverified Fig. 9, Fig. 8 baseline absent) and document `repo_fading` limitations.
- [ ] Cite the original IEEE TWC work prominently and do not imply endorsement.
- [ ] For public licensing, do not put an arbitrary MIT/Apache license over upstream code you do not own. Specify rights for your own contribution only after review.

- [ ] Verify Hugging Face URL and whether it is Public: https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction
- [ ] Review `GITHUB_UPLOAD_GUIDE_KO.md` and GitHub repo visibility.
