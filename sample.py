import ray
import rust_math  # Rust로 만든 확장 모듈

ray.init()

@ray.remote
def use_rust_double(x):
    return rust_math.double(x)

futures = [use_rust_double.remote(i) for i in range(10)]
results = ray.get(futures)

print(results)
# 출력 예시: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]