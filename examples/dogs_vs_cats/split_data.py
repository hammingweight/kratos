import os, shutil, pathlib

base_dir = pathlib.Path("PetImages")

def make_subset(subset_name, start_index, end_index):
    for category in ("Cat", "Dog"):
        dir = base_dir / subset_name / category
        os.makedirs(dir, exist_ok=True)
        #fnames = [f"{category}/{i}.jpg" for i in range(start_index, end_index)]
        for i in range(start_index, end_index):
            src_file = f"{base_dir}/{category}/{i}.jpg"
            print(src_file)
            dst_file = f"{dir}/{i}.jpg"
            shutil.move(src=src_file , dst=dst_file)

make_subset("train", start_index=0, end_index=10000)
make_subset("validation", start_index=10000, end_index=11250)
make_subset("test", start_index=11250, end_index=12500)
