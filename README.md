# oligo-stab-scoring
t.b.d
# Oligo Stability & Manufacturability Scoring

This project provides a rule-based, in silico framework to assess 
oligonucleotide stability and synthesis risk using sequence-level features.

## Problem
Oligo synthesis frequently fails due to secondary structure, 
self-complementarity, or poor sequence design — wasting time and resources.

## Approach
Each oligo sequence is evaluated using:
- Length
- GC content
- Homopolymer runs
- Predicted hairpin ΔG
- Self-dimerization risk

Each feature is converted into a binary risk flag (0 = safe, 1 = risky).
A composite score classifies oligos as:
- Stable
- Moderate risk
- High risk

## Example Rules
- GC content between 40–60% → safe
- Hairpin ΔG ≤ −10 kcal/mol → high risk
- Homopolymer ≥ 4 bases → high risk

## Intended Use
- Academic labs
- Early-stage biotech
- RNA therapeutic design screening

## Future Directions
- Incorporate crowdsourced lab outcomes
- Train ML models on synthesis success data
- Web-based interface for batch analysis
