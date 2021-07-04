with open("rosalind_gc.txt") as sequences_obj:
    sequences = sequences_obj.read()

seq_list = {}
for pos, item in enumerate(sequences):
    if item == ">":
        end_id = sequences.index("\n", pos)
        start_id = sequences.find(">", end_id)
        if start_id == -1:
            start_id = len(sequences)
        seq_list[sequences[pos+1:end_id]] = sequences[end_id:start_id].replace("\n", "")

highest_gc = ["none", 0]
for seq_id, string in seq_list.items():
    GC_content = (string.count("G") + string.count("C")) / len(string)
    if GC_content > highest_gc[1]:
        highest_gc = [seq_id, GC_content]
print(highest_gc)
