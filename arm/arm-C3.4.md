## C3.4 Loads and stores - SME, SME2, SVE2p1

The following subsections describe the SME, SME2 and SVE2p1 loads and stores:

- Array vector/table load and store.
- Consecutive multi-vector loads and stores.
- SVE2.1 quadword loads and stores.

## C3.4.1 Array vector/table load and store

These instructions transfer data between the ZA array vector or the ZT0 registers and memory.

These instructions are performed as contiguous byte accesses, with no endian conversion and no guarantee of single-copy atomicity larger than a byte.

## Table C3-74 SME array vector/table load and store

| Mnemonic   | Instruction          | See                |
|------------|----------------------|--------------------|
| LDR        | Load ZAarray vector  | LDR(array vector)  |
|            | Load ZT0 register    | LDR(table)         |
| STR        | Store ZAarray vector | STR (array vector) |
|            | Store ZT0 register   | STR (table)        |

## C3.4.2 Contiguous multi-vector loads and stores

## C3.4.2.1 Consecutive multi-vector loads and stores

Multi-vector load and store instructions that transfer data between memory and consecutive SVE vector registers.

Table C3-75 Consecutive multi-vector load and store instructions

| Mnemonic   | Instruction                                                                                                 | See                                                                                                      |
|------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| LD1        | Contiguous load of bytes to multiple consecutive vectors (immediate index, scalar index)                    | LD1B (scalar plus immediate, consecutive registers) LD1B (scalar plus scalar, consecutive registers)     |
| LD1        | Contiguous load of doublewords to multiple consecutive vectors (immediate index, scalar index)              | LD1D (scalar plus immediate, consecutive registers) LD1D (scalar plus scalar, consecutive registers)     |
| LD1        | Contiguous load of halfwords to multiple consecutive vectors (immediate index, scalar index)                | LD1H (scalar plus immediate, consecutive registers) LD1H (scalar plus scalar, consecutive registers)     |
| LD1        | Contiguous load of words to multiple consecutive vectors (immediate index, scalar index)                    | LD1W(scalar plus immediate, consecutive registers) LD1W(scalar plus scalar, consecutive registers)       |
| LDNT1      | Contiguous load non-temporal of bytes to multiple consecutive vectors (immediate index, scalar index)       | LDNT1B (scalar plus immediate, consecutive registers) LDNT1B (scalar plus scalar, consecutive registers) |
| LDNT1      | Contiguous load non-temporal of doublewords to multiple consecutive vectors (immediate index, scalar index) | LDNT1D (scalar plus immediate, consecutive registers) LDNT1D (scalar plus scalar, consecutive registers) |
| LDNT1      | Contiguous load non-temporal of halfwords to multiple consecutive vectors (immediate index, scalar index)   | LDNT1H (scalar plus immediate, consecutive registers) LDNT1H (scalar plus scalar, consecutive registers) |

| Mnemonic   | Instruction                                                                                                    | See                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
|            | Contiguous load non-temporal of words to multiple consecutive vectors (immediate index, scalar index)          | LDNT1W(scalar plus immediate, consecutive registers) LDNT1W(scalar plus scalar, consecutive registers)   |
| ST1        | Contiguous store of bytes from multiple consecutive vectors (immediate index, scalar index)                    | ST1B (scalar plus immediate, consecutive registers) ST1B (scalar plus scalar, consecutive registers)     |
| ST1        | Contiguous store of doublewords from multiple consecutive vectors (immediate index, scalar index)              | ST1D (scalar plus immediate, consecutive registers) ST1D (scalar plus scalar, consecutive registers)     |
| ST1        | Contiguous store of halfwords from multiple consecutive vectors (immediate index, scalar index)                | ST1H (scalar plus immediate, consecutive registers) ST1H (scalar plus scalar, consecutive registers)     |
| ST1        | Contiguous store of words from multiple consecutive vectors (immediate index, scalar index)                    | ST1W (scalar plus immediate, consecutive registers) ST1W (scalar plus scalar, consecutive registers)     |
| STNT1      | Contiguous store non-temporal of bytes from multiple consecutive vectors (immediate index, scalar index)       | STNT1B (scalar plus immediate, consecutive registers) STNT1B (scalar plus scalar, consecutive registers) |
| STNT1      | Contiguous store non-temporal of doublewords from multiple consecutive vectors (immediate index, scalar index) | STNT1D (scalar plus immediate, consecutive registers) STNT1D (scalar plus scalar, consecutive registers) |
| STNT1      | Contiguous store non-temporal of halfwords from multiple consecutive vectors (immediate index, scalar index)   | STNT1H (scalar plus immediate, consecutive registers) STNT1H (scalar plus scalar, consecutive registers) |
| STNT1      | Contiguous store non-temporal of words from multiple consecutive vectors (immediate index, scalar index)       | STNT1W (scalar plus immediate, consecutive registers) STNT1W (scalar plus scalar, consecutive registers) |

