# PADC: DeepJSCC-V 및 OraNet — Google Colab 재현

> W. Zhang 외, “Predictive and Adaptive Deep Coding for Wireless Image Transmission in Semantic Communication,” **IEEE TWC (2023)**. [논문 DOI](https://doi.org/10.1109/TWC.2023.3234408) · [원저자 GitHub](https://github.com/wyzhang-ustb/Predictive-and-Adaptive-Deep-Coding-for-Wireless-Image-Transmission-in-Semantic-Communication)

이 저장소는 **원저자 공식 저장소가 아닌 독립적인 Colab 재현 프로젝트**입니다. DeepJSCC-V·OraNet의 원저자 아키텍처를 실행 시 가져오고, 데이터셋·체크포인트·채널·평가·그래프 관리를 위한 노트북을 제공합니다.

## 노트북 구성

- [`01_PADC_AWGN_Colab.ipynb`](notebooks/01_PADC_AWGN_Colab.ipynb) — **AWGN** 학습·평가, CIFAR10 사전학습, ImageNet128 추가 학습 및 Kodak24 검증.
- [`02_PADC_Fading_Colab.ipynb`](notebooks/02_PADC_Fading_Colab.ipynb) — **`repo_fading`** 모드의 독립 학습·평가. 원논문의 slow Rayleigh 모델과 완전히 동일하다고 검증한 것은 아닙니다.
- [`03_CIFAR_Reaudit.ipynb`](notebooks/03_CIFAR_Reaudit.ipynb) — 기존 CSV로 CIFAR100 OraNet Fig. 7(a), Data-level CR과 feasible-only 평가를 분석하는 보조 노트북(재학습 없음).

## 데이터·결과·가중치

원본 CIFAR10·CIFAR100·Kodak24·ImageNet 데이터는 별도로 준비해야 합니다. `results/awgn`과 `results/repo_fading`에는 업로드된 실험에서 추출한 **실제 지표와 대표 그래프**가 있습니다. 체크포인트(`*_best.pt`)는 GitHub에 중복 보관하지 않고 Hugging Face에 공개하는 것을 권장하며, 저장소 주소 확정 후 [`checkpoints/README.md`](checkpoints/README.md)에 링크를 추가하세요.

| OraNet 예측 오류 | AWGN | `repo_fading` |
|---|---:|---:|
| CIFAR100 MAE | 0.550 dB | 0.612 dB |
| Kodak24 MAE | 0.377 dB | 0.288 dB |

위 값은 기존 실행의 `metrics_summary.json`에 근거하며, 본 GitHub 패키지 작성 시 모든 학습을 새로 실행한 값은 아닙니다.

## 코드 변경 및 재현 범위

**반드시 [`docs/MODIFICATIONS.md`](docs/MODIFICATIONS.md)를 확인하세요.** Colab 실행 환경, ImageNet Parquet 읽기, CR 변환, 채널 시뮬레이션, 체크포인트 재개, 평가 CSV 캐시 등이 원저자의 직접적인 스크립트 실행과 다릅니다. **모든 논문 Figure를 수치적으로 동일하게 재현했다고 주장하지 않습니다.** ADJSCC/BPG+LDPC 외부 비교군은 제외되어 있고, Fig. 9 단일 채널 분석은 아직 일치하지 않습니다.

실험 재현 과정은 [`docs/REPRODUCTION.md`](docs/REPRODUCTION.md), Figure별 상태는 [`docs/FIGURE_STATUS.md`](docs/FIGURE_STATUS.md), 저작권 및 인용은 [`docs/CITATION.md`](docs/CITATION.md)를 참고하세요.


## 사전학습 가중치 (Hugging Face)

- [PADC DeepJSCC-V / OraNet 가중치](https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction)
- [체크포인트 파일 및 다운로드 가이드](checkpoints/README.md)
- [GitHub 업로드 방법](GITHUB_UPLOAD_GUIDE_KO.md)

**주의:** 링크는 이전 단계에서 정한 모델 저장소 이름을 기준으로 넣었습니다. 실제 Hugging Face URL이 다르거나 비공개라면 공개 전에 변경해야 합니다.
