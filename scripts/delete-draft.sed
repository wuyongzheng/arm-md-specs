# Delete DRAFT in RMM spect v2 alpha

s/^DRAFT //
s/^## DRAFT /## /
s/^- DRAFT /- /
s/| DRAFT / /
/^DRAFT$/d
