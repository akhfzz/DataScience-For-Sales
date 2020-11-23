import numpy as np
mylist = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])
strc = lambda x: x[:,1]
print(strc(mylist))

transaction = np.array([[101,1000,2],
                [102,1500,4],
                [103,1750,1],
                [104,1650,5]
                ])
step = lambda x: x[:,1] * x[:,2]
gabung = np.insert(transaction,3,[step(transaction)],axis=1)
print(gabung)