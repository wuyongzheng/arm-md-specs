## C3.3 Loads and stores - SVE, SVE2

SVE vector load and store instructions transfer data in memory to or from elements of one or more vector or predicate transfer registers. SVE also includes vector prefetch instructions that provide read and write hints to the memory system. For SVE predicated load, store, and prefetch instructions, the memory element access size and type that is associated with each vector element is specified by a suffix to the instruction mnemonic, independently of the element size of the transfer registers. For example, LD1SH. The following table shows the supported instruction suffixes for SVE load, store, and prefetch instructions:

| Instruction suffix   | Memory element access size and type                    |
|----------------------|--------------------------------------------------------|
| B                    | Unsigned byte                                          |
| H                    | Unsigned halfword or half-precision floating-point     |
| W                    | Unsigned word or single-precision floating-point       |
| D                    | Unsigned doubleword or double-precision floating-point |
| SB                   | Signed byte                                            |
| SH                   | Signed halfword                                        |
| SW                   | Signed word                                            |

The element size of the transfer registers is always greater than or equal to the memory element access size. When the element size of the transfer registers is strictly greater than the memory element access size, then these are referred to as unpacked data accesses. In the case of unpacked data accesses:

- For load instructions, each element access is sign-extended or zero-extended to fill the vector element, according to its memory element access size and type.
- For store instructions, each vector element is truncated to the memory element access size.

Where the vector element size and the memory element access size are the same, then these are referred to as packed data accesses. Signed access types are not supported for packed data accesses. Packed and unpacked access sizes and types relate to the vector element size of the transfer registers, as defined in the following table:

| Vector element   | Packed access suffix   | Unpacked access suffixes   |
|------------------|------------------------|----------------------------|
| .B               | B                      | -                          |
| .H               | H                      | B, SB                      |
| .S               | W                      | H, SH, B, SB               |
| .D               | D                      | W, SW, H, SH, B, SB        |

For gather-load and scatter-store instructions, the vector element size can only be .S or .D. This means that any non-contiguous memory element access of less than a word is unpacked. Non-contiguous memory element accesses of a word can be either packed or unpacked, depending on the vector element size.

Load, store, and prefetch instructions consist of the following:

- Predicated single vector contiguous element accesses.
- Predicated multiple vector contiguous structure load/store.
- Predicated non-contiguous element accesses.
- Predicated replicating element loads.
- Unpredicated vector register load/store.

- Unpredicated predicate register load/store.
- Non-temporal gather/scatter.

All predicated load instructions zero the Inactive elements of the destination vector, except for Non-fault loads and First-fault loads when the corresponding FFR element is FALSE. When this happens, the content of the corresponding destination vector element is CONSTRAINED UNPREDICTABLE, as described in rule RNGFTJ.

Prefetch instructions provide hints to hardware and do not change architectural state. Therefore, a Governing predicate for a prefetch instruction provides an additional hint which indicates the memory locations to be prefetched. Prefetch instructions require a prefetch operation specifier. SVE prefetch instructions support all of the prefetch operations except for the PLI prefetch operand types.

Load, store, and prefetch instructions that multiply a scalar index register or an index vector element by the memory element access size specify a shift type, followed by a shift amount in bits. The shift type can be one of LSL , SXTW , or UXTW . The shift amount is always Log2 of the memory element access size, in bytes. The shift amount defaults to zero when the memory element access size is a byte, and the shift size can be omitted. The shift type of LSL must be omitted if the shift amount is omitted.

When included as part of the assembler syntax for an instruction, MUL VL indicates that the specified immediate index value is multiplied by the size of the addressed vector or predicate in memory, measured in bytes, irrespective of predication. For a detailed description of the meaning of this assembler syntax for each instruction, see the appropriate subsection below. When used in pseudocode, the symbol VL represents the vector length, measured in bits.

SVE load, store, and prefetch instructions do not support pre-indexed or post-indexed addressing.

## C3.3.1 Predicated single vector contiguous element accesses

Predicated contiguous load and store instructions access memory locations starting from an address that is defined by a scalar base register plus either:

- Ascalar index register.
- An immediate index value that is in the range -8 to 7, inclusive. This defaults to zero if omitted.

