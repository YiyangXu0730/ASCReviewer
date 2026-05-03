#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_EXCLUDE_PATHS = {
    "FINAL_DELIVERY_MANIFEST.json",
    "ASCReview_FINAL_DELIVERY_REMEDIATION_REPORT.md",
    ".ascreview/context/ARTIFACT_INDEX_final.json",
}

DEFAULT_EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
}

DEFAULT_EXCLUDE_PREFIXES = {
    ".ascreview/runs/FINAL_DELIVERY_REMEDIATION_",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print("REPACK_POSIX_ZIP_FAILED")
    print(message)
    sys.exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a POSIX-portable ASCReview ZIP archive.")
    parser.add_argument("--source-root", default=str(ROOT), help="Directory to pack.")
    parser.add_argument("--output", required=True, help="Output ZIP path.")
    parser.add_argument("--root-name", default="ASCReview_FINAL_DELIVERY", help="Top-level ZIP folder name.")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional source-root-relative path to exclude. Use forward slashes.",
    )
    return parser.parse_args()


def should_skip(rel_posix: str, path: Path, output_path: Path, excludes: set[str]) -> bool:
    if path.resolve() == output_path.resolve():
        return True
    if rel_posix in excludes:
        return True
    if any(rel_posix.startswith(prefix) for prefix in DEFAULT_EXCLUDE_PREFIXES):
        return True
    parts = set(Path(rel_posix).parts)
    return bool(parts & DEFAULT_EXCLUDE_DIRS)


def validate_member_name(name: str) -> None:
    if "\\" in name:
        fail(f"non-POSIX member path: {name}")
    if name.startswith("/") or name.startswith("\\"):
        fail(f"absolute member path: {name}")
    if len(name) > 1 and name[1] == ":":
        fail(f"drive-qualified member path: {name}")
    if any(part == ".." for part in name.split("/")):
        fail(f"path traversal member path: {name}")


def main() -> None:
    args = parse_args()
    source_root = Path(args.source_root).resolve()
    output_path = Path(args.output).resolve()
    root_name = args.root_name.strip().strip("/\\")
    if not source_root.is_dir():
        fail(f"source root is not a directory: {source_root}")
    if not root_name or "/" in root_name or "\\" in root_name or ".." in root_name:
        fail(f"unsafe root name: {args.root_name}")

    excludes = set(DEFAULT_EXCLUDE_PATHS)
    excludes.update(item.replace("\\", "/").strip("/") for item in args.exclude)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    seen: set[str] = set()
    file_count = 0
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_root.rglob("*")):
            if not path.is_file():
                continue
            rel_posix = path.relative_to(source_root).as_posix()
            if should_skip(rel_posix, path, output_path, excludes):
                continue
            member_name = f"{root_name}/{rel_posix}"
            validate_member_name(member_name)
            if member_name in seen:
                fail(f"duplicate member path after POSIX normalization: {member_name}")
            seen.add(member_name)
            archive.write(path, member_name)
            file_count += 1

    with zipfile.ZipFile(output_path) as archive:
        bad_member = archive.testzip()
        if bad_member is not None:
            fail(f"zip integrity check failed at member: {bad_member}")
        for member_name in archive.namelist():
            validate_member_name(member_name)

    print("REPACK_POSIX_ZIP_OK")
    print(f"output={output_path}")
    print(f"files={file_count}")
    print(f"sha256={sha256_file(output_path)}")


if __name__ == "__main__":
    main()
