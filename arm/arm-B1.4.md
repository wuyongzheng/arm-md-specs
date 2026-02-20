## B1.4 The Scalable Vector and Scalable Matrix Extensions (SVE &amp; SME)

This section contains:

- Maximum implemented SVE vector lengths.
- Configurable SVE vector lengths.
- Treatment of SVE scalable vector registers.
- SVE writes of scalar values to registers.
- Vector predication.
- Streaming SVE mode.
- About PSTATE.ZA.
- ZAstorage.
- ZAarray vector access.
- ZAtile access.
- ZAstorage layout.
- SME2 Multi-vector operands.
- SME2 ZT0 register.

## B1.4.1 Maximum implemented SVE vector lengths

RQSVCQ

There are the following IMPLEMENTATION DEFINED vector lengths for the SVE scalable vector registers, Z0-Z31:

- A Maximum implemented Streaming SVE vector length .
- A Maximum implemented Non-streaming SVE vector length .

For each IMPLEMENTATION DEFINED vector length, all the following apply:

- The smallest architecturally defined maximum length is 128 bits.
- The largest architecturally defined maximum length is 2048 bits.
- The length is a power of two.

IGZRPL There is no requirement for the Maximum implemented Streaming SVE vector length to be greater than or equal to the Maximum Non-streaming implemented SVE vector length.

ISGCVT

Where this architecture specification uses the term Maximum implemented SVE vector length , it means:

- The Maximum implemented Streaming SVE vector length when the PE is in Streaming SVE mode .
- The Maximum implemented Non-streaming SVE vector length otherwise.

See also:

- Z0-Z31.
- Configurable SVE vector lengths.

## B1.4.2 Configurable SVE vector lengths

RKFTHG

IQQRNR

There are the following configurable vector lengths for the SVE scalable vector registers, Z0-Z31:

- Effective Streaming SVE vector length (SVL).
- Effective Non-streaming SVE vector length (NSVL) .

SMCR\_ELx.LEN requests an SVL. The architecturally defined SVL set is all powers of two from 128 to 2048 bits inclusive. Implementing any subset is permitted, up to and including the Maximum implemented Streaming SVE vector length . The subset is not required to be contiguous and is not required to start at 128 bits. Implementing a single SVL is permitted.

| I NWYBP   | ZCR_ELx.LEN requests an NSVL. The architecturally defined NSVL set is all powers of two from 128 to 2048 bits inclusive. An implementation is required to implement all architecturally defined values up to and including the Maximum implemented Non-streaming SVE vector length .                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I WDKGR   | An implementation is permitted to implement an SVL set that does not overlap with the implemented NSVL set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R GWVHP   | When SMCR_ELx.LEN requests an SVL, the PE selects an SVL according to the steps described in the SMCR_ELx.LEN field descriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R MMCTJ   | When ZCR_ELx.LEN requests an NSVL, the PE selects an NSVL according to the steps described in the ZCR_ELx.LEN field descriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I VCQBB   | Where this architecture specification uses the term Effective SVE vector length (VL) , it means: • SVL when the PE is in Streaming SVE mode . • NSVL otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R PXZTM   | When executing at an Exception level where VLis less than the Maximum implemented SVE vector length , bits VLand higher in the SVE scalable vector registers, and bits VL÷8and higher in the SVE predicate registers and FFR, are inaccessible.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R YRPDH   | When VLis increased, it is CONSTRAINED UNPREDICTABLE whether the previously inaccessible bits that become accessible have:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I HGYPV   | VLmight increase because of an explicit action such as writing to SMCR_ELx.LEN or ZCR_ELx.LEN, or an implicit action such as taking an exception to an Exception level with a less constrained VL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| I PDLWX   | When changing VL, the contents in the bits that consistently remain accessible remain the same.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R KXKNK   | VLat Exception level ELx is 128 bits if all the following are true: • SVE instructions are disabled or trapped at ELx, or are not available because ELx is using AArch32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R DMBPN   | When taking an exception to a target Exception level, if SVE, SME, and floating-point instructions are disabled, trapped, or not available at all Exception levels below the target Exception level, for the current Security state, the SVE register state at the target Exception level is preserved.                                                                                                                                                                                                                                                                                                                                                                                               |
| I FMWZZ   | When VLis increased, steps must be taken to ensure the newly accessible area does not expose values unrelated to another body of software in a different trust or security scope. This might be achieved by, for example, ensuring that the previously inaccessible bits in the SVE Z, P, and FFR registers, and the SMEZAstorage and ZT0 register, are reset to zero before they are next used.                                                                                                                                                                                                                                                                                                      |
| I BRMMV   | System software provides a maximum VLto lower-privileged software, which might further constrain the VL. However, system software must initialize and context switch values consistent with the maximum VLit provides and should not make assumptions about any smaller length that lower-privileged software is using. For example, if a hypervisor exposes a VLof 512 to a VM, that VMmight choose to constrain VLto 256. The hypervisor must still save and restore 512-bit vectors to prevent leakage of values between VMs, because the VMmight later raise its SVL to 512 and must not be able to observe values created by other software in the newly visible upper portion of the registers. |
|           | See also:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|           | • Maximum implemented SVE vector lengths.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## B1.4.3 Treatment of SVE scalable vector registers

| I GKWYJ   | Unless stated otherwise in an instruction description, SVE instructions treat an SVE scalable vector register as containing one or more vector elements of equal size.                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I CDKJQ   | SVE instructions can process vector elements in parallel, unless an instruction description states otherwise.                                                                                                        |
| R CJZLM   | If the order of operations performed by an SVE instruction on vector or predicate elements has observable significance, elements are processed in increasing element number order.                                   |
| R KHDBN   | When an SVE instruction treats an SVE scalable vector register as containing multiple vector elements, the element size is encoded in the opcode of the instruction. The element size is 8, 16, 32, 64, or 128 bits. |
| R WKYLB   | When the Effective SVE vector length (VL) at the current Exception level is greater than 128 bits, any AArch64 instruction that writes to an 128-bit SIMD&FP register, V0-V31, sets bits [VL-1:128] to zero.         |

## B1.4.4 SVE writes of scalar values to registers

| I ZDLGD   | Certain SVE instructions generate a scalar result that is written to an AArch64 general-purpose register or to element[0] of a vector register.                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R HNVTM   | When an SVE instruction generates a scalar result of width Nbits, the instruction places the result in bits [N-1:0] of the destination register.                                                                  |
| R QCLSH   | When an SVE instruction generates a scalar result of width Nbits, and Nis less than the maximum accessible destination register width RW, the instruction sets bits [RW-1:N] of the destination register to zero. |

## B1.4.5 Vector predication

RJFJZX

IHWRFM

There are the following vector predication concepts:

- Predicate-as-mask, if FEAT\_SVE or FEAT\_SME is implemented.
- Predicate-as-counter, if FEAT\_SME2 or FEAT\_SVE2p1 is implemented.

The assembler syntax for a predicate register is of the form:

- Pg for predicate-as-mask.
- PNg for predicate-as-counter.

Pg and PNg refer to the same SVE predicate register.

The remainder of this section contains:

- Predicate-as-mask.
- Predicate-as-counter.
- SVE predicated instructions.

## B1.4.5.1 Predicate-as-mask