The predicated contiguous load and store instructions have two supporting addressing modes:

- Scalar base plus immediate index.
- Scalar base plus scalar index.

Predicated contiguous prefetch instructions address memory locations in a similar manner, with the index being either:

- Ascalar index register.
- An immediate index value that is in the range of -32 to 31, inclusive. This defaults to zero if omitted.

For predicated contiguous load and store SVE instructions:

- The immediate index value is a vector index, not an element index. The immediate index value is multiplied by the number of vector elements, irrespective of predication, and then multiplied by the memory element access size in bytes. The resulting offset is incremented following each element access by the memory element access size.
- The scalar index register value is multiplied by the memory element access size in bytes. The index value is incremented by one after each element access, but the scalar index register is not updated by the instruction.
- When alignment checking is enabled for loads and stores, the value of the base address register must be aligned to the memory element access size.

## Table C3-67 Predicated single vector contiguous element accesses

| Mnemonic   | Instruction                                                                                    | See                                                                                          |
|------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| LD1        | Contiguous load unsigned bytes to vector (scalar plus immediate, scalar plus scalar)           | LD1B (scalar plus immediate, single register) LD1B (scalar plus scalar, single register)     |
| LD1        | Contiguous load doublewords to vector (scalar plus immediate, scalar plus scalar)              | LD1D (scalar plus immediate, single register) LD1D (scalar plus scalar, single register)     |
| LD1        | Contiguous load unsigned halfwords to vector (scalar plus immediate, scalar plus scalar)       | LD1H (scalar plus immediate, single register) LD1H (scalar plus scalar, single register)     |
| LD1        | Contiguous load signed bytes to vector (scalar plus immediate)                                 | LD1SB (scalar plus immediate)                                                                |
| LD1        | Contiguous load signed halfwords to vector (scalar plus immediate)                             | LD1SH (scalar plus immediate)                                                                |
| LD1        | Contiguous load signed words to vector (scalar plus immediate)                                 | LD1SW(scalar plus immediate)                                                                 |
| LD1        | Contiguous load unsigned words to vector (scalar plus immediate)                               | LD1W(scalar plus immediate, single register)                                                 |
| ST1        | Contiguous store bytes from vector (scalar plus immediate, scalar plus scalar)                 | ST1B (scalar plus immediate, single register) ST1B (scalar plus scalar, single register)     |
| ST1        | Contiguous store doublewords from vector (scalar plus immediate, scalar plus scalar)           | ST1D (scalar plus immediate, single register) ST1D (scalar plus scalar, single register)     |
| ST1        | Contiguous store halfwords from vector (scalar plus immediate, scalar plus scalar)             | ST1H (scalar plus immediate, single register) ST1H (scalar plus scalar, single register)     |
| ST1        | Contiguous store words from vector (scalar plus immediate, scalar plus scalar)                 | ST1W (scalar plus immediate, single register) ST1W (scalar plus scalar, single register)     |
| LDFF1      | Contiguous load first-fault unsigned bytes to vector (scalar plus scalar)                      | LDFF1B (scalar plus scalar)                                                                  |
| LDFF1      | Contiguous load first-fault doublewords to vector (scalar plus scalar)                         | LDFF1D (scalar plus scalar)                                                                  |
| LDFF1      | Contiguous load first-fault unsigned halfwords to vector (scalar plus scalar)                  | LDFF1H (scalar plus scalar)                                                                  |
| LDFF1      | Contiguous load first-fault signed bytes to vector (scalar plus scalar)                        | LDFF1SB (scalar plus scalar)                                                                 |
| LDFF1      | Contiguous load first-fault signed halfwords to vector (scalar plus scalar)                    | LDFF1SH (scalar plus scalar)                                                                 |
| LDFF1      | Contiguous load first-fault signed words to vector (scalar plus scalar)                        | LDFF1SW (scalar plus scalar)                                                                 |
| LDFF1      | Contiguous load first-fault unsigned words to vector (scalar plus scalar)                      | LDFF1W (scalar plus scalar)                                                                  |
| LDNF1      | Contiguous load non-fault unsigned bytes to vector                                             | LDNF1B                                                                                       |
| LDNF1      | Contiguous load non-fault doublewords to vector                                                | LDNF1D                                                                                       |
| LDNF1      | Contiguous load non-fault unsigned halfwords to vector                                         | LDNF1H                                                                                       |
| LDNF1      | Contiguous load non-fault signed bytes to vector                                               | LDNF1SB                                                                                      |
| LDNF1      | Contiguous load non-fault signed halfwords to vector                                           | LDNF1SH                                                                                      |
| LDNF1      | Contiguous load non-fault signed words to vector                                               | LDNF1SW                                                                                      |
| LDNF1      | Contiguous load non-fault unsigned words to vector                                             | LDNF1W                                                                                       |
| LDNT1      | Contiguous load non-temporal bytes to vector (scalar plus immediate, scalar plus scalar)       | LDNT1B (scalar plus immediate, single register) LDNT1B (scalar plus scalar, single register) |
| LDNT1      | Contiguous load non-temporal doublewords to vector (scalar plus immediate, scalar plus scalar) | LDNT1D (scalar plus immediate, single register) LDNT1D (scalar plus scalar, single register) |

