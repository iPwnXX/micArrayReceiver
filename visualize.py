
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")
channel_num = 8
data_cache = [[] for i in range(channel_num)]
root_dir = 'dataset/test_channels/block1_B/'
print('current: ',root_dir)
for i in range(8):
    offset = 8
    data = np.loadtxt(root_dir+'ch%d.txt'%(i+offset))
    data.astype('float')
    data_cache[i] = data
    plt.subplot(4,2,i+1)
    plt.plot(data)
    print('channel %i, max %.2f' %(i+offset, max(data)))

plt.show()
# plt.savefig('multi_channel.png',dpi=300)