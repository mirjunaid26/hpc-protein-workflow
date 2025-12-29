from Bio import SeqIO
import numpy as np
import sys

def featurize(fasta_path):
	features = []
	for record in SeqIO.parse(fasta_path, "fasta"):
		seq = str(record.seq)
		length = len(seq)
		features.append([length])
	return np.array(features)

if __name__ == "__main__":
	fasta = sys.argv[1]
	X = featurize(fasta)
	print(X)
