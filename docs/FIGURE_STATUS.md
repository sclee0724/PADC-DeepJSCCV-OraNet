# Figure mapping and reproduction status

This is an **experiment provenance matrix**, not a statement that every original figure is numerically identical to the paper. All screenshot/plot names below come from the uploaded experimental result artifacts when present.

| Paper figure | Published question | What is provided in this repo | Honest status |
|---|---|---|---|
| Fig. 4(a) | DeepJSCC-V vs four fixed-CR ADJSCCs, AWGN | [DeepJSCC-V-only PSNR curves](../results/awgn/padc_only_paper_figures/fig4_deepjscc_v_only.png) | **PADC-only**, ADJSCC curves absent |
| Fig. 5(a) | Data-level minimum CR vs ADJSCC, AWGN | [DeepJSCC-V-only CR curves](../results/awgn/padc_only_paper_figures/fig5_deepjscc_v_only.png) | **PADC-only** post-hoc data-level lookup; no ADJSCC |
| Fig. 6 | CWM, CWSTD and PSNR for three CIFAR100 images | [Three-image feature analysis](../results/awgn/padc_only_paper_figures/fig6_three_cifar100_examples.png) | Qualitative counterpart; example images/features are not the paper's exact triples |
| Fig. 7(a) | OraNet PSNR-prediction MSE on CIFAR100, AWGN | [AWGN MSE by SNR](../results/awgn/padc_only_paper_figures/fig7_oranet_mse_paper_rates.png) | Core trend reproduced; numerical matching/seed protocol requires caution |
| Fig. 8(a,b) | DeepJSCC-V vs BPG+802.11n LDPC in AWGN | No fully implemented BPG+LDPC baseline included | **Not reproduced** as a comparative experiment |
| Fig. 9 | Single latent SC channel reconstruction | Not promoted in published plots; older exploratory output disagreed | **Not verified / discrepancy** |
| Fig. 10 | Kodak images PSNR vs CR | [AWGN Kodak sample curves](../results/awgn/padc_only_paper_figures/fig10_kodak_three_images.png) | PADC-only qualitative subset, rate range differs |
| Fig. 11(a) | Kodak PSNR vs SNR, tested / OraNet-predicted | [AWGN Kodak PSNR curves](../results/awgn/figures/Kodak24_test_psnr_vs_snr.png) | Close in broad trend; use matched CR-specific MAE for strict paper comparison |
| Fig. 12(a,b) | Two Kodak reconstructions at 12 dB, R=1/8 | Example PSNRs documented in run; source-image collages excluded here | Reported close numerical examples; do not redistribute source image without rights check |
| Fig. 13(a,c) | Per-image tested vs predicted optimal CR | [kodim13](../results/awgn/padc_only_paper_figures/fig13_kodim13.png), [kodim23](../results/awgn/padc_only_paper_figures/fig13_kodim23.png) | PADC-only CR decision trends; no strict guarantee claimed |

`results/repo_fading` contains repository-style fading results and must not automatically be labeled as a validated paper slow-Rayleigh reproduction. Details: [`LIMITATIONS.md`](LIMITATIONS.md).
