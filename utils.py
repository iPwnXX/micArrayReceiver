import json 
import numpy as np
# import matplotlib.pyplot as plt

# usage: host, port,_ = utils.get_config()
def get_config():
    
    with open('config.json', 'r') as f:
        config = json.load(f)
        host = config['host_ip']
        port = int(config['host_port'])
        root_dir = config['root_dir'] 
        read_time_duration = int(config['read_time_duration'] )
        flag = config['flag']

    return host, port, root_dir,read_time_duration,flag
