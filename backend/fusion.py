def compute_risk_score(artifact_prob: float, speaker_similarity: float) -> int:
    """
    artifact_prob: 0-1, probability audio is AI-synthesized
    speaker_similarity: 0-1, similarity to enrolled voiceprint (1 = perfect match)
    """
    identity_risk = 1 - speaker_similarity
    risk = 0.6 * artifact_prob + 0.4 * identity_risk
    return round(risk * 100)