import numpy as np

floder = './weight/'

weightbias = {}
for key, value in model_params.items():
    # print(key, value)
    if 'weight' in key or 'bias' in key:
        weightbias[key] = value.cpu().numpy()

# print(weightbias)
for key, value in weightbias.items():
    print(key, value.size)
    np.savetxt(floder+key+'.txt', value)
    