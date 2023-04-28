import os
a  = os.popen("termux-sensor -s LSM -n 20 -d 100").read()

print(a)