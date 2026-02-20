## E2.6 Alignment support

This section describes alignment support. It contains the following subsections:

- Instruction alignment.
- Unaligned data access.
- Cases where unaligned accesses are CONSTRAINED UNPREDICTABLE.
- Unaligned data access restrictions.
- Generation of Alignment faults by load/store multiple accesses to Device memory.

For more information about Alignment faults, see Alignment faults.

## E2.6.1 Instruction alignment

A32 instructions are word-aligned.

T32 instructions are halfword-aligned.

## E2.6.2 Unaligned data access

An A-profile implementation must support unaligned data accesses to Normal memory by some load and store instructions. As Table E2-3 shows, software can control whether a misaligned access to Normal memory by one of these instructions causes an Alignment fault Data Abort exception:

- By setting SCTLR.A, for unaligned accesses from any mode other than Hyp mode.
- By setting HSCTLR.A, for unaligned accesses from Hyp mode.

Table E2-3 Alignment requirements of load/store instructions

| Instructions                                                                           | Alignment check   | fails when:                              | fails when:              |
|----------------------------------------------------------------------------------------|-------------------|------------------------------------------|--------------------------|
|                                                                                        |                   | Result if check SCTLR.A or HSCTLR.A is 0 | SCTLR.A or HSCTLR.A is 1 |
| LDRB , LDREXB , LDRBT , LDRSB , LDRSBT , STRB , STREXB , STRBT , TBB                   | None              | -                                        | -                        |
| LDRH , LDRHT , LDRSH , LDRSHT , STRH , STRHT , TBH                                     | Halfword          | Unaligned access                         | Alignment fault          |
| LDREXH , STREXH , LDAH , STLH , LDAEXH , STLEXH                                        | Halfword          | Alignment fault                          | Alignment fault          |
| LDR , LDRT , STR , STRT PUSH , encodings T3 and A2 only POP , encodings T3 and A2 only | Word              | Unaligned access                         | Alignment fault          |
| LDREX , STREX , LDA , STL , LDAEX , STLEX                                              | Word              | Alignment fault                          | Alignment fault          |
| LDREXD , STREXD , LDAEXD , STLEXD                                                      | Doubleword        | Alignment fault                          | Alignment fault          |
| All forms of LDM and STM , LDRD , RFE , SRS , STRD                                     | Word              | Alignment fault                          | Alignment fault          |
| LDC , STC                                                                              | Word              | Alignment fault                          | Alignment fault          |
| VLDM , VPOP , VPUSH , VSTM                                                             | Word              | Alignment fault                          | Alignment fault          |
| VLDR, VSTR - single-precision scalar and double-precision scalar                       | Word              | Alignment fault                          | Alignment fault          |
| VLDR, VSTR - half-precision scalar                                                     | Halfword          | Alignment fault                          | Alignment fault          |
| VLD1 , VLD2 , VLD3 , VLD4 , VST1 , VST2 , VST3 , VST4 , all with standard alignment    | Element size      | Unaligned access                         | Alignment fault          |

## Instructions

## Alignment check

Result if check fails when:

SCTLR.A or HSCTLR.A is 0

SCTLR.A or HSCTLR.A is 1

VLD1 , VLD2 , VLD3 , VLD4 , VST1 , VST2 , VST3 , VST4 , all with :&lt;align&gt; specified a

As specified by :&lt;align&gt;

Alignment fault

Alignment fault

a. Previous versions of this manual used @&lt;align&gt; to specify alignment. Both forms are supported, see T32 and A32 Advanced SIMD and Floating-point Instruction Descriptionsfor more information.

Note

Any unaligned access to any type of Device memory generates an Alignment fault, see Alignment faults.

## E2.6.3 Cases where unaligned accesses are CONSTRAINED UNPREDICTABLE

Any load instruction that is not faulted by the alignment restrictions shown in Table E2-3 and that loads the PC has CONSTRAINED UNPREDICTABLE behavior if the address it loads from is not word-aligned, see Loads and Stores to unaligned locations. This overrules any permitted load/store behavior shown in Table E2-3.

## E2.6.4 Unaligned data access restrictions

The following points apply to unaligned data accesses:

- Accesses are not guaranteed to be single-copy atomic except at the byte access level, see Atomicity in the Arm architecture.
- Unaligned accesses typically take a number of additional cycles to complete compared to a naturally-aligned access.
- An operation that performs an unaligned access can abort on any memory access that it makes, and can abort on more than one access. This means that an unaligned access that occurs across a page boundary can generate an abort on either side of the boundary.

## E2.6.5 Generation of Alignment faults by load/store multiple accesses to Device memory

When FEAT\_LSMAOC is implemented and the value of the applicable nTLSMD field is 0, any memory access by an AArch32 Load Multiple or Store Multiple instruction to an address that the stage 1 translation assigns as Device-nGRE, Device-nGnRE, or Device-nGnRnE generates an Alignment fault.

The applicable nTLSMD field is the field in the SCTLR\_EL1, SCTLR\_EL2, HSCTLR, or SCTLR register that applies to the Exception level and Security state at which the LDM or STM instruction is executed.