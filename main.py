import pandas as pd

# ==================================================SPLITTING THE TEXT==================================================
# open text file
# may need to edit and fix text file later to make less messy -Pedro
with open("First_Aid_Step1.txt", "r") as f:
    text = f.read()

# split text file into chunks
# current test size: 400 word chunks -Pedro
words = text.split()
chunks = [' '.join(words[i:i+400]) for i in range(0, len(words), 400)]

# convert chunks into a pandas dataframe
df = pd.DataFrame({"chunks": chunks})

# test chunk
print(df.chunks[110:118])

# NOTES FOR IMPROVEMENT =================================== -Pedro
# improve text version of textbook                        |
# maybe find way to always end sentences in same chunk?   |
# =========================================================
