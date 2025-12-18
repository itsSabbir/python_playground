from __future__ import annotations

import sys
from pathlib import Path

# Ensure the repo root is on sys.path so `import src...` works under pytest.
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