| Mnemonic   | Instruction                                                                                       | See                                                                                          |
|------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| STNT1      | Contiguous load non-temporal halfwords to vector (scalar plus immediate, scalar plus scalar)      | LDNT1H (scalar plus immediate, single register) LDNT1H (scalar plus scalar, single register) |
| STNT1      | Contiguous load non-temporal words to vector (scalar plus immediate, scalar plus scalar)          | LDNT1W(scalar plus immediate, single register) LDNT1W(scalar plus scalar, single register)   |
|            | Contiguous store non-temporal bytes from vector (scalar plus immediate, scalar plus scalar)       | STNT1B (scalar plus immediate, single register) STNT1B (scalar plus scalar, single register) |
|            | Contiguous store non-temporal doublewords from vector (scalar plus immediate, scalar plus scalar) | STNT1D (scalar plus immediate, single register) STNT1D (scalar plus scalar, single register) |
|            | Contiguous store non-temporal halfwords from vector (scalar plus immediate, scalar plus scalar)   | STNT1H (scalar plus immediate, single register) STNT1H (scalar plus scalar, single register) |
|            | Contiguous store non-temporal words from vector (scalar plus immediate, scalar plus scalar)       | STNT1W (scalar plus immediate, single register) STNT1W (scalar plus scalar, single register) |
| PRF        | Contiguous prefetch bytes (scalar plus immediate, scalar plus scalar)                             | PRFB (scalar plus immediate) PRFB (scalar plus scalar)                                       |
| PRF        | Contiguous prefetch doublewords (scalar plus immediate, scalar plus scalar)                       | PRFD (scalar plus immediate) PRFD (scalar plus scalar)                                       |
| PRF        | Contiguous prefetch halfwords (scalar plus immediate, scalar plus scalar)                         | PRFH (scalar plus immediate) PRFH (scalar plus scalar)                                       |
| PRF        | Contiguous prefetch words (scalar plus immediate, scalar plus scalar)                             | PRFW(scalar plus immediate) PRFW(scalar plus scalar)                                         |

## C3.3.2 Predicated multiple vector contiguous structure load/store

Predicated multiple vector contiguous structure load/store instructions are defined by a scalar base register plus either:

- Ascalar index register.
- An immediate index that is a multiple of N, in the range -8 x Nto 7 x N, inclusive. This defaults to zero if omitted.

The predicated contiguous structure load and store instructions have two supporting addressing modes:

- Scalar base plus immediate index.
- Scalar base plus scalar index.

For the predicated multiple vector contiguous structure load/store SVE instructions:

- The immediate index value is a vector index, not an element index. The immediate index value is multiplied by the number of vector elements, irrespective of predication, and then multiplied by the memory element access size in bytes. The resulting offset is incremented following each element access by the memory element access size.
- The scalar index register value is multiplied by the memory element access size in bytes. Following each element access, the index value is incremented by one but the instruction does not update the scalar index register.
- Each predicate element applies to a single structure in memory, or equivalently to the same element number within each of the two, three, or four transferred vector registers.
- These instructions support packed data accesses only.
- When alignment checking is enabled for loads and stores, the base address must be aligned to the element access size.

