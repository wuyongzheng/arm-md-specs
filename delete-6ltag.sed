# Delete 6-letter tags

s/^- [A-Z][A-Z][A-Z][A-Z][A-Z][A-Z] \([A-Z]\)/- \1/
s/^## [A-Z][A-Z][A-Z][A-Z][A-Z][A-Z] \([A-Z]\)/## \1/
s/^[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z] \([A-Z]\)/\1/
/^- [A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]$/d
/^## [A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]$/d
/^[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]$/d
