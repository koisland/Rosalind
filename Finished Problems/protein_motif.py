import os
import re
import time
import pprint
from selenium import webdriver

# driver = webdriver.Firefox(
#     executable_path=os.path.expanduser('~/PycharmProjects/Selenium_Automaton/driver_resources/geckodriver.exe'),
#     service_log_path=os.devnull)
#
# with open('D:\\Users\\Keith\\Downloads\\rosalind_mprt.txt', 'r') as rosalind_prompt:
#     ids = [line[:6] for line in rosalind_prompt.readlines()]
#
# for id_ in ids:
#     link = 'http://www.uniprot.org/uniprot/' + id_
#     driver.get(link)
#     add_to_basket = driver.find_element_by_id('add-entry-basket')
#     add_to_basket.click()
#
# driver.find_element_by_id('basket-list').click()
# time.sleep(0.5)
# driver.find_element_by_id('basket-download-button').click()
# driver.find_element_by_id('menu-go').click()
# #
# # # Iterate through list of IDs and add each ID to Basket.
# # # Download basket of IDs as fasta file using Selenium
# #
# time.sleep(3)  # Save file during this time.

for file in os.listdir('D:\\Users\\Keith\\Downloads'):
    fasta_match = re.match('uniprot-yourlist (.*?)\.fasta', file)
    if fasta_match is not None:
        with open('D:\\Users\\Keith\\Downloads\\' + fasta_match.group(), 'r') as matches:
            protein_seqs = matches.readlines()


def fasta_breakdown(read_file):  # Takes file in readlines format.
    id_dict = {}
    key = 'No ID'

    for line in read_file:  # Create dictionary with ids as keys and seq lines in list as value.
        if line.startswith('>'):
            key = line.strip()
            id_dict[key] = []
        else:
            id_dict[key].append(line.strip())

    for id_, seq in id_dict.items():  # Merge seq lines into a single string.
        id_dict[id_] = ''.join(seq)

    return id_dict


string_id_dict = fasta_breakdown(protein_seqs)


for id_, seq in string_id_dict.items():
    abridged_id = re.search('(?<=>sp\|)(\w{6})(?=\|)(.*?) ', id_)
    n_glycosylation_motif = re.compile('(?=(N[^P][ST][^P]))')  # + Lookahead needed to find overlapping segments
    start_locations = []
    for pattern in re.finditer(n_glycosylation_motif, seq):
        start_locations.append(str(pattern.start() + 1))
    if len(start_locations) > 0:
        print(abridged_id.group(1))
        print(abridged_id.group(2).strip('|').strip())
        print(' '.join(start_locations))
