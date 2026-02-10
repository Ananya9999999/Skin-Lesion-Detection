import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

IMG_DIR_1 = "HAM10000_images_part_1"
IMG_DIR_2 = "HAM10000_images_part_2"
CSV_PATH = "HAM10000_metadata.csv"
OUT_DIR = "data"

df = pd.read_csv(CSV_PATH)

# Binary labels
df["label"] = df["dx"].apply(lambda x: "malignant" if x == "mel" else "benign")

train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    stratify=df["label"],
    random_state=42
)

def find_image(image_id):
    img_name = image_id + ".jpg"
    path1 = os.path.join(IMG_DIR_1, img_name)
    path2 = os.path.join(IMG_DIR_2, img_name)

    if os.path.exists(path1):
        return path1
    if os.path.exists(path2):
        return path2
    return None

for split, split_df in [("train", train_df), ("val", val_df)]:
    for label in ["benign", "malignant"]:
        os.makedirs(os.path.join(OUT_DIR, split, label), exist_ok=True)

    for _, row in split_df.iterrows():
        src = find_image(row["image_id"])
        if src is None:
            print("⚠️ Missing image:", row["image_id"])
            continue

        dst = os.path.join(
            OUT_DIR,
            split,
            row["label"],
            row["image_id"] + ".jpg"
        )
        shutil.copy(src, dst)

print("✅ Dataset prepared successfully")