| I JHCTW   | Most SVE instructions interpret SVE predicate registers as a predicate-as-mask encoding.                                                                                                  |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XMPLM   | Apredicate-as-mask encoding is divided into 1-bit, 2-bit, 4-bit, or 8-bit predicate elements . Each predicate element corresponds to a vector element in an SVE scalable vector register. |
| R XVRKX   | Unless stated otherwise in an instruction description, SVE instructions treat an SVE predicate register as containing one or more predicate elements of equal size.                       |
| R XCZQR   | When an SVE instruction treats an SVE predicate register as containing multiple predicate elements, the element size is encoded in the opcode of the instruction.                         |

RHRPMD

If the lowest-numbered bit of a predicate element is 0, the value of the predicate element is FALSE.

RDNMFH

If the lowest-numbered bit of a predicate element is 1, the value of the predicate element is TRUE.

RLTGQC

For SVE instructions that generate predicate-as-mask encodings, if all the following are true, all bits except the lowest-numbered bit of each destination predicate element are set to zero:

- The instructions are not used to move and permute predicate elements.

- The instructions are not predicate logical operations.

RHBMLS

For SVE instructions that consume predicate-as-mask encodings, if all the following are true, all bits except the lowest-numbered bit of each source predicate element are ignored on reads:

- The instructions are not used to move and permute predicate elements.

- The instructions are not predicate logical operations.

## B1.4.5.2 Predicate-as-counter

RDSFKR

SME2 and SVE2.1 multi-vector instructions interpret bits[15:0] of SVE predicate registers as a predicate-as-counter encoding :

## Table B1-4 Predicate-as-counter encoding

| Bit[15] Invert   | Bits[14:(LSZ+1)] a Element count b   | Bits[LSZ:0] Element size   | Meaning                                 |
|------------------|--------------------------------------|----------------------------|-----------------------------------------|
| 0bX              | 0bXXXXXXXXXXXXXX                     | 0b1                        | Byte-size elements                      |
| 0bX              | 0bXXXXXXXXXXXXX                      | 0b10                       | Halfword-size elements                  |
| 0bX              | 0bXXXXXXXXXXXX                       | 0b100                      | Word-size elements                      |
| 0bX              | 0bXXXXXXXXXXX                        | 0b1000                     | Doubleword-size elements                |
| 0bX              | 0bXXXXXXXXXXX                        | 0b0000                     | Any-size elements. All FALSE predicate. |

## Element size, bits[LSZ:0]

For values shown in Table B1-4 other than 0b0000 :

- Number of trailing zeroes = log2(element size in bytes). For example, 2 trailing zeroes = log2(4 bytes). This means word-size elements.

## Element count, bits[14:(LSZ+1)]

An unsigned integer value:

- The number of consecutive elements, starting from element 0, that are TRUE or FALSE according to bit[15].

## Invert, bit[15]

0b0

[14:(LSZ+1)] is holding the number of TRUE elements. All other elements are FALSE.

0b1

[14:(LSZ+1)] is holding the number of FALSE elements. All other elements are TRUE.

The maximum number of elements that the predicate-as-counter encoding can count is four vectors of byte elements, where the length of each vector is the largest architecturally defined length, 2048 bits:

IZPLKP

## Table B1-5

| Bit[15] Invert   | Bits[14:(LSZ+1)] Element count                                                                                                                                                                                                                                                                                               | Bits[LSZ:0] Element size                                                                                                                                                                                                                                                                                                     | Total number of bits                                                                                                                                                                                                                                                                                                         |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 bit            | 4 reserved bits. 10 count bits. 10 count bits can count 1024 elements, which is the number of byte elements in four 2048-bit long vectors.                                                                                                                                                                                   | 1 bit                                                                                                                                                                                                                                                                                                                        | 16 bits                                                                                                                                                                                                                                                                                                                      |
| D BJMYH          | The canonical all-FALSE predicate-as-counter encoding has an element count of zero, with the invert bit set to 0 and an element size field set to 0b0000 .                                                                                                                                                                   | The canonical all-FALSE predicate-as-counter encoding has an element count of zero, with the invert bit set to 0 and an element size field set to 0b0000 .                                                                                                                                                                   | The canonical all-FALSE predicate-as-counter encoding has an element count of zero, with the invert bit set to 0 and an element size field set to 0b0000 .                                                                                                                                                                   |
| D JGSYR          | The canonical all-TRUE predicate-as-counter encoding has an element count of zero, with the invert bit set to 1 and a nonzero element size field determined by the generating instruction.                                                                                                                                   | The canonical all-TRUE predicate-as-counter encoding has an element count of zero, with the invert bit set to 1 and a nonzero element size field determined by the generating instruction.                                                                                                                                   | The canonical all-TRUE predicate-as-counter encoding has an element count of zero, with the invert bit set to 1 and a nonzero element size field determined by the generating instruction.                                                                                                                                   |
| R YCRMW          | If the Effective SVE vector length (VL) is greater than 128 bits, then an instruction generating a predicate-as-counter encoding sets bits 16 and higher to zero.                                                                                                                                                            | If the Effective SVE vector length (VL) is greater than 128 bits, then an instruction generating a predicate-as-counter encoding sets bits 16 and higher to zero.                                                                                                                                                            | If the Effective SVE vector length (VL) is greater than 128 bits, then an instruction generating a predicate-as-counter encoding sets bits 16 and higher to zero.                                                                                                                                                            |
| R SGVTC          | If VLis greater than 128 bits, then an instruction consuming a predicate-as-counter encoding ignores bits 16 and higher.                                                                                                                                                                                                     | If VLis greater than 128 bits, then an instruction consuming a predicate-as-counter encoding ignores bits 16 and higher.                                                                                                                                                                                                     | If VLis greater than 128 bits, then an instruction consuming a predicate-as-counter encoding ignores bits 16 and higher.                                                                                                                                                                                                     |
| R YSTVC          | An instruction consuming a predicate-as-counter encoding uses the least significant bits of the element count field required to count the number of bytes in VLtimes four. The instruction ignores the more significant bits in the element count field. Table B1-6 gives an example for VL=512 bits and byte-size elements: | An instruction consuming a predicate-as-counter encoding uses the least significant bits of the element count field required to count the number of bytes in VLtimes four. The instruction ignores the more significant bits in the element count field. Table B1-6 gives an example for VL=512 bits and byte-size elements: | An instruction consuming a predicate-as-counter encoding uses the least significant bits of the element count field required to count the number of bytes in VLtimes four. The instruction ignores the more significant bits in the element count field. Table B1-6 gives an example for VL=512 bits and byte-size elements: |

## Table B1-6

| Bit[15]Invert   | Bits[14:(LSZ+1)] Element count                                                                                                                                                                                                                                               | Bits[LSZ:0] Element size   |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 1 bit           | 4 reserved bits, bits[14:11]. The instruction ignores these. 2 bits, bits[10:9]. The instruction ignores these. 8 count bits, bits[8:1]. The instruction uses these. 8 count bits can count 256 elements, which is the number of byte elements in four 512-bit long vectors. | 1 bit                      |

## See also:

- P0-P15.
- Configurable SVE vector lengths.

## B1.4.5.3 SVE predicated instructions

