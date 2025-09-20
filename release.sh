#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <version-tag>"
  echo "Example: $0 v0.1.0-alpha"
  exit 1
fi

VERSION=$1

# Ensure working tree is clean
if [ -n "$(git status --porcelain)" ]; then
  echo "Error: working directory not clean. Commit or stash changes first."
  exit 1
fi

# Ensure branch is up to date
git fetch origin
if ! git diff --quiet origin/dev..dev; then
  echo "Error: dev branch not up to date with origin/dev. Please pull first."
  exit 1
fi

# Create annotated tag
git tag -a "$VERSION" -m "Release $VERSION"

# Push tag to GitHub
git push origin "$VERSION"

echo "✅ Release $VERSION created and pushed."
echo "Check GitHub Releases page to publish a formal release if needed."
