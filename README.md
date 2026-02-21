# ARM Architecture Markdown Specification

This repository provides Markdown-formatted versions of Arm® Architecture
Specifications, specifically optimized for LLMs and coding agents. By
converting official PDF documentation into clean Markdown, we reduce structural
noise and improve the accuracy of AI-assisted development for Arm system
software, such as the Realm Management Monitor (RMM) and SMMU.

## Markdown Specifications

* [Realm Management Monitor specification](rmm/rmm-contents.md)
  * Version 1.0-rel0
  * DEN0137\_1.0-rel0\_rmm-arch\_external.pdf
* [Arm® Architecture Reference Manual for A-profile architecture](arm/arm-contents.md)
  * Version M.a.a
  * DDI0487\_M.a.a\_a-profile\_architecture\_reference\_manual.pdf
* [Arm System Memory Management Unit Architecture Specification SMMU architecture version 3](smmu/smmu-contents.md)
  * Version G.b
  * IHI0070G\_b-System\_Memory\_Management\_Unit\_Architecture\_Specification.pdf

## Build Process

* Install docling and mupdf
* mutool clean DEN0137\_1.0-rel0\_rmm-arch\_external.pdf rmm-chaps.pdf 9-16
* docling --to md --image-export-mode placeholder rmm-chaps.pdf
* gawk -f chaps-to-tsv.awk rmm-chaps.md > rmm-chaps.tsv
* manually fix rmm-chaps.tsv
* bash gen\_mds.sh rmm-chaps.tsv DEN0137\_1.0-rel0\_rmm-arch\_external.pdf rmm

## Credits & Legal
* Arm Limited: All original specifications, diagrams, and technical content are the intellectual property of Arm Limited. These Markdown files are derivative works intended for development efficiency. Please refer to the official  website for the authoritative versions of these documents.
* [docling](https://www.docling.ai/) is used for PDF to MD conversion.
* [MuPDF](https://mupdf.com/) is used for PDF page and contents extraction.
