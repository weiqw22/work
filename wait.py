"""
wait处理僵尸进程
"""

import os

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process",os.getpid())
    os._exit(5)
else:
    # pid,status = os.wait() #　等待处理僵尸
    pid, status = os.waitpid(-1,os.WNOHANG) #非阻塞
    print("pid:",pid)
    print("status:",os.WEXITSTATUS(status))
    while True:
        pass