| I VKHDR   | If an instruction supports predication, it is known as a predicated instruction .                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FNFRN   | The predicate operand that is used to determine the Active elements of a predicated instruction is known as the Governing predicate .                                             |
| I SVYXB   | An instruction that does not have a Governing predicate operand and implicitly treats all other vector and predicate elements as Active is known as an unpredicated instruction . |
| I KNKBN   | Many predicated instructions can only use P0-P7 as the Governing predicate.                                                                                                       |
| R LZVFJ   | When a Governing predicate element is TRUE, the corresponding element in other vector or predicate operands is an Active element.                                                 |
| R CNFLG   | When a Governing predicate element is FALSE, the corresponding element in other vector or predicate operands is an Inactive element .                                             |

The AArch64 Application Level Programmers' Model B1.4 The Scalable Vector and Scalable Matrix Extensions (SVE &amp; SME)

| R CBYJH   | Predicated instructions process Active elements.                                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| R LDXSF   | Predicated instructions do not process Inactive elements.                                                                                |
| R GJLPZ   | Unpredicated instructions process all elements in their vector or predicate operands.                                                    |
| R WLQBD   | When a predicated instruction writes to a vector destination register or a predicate destination register, one of the following happens: |
| I QBHRN   | Zeroing predication is performed when the Inactive elements in the destination register are set to zero.                                 |
| I YPYRF   | Merging predication is performed when Inactive elements in the destination register retain their previous value.                         |

## B1.4.6 Streaming SVE mode

RXDPXS APEwith FEAT\_SME has Streaming SVE mode .

## IZTTNW

In Streaming SVE mode:

- SMEand SME2 instructions access Streaming SVE register state , which comprises:

- SVE scalable vector registers, Z0 to Z31.

- SVE predicate registers, P0 to P15.

- SVE First Fault register, FFR, if FEAT\_SME\_FA64 is implemented and enabled at the current Exception level.

- PSTATE.ZA can be toggled, to enable and disable the ZA storage and ZT0 register as required.

RRSWFQ When the Effective value of PSTATE.SM is changed by any method from 0 to 1, an entry to Streaming SVE mode is performed, and all implemented bits of Streaming SVE register state are set to zero.

RKFRQZ When the Effective value of PSTATE.SM is changed by any method from 1 to 0, an exit from Streaming SVE mode is performed, and in the newly-entered mode, all implemented bits of the SVE scalable vector registers, SVE predicate registers, and FFR, are set to zero.

INHNFF A legal instruction is an instruction that the architecture permits execution of when PSTATE.{SM, ZA} are in the required state, unless its execution at the current Exception level is prevented by a configurable trap or enable.

- IHZFSG instruction is an instruction whose attempted execution by a PE when PSTATE.SM and PSTATE.ZA are not

An illegal in the required state causes an SME illegal instruction exception to be taken, unless its execution at the current Exception level is prevented by a higher-priority configurable trap or enable.

## RVJZBC

## RXBBFD

In Streaming SVE mode:

- Streaming SVE register state is valid, and SME and SME2 instructions that access it are legal.
- When PSTATE.ZA is 1, SME and SME2 instructions that access ZA storage or the ZT0 register are legal.
- SMEand SME2 instructions that do not access ZA storage or the ZT0 register are legal.
- Legal instructions that access the SVE scalar vector registers or their correspondingly numbered SIMD&amp;FP registers access Streaming SVE register state.
- The following are illegal if FEAT\_SME\_FA64 is not implemented or not enabled at the current Exception level:
- -Some SVE and SVE2 instructions. The individual instruction descriptions in SVE Instruction Descriptions describe which are illegal.
- -All those instructions that call the AArch64.CheckFPAdvSIMDEnabled() function.

When the PE is not in Streaming SVE mode:

- Streaming SVE register state is not valid, and SME and SME2 instructions that access it are illegal.
- When PSTATE.ZA is 1:
- -SME LDR (array vector), STR (array vector), and ZERO (tiles) instructions that access ZA storage are legal. All other instructions that access ZA storage are illegal.

- -SME2 LDR (table), STR (table), and ZERO (table) instructions that access the ZT0 register are legal. All other instructions that access the ZT0 register are illegal.
- ITDSPN In Streaming SVE mode, the following instructions might be significantly delayed if FEAT\_SME\_FA64 is not implemented or not enabled at the current Exception level:
- Instructions which are dependent on results generated from vector or SIMD&amp;FP register sources written to a general-purpose destination register, a predicate destination register, or the NZCV condition flags.

The Operational information sections of instruction descriptions in A64 Advanced SIMD and Floating-point Instruction Descriptions and SVE Instruction Descriptions describe which instructions are affected.

- IMHTLZ When the Effective value of PSTATE.SM is changed by any method from 0 to 1 or from 1 to 0, the FPSR is set to the value 0x0000\_0000\_0800\_009f , setting all the cumulative status bits to 1.
- IYTZVD Statements which refer to the value of the SVE scalable vector registers, Z0-Z31, implicitly also refer to the lower bits of those registers accessed by the SIMD&amp;FP register names V0-V31, Q0-Q31, D0-D31, S0-S31, H0-H31, and B0-B31.

See also:

- Registers in AArch64 Execution state.
- About PSTATE.ZA.
- Accessing PSTATE fields at EL0.
- Floating-point behaviors in Streaming SVE mode.

## B1.4.7 About PSTATE.ZA

- IHVKTL PSTATE.ZA enables ZA storage and, if FEAT\_SME2 is implemented, the ZT0 register.
- RJHMYL When PSTATE.ZA is 0, the contents of ZA storage and the ZT0 register are not valid, and SME and SME2 instructions that access them are illegal .
- RSFWMY When PSTATE.ZA is 1, the contents of ZA storage and the ZT0 register are valid and are retained by hardware irrespective of whether the PE is in Streaming SVE mode , and:
- SME LDR (array vector), STR (array vector), and ZERO (tiles) instructions that access ZA storage are legal.
- SME2 LDR (table), STR (table), and ZERO (table) instructions that access the ZT0 register are legal.
- When the PE is in Streaming SVE mode, all other SME and SME2 instructions that access ZA storage or the ZT0 register are legal.
- RYRZRM When PSTATE.ZA is changed by any method from 0 to 1, all implemented bits of ZA storage and the ZT0 register are set to zero.
- ILRDZR When PSTATE.ZA is changed from 1 to 0, there is no architecturally defined effect on ZA storage and the ZT0 register, because the contents of ZA storage and the ZT0 register cannot be observed when PSTATE.ZA is 0.
- IQWCJS When PSTATE.ZA is changed from 0 to 1, or from 1 to 0, there is no effect on the SVE scalable vector registers, SVE predicate registers, and FPSR if PSTATE.SM is not changed.

See also:

- Streaming SVE mode.
- ZAstorage.
- SME2 ZT0 register.

## B1.4.8 ZA storage

RFFWLL

APEwith FEAT\_SME has ZA storage .

DJBVYJ

There are the following terms for the number of elements in a vector of SVL bits:

SVLB

The number of byte elements, SVL ÷ 8.

SVLH

The number of halfword elements, SVL ÷ 16.

SVLS

The number of word elements, SVL ÷ 32.

SVLD

The number of doubleword elements, SVL ÷ 64.

