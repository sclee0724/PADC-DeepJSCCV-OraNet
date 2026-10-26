# GitHub 업로드 가이드 (PADC Colab Reproduction)

## 업로드 파일의 역할

- `README.md`: 저장소 표지 및 논문/원저자 크레딧, 실험 요약, Hugging Face 링크
- `notebooks/`: AWGN, fading 학습/평가와 CIFAR 재검증 노트북
- `results/`: 대표 PNG 그래프와 요약 JSON (원시 80만 행 CSV는 별도 보관)
- `docs/MODIFICATIONS.md`: 원본 대비 코드 변경점
- `docs/FIGURE_STATUS.md`: Fig.별 재현 여부와 한계
- `checkpoints/README.md`: Hugging Face `.pt` 파일의 구성, 쌍, 다운로드 예시
- `.gitignore`: 불필요한 체크포인트/데이터/로그/비밀정보의 Git 업로드 방지

## 1. GitHub에서 비어 있는 저장소 생성

1. https://github.com/new 에 로그인
2. Repository name: `PADC-DeepJSCCV-OraNet-Colab`
3. Description: `Unofficial Google Colab reproduction of PADC (IEEE TWC 2023)`
4. 처음에는 **Private** 추천 (출처·권리·링크 확인 후 Public)
5. **Add a README / Add .gitignore / Choose a license** 모두 선택하지 않기 (패키지에 README와 .gitignore가 이미 있음)
6. **Create repository**

## 2-A. GitHub 웹 브라우저로 업로드 (처음 사용하기 쉬운 방법)

1. 제공된 ZIP을 로컬 PC에 **압축 해제**하기. ZIP 단일 파일만 업로드하지 않기.
2. GitHub 새 저장소 화면에서 **uploading an existing file** 또는 `Add file > Upload files` 열기.
3. 압축 해제한 `PADC-GitHub-Publish-With-HF/` **폴더의 내용물**(`README.md`, `README_KO.md`, `notebooks/`, `docs/`, `results/`, `.gitignore` 등)을 드래그하여 업로드. 상위 폴더 한 겹이 새로 만들어지지 않도록 확인하기.
4. 업로드 미리보기에서 `README.md`가 **저장소 최상위**에 있고 `notebooks/`가 폴더로 나타나는지 확인하기. (웹 업로드에서 숨김 파일 `.gitignore`가 누락되었으면 나중에 추가.)
5. `Commit message`에 `Initial PADC Colab reproduction` 입력 후 커밋.

브라우저 업로드는 파일당 25 MiB/한 번에 100파일 제한이 있지만, 이 패키지는 50개 이내이며 개별 파일 용량도 해당 제한 아래임. *Google Drive의 146MB 가중치는 여기에 올리지 않음.*

## 2-B. Git Bash 또는 WSL로 올리기 (갱신이 잦으면 권장)

압축을 해제한 폴더로 이동한 다음 다음 명령을 실행. `YOUR_GITHUB_ID`는 **GitHub 사용자 이름** (Hugging Face 사용자명과 같을 필요 없음).

```bash
cd PADC-GitHub-Publish-With-HF
git init
git branch -M main
git add .
git status
git commit -m "Initial PADC Colab reproduction"
git remote add origin https://github.com/YOUR_GITHUB_ID/PADC-DeepJSCCV-OraNet-Colab.git
git push -u origin main
```

`git commit`에 사용자 정보가 없다고 나오면 `git config --global user.name "YOUR_NAME"`와 `git config --global user.email "YOUR_EMAIL"`을 먼저 실행. 푸시 인증은 GitHub 웹/credential manager/PAT 등의 지원 방식으로 진행하며 비밀번호나 토큰을 코드에 입력하거나 커밋하지 않기.

## 3. Hugging Face 가중치 링크 연결

현재 README와 `checkpoints/README.md`에는 아래 **예상 URL**을 넣어둠:

`https://huggingface.co/sclee0724/PADC-DeepJSCCV-OraNet-Reproduction`

- Hugging Face에서 자신이 실제로 만든 모델 저장소의 주소를 복사하고 위와 같은지 확인.
- `Files and versions`에서 `awgn/`과 `repo_fading/` 폴더의 `.pt` 8개가 업로드되어 있는지 확인. 파일명이 다르면 `checkpoints/README.md`도 바꿀 것.
- 공개 GitHub에서 다른 사람이 다운로드하려면 HF 모델 저장소도 Public이어야 함.
- 실제 URL이 다르면 `README.md`, `README_KO.md`, `checkpoints/README.md`의 URL을 바꾸고 커밋.
- `best.pt`는 추론/평가용, `last.pt`는 학습 재개용. 원본 노트북이 평가-only 노트북인 것은 아니므로 가중치만 받으면 'Run all'로 평가만 되는 것처럼 설명하지 않기.

## 4. GitHub 공개 전 마지막 확인

- 실제 HF URL 및 public visibility 확인
- README에서 논문 저자와 원저자 GitHub 명확히 인용
- 공개 권리를 확인하지 않은 원저자 원본 소스·이미지 데이터·학습 체크포인트 무단 배포 피하기
- Colab 인증 토큰, API 키, 개인 경로 또는 메타데이터가 포함되어 있지 않은지 확인
- `Fig. 9` 단일 채널 ablation의 불일치와 `repo_fading`의 원 논문 slow Rayleigh와의 차이를 `docs/LIMITATIONS.md`에 명확히 표기
- 저장소를 Public으로 전환한 후 시크릿이 과거 커밋에 남지 않았는지 확인

**참고:** 이 ZIP만으로 별도 HF 모델 저장소를 생성/공개하거나 GitHub 저장소에 자동 푸시되지는 않음.
