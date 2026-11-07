#!/usr/bin/env python3
"""Build a deterministic local ZIP for the Stark Skill; no network or install."""
from __future__ import annotations

import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RELEASES = ROOT / "release"
FIXED_TIME = (2026, 11, 7, 0, 0, 0)
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "release"}
PACKAGE_ROOT_FILES = {
    "SKILL.md", "README.md", "INSTALL.md", "COPYABLE_INSTALL_PROMPT.md",
    "VERSION", "CHANGELOG.md", "LICENSE",
}
PACKAGE_DIRS = {"agents", "references", "templates", "examples", "fixtures", "scripts"}


def files_to_package() -> list[Path]:
    found: list[Path] = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        root_file = len(rel.parts) == 1 and rel.name in PACKAGE_ROOT_FILES
        public_directory = bool(rel.parts) and rel.parts[0] in PACKAGE_DIRS
        if not (root_file or public_directory):
            continue
        if path.suffix.lower() in {".pyc", ".pyo"}:
            continue
        found.append(path)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version or any(c not in "0123456789." for c in version):
        raise SystemExit("VERSION must contain a numeric dotted version.")
    if not (ROOT / "SKILL.md").is_file():
        raise SystemExit("SKILL.md is missing.")

    RELEASES.mkdir(exist_ok=True)
    archive = RELEASES / f"Stark-Skill-v{version}.zip"
    checksum_file = archive.with_suffix(archive.suffix + ".sha256")
    with zipfile.ZipFile(archive, "w") as zf:
        for path in files_to_package():
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"stark/{relative}", date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            zf.writestr(info, path.read_bytes())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum_file.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"Created {archive}")
    print(f"SHA-256 {digest}")
    print(f"Files packaged: {len(files_to_package())}")


if __name__ == "__main__":
    main()