SVLQ The number of quadword elements, SVL ÷ 128.

RSSXPL

ZAstorage is architectural register state consisting of a two-dimensional ZA array of [SVLB × SVLB] bytes.

## See also:

- About PSTATE.ZA.
- Accessing PSTATE fields at EL0.
- Streaming SVE mode.

## B1.4.9 ZA array vector access

| R FFWNB   | The ZA array can be accessed as vectors of SVL bits.                                                                                                                                                                              |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D PPPCM   | An untyped vector access to the ZA array is represented by ZA[ N ], where N is in the range 0 to SVL B -1 inclusive.                                                                                                              |
| D DTVZN   | InSME LDR (array vector) and STR (array vector) instructions, an untyped ZA array vector is selected by the sum of a 32-bit general-purpose vector select registerW v and an immediate vector select offset offs , modulo SVL B . |
| D YXHFR   | The preferred disassembly for an untyped ZA array vector is ZA[W v , offs ], where offs is an immediate in the range 0-15 inclusive.                                                                                              |
| D CRJPC   | The ZA array can be accessed as vectors of 8-bit, 16-bit, 32-bit, 64-bit, or 128-bit elements.                                                                                                                                    |
| D WMVZT   | An elementwise vector access to the ZA array is indicated by appending a vector index '[ N ]' to the ZA array name and element size qualifier, where N is in the range 0 to SVL B -1 inclusive, as follows:                       |
|           | • An 8-bit element vector access to the ZA array is represented by ZA.B[ N ].                                                                                                                                                     |
|           | • A16-bit element vector access to the ZA array is represented by ZA.H[ N ].                                                                                                                                                      |
|           | • A32-bit element vector access to the ZA array is represented by ZA.S[ N ].                                                                                                                                                      |
|           | • A64-bit element vector access to the ZA array is represented by ZA.D[ N ].                                                                                                                                                      |
|           | • A128-bit element vector access to the ZA array is represented by ZA.Q[ N ].                                                                                                                                                     |

## B1.4.10 ZA tile access

| D VSVMX   | A ZA tile is a square, two-dimensional sub-array of elements within the ZA array.                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I WLRTV   | Depending on the element size with which it is accessed, the ZAarray is treated as containing one or more ZA tiles, as described in the following sections. |
| D DWMYT   | A ZA tile is indicated by appending the tile number to the ZA name.                                                                                         |
| D ZGBHT   | A ZA tile slice is a one-dimensional set of horizontally or vertically contiguous elements within a ZA tile.                                                |
| R PZNWB   | Avector access to a tile reads or writes a ZA tile slice.                                                                                                   |
| I NFXHH   | A ZA tile can be accessed as vectors of 8-bit, 16-bit, 32-bit, 64-bit, or 128-bit elements.                                                                 |

The AArch64 Application Level Programmers' Model B1.4 The Scalable Vector and Scalable Matrix Extensions (SVE &amp; SME)

| I YZDBS   | A ZA tile can be accessed as horizontal slices of SVL bits.                                                                                                                                                                                                                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GPVSZ   | A ZA tile is accessed as horizontal slices if the Vfield in the accessing instruction opcode is 0.                                                                                                                                                                                                                                                                                      |
| D TRHTX   | An access to horizontal tile slices is indicated by an 'H' suffix on the ZA tile name.                                                                                                                                                                                                                                                                                                  |
| I HBYTT   | A ZA tile can be accessed as vertical slices of SVL bits.                                                                                                                                                                                                                                                                                                                               |
| R GPPPK   | A ZA tile is accessed as vertical slices if the Vfield in the accessing instruction opcode is 1.                                                                                                                                                                                                                                                                                        |
| D WSBVG   | An access to vertical tile slices is indicated by a suffix on the ZA tile name.                                                                                                                                                                                                                                                                                                         |
| R TWWTL   | In SMEinstructions, the tile slice is selected by the sum of a 32-bit general-purpose slice index registerW s and an immediate slice index offset offs , modulo the number of slices in the named tile.                                                                                                                                                                                 |
|           | B1.4.10.1 Accessing an 8-bit element ZA tile                                                                                                                                                                                                                                                                                                                                            |
| D HMSNH   | An 8-bit element ZA tile is indicated by a '.B' qualifier following the tile name.                                                                                                                                                                                                                                                                                                      |
| D NLCNH   | There is a single tile named ZA0.B which consists of [SVL B × SVL B ] 8-bit elements and occupies all of the ZA storage.                                                                                                                                                                                                                                                                |
| R NBSMJ   | An access to a horizontal or vertical 8-bit element ZAtile slice reads or writes SVL B 8-bit elements.                                                                                                                                                                                                                                                                                  |
| D NMHLM   | An access to a horizontal or vertical 8-bit element ZAtile slice is indicated by appending a slice index '[ N ]' to the tile name, direction suffix, and qualifier. For example, where N is in the range 0 to SVL B -1 inclusive: • ZA0H.B[ N ] indicates a horizontal 8-bit element ZA tile slice selection. • ZA0V.B[ N ] indicates a vertical 8-bit element ZA tile slice selection. |
| I JVTNY   | Horizontal and vertical ZA0.B slice accesses are illustrated in the following diagram for SVL of 256 bits:                                                                                                                                                                                                                                                                              |

<!-- image -->

Figure B1-4 Horizontal and vertical ZA0.B slice for SVL of 256

| R DCSDX   | An access to the horizontal slice ZA0H.B[ N ] reads or writes the SVL B bytes in ZA array vector ZA.B[ N ].                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FHYSQ   | An access to the vertical slice ZA0V.B[ N ] reads or writes the 8-bit element [ N ] within each horizontal slice of ZA0.B.                                                                                                                        |
| D CDDVV   | The preferred disassembly is: • ZA0H.B[W s , offs ], for a horizontal 8-bit element ZA tile slice selection. • ZA0V.B[W s , offs ], for a vertical 8-bit element ZA tile slice selection. Where offs is an immediate in the range 0-15 inclusive. |
| D LNXPD   | A16-bit element ZA tile is indicated by a '.H' qualifier following the tile name.                                                                                                                                                                 |
| D GWZDM   | There are two tiles named ZA0.H and ZA1.H. Each tile consists of [SVL H × SVL H ] 16-bit elements, and occupies half of the ZA storage.                                                                                                           |

| R NMGXG   | An access to a horizontal or vertical 16-bit element ZAtile slice reads or writes SVL H 16-bit elements.                                                                                                                                                                                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D DHKMC   | An access to a horizontal or vertical 16-bit element ZAtile slice is indicated by appending a slice index '[ N ]' to the tile name, direction suffix, and qualifier. For example, where t is 0 or 1, and N is in the range 0 to SVL H -1 inclusive: • ZA t H.H[ N ] indicates a horizontal 16-bit element ZA tile slice selection. • ZA t V.H[ N ] indicates a vertical 16-bit element ZA tile slice selection. |
| I ZSWJW   | Horizontal and verticalZA t .H slice accesses, where t is 0 or 1, are illustrated in the following diagram for SVL of 256 bits:                                                                                                                                                                                                                                                                                 |

<!-- image -->

Figure B1-5 Horizontal and vertical ZAt.H slice for SVL of 256