## Table C3-68 Predicated multiple vector contiguous structure load/store

| Mnemonic   | Instruction                                                                                                 | See                                                    |
|------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| LD2        | Contiguous load 2-byte structures to two vectors (scalar plus immediate, scalar plus scalar)                | LD2B (scalar plus immediate) LD2B (scalar plus scalar) |
| LD2        | Contiguous load two-doubleword structures to two vectors (scalar plus immediate, scalar plus scalar)        | LD2D (scalar plus immediate) LD2D (scalar plus scalar) |
| LD2        | Contiguous load two-halfword structures to two vectors (scalar plus immediate, scalar plus scalar)          | LD2H (scalar plus immediate) LD2H (scalar plus scalar) |
| LD2        | Contiguous load two-word structures to two vectors (scalar plus immediate, scalar plus scalar)              | LD2W(scalar plus immediate) LD2W(scalar plus scalar)   |
| LD3        | Contiguous load 3-byte structures to three vectors (scalar plus immediate, scalar plus scalar)              | LD3B (scalar plus immediate) LD3B (scalar plus scalar) |
| LD3        | Contiguous load three-doubleword structures to three vectors (scalar plus immediate, scalar plus scalar)    | LD3D (scalar plus immediate) LD3D (scalar plus scalar) |
| LD3        | Contiguous load three-halfword structures to three vectors (scalar plus immediate, scalar plus scalar)      | LD3H (scalar plus immediate) LD3H (scalar plus scalar) |
| LD3        | Contiguous load three-word structures to three vectors (scalar plus immediate, scalar plus scalar)          | LD3W(scalar plus immediate) LD3W(scalar plus scalar)   |
| LD4        | Contiguous load 4-byte structures to four vectors (scalar plus immediate, scalar plus scalar)               | LD4B (scalar plus immediate) LD4B (scalar plus scalar) |
| LD4        | Contiguous load four-doubleword structures to four vectors (scalar plus immediate, scalar plus scalar)      | LD4D (scalar plus immediate) LD4D (scalar plus scalar) |
| LD4        | Contiguous load four-halfword structures to four vectors (scalar plus immediate, scalar plus scalar)        | LD4H (scalar plus immediate) LD4H (scalar plus scalar) |
| LD4        | Contiguous load four-word structures to four vectors (scalar plus immediate, scalar plus scalar)            | LD4W(scalar plus immediate) LD4W(scalar plus scalar)   |
| ST2        | Contiguous store 2-byte structures from two vectors (scalar plus immediate, scalar plus scalar)             | ST2B (scalar plus immediate) ST2B (scalar plus scalar) |
| ST2        | Contiguous store two-doubleword structures from two vectors (scalar plus immediate, scalar plus scalar)     | ST2D (scalar plus immediate) ST2D (scalar plus scalar) |
| ST2        | Contiguous store two-halfword structures from two vectors (scalar plus immediate, scalar plus scalar)       | ST2H (scalar plus immediate) ST2H (scalar plus scalar) |
| ST2        | Contiguous store two-word structures from two vectors (scalar plus immediate, scalar plus scalar)           | ST2W (scalar plus immediate) ST2W (scalar plus scalar) |
| ST3        | Contiguous store 3-byte structures from three vectors (scalar plus immediate, scalar plus scalar)           | ST3B (scalar plus immediate) ST3B (scalar plus scalar) |
| ST3        | Contiguous store three-doubleword structures from three vectors (scalar plus immediate, scalar plus scalar) | ST3D (scalar plus immediate) ST3D (scalar plus scalar) |
| ST3        | Contiguous store three-halfword structures from three vectors (scalar plus immediate, scalar plus scalar)   | ST3H (scalar plus immediate) ST3H (scalar plus scalar) |
| ST3        | Contiguous store three-word structures from three vectors (scalar plus immediate, scalar plus scalar)       | ST3W (scalar plus immediate) ST3W (scalar plus scalar) |
| ST4        | Contiguous store 4-byte structures from four vectors (scalar plus immediate, scalar plus scalar)            | ST4B (scalar plus immediate) ST4B (scalar plus scalar) |
| ST4        | Contiguous store four-doubleword structures from four vectors (scalar plus immediate, scalar plus scalar)   | ST4D (scalar plus immediate) ST4D (scalar plus scalar) |
| ST4        | Contiguous store four-halfword structures from four vectors (scalar plus immediate, scalar plus scalar)     | ST4H (scalar plus immediate) ST4H (scalar plus scalar) |

