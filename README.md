# reviewer3-test-code-verified

Reproducibility repo for the paper:

> **Random Forest Baseline for Breast Cancer Diagnosis (Verified Variant)**
> T. J. Reed, N. Simpson, Reviewer3 Applied Research Group

## Reproducing the headline result

```bash
python3 -m pip install -r requirements.txt
python3 train_and_eval.py
```

Expected stdout:

```
Test accuracy: 95.61%
Test samples:  114
```

## About this repo

This is one of a small family of synthetic test fixtures for the reviewer3
code-replication pipeline. All four variants share the same underlying training
setup (UCI Breast Cancer Wisconsin, `RandomForestClassifier(n_estimators=200,
random_state=42)`, stratified 80/20 split with `random_state=42`). Only the
paper's declared claim (and, in one variant, the code itself) differs across
the fixtures so we can grade the reviewer end-to-end.

**This variant's expected reviewer verdict:** `fully_reproduced` — the paper's
claim of 95.61% test accuracy matches what the code produces exactly.
