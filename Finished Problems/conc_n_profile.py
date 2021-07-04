import pandas as pd
from rosalind_resources import unpack_fasta

entries = unpack_fasta('rosalind_cons.txt')

conc_str = ''

# print(entries)
n = len(list(entries.values())[0]) + 1
df = pd.DataFrame(0, index=list('ATGC'), columns=[str(col) for col in range(1, n)])

for entry in entries.values():
    for pos, nt in enumerate(entry, 1):
        df.loc[nt, str(pos)] += 1

for pos in range(1, n):
    top_nt = df.loc[df[str(pos)].idxmax()]
    conc_str += top_nt.name

with open('ros_df.txt', 'w') as text:
    text.write(f"{conc_str}\n")
    raw_csv_text = str(df.to_csv(header=False)).replace(',', ' ')
    text.write(raw_csv_text)
