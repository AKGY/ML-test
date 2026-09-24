import multiprocessing as mp
import os
import time

TOTAL = 10_000_000_000_000   # 총 루프 실행 횟수 -10조번
CHUNK = 1_000_000_000          # cpu쓰레드당 10억 번씩 처리


def loop_100m(count):
    #count번 루프 실행
    for i in range(count):
        pass

    return count


if __name__ == "__main__":
    workers = os.cpu_count()

    full_chunks = TOTAL // CHUNK
    
    jobs = [CHUNK] * full_chunks
 

    start_time = time.time()

    completed = 0

    with mp.Pool(processes=workers) as pool:

        for finished in pool.imap_unordered(loop_100m, jobs, chunksize=1):
            completed += finished

            print(f"{completed:,}번째 루프가 실행되었습니다.")

    end_time = time.time()

    print(f"\n총 반복 횟수: {completed:,}")
    print(f"걸린 시간: {end_time - start_time:.3f}초")