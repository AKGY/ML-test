import time

start_time=time.time()

for i in range (100_000_000_000_0):
    if i% 1000 == 0:
        print(f"{i}번째 루프를 실행중입니다.")

end_time = time.time()

print(f"1조번 루프를 도는데 걸리는 시간 : {end_time - start_time} 초")

