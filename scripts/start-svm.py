import os
num_of_nodes = 5
cmd = ""
port = 13800
master_port = 32800
for i in range(0, num_of_nodes):
    cmd = cmd + "ssh 1155086998@proj" + str(10 - i) + " "
    cmd = cmd + "/data/opt/tmp/1155086998/pms/build/./TestSVM " + \
        str(10 - i) + " " + str(num_of_nodes) + " " + \
        str(port) + " " + str(master_port + i) + "&"
    print cmd
    os.system(cmd)
    cmd = ""
while (True):
    pass
# print cmd
