# Limitations / not yet independently validated

- **AWGN and `repo_fading` are two run labels, not interchangeable models.** `repo_fading` follows the selected notebook implementation; exact equivalence with the paper's slow-Rayleigh channel requires an explicit channel-law audit.
- The result-archive manifests summarize preexisting runs; this starter package has not rerun 400+150 and 50+150 epoch training.
- Fig. 4/5 comparisons to independently trained ADJSCC were not included in the attached results. BPG+LDPC end-to-end baseline in Fig. 8 is also absent. Do not market those baseline comparisons as reproduced.
- Additional PADC-only Fig. 9 single-channel ablation was experimentally mismatched to the reported paper values. It is placed under `results/awgn/analysis_only/` instead of promoted as a verified reproduction.
- CIFAR benchmark tables contain one channel realization per image/rate/SNR in the provided manifests; Kodak uses 100 Monte Carlo repeats. These are different estimators and should be described separately.
- Full grid `cifar100_test_grid.csv` caches may have only JSCC checkpoint hashes, not OraNet hashes. Before assessing a **retrained** OraNet, regenerate predictions or perform a weight-hash and spot-check audit. Without this, stale cached PSNR predictions are possible.
- Mean target-constraint satisfaction reported over all targets includes cases infeasible at the maximum allowed CR. Report feasible-only satisfaction separately when making quality-control claims.
- Each figure may be a PADC-only counterpart of a figure whose original purpose was an external-baseline comparison; label these as *-like* and describe the omitted baselines.
- No datasets or checkpoints were supplied for packaging; weights must be added separately after right-to-distribute and provenance checks.
