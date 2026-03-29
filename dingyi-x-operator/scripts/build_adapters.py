from __future__ import annotations

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "core"
ADAPTERS = ["codex", "claude-code", "openclaw"]


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    shutil.copytree(src, dst)


def build_adapter(name: str) -> None:
    adapter_dir = ROOT / name
    adapter_dir.mkdir(parents=True, exist_ok=True)

    skill_src = CORE / "SKILL.md"
    skill_dst = adapter_dir / "SKILL.md"
    skill_dst.write_text(skill_src.read_text(), encoding="utf-8")

    core_link = adapter_dir / "CORE-SKILL.md"
    if core_link.exists() or core_link.is_symlink():
        core_link.unlink()

    copy_tree(CORE / "references", adapter_dir / "references")


def main() -> None:
    for adapter in ADAPTERS:
        build_adapter(adapter)


if __name__ == "__main__":
    main()
