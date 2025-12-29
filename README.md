HPC Protein Workflow

A minimal, reproducible, HPC-aware protein machine learning workflow.

This repository demonstrates how to structure and execute a small protein-related ML pipeline with a systems and workflow focus, suitable for HPC environments (e.g., Slurm-based clusters).

The goal is not biological novelty, but clean experiment design, reproducibility, and scalability — exactly the kind of starter project expected in HPC + computational biology contexts.

⸻

What This Project Does
	•	Reads protein sequences from FASTA files
	•	Extracts simple, interpretable features
	•	Trains a lightweight ML model
	•	Can be executed locally or on an HPC system

⸻

Repository Structure

hpc-protein-workflow/
├── README.md
├── data/              # Sample protein data (FASTA)
├── src/               # Feature extraction and training code
├── scripts/           # Local and Slurm execution scripts
├── env/               # Environment definitions
└── results/           # Outputs (ignored by git)


⸻

Requirements
	•	Python 3.9+
	•	NumPy
	•	Biopython
	•	scikit-learn

⸻

Quick Start (Local)

pip install numpy biopython scikit-learn
python src/featurize.py data/sample.fasta


⸻

HPC Usage (Slurm)

This project is designed to be runnable on Slurm-based HPC systems.
A sample job script will be provided in scripts/run_slurm.sh.

⸻

Motivation

Large-scale biological workloads increasingly rely on HPC systems, yet many workflows are not designed with performance, reproducibility, or scalability in mind.

This project serves as a minimal reference implementation for building such workflows correctly from the start.

⸻

License

MIT

HPC-Aware Protein Workflow (Starter Project)

This repository is a minimal, publishable starter project demonstrating how to design and run a reproducible, HPC-aware workflow for protein-related machine learning or bioinformatics tasks.

The goal is not biology novelty, but systems correctness:
	•	reproducible pipelines
	•	clean experiment structure
	•	HPC-ready execution
	•	performance measurement

This is intentionally small, readable, and extensible.

⸻

Project Idea (What We Are Building)

We implement a simple protein-sequence classification workflow:
	1.	Load protein sequences (FASTA)
	2.	Extract lightweight features (length, amino-acid composition)
	3.	Train a simple ML model (logistic regression / random forest)
	4.	Measure runtime and scalability
	5.	Run locally and on an HPC system (Slurm)

This gives us:
	•	a biological use case
	•	a full ML pipeline
	•	something we can benchmark
	•	something publishable on GitHub

⸻

Why This Project Is Good for You

✔ Minimal coding
✔ Clear systems focus
✔ HPC-friendly
✔ Extensible later to real protein models

⸻

Repository Structure

hpc-protein-workflow/
├── README.md
├── data/
│   └── sample.fasta
├── src/
│   ├── featurize.py
│   ├── train.py
│   └── evaluate.py
├── scripts/
│   ├── run_local.sh
│   └── run_slurm.sh
├── env/
│   └── environment.yml
└── results/


⸻

Tech Stack (Minimal)
	•	Python 3.10+
	•	NumPy
	•	scikit-learn
	•	Biopython
	•	Slurm (optional)

⸻

Step-by-Step Learning Plan

Step 1 — Environment (Day 1)
	•	Create conda environment
	•	Install dependencies

Step 2 — Protein Basics (Day 2)
	•	Parse FASTA files
	•	Extract simple features

Step 3 — ML Pipeline (Day 3)
	•	Train simple classifier
	•	Save results

Step 4 — HPC Execution (Day 4)
	•	Write Slurm script
	•	Run batch job

Step 5 — Polish (Day 5)
	•	Clean README
	•	Push to GitHub

⸻

What This Demonstrates
	•	You understand workflows
	•	You can structure experiments
	•	You can run on HPC systems

Next Steps (Later)
	•	Replace features with embeddings
	•	Add scaling experiments
	•	Add workflow engine (Snakemake)
	•	Add containerization

⸻

License

MIT
