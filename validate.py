"""Run every local check in the order CLAUDE.md lists: build, static audit, Python tests, Node tests.

    python validate.py            (on Windows: .venv\\Scripts\\python.exe validate.py)

Test files are found by name (test_*.py and test-*.cjs in the project root), so a new test file runs
without editing this script, the docs or CI. Exits non-zero at the first failing step.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(title, command):
    print(f'\n== {title}', flush=True)
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode:
        print(f'\n{title} failed (exit {result.returncode}).')
        sys.exit(result.returncode)


def main():
    python = sys.executable
    run('Build', [python, 'build_site.py'])

    print('\n== Static audit', flush=True)
    audit = subprocess.run([python, 'check_site.py'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    report = json.loads(audit.stdout[audit.stdout.index('{'):])
    for error in report['errors']:
        print('  error:', error)
    print(f"{len(report['errors'])} errors, {len(report['warnings'])} warnings")
    if audit.returncode or report['errors']:
        sys.exit(audit.returncode or 1)

    python_tests = sorted(path.name for path in ROOT.glob('test_*.py'))
    run(f'Python tests ({len(python_tests)} files)', [python, '-m', 'unittest', *python_tests])

    node_tests = sorted(path.name for path in ROOT.glob('test-*.cjs'))
    if not shutil.which('node'):
        print('\nNode tests need Node.js 24 (.nvmrc) on PATH; install it and run validate.py again.')
        sys.exit(1)
    run(f'Node tests ({len(node_tests)} files)', ['node', '--test', *node_tests])
    print('\nAll checks passed.')


if __name__ == '__main__':
    main()
