import sys
import time
import json
from pathlib import Path
from statistics import mean
import subprocess
from dataclasses import dataclass


def run_solution(file_path: Path) -> tuple[str, float | None]:
    start = time.time()
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=100,
            check=True,
        )
        end = time.time()
        return result.stdout.strip(), end - start
    except subprocess.TimeoutExpired:
        print(f"Timeout for {file_path}")
        return "", None
    except subprocess.CalledProcessError:
        print(f"Error in {file_path}")
        return "", None


@dataclass
class TestResult:
    file: str
    average_time: float


def test_solution(file_path: Path) -> TestResult | None:
    # Get answer file path
    path = Path(file_path)
    answer_file = path.parent / f"{path.stem}.answer.txt"

    with open(file_path, encoding="utf-8") as f:
        code = f.read()
        if code.startswith("# REQUIRES HUMAN"):
            print(f"Skipping {file_path} as it requires human intervention")
            return None
        if code.count("print") == 0:
            print(f"No print statement found in {file_path}")
            return None

    if not answer_file.exists():
        print(f"No answer file found for {file_path}")
        return None

    with open(answer_file, encoding="utf-8") as f:
        expected = f.read().strip()

    if not expected:
        print(f"No expected answer recorded for {file_path}")
        return None

    times = []

    # Run 3 times
    for i in range(3):
        output, duration = run_solution(file_path)
        times.append(duration)

        if output != expected:
            print(f"Test {i+1} failed for {file_path}")
            print(f"Expected: {expected}")
            print(f"Got: {output}")
            return None

    avg_time = mean(filter(None, times))

    print(f"Passed {file_path} in {avg_time:.4f} seconds")

    return TestResult(
        file=str(file_path).replace("\\", "/"),
        average_time=avg_time,
    )


def main():
    if len(sys.argv) > 1:
        changed_files = [Path(file) for file in sys.argv[1:]]
    else:
        changed_files = list(Path(".").rglob("*.py"))
    results: list[TestResult] = []

    try:
        for file in changed_files:
            if not file.name.endswith("a.py") and not file.name.endswith("b.py"):
                continue

            result = test_solution(file)
            if result:
                results.append(result)
    except KeyboardInterrupt:
        pass

    # Update timesheet.json
    timesheet_path = Path("timesheet.json")
    existing_data = {}

    if timesheet_path.exists():
        with open(timesheet_path, encoding="utf-8") as f:
            existing_data = json.load(f)

    for result in results:
        existing_data[result.file] = {
            "average_time": result.average_time,
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    timesheet_path.parent.mkdir(exist_ok=True)
    with open(timesheet_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=2)

    # Generate markdown
    with open("timesheet.md", "w", encoding="utf-8") as f:
        f.write("# Solution Timings\n\n")
        f.write("| Year | Day | Part | Average Time (s) | Last Updated |\n")
        f.write("|------|-----|------|------------------|--------------|\n")

        for file, data in sorted(existing_data.items()):
            p = Path(file)
            f.write(
                f"| {p.parent.name} | [{p.name.split('.')[0]}]({p.parent.name}/{p.name.split('.')[0]}.md) | [{'1' if p.name.split('.')[1] == 'a' else '2'}]({p.parent.name}/{p.name}) | {data['average_time']:.4f} | {data['last_updated']} |\n"
            )


if __name__ == "__main__":
    main()
