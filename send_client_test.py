import socket
import utils
import time

""" UDP往server端发送采集数据， 测试使用。
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host, port, root_dir, *_ = utils.get_config()

f_name = 'rawdata.txt'
client_addr = (host, port)

count = 0
start_time = time.time()
root_dir += 'block1_A/'
with open(root_dir+f_name,'rb') as f:
    
    while True:
        data = f.read(2000)
        if str(data) != "b''":
            s.sendto(data, client_addr)
            print(count)
            if not count%50:
                time.sleep(0.01)
        else:
            break
        count += 1   

    print('send count: %d. time taken: %f' %(count,time.time() - start_time))
    s.close()