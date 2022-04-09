import numpy as np

PATH_DATA = "prompts/rosalind_eval.txt"


def num_overlaps(seq_len, substr_len):
    """
    The number of times a substring can overlap in a given sequence.
    :param seq_len:
    :param substr_len:
    :return:
    """
    return seq_len - (substr_len - 1)


def exp_num_rsites(str_fmt=True):
    """
    Calculates the expected number of restriction sites (substr) in a random DNA string of n length (n)
    given the DNA string's GC content (gc_content).
    :param str_fmt: [bool] - return results as string delimited by spaces
    :return res: [list] - expected number of restriction sites.
    """
    with open(PATH_DATA) as fobj:
        (n, substr, gc_content_str) = [ln.strip() for ln in fobj.readlines()]
        gc_content = np.array(gc_content_str.split(" ")).astype(np.float32)

    n_overlaps = num_overlaps(int(n), len(substr))
    res = []

    for pc_gc in gc_content:
        pc_at = 1 - pc_gc
        pc_nts = {"A": pc_at / 2, "T": pc_at / 2, "G": pc_gc / 2, "C": pc_gc / 2}
        pr_substr = np.product([pc_nts.get(nt) for nt in substr])
        exp_num_substr = round(pr_substr * n_overlaps, 3)
        res.append(exp_num_substr)

    if str_fmt:
        return " ".join(str(r) for r in res)
    else:
        return res
