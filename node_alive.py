import subprocess

def ping(hostname):
    p = subprocess.Popen('ping ' + hostname + ' -n 1', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    pingStatus = 0;

    for line in p.stdout:
        output = line.rstrip().decode('UTF-8')

        if (output.endswith('unreachable.')):
            pingStatus = 1
            break
    return pingStatus


activehosts=[]

for i in range(180,190):
    ip="192.168.42."+str(i)
    status=ping(ip)
    if status==0 :
        activehosts.append(ip)
        print(ip+"is an active host")
    else:
        print(ip+"is a dead host")

print("total hosts that are active="+str(len(activehosts)))

print(activehosts)