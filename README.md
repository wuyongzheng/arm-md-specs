# ARM Architecture Markdown Specification

Markdown files are easier for coding agents to understand.
They are converted from the PDF files.

## Specifications

* [Realm Management Monitor specification](rmm/rmm-contents.md) DEN0137\_1.0-rel0\_rmm-arch\_external.pdf
* [Arm® Architecture Reference Manual for A-profile architecture](arm/arm-contents.md) DDI0487\_M.a.a\_a-profile\_architecture\_reference\_manual.pdf
* [Arm System Memory Management Unit Architecture Specification SMMU architecture version 3](smmu/smmu-contents.md) IHI0070G\_b-System\_Memory\_Management\_Unit\_Architecture\_Specification.pdf

## The Backstage

* Install docling and mupdf
* mutool clean DEN0137\_1.0-rel0\_rmm-arch\_external.pdf rmm-chaps.pdf 9-16
* docling --to md --image-export-mode placeholder rmm-chaps.pdf
* gawk -f chaps-to-tsv.awk rmm-chaps.md > rmm-chaps.tsv
* manually fix rmm-chaps.tsv
* bash gen\_mds.sh rmm-chaps.tsv DEN0137\_1.0-rel0\_rmm-arch\_external.pdf rmm
