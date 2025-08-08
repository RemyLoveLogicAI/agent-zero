# Problem
Run a small viral video experiment by downloading trending clips, adding branding and a CTA, and logging processed files.

# Solution
1. If a working folder is required, `cd` to it.
2. Run the shell script with your query, number of clips, branding text, and CTA text:

```bash
bash /a0/instruments/default/viral_video_experiment/viral_video_experiment.sh "<query>" <count> "<branding>" "<cta>"
```

Example:

```bash
bash /a0/instruments/default/viral_video_experiment/viral_video_experiment.sh "morning routines" 5 "MyBrand" "Visit example.com"
```

3. Processed videos are stored in `tmp/viral_videos/processed` and a CSV log is written to `tmp/viral_videos/experiment_metrics.csv`.
