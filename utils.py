import json 


# usage: host, port,_ = utils.get_config()
def get_config():
    
    with open('config.json', 'r') as f:
        config = json.load(f)
        host = config['host_ip']
        port = int(config['host_port'])
        flag = config['flag']
        root_dir = config['root_dir'] 

    return host, port, root_dir,flag
