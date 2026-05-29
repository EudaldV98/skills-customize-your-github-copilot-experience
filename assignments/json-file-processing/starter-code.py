import json
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).parent / "data.json"


def load_data(filename: Path) -> Any:
    try:
        with filename.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {filename}: {exc}")


def save_data(filename: Path, data: Any) -> None:
    with filename.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def add_person(data: list[dict[str, Any]], new_person: dict[str, Any]) -> None:
    data.append(new_person)


def print_summary(data: list[dict[str, Any]]) -> None:
    print(f"Loaded {len(data)} people from the JSON file.")
    for person in data:
        print(f"- {person['name']} ({person['age']} years old)")


def main() -> None:
    data = load_data(DATA_FILE)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of people.")

    print_summary(data)

    new_person = {
        "name": "Nina",
        "age": 28,
        "city": "Portland",
        "skills": ["Python", "JSON", "file I/O"]
    }
    add_person(data, new_person)

    print("\nAdded a new person to the data set.")
    save_data(DATA_FILE, data)
    print("Saved updated data to data.json")


if __name__ == "__main__":
    main()
