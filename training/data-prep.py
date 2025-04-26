import sys
from sklearn.model_selection import train_test_split
import os
import shutil
from tqdm import tqdm
from glob import glob

#%%

RAW_DATA_PATH = os.path.normpath('training/data/dataset')
DATA_PATH = os.path.normpath('training/data')
DATA_DIR_NAME = 'digit'

TEST_SIZE = 0.2

dataset_path = os.path.join(DATA_PATH, DATA_DIR_NAME)


def create_dir(dir_path):
    '''
    Create train/test Directories. 
    '''
    try:
        os.makedirs(dir_path)
        
    except Exception as e:
        print(f'Error occured during creating new directory: {e}')
    
    
    
def copy_images(images_path_list, dir_path):
    '''
    Create train/test directories and copying images to them.
    '''
    create_dir(dir_path)
    
    for image in images_path_list:
        shutil.copy(image, dir_path)
        
    
#  Check if dataset_path exists and taken action.
if os.path.exists(dataset_path):
    
    action = None
    while True:
        try:
            action = int(input(f'''
                   
Directory "{dataset_path}" arleady exists.
          
Select an action below:
1. Replace Directory "{dataset_path}".
2. Create Sufix name Directory (e.g. "{dataset_path}_1")
3. Pass the process.
                  
'''))
        except Exception as e:
            print(f'Error {e} occured. Please select number from 1 to 3.')
        print()
        
        # Replacing exist directory
        if action == 1:
            print(f'Replacing "{dataset_path}" Directory.')
            shutil.rmtree(dataset_path)
            break
        
        # Create sufix
        elif action == 2:
            sufix = '_'
            dataset_dir_list = [x for x in os.listdir(DATA_PATH) if (x[: x.find(sufix)] == DATA_DIR_NAME)
                                and (x[x.find(sufix)+1:].isdigit())]
            if dataset_dir_list:
                dataset_dir_list_index = [int(x[x.find(sufix)+1:]) for x in dataset_dir_list]
                dir_index = str(max(dataset_dir_list_index)+1)
    
            else:
                dir_index = '1'
            
            dataset_path = os.path.join(DATA_PATH, DATA_DIR_NAME + sufix + dir_index)
            print(f'Directory "{dataset_path}" has been created.')
            break
        
        # Passing the copying
        elif action == 3:
            print('Exitinng.')
            sys.exit()
        
        # Wrong user input
        else:
            print('Please select number from 1 to 3.')
     
    
# Iterate per classes
for img_class in tqdm(os.listdir(RAW_DATA_PATH)):
    
    # Get the imges paths into list and shuffle
    img_class_path = os.path.join(RAW_DATA_PATH, img_class)
    img_path_list = glob(os.path.join(img_class_path, '**', '*.png'))

    # Prepare test and train image paths list
    train_img_paths, test_img_paths = train_test_split(img_path_list, test_size=TEST_SIZE, shuffle=True)
    
    # Copying images train and test directory
    test_dir = os.path.join(dataset_path, 'test', img_class)
    train_dir = os.path.join(dataset_path, 'train', img_class)
    
    copy_images(train_img_paths, train_dir)
    copy_images(test_img_paths, test_dir)
    
    

