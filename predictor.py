import os
import torch

import elnet
import numpy as np

def check(input_img):
    
    print(" your image is : " + input_img)
   
    input_img1=f'../app/images/{input_img}'
    img = np.load(input_img1)
    img=img/255
    img=torch.Tensor(img)
    img=img.repeat(1,1,1,1)
    print(img.size())
    l=['Abnormal','Meniscus','ACL']
    model_path=[]
    elNet=[]
    output=[]
    probas=[]
    label={}
    model_name = ['model_patience_5 _gamma_2n_abnormal_axial_val_auc_0.8636_train_auc_0.9016_epoch_39.pth','model_patience_5 _gamma_2n_meniscus_axial_val_auc_0.7322_train_auc_0.7526_epoch_22.pth',
                     'model_gamma_0.9_acl_axial_val_auc_0.8698_train_auc_0.8795_epoch_27.pth'   ]     
    for i in range(0,3):
        model_name1=model_name[i]
        m = f'../app/models/{model_name1}'
        model_path.append(m)
        elNet.append(torch.load(model_path[i],map_location='cpu'))
        _ = elNet[i].eval()
        x=elNet[i].forward(img.float())
        output.append(x)
        y=torch.sigmoid(x)
        probas.append(y)
        #label[l[i]]=(probas[i][0][1].item())
        if probas[i][0][1].item()>0.5:
            label[l[i]]=('Present')
        else:
            label[l[i]]=('Not Present')


        #print(probas)
            #print(probas[0][1][1].item()
    print(label)        
    return label




#check('images/1136.npy')