| Mnemonic   | Instruction                                                                                         | See                                                    |
|------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
|            | Contiguous store four-word structures from four vectors (scalar plus immediate, scalar plus scalar) | ST4W (scalar plus immediate) ST4W (scalar plus scalar) |

## C3.3.3 Predicated non-contiguous element accesses

Predicated non-contiguous element accesses address non-contiguous memory locations that are specified by either:

- Ascalar base register plus a vector of indices or offsets.
- Avector of base addresses plus an immediate byte offset. The immediate byte offset is a multiple of the memory element access size, in the range 0 to 31 times the memory element access size, inclusive, and defaults to zero if omitted.

The predicated non-contiguous element accesses have two supporting addressing modes:

- Scalar base plus 64-bit vector index.
- Scalar base plus 32-bit vector index.
- Vector base plus immediate offset.

For this group of SVE instructions:

- Vector registers used as part of the address must specify a vector element size of 32 bits or 64 bits, .S or .D. For load and store instructions, the transfer register must specify the same vector element size.
- If the index vector register contains 32-bit index values then the lowest 32 bits of each index vector element can either be zero-extended or sign-extended to 64 bits.
- For load and store instructions, the index vector elements are then optionally multiplied by the memory element access size, in bytes, if a shift amount is specified. For prefetch instructions, the index vector elements are always multiplied by the memory element access size, in bytes.
- When alignment checking is enabled for loads and stores, the computed virtual address of each element must be aligned to the memory element access size.

## Table C3-69 Predicated non-contiguous element accesses

| Mnemonic   | Instructions                                                                       | See                                                      |
|------------|------------------------------------------------------------------------------------|----------------------------------------------------------|
| LD1        | Gather load unsigned bytes to vector (scalar plus vector, vector plus immediate)   | LD1B (scalar plus vector) LD1B (vector plus immediate)   |
| LD1        | Gather load doublewords to vector (scalar plus vector, vector plus immediate)      | LD1D (scalar plus vector) LD1D (vector plus immediate)   |
| LD1        | Gather load unsigned halfwords (scalar plus vector, vector plus immediate)         | LD1H (scalar plus vector) LD1H (vector plus immediate)   |
| LD1        | Gather load signed bytes to vector (scalar plus vector, vector plus immediate)     | LD1SB (scalar plus vector) LD1SB (vector plus immediate) |
| LD1        | Gather load signed halfwords to vector (scalar plus vector, vector plus immediate) | LD1SH (scalar plus vector) LD1SH (vector plus immediate) |
| LD1        | Gather load unsigned words to vector (scalar plus vector, vector plus immediate)   | LD1SW(scalar plus vector) LD1SW(vector plus immediate)   |
| ST1        | Scatter store bytes from a vector (scalar plus vector, vector plus immediate)      | ST1B (scalar plus vector) ST1B (vector plus immediate)   |

