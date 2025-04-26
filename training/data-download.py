import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('jcprogjava/handwritten-digits-dataset-not-in-mnist', path='training/data', unzip=True)