| R BTLQC   | An access to the horizontal sliceZA t H.H[ N ] reads or writes the SVL H 16-bit elements in ZA array vector ZA.H[ t + 2 * N ].                                                                                                                                                     |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R NGJBJ   | An access to the vertical sliceZA t V.H[ N ] reads or writes the 16-bit element [ N ] within each horizontal slice ofZA t .H.                                                                                                                                                      |
| D RHQJT   | The preferred disassembly is as follows: • ZA t H.H[W s , offs ], for a horizontal 16-bit element ZA tile slice selection. • ZA t V.H[W s , offs ], for a vertical 16-bit element ZA tile slice selection. Where t is 0 or 1, and offs is an immediate in the range 0-7 inclusive. |
| D HBKZV   | A32-bit element ZA tile is indicated by a '.S' qualifier following the tile name.                                                                                                                                                                                                  |
| D RDRRT   | There are four tiles named ZA0.S, ZA1.S, ZA2.S, and ZA3.S. Each tile consists of [SVL S × SVL S ] 32-bit elements, and occupies a quarter of the ZA storage.                                                                                                                       |
| R XFPPL   | An access to a horizontal or vertical 32-bit element ZAtile slice reads or writes SVL S 32-bit elements.                                                                                                                                                                           |

DJFPSJ

An access to a horizontal or vertical 32-bit element ZA tile slice is indicated by appending a slice index '[ N ]' to the tile name, direction suffix, and qualifier. For example, where t is 0, 1, 2, or 3, and N is in the range 0 to SVLS-1 inclusive:

- ZA t H.S[ N ] indicates a horizontal 32-bit element ZA tile slice selection.

- ZA t V.S[ N ] indicates a vertical 32-bit element ZA tile slice selection.

ISZXZR

Horizontal and vertical ZA t .S slice accesses, where t is 0, 1, 2, or 3, are illustrated in the following diagram for SVL of 256 bits:

<!-- image -->

Figure B1-6 Horizontal and vertical ZAt.S slice for SVL of 256

| R JBJZY   | An access to the horizontal sliceZA t H.S[ N ] reads or writes the SVL S 32-bit elements in ZA array vector ZA.S[ t + 4 * N ].                                                                                                                                                                                                                                                                                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GBYSJ   | An access to the vertical sliceZA t V.S[ N ] reads or writes the 32-bit element [ N ] within each horizontal slice ofZA t .S.                                                                                                                                                                                                                                                                                                       |
| D LQLJH   | The preferred disassembly is: • ZA t H.S[W s , offs ], for a horizontal 32-bit element ZA tile slice selection. • ZA t V.S[W s , offs ], for a vertical 32-bit element ZA tile slice selection. Where t is 0, 1, 2, or 3, and offs is 0, 1, 2, or 3.                                                                                                                                                                                |
|           | B1.4.10.4 Accessing a 64-bit element ZA tile                                                                                                                                                                                                                                                                                                                                                                                        |
| D TWMMM   | A64-bit element ZA tile is indicated by a '.D' qualifier following the tile name.                                                                                                                                                                                                                                                                                                                                                   |
| D THPSD   | There are eight tiles named ZA0.D, ZA1.D, ZA2.D, ZA3.D, ZA4.D, ZA5.D, ZA6.D, and ZA7.D. Each tile consists of [SVL D × SVL D ] 64-bit elements, and occupies an eighth of the ZA storage.                                                                                                                                                                                                                                           |
| R ZXYBQ   | An access to a horizontal or vertical 64-bit element ZAtile slice reads or writes SVL D 64-bit elements.                                                                                                                                                                                                                                                                                                                            |
| D DCXSX   | An access to a horizontal or vertical 64-bit element ZAtile slice is indicated by appending a slice index '[ N ]' to the tile name, direction suffix, and qualifier. For example, where t is in the range 0-7 inclusive, and N is in the range 0 to SVL D -1 inclusive: • ZA t H.D[ N ] indicates a horizontal 64-bit element ZA tile slice selection. • ZA t V.D[ N ] indicates a vertical 64-bit element ZA tile slice selection. |
| I LGJZC   | Horizontal and verticalZA t .D slice accesses, where t is in the range 0-7 inclusive, are illustrated in the following diagram for SVL of 256 bits:                                                                                                                                                                                                                                                                                 |

Figure B1-7 Horizontal and vertical ZAt.D slice for SVL of 256

<!-- image -->

RCVVJK An access to the horizontal slice ZA t H.D[ N ] reads or writes the SVLD 64-bit elements in ZA array vector ZA.D[ t + 8 *

N ].

RJYQKK An access to the vertical slice ZA t V.D[ N ] reads or writes the 64-bit element [ N ] within each horizontal slice of ZA t .D.

DMQQPX

The preferred disassembly is:

- ZA t H.D[W s , offs ], for a horizontal 64-bit element ZA tile slice selection.
- ZA t V.D[W s , offs ], for a vertical 64-bit element ZA tile slice selection.

Where t is in the range 0-7 inclusive, and offs is 0 or 1.

## B1.4.10.5 Accessing a 128-bit element ZA tile

DGZDSH A128-bit element ZA tile is indicated by a '.Q' qualifier following the tile name.

DRPMJL There are 16 tiles named ZA0.Q, ZA1.Q, ZA2.Q, ZA3.Q, ZA4.Q, ZA5.Q, ZA6.Q, ZA7.Q, ZA8.Q, ZA9.Q, ZA10.Q, ZA11.Q, ZA12.Q, ZA13.Q, ZA14.Q, and ZA15.Q. Each tile consists of [SVLQ × SVLQ] 128-bit elements, and occupies 1/16 of the ZA storage.

RQGHPF An access to a horizontal or vertical 128-bit element ZA tile slice reads or writes SVLQ 128-bit elements.

DRLQKW

IYQPWS

An access to a horizontal or vertical 128-bit element ZA tile slice is indicated by appending a slice index '[ N ]' to the tile name, direction suffix, and qualifier. For example, where t is in the range 0-15 inclusive, and N is in the range 0 to SVLQ-1 inclusive:

- ZA t H.Q[ N ] indicates a horizontal 128-bit element ZA tile slice selection.
- ZA t V.Q[ N ] indicates a vertical 128-bit element ZA tile slice selection.

Horizontal and vertical ZA t .Q slice accesses, where t is in the range 0-15 inclusive, are illustrated in the following diagram for SVL of 256 bits:

Figure B1-8 Horizontal and vertical ZAt.Q slice for SVL of 256

<!-- image -->

RPJTQJ

An access to the horizontal slice ZA t H.Q[ N ] reads or writes the SVLQ 128-bit elements in ZA array vector ZA.Q[ t + 16 * N ].

RTRJFZ

An access to the vertical slice ZA t V.Q[ N ] reads or writes the 128-bit element [ N ] within each horizontal slice of ZA t .Q.

DVCLJP

The preferred disassembly is:

- ZA t H.Q[W s , 0], for a horizontal 128-bit element ZA tile slice selection.

- ZA t V.Q[W s , 0], for a vertical 128-bit element ZA tile slice selection.

Where t is in the range 0-15 inclusive, and the slice index offset is always zero.

## B1.4.11 ZA storage layout

## B1.4.11.1 ZA array vector and tile slice mappings

IPYTLW

