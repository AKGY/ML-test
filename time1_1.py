import sys
import time

TOTAL = 1_000_000_000_000
CHUNK = 10_000

start_time = time.time()

for start in range(0, TOTAL, CHUNK):

    end = min(start + CHUNK, TOTAL)

    output = "".join(
        f"{i}번째 루프를 실행중입니다.\n"
        for i in range(start, end)
    )

    sys.stdout.write(output)

sys.stdout.flush()

end_time = time.time()

print(f"걸린 시간: {end_time - start_time}초")