import os
import re
import pprint
from os.path import dirname as up
import requests


n_glyc_motif = re.compile('(?=(N[^P][ST][^P]))')


def main():
    uniprot_url = "https://uniprot.org/uniprot/"
    prompt_dir = os.path.join(up(up(__file__)), "prompts")
    prot_ls_path = os.path.join(prompt_dir, "rosalind_mprt.txt")
    prot_list = open(prot_ls_path, "r").read().splitlines()

    for prot_id in prot_list:
        prot_cont = requests.get(f"{uniprot_url}{prot_id}.fasta")\

        if prot_cont.ok:
            fasta = prot_cont.text
            seq = ''.join(fasta.splitlines()[1:])
            match_pos = [match.start() + 1 for match in re.finditer(n_glyc_motif, seq)]
            if len(match_pos) > 1:
                print(prot_id)
                print(*match_pos)
        else:
            print("Bad request.")


if __name__ == "__main__":
    main()
