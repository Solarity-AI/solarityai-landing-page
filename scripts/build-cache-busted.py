#!/usr/bin/env python3
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys

IGNORE_NAMES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    ".cursor",
    "ansible",
    "scripts",
    "dist",
    "build",
    "node_modules",
}
IGNORE_SUFFIXES = (".md", ".bak", ".backup", ".tmp")
IGNORE_FILES = {"TestCommit"}
TEXT_EXTENSIONS = {".html", ".css", ".js"}


def hash_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()[:8]


def copy_source(src_root: Path, out_root: Path) -> None:
    if out_root.exists():
        shutil.rmtree(out_root)

    def _ignore(path: str, names):
        ignored = set()
        for name in names:
            if name in IGNORE_NAMES:
                ignored.add(name)
                continue
            if name in IGNORE_FILES:
                ignored.add(name)
                continue
            if name.endswith(IGNORE_SUFFIXES):
                ignored.add(name)
        return ignored

    shutil.copytree(src_root, out_root, ignore=_ignore)


def build_asset_map(src_root: Path):
    assets_dir = src_root / "assets"
    if not assets_dir.exists():
        return {}

    asset_map = {}
    for asset_path in assets_dir.rglob("*"):
        if not asset_path.is_file():
            continue
        if not asset_path.suffix:
            continue
        digest = hash_file(asset_path)
        hashed_name = f"{asset_path.stem}.{digest}{asset_path.suffix}"
        hashed_path = asset_path.with_name(hashed_name)
        asset_map[asset_path.relative_to(src_root).as_posix()] = (
            hashed_path.relative_to(src_root).as_posix()
        )
    return asset_map


def rename_assets(out_root: Path, asset_map) -> None:
    for original_rel, hashed_rel in asset_map.items():
        original_path = out_root / original_rel
        hashed_path = out_root / hashed_rel
        if not original_path.exists():
            continue
        hashed_path.parent.mkdir(parents=True, exist_ok=True)
        original_path.replace(hashed_path)


def update_text_references(out_root: Path, asset_map) -> None:
    for text_path in out_root.rglob("*"):
        if not text_path.is_file():
            continue
        if text_path.suffix not in TEXT_EXTENSIONS:
            continue

        content = text_path.read_text(encoding="utf-8")
        updated = content
        for original_rel, hashed_rel in asset_map.items():
            if original_rel in updated:
                updated = updated.replace(original_rel, hashed_rel)

            original_abs = out_root / original_rel
            hashed_abs = out_root / hashed_rel
            rel_from_file = os.path.relpath(original_abs, start=text_path.parent)
            rel_from_file = rel_from_file.replace(os.sep, "/")
            hashed_rel_from_file = os.path.relpath(hashed_abs, start=text_path.parent)
            hashed_rel_from_file = hashed_rel_from_file.replace(os.sep, "/")
            if rel_from_file in updated:
                updated = updated.replace(rel_from_file, hashed_rel_from_file)

        if updated != content:
            text_path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build cache-busted static assets.")
    parser.add_argument("--source", default=".", help="Source directory (default: .)")
    parser.add_argument("--output", default="dist", help="Output directory (default: dist)")
    args = parser.parse_args()

    src_root = Path(args.source).resolve()
    out_root = Path(args.output).resolve()

    if not src_root.exists():
        print(f"Source directory not found: {src_root}", file=sys.stderr)
        return 1

    copy_source(src_root, out_root)
    asset_map = build_asset_map(src_root)
    rename_assets(out_root, asset_map)
    update_text_references(out_root, asset_map)

    print(f"OK: Cache-busted build created at {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
