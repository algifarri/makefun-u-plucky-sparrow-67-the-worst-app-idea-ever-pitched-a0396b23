"""Entry for the make.fun bounty "The Worst App Idea Ever Pitched".

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt. Deterministic, stdlib-only, no network access.
"""

import os

ENTRY = (
    "DoorbellDJ composes a unique 45-second orchestral fanfare every time "
    "someone rings your doorbell, because every guest deserves a grand "
    "entrance and busy homeowners should never have to greet anyone in "
    "silence."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
