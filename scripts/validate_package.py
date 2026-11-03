"""Check the package's structure and internal references; not a prose-quality test."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'research-writing-editor'
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

entry = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
require(entry.startswith('---\n'), 'Missing YAML frontmatter')
parts = entry.split('---', 2)
front = parts[1] if len(parts) == 3 else ''
require('name: research-writing-editor' in front, 'Skill name mismatch')
require(bool(re.search(r'^description: .+', front, re.M)), 'Missing description')
for f in list(SKILL.rglob('*.md')) + [ROOT / 'README.md', ROOT / 'README.zh-CN.md', ROOT / 'evaluation' / 'README.md']:
    s = f.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', s):
        if '://' in link or link.startswith('#'):
            continue
        dest = (f.parent / link.split('#')[0]).resolve()
        require(dest.is_relative_to(ROOT), f'Link leaves package: {f.name}: {link}')
        require(dest.exists(), f'Broken link: {f.name}: {link}')
    require(not re.search(r'(?i)[a-z]:[/\\](?:users|sdxl)[/\\]', s), f'Private host path in {f.name}')
    require('[TODO:' not in s, f'Unfinished scaffold in {f.name}')
ui = (SKILL / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
require('$research-writing-editor' in ui, 'UI prompt does not name the skill')
require('allow_implicit_invocation: false' not in ui, 'Unexpected explicit-only invocation policy')
cases = json.loads((ROOT / 'evaluation' / 'cases.json').read_text(encoding='utf-8'))
require(len({c['id'] for c in cases}) == len(cases), 'Duplicate evaluation IDs')
for c in cases:
    require(all(c.get(k) for k in ('id', 'domain', 'task', 'facts', 'draft', 'checks')), f'Incomplete case: {c.get("id")}')
refs = list((SKILL / 'references').glob('*.md'))
for f in refs:
    require('references/' + f.name in entry, f'Unrouted reference: {f.name}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'Package structure valid: {len(refs)} routed guides; {len(cases)} evaluation cases.')
print('Behavioural quality must be assessed from actual revision outputs.')