Each horizontal tile slice corresponds to one ZA array vector.

The horizontal slice mappings for all tile sizes are illustrated by this table:

| ZA Array Vector                      | 8-bit element Tile Horizontal Slice   | 16-bit element Tile Horizontal Slice   | 32-bit element Tile Horizontal Slice   | 64-bit element Tile Horizontal Slice   | 128-bit element Tile Horizontal Slice   |
|--------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|-----------------------------------------|
| ZA[0]                                | ZA0H.B[0]                             | ZA0H.H[0]                              | ZA0H.S[0]                              | ZA0H.D[0]                              | ZA0H.Q[0]                               |
| ZA[1]                                | ZA0H.B[1]                             | ZA1H.H[0]                              | ZA1H.S[0]                              | ZA1H.D[0]                              | ZA1H.Q[0]                               |
| ZA[2]                                | ZA0H.B[2]                             | ZA0H.H[1]                              | ZA2H.S[0]                              | ZA2H.D[0]                              | ZA2H.Q[0]                               |
| ZA[3]                                | ZA0H.B[3]                             | ZA1H.H[1]                              | ZA3H.S[0]                              | ZA3H.D[0]                              | ZA3H.Q[0]                               |
| ZA[4]                                | ZA0H.B[4]                             | ZA0H.H[2]                              | ZA0H.S[1]                              | ZA4H.D[0]                              | ZA4H.Q[0]                               |
| ZA[5]                                | ZA0H.B[5]                             | ZA1H.H[2]                              | ZA1H.S[1]                              | ZA5H.D[0]                              | ZA5H.Q[0]                               |
| ZA[6]                                | ZA0H.B[6]                             | ZA0H.H[3]                              | ZA2H.S[1]                              | ZA6H.D[0]                              | ZA6H.Q[0]                               |
| ZA[7]                                | ZA0H.B[7]                             | ZA1H.H[3]                              | ZA3H.S[1]                              | ZA7H.D[0]                              | ZA7H.Q[0]                               |
| ZA[8]                                | ZA0H.B[8]                             | ZA0H.H[4]                              | ZA0H.S[2]                              | ZA0H.D[1]                              | ZA8H.Q[0]                               |
| ZA[9]                                | ZA0H.B[9]                             | ZA1H.H[4]                              | ZA1H.S[2]                              | ZA1H.D[1]                              | ZA9H.Q[0]                               |
| ZA[10]                               | ZA0H.B[10]                            | ZA0H.H[5]                              | ZA2H.S[2]                              | ZA2H.D[1]                              | ZA10H.Q[0]                              |
| ZA[11]                               | ZA0H.B[11]                            | ZA1H.H[5]                              | ZA3H.S[2]                              | ZA3H.D[1]                              | ZA11H.Q[0]                              |
| ZA[12]                               | ZA0H.B[12]                            | ZA0H.H[6]                              | ZA0H.S[3]                              | ZA4H.D[1]                              | ZA12H.Q[0]                              |
| ZA[13]                               | ZA0H.B[13]                            | ZA1H.H[6]                              | ZA1H.S[3]                              | ZA5H.D[1]                              | ZA13H.Q[0]                              |
| ZA[14]                               | ZA0H.B[14]                            | ZA0H.H[7]                              | ZA2H.S[3]                              | ZA6H.D[1]                              | ZA14H.Q[0]                              |
| ZA[15]                               | ZA0H.B[15]                            | ZA1H.H[7]                              | ZA3H.S[3]                              | ZA7H.D[1]                              | ZA15H.Q[0]                              |
| if applicable ZA[16] to ZA[SVL B -1] | . . .                                 | . . .                                  | . . .                                  | . . .                                  | . . .                                   |

## B1.4.11.2 Tile mappings

The smallest ZA tile granule is the 128-bit element tile. When the ZA storage is viewed as an array of tiles, the larger 64-bit, 32-bit, 16-bit, and 8-bit element tiles overlap multiple 128-bit element tiles as follows:

IYVYJP

| Tile   | Overlaps                                                                                                             |
|--------|----------------------------------------------------------------------------------------------------------------------|
| ZA0.B  | ZA0.Q, ZA1.Q, ZA2.Q, ZA3.Q, ZA4.Q, ZA5.Q, ZA6.Q, ZA7.Q, ZA8.Q, ZA9.Q, ZA10.Q, ZA11.Q, ZA12.Q, ZA13.Q, ZA14.Q, ZA15.Q |
| ZA0.H  | ZA0.Q, ZA2.Q, ZA4.Q, ZA6.Q, ZA8.Q, ZA10.Q, ZA12.Q, ZA14.Q                                                            |
| ZA1.H  | ZA1.Q, ZA3.Q, ZA5.Q, ZA7.Q, ZA9.Q, ZA11.Q, ZA13.Q, ZA15.Q                                                            |
| ZA0.S  | ZA0.Q, ZA4.Q, ZA8.Q, ZA12.Q                                                                                          |
| ZA1.S  | ZA1.Q, ZA5.Q, ZA9.Q, ZA13.Q                                                                                          |
| ZA2.S  | ZA2.Q, ZA6.Q, ZA10.Q, ZA14.Q                                                                                         |
| ZA3.S  | ZA3.Q, ZA7.Q, ZA11.Q, ZA15.Q                                                                                         |
| ZA0.D  | ZA0.Q, ZA8.Q                                                                                                         |
| ZA1.D  | ZA1.Q, ZA9.Q                                                                                                         |
| ZA2.D  | ZA2.Q, ZA10.Q                                                                                                        |
| ZA3.D  | ZA3.Q, ZA11.Q                                                                                                        |
| ZA4.D  | ZA4.Q, ZA12.Q                                                                                                        |
| ZA5.D  | ZA5.Q, ZA13.Q                                                                                                        |
| ZA6.D  | ZA6.Q, ZA14.Q                                                                                                        |
| ZA7.D  | ZA7.Q, ZA15.Q                                                                                                        |

IWGZBT

The architecture permits concurrent use of different element size tiles.

## B1.4.11.3 Horizontal tile slice mappings

INJJXW

The following diagram illustrates the ZA storage mapping for SVL of 256 bits, for a 32-bit element and 64-bit element horizontal tile slice.

Each small numbered square represents 8 bits.

Figure B1-9 ZA storage mapping for SVL of 256 bits: 32-bit and 64-bit element horizontal tile slice

<!-- image -->

An SME vector load, store, or move instruction that accesses horizontal tile slices ZA2H.S[1] or ZA4H.D[2] treats the slices as vectors with the following layout:

Figure B1-10 ZA2H.S[1] and ZA4H.D[2] vector layout

<!-- image -->

ITNCCV

## B1.4.11.4 Vertical tile slice mappings

The following diagram illustrates the ZA storage mapping for SVL of 256 bits, for a 32-bit element and 64-bit element vertical tile slice.

Each small numbered square represents 8 bits.

Figure B1-11 ZA storage mapping for SVL of 256 bits: 32-bit and 64-bit element vertical tile slices

<!-- image -->

An SME vector load, store, or move instruction which accesses vertical tile slices ZA2V .S[1] or ZA4V .D[2] treats the slices as vectors with the following layout:

Figure B1-12 ZA2V.S[1] and ZA4V.D[2] vector layout

<!-- image -->

