import argparse
import csv
import subprocess
from pathlib import Path


def download_videos(query: str, count: int, output_dir: Path) -> None:
    """Download `count` videos matching `query` into `output_dir` using yt-dlp."""
    output_dir.mkdir(parents=True, exist_ok=True)
    search_term = f"ytsearch{count}:{query}"
    cmd = [
        "yt-dlp",
        search_term,
        "-o",
        str(output_dir / "%(id)s.%(ext)s"),
        "--format",
        "mp4",
    ]
    subprocess.run(cmd, check=True)


def brand_video(source: Path, branding: str, cta: str, output_dir: Path) -> Path:
    """Add simple text overlays for branding and CTA using ffmpeg."""
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{source.stem}_branded.mp4"
    drawtext = (
        f"drawtext=text='{branding}':x=10:y=h-th-10:fontcolor=white:fontsize=24:"
        f"box=1:boxcolor=black@0.5,"
        f"drawtext=text='{cta}':x=w-tw-10:y=h-th-10:fontcolor=white:fontsize=24:"
        "box=1:boxcolor=black@0.5"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(source),
        "-vf",
        drawtext,
        "-c:a",
        "copy",
        str(target),
    ]
    subprocess.run(cmd, check=True)
    return target


def main():
    parser = argparse.ArgumentParser(description="Run a viral video experiment")
    parser.add_argument("query", help="Search term for trending clips")
    parser.add_argument("count", type=int, help="Number of clips to download")
    parser.add_argument("branding", help="Branding text to overlay")
    parser.add_argument("cta", help="CTA text or link to overlay")
    parser.add_argument(
        "--workdir",
        default="tmp/viral_videos",
        help="Directory to store downloads and processed clips",
    )
    args = parser.parse_args()

    workdir = Path(args.workdir)
    downloads = workdir / "downloads"
    processed = workdir / "processed"

    download_videos(args.query, args.count, downloads)

    csv_path = workdir / "experiment_metrics.csv"
    with csv_path.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["original_path", "processed_path"])
        for video in downloads.glob("*.mp4"):
            branded = brand_video(video, args.branding, args.cta, processed)
            writer.writerow([video, branded])

    print(f"Processed videos saved to {processed}")
    print(f"Metrics CSV written to {csv_path}")


if __name__ == "__main__":
    main()
