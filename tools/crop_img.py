import os
import cv2
from tqdm import tqdm
#original test set path
rootDir="/data/XCZ/baidu/test"
# new test set path
save_dir="/data/XCZ/baidu/test_crop"
filenames=os.listdir(rootDir)
filenames.sort(key=str.lower)
for filename in tqdm(filenames):
    img_path=os.path.join(rootDir,filename)
    im=cv2.imread(img_path)
    im=im[1500:,:,:]
    cv2.imwrite(os.path.join(save_dir,filename),im)
