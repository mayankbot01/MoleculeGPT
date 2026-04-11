# MoleculeGPT 🧬💡
> De Novo Drug Design via Fine-Tuned LLM + RLHF

**Part of the [GENAI_drughunter](https://github.com/mayankbot01/GENAI_drughunter) series — Project 1 of 10**

## Overview
MoleculeGPT solves the bottleneck of generating novel, synthesizable, and bioactive molecules from scratch. Most drug discovery projects rely on existing libraries; we build new ones using Generative AI.

## Key Features
- SELFIES tokenization with custom vocabulary injection into the LLM tokenizer
- RLHF loop using QED (drug-likeness) and SA Score (synthetic accessibility) reward model
- Fine-tuned ChemBERTa / GPT-NeoX on 2M+ ChEMBL SMILES
- Streamlit interface for medicinal chemists

## Tech Stack
- **Base Models**: ChemBERTa / GPT-NeoX fine-tuned on ChEMBL
- **RL Framework**: PPO with custom molecular reward model
- **Agents**: LangChain orchestrator for scoring and iterative refinement
- **Frontend**: Streamlit

## Quick Start
```bash
git clone https://github.com/mayankbot01/MoleculeGPT.git
cd MoleculeGPT
pip install -r requirements.txt
```

## Project Structure
```
MoleculeGPT/
├── src/
│   ├── tokenization/   # Custom SELFIES tokenizer
│   ├── rlhf/           # Reward model + PPO loops
│   └── generation/     # De novo molecular generation pipeline
├── app/                # Streamlit interface
├── MYWORK.md           # Detailed implementation notes
├── requirements.txt
└── README.md
```

## References
- [SELFIES](https://github.com/aspuru-guzik-group/selfies)
- [ChEMBL Database](https://www.ebi.ac.uk/chembl/)
- [RLHF for Molecular Generation](https://arxiv.org/abs/2110.14732)

---
*Maintained by [mayankbot01](https://github.com/mayankbot01) | GENAI_drughunter Series — Project 1 of 10*
