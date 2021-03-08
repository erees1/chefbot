import sys

required = "3.7"


def main():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"

    if version != required:
        raise TypeError(f"This project requires Python {required} Found: Python {version}")
    else:
        print(">>> Development environment passes all tests!")


if __name__ == "__main__":
    main()
