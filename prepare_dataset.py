import pandas as pd
import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
IMAGE_DIR = "HAM10000_images"
CSV_PATH = "HAM10000_metadata.csv"
OUTPUT_DIR = "dataset"

df = pd.read_csv(CSV_PATH)

# Label mapping
malignant = ['mel', 'bcc', 'akiec']
df['label'] = df['dx'].apply(lambda x: 'malignant' if x in malignant else 'benign')

train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    stratify=df['label'],
    random_state=42
)

def copy_images(dataframe, split):
    for _, row in dataframe.iterrows():
        src = os.path.join(IMAGE_DIR, row['image_id'] + ".jpg")
        dst = os.path.join(OUTPUT_DIR, split, row['label'])
        os.makedirs(dst, exist_ok=True)
        shutil.copy(src, dst)

copy_images(train_df, "train")
copy_images(val_df, "val")

print("Dataset prepared successfully.")
