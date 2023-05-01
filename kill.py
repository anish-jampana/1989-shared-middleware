import psutil
from subprocess import Popen

def get_pid_using_port(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return conn.pid
    return None

ports = [5000, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008]
for port in ports: 
    pid = str(get_pid_using_port(port))
    print(pid)
    p = Popen(["kill","-9", pid])