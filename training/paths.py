from pathlib import Path

data_dir = Path('data')
images_dir = data_dir / 'prod_digit'

train_dir = Path(images_dir / "train")
test_dir = Path(images_dir / "test")

models_dir = 'models'
model_dir_prefix = 'model_'
results_filename = 'results.csv'
