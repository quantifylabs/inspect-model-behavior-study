# Evidence manifest — Inspect shipment evaluator study

**Status:** Exploratory evidence inventory. This manifest identifies the archived run and a later source-code snapshot. It **does not** establish that the later commit generated the historical run.

## Primary run archive

| Field | Recorded value |
|---|---|
| Original filename | `2026-10-04T08-48-31-00-00_shipment-eval_C3M5dWAM7NgPDr8CXJPF5n.eval` |
| Date in archive filename | 2026-10-04 |
| File size | 1,293,481 bytes |
| SHA-256 | `1ff2a518d57dfe725216801786e33c6af1ce1863624ee925e43727cad9a89cb3` |
| Stored locally | `logs/` (intentionally excluded from Git) |
| Run identifier (as recorded in technical report) | `SAd2xLX5TBBztrRZDwTW5K` |
| Evaluation identifier (as recorded in technical report) | `JGzMF4TQCpyPCuFKXeyHPJ` |
| Inspect task | `eval.py@shipment_eval` |
| Inspect AI (archived run) | `0.3.259` |
| Model argument | `openai/gpt-5` |
| Resolved model snapshot | `gpt-5-2025-08-07` |
| Dataset | Five shipment problems × five conditions = 25 samples |
| Epochs | 5 repetitions per sample |
| Recorded sample trajectories | 125 |
| Model generation overrides | None documented in archive (`model_generate_config={}`) |

The SHA-256 above was independently checked against the conversation-uploaded archive and matched the user's local PowerShell `Get-FileHash` output.

### Reproducing the procedure

```powershell
python -m pip install -r requirements.txt
python -m pytest -v
inspect eval eval.py@shipment_eval --model openai/gpt-5 --epochs 5
```

This command **makes paid API calls**, and repeated runs may yield different model outputs. The October 4 exact package environment and model-serving defaults have not been fully pinned; inspect the current `requirements.txt` before rerunning.

### Verifying the original archive

```powershell
Get-FileHash -Algorithm SHA256 -Path ".\logs\2026-10-04T08-48-31-00-00_shipment-eval_C3M5dWAM7NgPDr8CXJPF5n.eval"
```

Expected SHA-256:

```text
1FF2A518D57DFE725216801786E33C6AF1CE1863624EE925E43727CAD9A89CB3
```

## Published source snapshot (later than the evaluated run)

- GitHub repository: `https://github.com/quantifylabs/inspect-model-behavior-study`
- Branch: `main`
- Initial publication commit: [`63363b0e2a105f3322b2cd2b45402267c517ca74`](https://github.com/quantifylabs/inspect-model-behavior-study/commit/63363b0e2a105f3322b2cd2b45402267c517ca74)
- User-confirmed state at initial publication: local tree clean; branch synchronized to `origin/main`; source, tests, analysis, README and technical report tracked.

**Historical provenance limitation:** the initial publication commit postdates the October 4 run. There is no verified snapshot or diff establishing that this commit's exact code, dependencies and prompts generated the historical archive. Treat it as a *current published implementation*, not the verified original execution commit.

## Verification already performed

- The original archive records 125 trajectories (five shipment instances × five conditions × five epochs).
- Retrospective recomputation of 125 recorded tool submissions matched the saved vulnerable/trusted/exploit scorer outcomes, as reported in `report/shipment_capability_propensity_technical_report.md`.
- The owner confirmed six production-scorer test cases passed and the entire local test suite passed on 2026-11-06. These tests validate named cases, not all possible malformed inputs.
- Frozen qualitative rubric: `analysis/trajectory_analysis_rubric_v1_1_FROZEN.md`.
- Expanded annotations: `analysis/trajectory_annotations_30_v1_1.csv` and `analysis/trajectory_selection_manifest_30.csv`.
- Detailed analysis: `analysis/expanded_trajectory_analysis_v1_1.md`.

## Publication status and open checks

- **Primary archive availability:** not yet publicly linked. `logs/` is excluded by `.gitignore`; the checksum is publishable, but a reviewer cannot validate it without a copy of the file.
- **Source-to-archive provenance:** unverified. Preserve this limitation; do not backdate or retroactively attribute the run to the published commit.
- **Before releasing the `.eval` file:** inspect the archive for any API-related metadata, user/private details or other unintended disclosures. Publish a curated archive or an appropriate release asset only after review; retain and verify the original unchanged.
- **Before calling the work fully reproducible:** review `requirements.txt`, ensure instructions and source reflect the current `main` branch, and make the primary archive accessible or document a retrieval procedure.