## C3.4.2.2 Strided multi-vector loads and stores

Multi-vector load and store instructions that transfer data between memory and strided numbered vector registers.

## Table C3-76 Strided multi-vector load and store instructions

| Mnemonic   | Instruction                                                                                             | See                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| LD1        | Contiguous load of bytes to multiple strided vectors (immediate index, scalar index)                    | LD1B (scalar plus immediate, strided registers) LD1B (scalar plus scalar, strided registers)     |
|            | Contiguous load of doublewords to multiple strided vectors (immediate index, scalar index)              | LD1D (scalar plus immediate, strided registers) LD1D (scalar plus scalar, strided registers)     |
|            | Contiguous load of halfwords to multiple strided vectors (immediate index, scalar index)                | LD1H (scalar plus immediate, strided registers) LD1H (scalar plus scalar, strided registers)     |
|            | Contiguous load of words to multiple strided vectors (immediate index, scalar index)                    | LD1W(scalar plus immediate, strided registers) LD1W(scalar plus scalar, strided registers)       |
| LDNT1      | Contiguous load non-temporal of bytes to multiple strided vectors (immediate index, scalar index)       | LDNT1B (scalar plus immediate, strided registers) LDNT1B (scalar plus scalar, strided registers) |
|            | Contiguous load non-temporal of doublewords to multiple strided vectors (immediate index, scalar index) | LDNT1D (scalar plus immediate, strided registers) LDNT1D (scalar plus scalar, strided registers) |

| Mnemonic   | Instruction                                                                                                | See                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
|            | Contiguous load non-temporal of halfwords to multiple strided vectors (immediate index, scalar index)      | LDNT1H (scalar plus immediate, strided registers) LDNT1H (scalar plus scalar, strided registers) |
|            | Contiguous load non-temporal of words to multiple strided vectors (immediate index, scalar index)          | LDNT1W(scalar plus immediate, strided registers) LDNT1W(scalar plus scalar, strided registers)   |
| ST1        | Contiguous store of bytes from multiple strided vectors (immediate index, scalar index)                    | ST1B (scalar plus immediate, strided registers) ST1B (scalar plus scalar, strided registers)     |
|            | Contiguous store of doublewords from multiple strided vectors (immediate index, scalar index)              | ST1D (scalar plus immediate, strided registers) ST1D (scalar plus scalar, strided registers)     |
|            | Contiguous store of halfwords from multiple strided vectors (immediate index, scalar index)                | ST1H (scalar plus immediate, strided registers) ST1H (scalar plus scalar, strided registers)     |
|            | Contiguous store of words from multiple strided vectors (immediate index, scalar index)                    | ST1W (scalar plus immediate, strided registers) ST1W (scalar plus scalar, strided registers)     |
| STNT1      | Contiguous store non-temporal of bytes from multiple strided vectors (immediate index, scalar index)       | STNT1B (scalar plus immediate, strided registers) STNT1B (scalar plus scalar, strided registers) |
|            | Contiguous store non-temporal of doublewords from multiple strided vectors (immediate index, scalar index) | STNT1D (scalar plus immediate, strided registers) STNT1D (scalar plus scalar, strided registers) |
|            | Contiguous store non-temporal of halfwords from multiple strided vectors (immediate index, scalar index)   | STNT1H (scalar plus immediate, strided registers) STNT1H (scalar plus scalar, strided registers) |
|            | Contiguous store non-temporal of words from multiple strided vectors (immediate index, scalar index)       | STNT1W (scalar plus immediate, strided registers) STNT1W (scalar plus scalar, strided registers) |

## C3.4.2.3 Tile slice multi-vector loads and stores

Tile slice load and store instructions transfer bytes between a tile slice and memory.

## Table C3-77 Tile slice multi-vector load and store instructions