| Mnemonic   | Instructions                                                                                     | See                                                          |
|------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
|            | Scatter store doublewords from a vector (scalar plus vector, vector plus immediate)              | ST1D (scalar plus vector) ST1D (vector plus immediate)       |
|            | Scatter store halfwords from a vector (scalar plus vector, vector plus immediate)                | ST1H (scalar plus vector) ST1H (vector plus immediate)       |
|            | Scatter store words from a vector (scalar plus vector, vector plus immediate)                    | ST1W (scalar plus vector) ST1W (vector plus immediate)       |
| LDFF1      | Gather load first-fault unsigned bytes to vector (scalar plus vector, vector plus immediate)     | LDFF1B (scalar plus vector) LDFF1B (vector plus immediate)   |
| LDFF1      | Gather load first-fault doublewords to vector (scalar plus vector, vector plus immediate)        | LDFF1D (scalar plus vector) LDFF1D (vector plus immediate)   |
| LDFF1      | Gather load first-fault unsigned halfwords to vector (scalar plus vector, vector plus immediate) | LDFF1H (scalar plus vector) LDFF1SH (vector plus immediate)  |
| LDFF1      | Gather load first-fault signed bytes to vector (scalar plus vector, vector plus immediate)       | LDFF1SB (scalar plus vector) LDFF1SB (vector plus immediate) |
| LDFF1      | Gather load first-fault signed halfwords to vector (scalar plus vector, vector plus immediate)   | LDFF1SH (scalar plus vector) LDFF1SH (vector plus immediate) |
| LDFF1      | Gather load first-fault signed words to vector (scalar plus vector, vector plus immediate)       | LDFF1SW (scalar plus vector) LDFF1SW (vector plus immediate) |
| LDFF1      | Gather load first-fault unsigned words to vector (scalar plus vector, vector plus immediate)     | LDFF1W (scalar plus vector) LDFF1W (vector plus immediate)   |
| PRF        | Gather prefetch bytes (scalar plus vector, vector plus immediate)                                | PRFB (scalar plus vector) PRFB (vector plus immediate)       |
| PRF        | Gather prefetch doublewords (scalar plus vector, vector plus immediate)                          | PRFD (scalar plus vector) PRFD (vector plus immediate)       |
| PRF        | Gather prefetch halfwords (scalar plus vector, vector plus immediate)                            | PRFH (scalar plus vector) PRFH (vector plus immediate)       |
| PRF        | Gather prefetch words (scalar plus vector, vector plus immediate)                                | PRFW(scalar plus vector) PRFW(vector plus immediate)         |

## C3.3.4 Predicated replicating element loads

The load and replicate instructions read one or more contiguous memory locations starting from an address that is defined by a scalar base register plus either:

- Ascalar index register.
- An immediate byte offset.

The predicated contiguous load and store instructions have two supporting addressing modes:

- Scalar base plus immediate offset.
- Scalar base plus scalar index.

This defaults to zero if omitted. For predicated replicating element load SVE instructions:

- When alignment checking is enabled, the base address must be aligned to the memory element access size.

| Mnemonic   | Instructions                                                                               | See                                                        |
|------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------|
| LD1RB      | Load and broadcast unsigned byte to vector                                                 | LD1RB                                                      |
| LD1RD      | Load and broadcast doubleword to vector                                                    | LD1RD                                                      |
| LD1RH      | Load and broadcast unsigned halfword to vector                                             | LD1RH                                                      |
| LD1ROB     | Contiguous load and replicate 32-bytes (scalar plus immediate, scalar plus scalar)         | LD1ROB (scalar plus immediate) LD1ROB (scalar plus scalar) |
| LD1ROD     | Contiguous load and replicate four doublewords (scalar plus immediate, scalar plus scalar) | LD1ROD (scalar plus immediate) LD1ROD (scalar plus scalar) |
| LD1ROH     | Contiguous load and replicate 16 halfwords (scalar plus immediate, scalar plus scalar)     | LD1ROH (scalar plus immediate) LD1ROH (scalar plus scalar) |
| LD1ROW     | Contiguous load and replicate eight words (scalar plus immediate, scalar plus scalar)      | LD1ROW(scalar plus immediate) LD1ROW(scalar plus scalar)   |
| LD1RQB     | Contiguous load and replicate 16 bytes (scalar plus immediate, scalar plus scalar)         | LD1RQB (scalar plus immediate) LD1RQB (scalar plus scalar) |
| LD1RQD     | Contiguous load and replicate two doublewords (scalar plus immediate, scalar plus scalar)  | LD1RQD (scalar plus immediate) LD1RQD (scalar plus scalar) |
| LD1RQH     | Contiguous load and replicate eight halfwords (scalar plus immediate, scalar plus scalar)  | LD1RQH (scalar plus immediate) LD1RQH (scalar plus scalar) |
| LD1RQW     | Contiguous load and replicate four words (scalar plus immediate, scalar plus scalar)       | LD1RQW(scalar plus immediate) LD1RQW(scalar plus scalar)   |
| LD1RSB     | Load and broadcast signed byte to vector                                                   | LD1RSB                                                     |
| LD1RSH     | Load and broadcast signed halfword to vector                                               | LD1RSH                                                     |
| LD1RSW     | Load and broadcast signed word to vector                                                   | LD1RSW                                                     |
| LD1RW      | Load and broadcast unsigned word to vector                                                 | LD1RW                                                      |

