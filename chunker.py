# ================================== CONVERTING TO TEXT =====================================
import pandas as pd

# CONSTANTS
MAX_TOKENS = 4000

def text_chunker():
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

    # overlap parts to avoid losing significant info
    chunks_improved = []
    window = 5 # number of segments that can be combined
    stride = 2 # number of segments to stride over, creates overlap
    for i in (range(0, len(chunks)-1, stride)):
        i_end = min(len(chunks)-1, i+window)
        text = ' '.join(_ for _ in chunks[i:i_end])

        # adds tags for source that can be used later when filtering info from certain books
        chunks_improved.append({
            "source": "First Aid Step 1",
            "text": text,
        })

    # test chunks
    print("Prints chunks 110 and 111")
    print(chunks_improved[110])
    print()
    print(chunks_improved[111])

    chunk_df = pd.DataFrame(chunks_improved)

    # filters empty text
    chunk_df = [chunk_df.text.ne('')]

    return chunk_df

    # NOTES FOR IMPROVEMENT =================================== -Pedro
    # improve text version of textbook ✖                      |
    #       |-> needs to happen BADLY, almost unreadable      |
    # add overlap incase missing information ✓                |
    #       |-> edit the overlap code to improve if need be   |
    # filter text thats too long for tokens
    # =========================================================