# %%
import os

# %%
os.listdir("./data")

# %%
from tqdm.auto import tqdm

directory = "./data"

train_out = "train.csv"
test_out = "test.csv"
unsup_out = "unsup.csv"

for filename in os.listdir(directory):
    if filename in ["train", "test"]:
        is_train = filename == "train"
        with open(train_out if is_train else test_out, "w") as out_f:
            out_f.write("id,text,rating,label\n")
            for claz in ["neg", "pos"]:
                data_dir = os.path.join(directory, filename, claz)
                obs_label = "0" if claz == "neg" else "1"
                for obs_filename in tqdm(os.listdir(data_dir)):
                    obs_id, obs_rating = obs_filename.split(".")[0].split("_")
                    obs_text = open(os.path.join(data_dir, obs_filename)).readline().replace(",", " | ")
                    out_f.write(",".join([obs_id, obs_text, obs_rating, obs_label]) + "\n")