## C3.3.5 Unpredicated vector register load/store

The unpredicated vector register load, LDR, and store, STR, instructions transfer a single vector register from or to memory locations that are specified by a scalar base register plus an immediate index value that is in the range -256 to 255, inclusive. The immediate index value defaults to zero if omitted.

The unpredicated vector register load/store instructions have one supporting addressing mode:

- Scalar base plus immediate index.

For the unpredicated vector register load/store SVE instructions:

- The immediate index value is a vector index, not an element index. The immediate index value is multiplied by the current vector register length in bytes.
- The data transfer is performed as a contiguous stream of byte accesses in ascending element order, without endianness conversion.
- When alignment checking is enabled for loads and stores, the base address must be 16-byte aligned.

## Table C3-71 Unpredicated vector register load/store

| Mnemonic   | Instruction                    | See          |
|------------|--------------------------------|--------------|
| LDR        | Load vector register (vector)  | LDR(vector)  |
| STR        | Store vector register (vector) | STR (vector) |

## C3.3.6 Unpredicated predicate register load/store

The unpredicated predicate register load, LDR, and store, STR, instructions transfer a single predicate register from or to memory locations that are specified by a scalar base register plus an immediate index value that is in the range -256 to 255, inclusive. The immediate index value defaults to zero if omitted.

The unpredicated predicate register load/store instructions have one supporting addressing mode:

- Scalar base plus immediate index.

For unpredicated predicate register load/store SVE instructions:

- The immediate index value is a predicate index, not an element index. The immediate index value is multiplied by the current predicate register length, in bytes.
- The data transfer is performed as a contiguous stream of byte accesses, each byte containing 8 consecutive predicate bits, in ascending bit and element order, without endian conversion.
- When alignment checking is enabled for loads and stores, the base address must be 2-byte aligned.

Table C3-72 Unpredicated predicate register load/store

| Mnemonic   | Instruction                          | See             |
|------------|--------------------------------------|-----------------|
| LDR        | Load predicate register (predicate)  | LDR(predicate)  |
| STR        | Store predicate register (predicate) | STR (predicate) |

## C3.3.7 Non-temporal gather/scatter

The non-temporal gather load and scatter store instructions provide a hint to the memory system that the data structure being accessed has a low reuse frequency. The memory system can use the hint to avoid retaining the data or evicting more frequently-used data from the caches.

These instructions support a single addressing mode consisting of 64-bit or 32-bit vector base addresses plus an unscaled 64-bit scalar offset that defaults to the zero register, XZR. Other addressing modes can be constructed using extra instructions.

Table C3-73 Non-temporal gather load and scatter store instructions

| Mnemonic   | Instruction                                   | See                         |
|------------|-----------------------------------------------|-----------------------------|
| LDNT1B     | Gather load non-temporal unsigned bytes       | LDNT1B (vector plus scalar) |
| LDNT1D     | Gather load non-temporal unsigned doublewords | LDNT1D (vector plus scalar) |
| LDNT1H     | Gather load non-temporal unsigned halfwords   | LDNT1H (vector plus scalar) |

| Mnemonic   | Instruction                               | See                         |
|------------|-------------------------------------------|-----------------------------|
| LDNT1SB    | Gather load non-temporal signed bytes     | LDNT1SB                     |
| LSNT1SH    | Gather load non-temporal signed halfwords | LDNT1SH                     |
| LSNT1SW    | Gather load non-temporal signed words     | LDNT1SW                     |
| LDNT1W     | Gather load non-temporal unsigned words   | LDNT1W(vector plus scalar)  |
| STNT1B     | Scatter store non-temporal bytes          | STNT1B (vector plus scalar) |
| STNT1D     | Scatter store non-temporal doublewords    | STNT1D (vector plus scalar) |
| STNT1H     | Scatter store non-temporal halfwords      | STNT1H (vector plus scalar) |
| STNT1W     | Scatter store non-temporal words          | STNT1W (vector plus scalar) |