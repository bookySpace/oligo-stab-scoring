def score_oligo(length, gc, hairpin_dg, homopolymer):
    score = 0
    if length >= 50:
        score += 1
    if gc < 40 or gc > 60:
        score += 1
    if hairpin_dg <= -10:
        score += 1
    if homopolymer >= 4:
        score += 1
    return score
