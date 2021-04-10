import struct
import matplotlib.pyplot as plt
import numpy as np

""" read data saved from UDP and do Base conversion; visualize data amplitude of each channel.
"""

def transfer_and_plot(root_dir, WRITE_DATA=False):

    f_name = 'rawdata.txt'
    flag = '205a'
    b_flag = bytes.fromhex(flag)
    CH_MAX_NUM = 40
    cur_CH_Index = 0
    Valid_flag = True
    CH_cache = [[] for i in range(CH_MAX_NUM)]

    print('\nstart process...')
    with open(root_dir+f_name,'rb') as f:
        
        raw_data = f.read()

        if len(raw_data) == 0:
            Valid_flag = False
        
        else:
            itr = 0

            while itr < len(raw_data)-1:
                b_read = raw_data[itr:itr+2]
                
                if b_read == b_flag:

                    cur_CH_Index = 0

                else:
                    uncode_data = struct.unpack("<h",b_read)[0]
                    
                    transfered_data = uncode_data / 3276.8*10

                    CH_cache[cur_CH_Index].append(transfered_data)

                    cur_CH_Index += 1
                
                itr+=2

    # save transferred data in local.
    import numpy as np

    if WRITE_DATA:

        print('transfer finished\nstart writing files...')
        for ch_index in range(cur_CH_Index):

                f_name = root_dir+"ch%d.txt"%(ch_index)

                saved_data = np.array(CH_cache[ch_index])
                np.savetxt(f_name,saved_data,fmt='%.3f')

    # plot / visualize data.
    if not Valid_flag:
        print('\nno data received.')
    else:
        print('start visualizing...')
        plt.style.use("ggplot")
        
        for offset in [8*i for i in range(5)]: 
            fig, axs = plt.subplots(4, 2)
            fig.suptitle('channels from %d to %d (left column: amplified)'\
                %(offset//2+1,(offset + 8)//2))
            for i in range(8):
                index = i+offset
                if len(CH_cache[index]) == 0:
                    print('channel %d has no data.' %(i + offset))
                    break
                data = np.array(CH_cache[index]).astype('float')
                axs[i//2, i%2].plot(data)
                print('channel %i, max %.2f' %(index, max(data)))
        plt.show()           


if __name__ == "__main__":
    
    root_dir = 'dataset/test_channels/'
    transfer_and_plot(root_dir)