## B1.4.11.5 Mixed horizontal and vertical tile slice mappings

The following diagram illustrates the ZA storage mapping for SVL of 256 bits, for various element size tiles, horizontal tile slices, and vertical tile slices.

Each small square represents 8 bits.

ICGXPJ

Figure B1-13 ZA storage mapping for SVL of 256 bits: various vertical and tile slices

<!-- image -->

It is possible to simultaneously use non-overlapping ZA array vectors within tiles of differing element sizes. For example, tiles ZA1.H, ZA0.S, and ZA2.D have no ZA array vectors in common, as illustrated in the following diagram for SVL of 256 bits:

IHVFMB

Figure B1-14 Using various non-overlapping ZA array vectors within tiles of different element sizes

<!-- image -->

It is possible to access overlapping ZA array vectors within tiles of differing element sizes. For example, tiles ZA0.H, ZA2.S, and ZA6.D have common ZA array vectors.

IWDMCK

## B1.4.12 SME2 Multi-vector operands

RKLRKJ

Multi-vector operands allow certain SME2 instructions to access as source and destination operands:

- Agroup of two or four SVE Z vector registers.
- Agroup of two or four ZA tile slices.
- Agroup of two, four, eight, or sixteen ZA array vectors.

## B1.4.12.1 Z multi-vector operands

DPSTFY Amulti-vector operand consisting of two or four SVE Z vector registers is called Z

RVCXBQ A Z

multi-vector operand can occupy:

- Consecutively numbered Z registers.
- Z registers with strided numbering.

DNYNRZ A Z multi-vector operand occupying two consecutively numbered Z vectors consists of Z n+0 and Z n+1 , where n+x modulo 32 is a register number in the range 0 to 31 inclusive.

DDZDBM

A Z multi-vector operand occupying four consecutively numbered Z vectors consists of Z n+0 to Z n+3 , where n+x modulo 32 is a register number in the range 0 to 31 inclusive.

DVYKCM

The preferred disassembly for a Z multi-vector operand of consecutively numbered Z vectors is a dash-separated register range, for example { Z0.S-Z1.S } or { Z30.B-Z1.B }. Toolchains must also support assembler source code which uses multi-vector operand.

IKLBYZ

the alternative comma-separated list notation, for example { Z0.S, Z1.S } or { Z30.B, Z31.B, Z0.B, Z1.B}, and disassemblers may provide an option to select between the dash-separated range and comma-separated list notations.

DPCYZS A Z multi-vector operand occupying two Z vectors with strided register numbering consists of a first register in the range Z0-Z7 or Z16-Z23, followed by a second register with a number that is 8 higher than the first.

DRZTTV A Z multi-vector operand occupying four Z vectors with strided register numbering consists of a first register in the range Z0-Z3 or Z16-Z19, followed by three registers with a number that is each 4 higher than the last.

- DDMTSL

The preferred disassembly for a Z multi-vector operand of Z vectors with strided register numbering is a comma-separated register list, for example { Z0.D, Z8.D } or { Z0.H, Z4.H, Z8.H, Z12.H }.

## B1.4.12.2 ZA multi-slice operands

DJMCTK Amulti-vector operand consisting of two or four ZA tile slices is called ZA multi-slice operand.

RSCHNH A ZA multi-slice operand can occupy:

- Consecutively numbered horizontal ZA tile slices.
- Consecutively numbered vertical ZA tile slices.

DVXMGC In a ZA multi-slice operand that consists of:

- Two ZA tile slices, the lowest numbered slice is a multiple of 2.
- Four ZA tile slices, the lowest numbered slice is a multiple of 4.

DJFDSB In instructions operating on ZA multi-slice operands, the lowest-numbered slice is selected by rounding down the sum of a 32-bit general-purpose register (slice index register W s ) and an offset (slice index offset offs ) to the nearest lower multiple of the number of the slices in the ZA multi-slice operand, modulo the number of slices in the named tile.

RXMMKZ Instructions operating on the following ZA multi-slice operands are treated as UNDEFINED:

- The four-slice operand in a 64-bit element tile when SVL is 128 bits.
- The two-slice operand in a 128-bit element tile when SVL is 128 bits.
- The four-slice operand in a 128-bit element tile when SVL is 128 bits or 256 bits.

DGJTMX The preferred disassembly for a ZA multi-slice operand is as follows:

- ZA t H. T [W s , offs1 : offs2 ], for horizontal ZA two-slice operands, where offs2 = offs1 + 1.
- ZA t H. T [W s , offs1 : offs4 ], for horizontal ZA four-slice operands, where offs4 = offs1 + 3.
- ZA t V. T [W s , offs1 : offs2 ], for vertical ZA two-slice operands, where offs2 = offs1 + 1.
- ZA t V. T [W s , offs1 : offs4 ], for vertical ZA four-slice operands, where offs4 = offs1 + 3.

## B1.4.12.3 ZA multi-vector operands

DRGXBK Amulti-vector operand consisting of two, four, eight, or sixteen ZA array vectors is called ZA multi-vector operand.

DTGDRF One ZA array vector is called a ZA single-vector group.

DFCYGL Two consecutively-numbered vectors in the ZA array are called a ZA double-vector group.

DGCTYB Four consecutively-numbered vectors in the ZA array are called a ZA quad-vector group.

IPMQRQ The ZA multi-vector operand consists of one, two, or four vector groups, where a vector group is one of the following:

- ZA single-vector group.
- ZA double-vector group.
- ZA quad-vector group.

The SME2 architecture includes multi-vector instructions that access a

ZA

multi-vector operand consisting of the same number of vector groups as there are vectors in each

multi-vector operand.

Z

| I HPKZM   | The preferred disassembly for a ZA multi-vector operand consisting of two or four vector groups, defined in declarations D KQZYZ ,D JWRSN , andD TTNGH , includes the symbol VGx2 or VGx4 , respectively. The symbol VGx2 or VGx4 can optionally be omitted in assembler source code if it can be inferred from the other operands.                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D CLJBX   | In instructions that access a ZA multi-vector operand, the lowest-numbered vector is selected by the sum of a 32-bit general-purpose register (vector select registerW v ) and an offset (vector select offset offs ), modulo one of the following values: • SVL B when the operand consists of one ZA vector group. • SVL B /2 when the operand consists of two ZA vector groups. • SVL B /4 when the operand consists of four ZA vector groups. |
| D QFPHH   | In instructions where the ZA multi-vector operand consists of two single-vector groups, each vector group is held in a separate half of the ZA array: ZA[ n+0 ] and ZA[SVL /2 + n+0 ], where n is in the range 0 to (SVL /2 - 1) inclusive.                                                                                                                                                                                                       |
| D TTHGQ   | In instructions where the ZA multi-vector operand consists of four single-vector groups, each vector group is held in a separate quarter of the ZA array: ZA[ n+0 ], ZA[SVL B /4 + n+0 ], ZA[SVL B /2 + n+0 ], and ZA[SVL B *3/4 + n+0 ], where n is in the range 0 to (SVL B /4 - 1) inclusive.                                                                                                                                                  |
| D KQZYZ   | The preferred disassembly for a ZA multi-vector operand of single-vector groups is: • ZA. T [W v , offs , VGx2], when the operand consists of two single-vector groups. • ZA. T [W v , offs , VGx4], when the operand consists of four single-vector groups. Where offs is in the range 0 to 7 inclusive, and T is one of B, H, S, or D.                                                                                                          |
| I BYBQLI  | The mapping between ZA multi-vector operands of single-vector groups and 32-bit element ZA tile slices when SVL is 256 bits is illustrated in the following diagram:                                                                                                                                                                                                                                                                              |

