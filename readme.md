# Overview

이 프로젝트는 Rust로 작성된 라이브러리를 maturin을 활용하여 python 패키지화해서 Ray에서 활용하는 예를 보여줍니다.

## 사전 요구사항

- Rust (최신 버전)
- Python 3.7 이상
- maturin (Rust-Python 바인딩을 위한 도구)
- Ray

## 설치 방법

1. maturin 설치:
```bash
pip install maturin
```

2. ray 설치 
 ```bash
pip install ray
```  

3. 프로젝트 빌드 및 설치:
```bash
# 프로젝트 루트 디렉토리에서
maturin develop
```

## 사용 방법
Python에서 다음과 같이 사용할 수 있습니다:

```python
from rust_math import double

# 숫자를 2배로 만드는 함수 사용
result = double(5)  # 결과: 10
```

## 실행 
1. 가상환경 설정
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
```
2. 실행 
```bash
python3 ./sample.py
```
3. 대시보드를 사용하여 현재 실행 상태 확인 가능 http://127.0.0.1:8265/#/jobs


## 프로젝트 구조

```
.
├── rust_math/          # Rust 라이브러리 소스 코드
│   └── src/
│       └── lib.rs      # Rust 구현 코드
├── tests/              # Python 테스트 코드
├── Cargo.toml          # Rust 의존성 관리
├── pyproject.toml      # Python 프로젝트 설정
└── requirements.txt    # Python 의존성 목록
```

