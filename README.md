# Polarization marking against coherent inter-beam fading

Reproducible code for the article *When Does Polarization Marking Suppress Coherent Inter-Beam Fading? Path Distinguishability and Propagated-Field Regimes for Multi-Beam SLM Transmitters*.

A multi-beam transmitter built on a phase-only spatial light modulator (SLM) serves overlapping coverage cells from one coherent source. Where beams overlap, they interfere and a polarization-insensitive receiver can sit on a dark fringe. Assigning a fixed polarization marker to each beam acts as a which-path label and removes the interference between differently marked beams. The notebook quantifies how much this helps.

## Contents

| File | Purpose |
|---|---|
| `owc_marking.ipynb` | Executed notebook reproducing every number, table and figure (Figs. 2–5) |
| `schematic.py` | Draws the transmitter overview figure (Fig. 1) |
| `results/owc_results.json` | All numerical results written by the notebook |
| `results/fig_*.pdf, .png` | Figures written by the notebook |

## What the notebook computes

1. Fade floors of structured two-dimensional marker sets (coherent, trine, H/V/D/R, tetrahedral, grouping).
2. A branch-and-bound certificate for the tetrahedral floor 4 − 2√3.
3. A global search for the largest fade floor over all two-dimensional marker sets for three and four beams.
4. A propagated-field model of the transmitter: pixelated phase-only SLM (1500 × 1500 pixels, 8 µm pitch, 8-bit phase, 93 % fill factor, zero-order leakage), afocal relay (angular magnification 5) and Fresnel propagation over 2 m.
5. Segmented transmitter: marker-assignment objectives, variance identity check, phase-independent fade certificate, receiver-aperture sweep, coverage-wide statistics, phase dithering, marker tolerances and a source-linewidth regime map, all on held-out positions and phases.
6. Full-aperture (multi-spot hologram) transmitter, coherent and polarization-multiplexed at matched launch power.

## Running

Python 3 with `numpy`, `scipy` and `matplotlib` (the first cell installs them). Open the notebook in Jupyter or Google Colab and run all cells. Seeds are fixed. A full run takes about 30 minutes on two CPU cores; results go to `results/`.

## License

MIT (see `LICENSE`).
