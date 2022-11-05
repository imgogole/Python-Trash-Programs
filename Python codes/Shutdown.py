# Shutdown
# Function that shutdowns your PC. Absolutly not useful, instead of trolling your friends (I have no friend so I never used it :c)

import os
import time
  
shutdown = input("How many time ? : ")

time.sleep(int(shutdown))
  
os.system("shutdown /s /t 1")
