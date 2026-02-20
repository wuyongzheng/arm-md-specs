## C3.6 Data Processing - MTE

The following subsections describe the MTE processing instructions:

- Pointer arithmetic instructions.
- Tag generation instructions.

## C3.6.1 Pointer arithmetic instructions

Table C3-92 shows the Memory Tagging Extension Pointer Arithmetic instruction.

## Table C3-92 MTE Pointer Arithmetic instruction

| Mnemonic   | Instruction                     | See   |
|------------|---------------------------------|-------|
| SUBP       | Subtract pointer                | SUBP  |
| SUBPS      | Subtract pointer, setting flags | SUBPS |

## C3.6.2 Tag generation instructions

Table C3-93 shows the Memory Tagging Extension Tag generation instructions.

## Table C3-93 Tag generation instructions

| Mnemonic   | Instruction       | See   |
|------------|-------------------|-------|
| ADDG       | Add with tag      | ADDG  |
| GMI        | Tag mask insert   | GMI   |
| IRG        | Insert random tag | IRG   |
| SUBG       | Subtract with tag | SUBG  |