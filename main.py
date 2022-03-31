import itertools
import threading
import time
import sys
import os

#Loading screen animation
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

i=0
while i<10000000:
  i=i+1

done = True
os.system('cls' if os.name == 'nt' else 'clear')

print("done")