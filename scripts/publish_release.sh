#!/usr/bin/env bash
set -euo pipefail

# Local automation script to package and publish a GitHub Release via gh CLI
# Usage: ./scripts/publish_release.sh [version] (e.g. ./scripts/publish_release.sh v1.0.0)

TAG="${1:-}"

if [ -z "$TAG" ]; then
  echo "Usage: $0 <version-tag> (e.g., $0 v1.0.0)"
  exit 1
fi

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

# Ensure repo is clean or committed
if [ -n "$(git status --porcelain)" ]; then
  echo "Error: Working directory has uncommitted changes. Please commit or stash first."
  exit 1
fi

# Ensure tag exists or create it
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "Tag $TAG already exists locally."
else
  echo "Creating git tag $TAG..."
  git tag -a "$TAG" -m "Release $TAG"
fi

echo "Pushing commits and tags to origin..."
git push origin main
git push origin "$TAG"

# Create a zip bundle for the release
ZIP_NAME="learn-ai-curriculum-${TAG}.zip"
echo "Creating release archive $ZIP_NAME..."
zip -r "$ZIP_NAME" . -x "*.git*" ".github/*" ".DS_Store" "$ZIP_NAME"

echo "Creating GitHub Release via gh CLI..."
gh release create "$TAG" "$ZIP_NAME" \
  --title "Release $TAG" \
  --notes "### Architecting Unstructured Data & Knowledge Retrieval for LLMs - Release $TAG

- 20 complete interactive lessons across 6 phases
- 4 system reference & cheatsheet documents
- Dedicated mobile & tablet offline edition (\`mobile/\`)
- Visual architecture diagrams, code samples, and self-test quizzes

Online version available on GitHub Pages."

# Clean up local zip
rm -f "$ZIP_NAME"

echo "Successfully published release $TAG to GitHub!"
