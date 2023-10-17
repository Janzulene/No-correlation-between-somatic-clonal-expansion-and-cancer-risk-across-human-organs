from pathlib import Path


class Location(object):
    root: Path = Path(__file__).parents[1]
    raw_data: Path = root / "data" / "raw"
    processed_data: Path = root / "data" / "processed"
    final_data: Path = root / "data" / "final"
 