| Mnemonic   | Instruction                                                   | See                                   |
|------------|---------------------------------------------------------------|---------------------------------------|
| LD1        | Contiguous load of bytes to 8-bit element ZAtile slice        | LD1B (scalar plus scalar, tile slice) |
| LD1        | Contiguous load of doublewords to 64-bit element ZAtile slice | LD1D (scalar plus scalar, tile slice) |
| LD1        | Contiguous load of halfwords to 16-bit element ZAtile slice   | LD1H (scalar plus scalar, tile slice) |
| LD1        | Contiguous load of quadwords to 128-bit element ZAtile slice  | LD1Q                                  |
| LD1        | Contiguous load of words to 32-bit element ZAtile slice       | LD1W(scalar plus scalar, tile slice)  |

| Mnemonic   | Instruction                                                         | See                                   |
|------------|---------------------------------------------------------------------|---------------------------------------|
| ST1        | Contiguous store of bytes from 8-bit element ZAtile slice           | ST1B (scalar plus scalar, tile slice) |
| ST1        | Contiguous store of doublewords from to 64-bit element ZAtile slice | ST1D (scalar plus scalar, tile slice) |
| ST1        | Contiguous store of halfwords from 16-bit element ZAtile slice      | ST1H (scalar plus scalar, tile slice) |
| ST1        | Contiguous store of quadwords from 128-bit element ZAtile slice     | ST1Q                                  |
| ST1        | Contiguous store of words from 32-bit element ZAtile slice          | ST1W (scalar plus scalar, tile slice) |

## C3.4.3 SVE2.1 quadword loads and stores

## C3.4.3.1 Contiguous quadword loads and stores

Contiguous load or store to/from elements of a vector register from/to the memory address generated by a scalar base and an immediate index, which is multiplied and added to the base address, or a scalar index, which is added to the base address. Inactive elements will not cause a read from Device memory or signal a fault, and are set to zero in the destination vector.

Table C3-78 SME2/SVE2.1 Contiguous quadword load and store instructions

| Mnemonic   | Instruction                                                                | See                                                                                      |
|------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| LD1D       | Contiguous load unsigned doublewords to vector (immediate or scalar index) | LD1D (scalar plus immediate, single register) LD1D (scalar plus scalar, single register) |
| LD1W       | Contiguous load unsigned words to vector (immediate or scalar index)       | LD1W(scalar plus immediate, single register) LD1W(scalar plus scalar, single register)   |
| ST1D       | Contiguous store doublewords from vector (immediate or scalar index)       | ST1D (scalar plus immediate, single register) ST1D (scalar plus scalar, single register) |
| ST1W       | Contiguous store words from vector (immediate or scalar index)             | ST1W (scalar plus immediate, single register) ST1W (scalar plus scalar, single register) |

## C3.4.3.2 Quadword gather and scatter

Gather load or scatter store of quadwords between Active elements of a vector register and memory addresses generated by a vector base plus an unscaled scalar register offset.

Table C3-79 SME2/SVE2.1 Quadword gather and scatter instructions

| Mnemonic   | Instruction             | See   |
|------------|-------------------------|-------|
| LD1Q       | Gather load quadwords   | LD1Q  |
| ST1Q       | Scatter store quadwords | ST1Q  |

## C3.4.3.3 Quadword structure loads and stores

## Table C3-80 SVE2.1 Quadword structure load and store instructions

| Mnemonic   | Instruction                                                                                   | See                                                    |
|------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| LD         | Contiguous load two-quadword structures to two vectors (immediate index, scalar index)        | LD2Q (scalar plus immediate) LD2Q (scalar plus scalar) |
| LD         | Contiguous load three-quadword structures to three vectors (immediate index, scalar index)    | LD3Q (scalar plus immediate) LD3Q (scalar plus scalar) |
| LD         | Contiguous load four-quadword structures to four vectors (immediate index, scalar index)      | LD4Q (scalar plus immediate) LD4Q (scalar plus scalar) |
| ST         | Contiguous store two-quadword structures from two vectors (immediate index, scalar index)     | ST2Q (scalar plus immediate) ST2Q (scalar plus scalar) |
| ST         | Contiguous store three-quadword structures from three vectors (immediate index, scalar index) | ST3Q (scalar plus immediate) ST3Q (scalar plus scalar) |
| ST         | Contiguous store four-quadword structures from four vectors (immediate index, scalar index)   | ST4Q (scalar plus immediate) ST4Q (scalar plus scalar) |