Figure B1-15 ZA array vector view and 32-bit element ZA tile slice view for single-vector groups

<!-- image -->

<!-- image -->

IMLNNG The mapping between ZA multi-vector operands of single-vector groups and 64-bit element ZA tile slices when SVL is 256 bits is illustrated in the following diagram:

<!-- image -->

Figure B1-16 ZA array vector view and 64-bit element ZA tile slice view for single-vector groups

|         | B1.4.12.3.2 ZA multi-vector operands of double-vector groups                                                                                                                                                                                                                                                                                                                                         |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D RBSQJ | In instructions where the ZA multi-vector operand consists of one double-vector group, the vector group is held in ZA array vectors: ZA[ n+0 ] to ZA[ n+1 ], where n is a multiple of 2 in the range 0 to (SVL B - 2) inclusive.                                                                                                                                                                     |
| D KKVVG | In instructions where the ZA multi-vector operand consists of two double-vector groups, each vector group is held in a separate half of the ZA array: ZA[ n+0 ] to ZA[ n+1 ], and ZA[SVL B /2 + n+0 ] to ZA[SVL B /2 + n+1 ], where n is a multiple of 2 in the range 0 to (SVL B /2 - 2) inclusive.                                                                                                 |
| D VMYGN | In instructions where the ZA multi-vector operand consists of four double-vector groups, each vector group is held in a separate quarter of the ZA array: ZA[ n+0 ] to ZA[ n+1 ], ZA[SVL B /4 + n+0 ] to ZA[SVL B /4 + n+1 ], ZA[SVL B /2 + n+0 ] to ZA[SVL B /2 + n+1 ], and ZA[SVL B *3/4 + n+0 ] to ZA[SVL B *3/4 + n+1 ], where n is a multiple of 2 in the range 0 to (SVL B /4 - 2) inclusive. |
| D JWRSN | The preferred disassembly for a ZA multi-vector operand of double-vector groups is:                                                                                                                                                                                                                                                                                                                  |

- ZA. T [W v , offs1 : offs2 ], where: offs1 is a multiple of 2 in the range 0 to 14 inclusive, when the operand consists of one double-vector group.
- ZA. T [W v , offs1 : offs2 , VGx2], where offs1 is a multiple of 2 in the range 0 to 6 inclusive, when the operand consists of two double-vector groups.
- ZA. T [W v , offs1 : offs2 , VGx4], where offs1 is a multiple of 2 in the range 0 to 6 inclusive, when the operand consists of four double-vector groups.

Where offs2 = offs1 + 1, and T is one of B, H, S, or D.

ILZRTK The mapping between ZA multi-vector operands of double-vector groups and 32-bit element ZA tile slices when SVL is 256 bits is illustrated in the following diagram:

Figure B1-17 ZA array vector view and 32-bit element ZA tile slice view for double-vector groups

<!-- image -->

IJYQTB

DWSTWB

DQJXHS

The mapping between ZA multi-vector operands of double-vector groups and 64-bit element ZA tile slices when SVL is 256 bits is illustrated in the following diagram:

Figure B1-18 ZA array vector view and 64-bit element ZA tile slice view for double-vector groups

<!-- image -->

B1.4.12.3.3 ZA multi-vector operands of quad-vector groups

In instructions where the ZA multi-vector operand consists of one quad-vector group, the vector group is held in ZA array vectors: ZA[ n+0 ] to ZA[ n+3 ], where n is a multiple of 4 in the range 0 to (SVLB - 4) inclusive.

In instructions where the ZA multi-vector operand consists of two quad-vector groups, each vector group is held in a separate half of the ZA array: ZA[ n+0 ] to ZA[ n+3 ], and ZA[SVLB/2 + n+0 ] to ZA[SVLB/2 + n+3 ], where n is a

multiple of 4 in the range 0 to (SVLB/2 - 4) inclusive.

| D BQWJD   | In instructions where the ZA multi-vector operand consists of four quad-vector groups, each vector group is held in a separate quarter of the ZA array: ZA[ n+0 ] to ZA[ n+3 ], ZA[SVL B /4 + n+0 ] to ZA[SVL B /4 + n+3 ], ZA[SVL B /2 + n+0 to ZA[SVL B /2 + n+3 ], and ZA[SVL B *3/4 + n+0 ] to ZA[SVL B *3/4 + n+3 ], where n is a multiple of 4 in the range 0 to (SVL B /4 - 4) inclusive.                                                                                                                                   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D TTNGH   | The preferred disassembly for a ZA multi-vector operand of quad-vector groups is: • ZA. T [W v , offs1 : offs4 ], where: offs1 is a multiple of 4 in the range 0 to 12 inclusive, when the operand consists of one quad-vector group. • ZA. T [W v , offs1 : offs4 , VGx2], where offs1 is 0 or 4, when the operand consists of two quad-vector groups. • ZA. T [W v , offs1 : offs4 , VGx4], where offs1 is 0 or 4, when the operand consists of four quad-vector groups. Where offs4 = offs1 + 3, and T is one of B, H, S, or D. |
| I ZNSGW   | The mapping between ZA multi-vector operands of quad-vector groups and 32-bit element ZA tile slices when SVL is 256 bits is illustrated in the following diagram:                                                                                                                                                                                                                                                                                                                                                                 |

Figure B1-19 ZA array vector view and 32-bit element ZA tile slice view for quad-vector groups

<!-- image -->

IKBMLX The mapping between ZA multi-vector operands of quad-vector groups and 64-bit element ZA tile slices when SVL is

256 bits is illustrated in the following diagram:

Figure B1-20 ZA array vector view and 64-bit element ZA tile slice view for quad-vector groups

<!-- image -->

## B1.4.13 SME2 ZT0 register

| R KHZMV   | APEwith FEAT_SME2 has a 512-bit register, ZT0 , to store a lookup table.                                                                                                                                                                                                        |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R WDJBC   | The ZT0 register holds 8-bit, 16-bit, or 32-bit lookup table elements that are stored in the least significant bits of 32-bit table entries. The lowest numbered 32 bits in the register hold table entry 0.                                                                    |
| R JQXLS   | The ZT0 register lookup table can be accessed using fully packed 2-bit or 4-bit indices from a numbered portion of one source Z n SVE scalable vector register.                                                                                                                 |
| I BRRGG   | When the ZT0 register lookup table is addressed by 2-bit indices, four different table elements (0-3) of a given element size can be accessed. When the lookup table is addressed by 4-bit indices, 16 different table elements (0-15) of a given element size can be accessed. |
| R JKYRB   | The indexed 8-bit, 16-bit, or 32-bit table elements are read from the ZT0 register and packed into consecutive or strided elements of an SVE Z vector or Z multi-vector operand.                                                                                                |

See also:

- About PSTATE.ZA.
- Streaming SVE mode.
- Accessing PSTATE fields at EL0.