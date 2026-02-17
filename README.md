# ARM Architecture Markdown Specification

Markdown files are easier for coding agents to understand.
They are converted from the PDF files.

## Specifications

* [Realm Management Monitor specification](rmm/rmm-contents.md) DEN0137\_1.0-rel0\_rmm-arch\_external.pdf

## The Backstage

* Install docling and mupdf
* mutool clean DEN0137_1.0-rel0_rmm-arch_external.pdf rmm-chaps.pdf 9-16
* docling --to md --image-export-mode placeholder rmm-chaps.pdf
* gawk -f chaps-to-tsv.awk rmm-chaps.md > rmm-chaps.tsv
* manually fix rmm-chaps.tsv
* bash gen_mds.sh rmm-chaps.tsv DEN0137_1.0-rel0_rmm-arch_external.pdf rmm
