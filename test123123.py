import time
time.sleep(1)
tic = time.perf_counter()
time.sleep(2)
tac = time.perf_counter()

print(tic)
print(tac - tic)