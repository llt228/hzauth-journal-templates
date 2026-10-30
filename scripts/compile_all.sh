#!/usr/bin/env bash
# Compile every journal template with latexmk.
#
# Usage:
#   bash scripts/compile_all.sh
#   JOBS=8 bash scripts/compile_all.sh
#
# A writable TEXMFVAR is used so that bitmap fonts (EC/TS1) can be generated
# in restricted environments.  Normal TeX Live installations work as well.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
JOBS="${JOBS:-4}"
TEXMFVAR="${TEXMFVAR:-$ROOT/.texmf-var}"
export TEXMFVAR
mkdir -p "$TEXMFVAR"

compile_one() {
  local dir="$1"
  ( cd "$dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1 )
}

# Pre-generate the shared font cache with one journal per class to avoid
# concurrent mktexpk races on the first run.
for slug in cell accounts-of-chemical-research national-science-review \
            ieee-transactions-on-pattern-analysis-and-machine-intelligence \
            reviews-of-modern-physics; do
  dir="$ROOT/journals/$slug"
  [ -d "$dir" ] && compile_one "$dir"
done

mapfile -t dirs < <(find "$ROOT/journals" -mindepth 1 -maxdepth 1 -type d | sort)
: > /tmp/hzauth_failed.txt
printf '%s\0' "${dirs[@]}" | xargs -0 -P "$JOBS" -I{} bash -c '
  dir="$1"
  ( cd "$dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1 ) || echo "$dir" >> /tmp/hzauth_failed.txt
' _ {}

failed=()
if [ -s /tmp/hzauth_failed.txt ]; then
  mapfile -t failed < /tmp/hzauth_failed.txt
fi

# Retry failures once, sequentially (font cache races are the usual cause).
if [ "${#failed[@]}" -gt 0 ]; then
  echo "retrying ${#failed[@]} failed build(s) sequentially..."
  still_failed=()
  for dir in "${failed[@]}"; do
    if ! compile_one "$dir"; then
      still_failed+=("$dir")
    fi
  done
  failed=("${still_failed[@]}")
fi

total="${#dirs[@]}"
if [ "${#failed[@]}" -gt 0 ]; then
  echo "FAILED ${#failed[@]}/$total:"
  printf '  %s\n' "${failed[@]}"
  exit 1
fi

echo "compiled $total journal template(s) successfully"
