"""
Academic reference implementation.
Determin
 
# ===============================
# SPECTRUM-ACADEMIC CANONICAL BUILD
# ===============================

set -euo pipefail

# 1) Move to home workspace
cd ~
pwd

# 2) Clone or create repo
if [ -d "spectrum-academic" ]; then
  echo "ℹ️ spectrum-academic already exists, entering"
  cd spectrum-academic
else
  git clone git@github.com:AttraQter-Labs/spectrum-academic.git || {
    mkdir spectrum-academic
    cd spectrum-academic
    git init
    git branch -m main
    git remote add origin git@github.com:AttraQter-Labs/spectrum-academic.git
  }
fi

# 3) Hard reset (academic mirror must be clean)
rm -rf *
rm -rf .github || true

# 4) Base structure
mkdir -p spectrum_academic
mkdir -p notebooks
mkdir -p tests

touch spectrum_academic/__init__.py

# 5) Minimal exact metric (academic reference)
cat > spectrum_academic/minimal_exact_metrics.py <<'EOF'
"""
Academic reference implementation.
Deterministic. Exact. No floats. No randomness.
"""

from collections import defaultdict

def demographic_parity(outputs, groups):
    counts = defaultdict(int)
    totals = defaultdict(int)

    for o, g in zip(outputs, groups):
        totals[g] += 1
        counts[g] += int(o)

    rates = {}
    for g in totals:
        rates[g] = (counts[g], totals[g])  # exact rational pair

    return rates
