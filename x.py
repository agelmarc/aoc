import argparse
import datetime
import importlib
import time
from pathlib import Path


def run(func, input):
    start = time.monotonic_ns()
    print(func(input), end="\t")
    end = time.monotonic_ns()
    print(f"[{(end-start) / 10**6:.3f} ms]")


INPUT_DIR = Path("./input")

if __name__ == "__main__":
    now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-5)))

    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument(
        "--year", "-y", type=int, help="The year to run.", default=now.year
    )

    parser.add_argument(
        "--day", "-d", type=int, help="The day to run.", default=now.day
    )

    args = parser.parse_args()
    year, day = args.year, args.day

    INPUT_DIR.mkdir(exist_ok=True, parents=True)
    input_path = INPUT_DIR.joinpath(f"{year}/{day:02}.txt")

    if not input_path.exists():
        input_path.parent.mkdir(exist_ok=True, parents=True)
        import aocd

        data = aocd.get_data(day=day, year=year)

        with open(input_path, "w") as f:
            f.write(data)

    module_name = f"src.{year}.day{day:02}"
    module = importlib.import_module(module_name)

    if hasattr(module, "PART"):
        if module.PART == "both":
            parts = ["p1", "p2"]
        elif module.PART == 1:
            parts = ["p1"]
        elif module.PART == 2:
            parts = ["p2"]
        else:
            parts = ["p1", "p2"]

    sample = None

    if hasattr(module, "SAMPLE"):
        sample = module.SAMPLE

    with open(input_path, "r") as f:
        input = f.read()

    for part in parts:
        print(f"--- {part} ---")
        if not hasattr(module, part):
            continue
        if sample is not None:
            print("sample:")
            run(getattr(module, part), sample)
            importlib.reload(module)
        print("input:")
        run(getattr(module, part), input)
