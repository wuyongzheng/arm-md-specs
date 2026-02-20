## G7.3 Organization of registers in the ( coproc == 0b1111 ) encoding space

For 32-bit accesses to the System registers in the ( coproc == 0b1111 ) encoding space, the ordered set of parameters { CRn , opc1 , CRm , opc2 } determine the register order. Within this ordering, the CRn value originally provided a functional grouping of these registers. As the number of System registers has increased this ordering has become less appropriate.

This document now:

- Groups the System registers in the ( coproc == 0b1111 ) encoding space by functional group, see Functional index of AArch32 registers and System instructions.
- Describes all of the System registers for the AArch32 VMSA, in AArch32 System Register Descriptions.
- Gives additional information about the organization of the AArch32 VMSA System registers in the ( coproc == 0b1111 ) encoding space, in the remainder of this section.

Note

Not all System registers introduced by architectural extensions are described in AArch32 System Register Descriptions. For information about the System registers introduced by architectural extensions, see A-profile Architecture Extensions.

This section presents information about the register ordering by { CRn , opc1 , CRm , opc2 }. It contains the following subsections:

- System register summary for ( coproc == 0b1111 ) encodings by CRn value.
- Full list of AArch32 VMSA System registers in the ( coproc == 0b1111 ) encoding space.

Note

The ordered listing of ( coproc == 0b1111 ) registers by the { CRn , opc1 , CRm , opc2 } encoding of the 32-bit registers is most likely to be useful to those implementing AArch32 state, and to those validating such implementations. However, otherwise, the grouping of registers by function is more logical.

In addition, the indexes in Registers Index include all of the System registers.

## G7.3.1 System register summary for ( coproc == 0b1111 ) encodings by CRn value

Figure G7-1 summarizes the grouping of the System registers in the ( coproc == 0b1111 ) encoding space, for an AArch32 VMSA implementation, by the value of CRn used for a 32-bit access to the register.

Figure G7-1 AArch32 System register groupings for (coproc == 0b1111), for 32-bit registers

<!-- image -->

Note

For the System registers in the ( coproc == 0b1111 ) encoding space, Figure G7-1 gives only an overview of the assigned encodings for 32-bit registers for each of the CRn values c0 -c15 . For more information, see:

- The full list of registers in the ( coproc == 0b1111 ) encoding space, in Full list of AArch32 VMSA System registers in the ( coproc == 0b1111 ) encoding space, for the definition of the assigned and unassigned encodings for that register.
- The register definitions in AArch32 System Register Descriptions for any dependencies on the implemented Exception levels.

In general, System register accesses using an unallocated set of { CRn , opc1 , CRm , opc2 } values are UNDEFINED. Behavior of AArch32 VMSA System registers with ( coproc == 0b1111 , CRn == c0) described the only exceptions to this rule.

The 32-bit System registers with ( coproc == 0b1111 , CRn == c15), and the corresponding 64-bit System registers, are reserved for IMPLEMENTATION DEFINED registers. For more information, see Reserved encodings in the AArch32 VMSA System register ( coproc == 0b1111 ) space.

## G7.3.1.1 The HSTR.Tn trap on ( coproc == 0b1111 ) System registers

When the value of HSTR.T n is 1, Non-secure PL1 accesses to System registers in the ( coproc == 0b1111 ) encoding space using a CRn or CRm value that corresponds to the value of T n are trapped to EL2, even if the encoding is UNDEFINED when the value of HSTR.T n is 0. This applies:

- For 32 bit register accesses when the value of Rn in the MCR or MRC instruction corresponds to T n .
- For 64 bit register accesses when the value of Rm in the MCRR or MRRC instruction corresponds to T n .

If there are matching System register encodings that are accessible from Non-secure EL0 then those accesses are also trapped to EL2 when the value of HSTR.T n is 1.

## G7.3.1.2 Behavior of AArch32 VMSA System registers with ( coproc == 0b1111 , CRn == c0)

In the ( coproc == 0b1111 ) encoding space, the 32-bit System registers with ( CRn == c0 ) provide device and feature identification.

Table G7-3 shows all of the architecturally required System registers with { coproc == 0b1111 , CRn == c0 }. The behavior of 32-bit System register encodings in this group that are not shown in the table, and encodings that are part of an unimplemented Exception level, depends on the value of opc1 , and possibly on the value of CRm and opc2 , as follows:

opc1 == 0 All write accesses to the encodings are UNDEFINED.

For read accesses:

- The following encodings return an UNKNOWN value:
- -CRm == 3, opc2 == {0, 1, 2}.
- -CRm == {4, 6, 7}, opc2 == {0, 1}.
- -CRm == 5, opc2 == {0, 1, 4, 5}.
- All other encodings are RES0.
- opc1 &gt; 0 All accesses to the encodings are UNDEFINED.

See also Accesses to unallocated encodings in the ( coproc == 0b111x ) encoding space.

Note

Some of these registers were previously described as being part of the CPUID identification scheme, see The CPUID identification scheme.

## G7.3.1.3 Reserved encodings in the AArch32 VMSA System register ( coproc == 0b1111 ) space

AArch32 state reserves a number of regions in the (coproc == 0b1111 ) encoding space for IMPLEMENTATION DEFINED System registers. These reservations are defined in terms of the encoding of 32-bit accesses to the System register encoding space. That is, they are defined by the reserved 32-bit { CRn , opc1 , CRm , opc2 } encodings.

Reserved encodings that do not have an IMPLEMENTATION DEFINED function are UNDEFINED.

The following subsections give more information about these reserved encodings:

- Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c9 }. · Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c10 }. · Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c11 }. · Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c15 }.

## G7.3.1.3.1 Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c9 }

In the AArch32 encoding space, for 32-bit encodings with { coproc == 0b1111 , CRn == c9 }, the following encodings are reserved for IMPLEMENTATION DEFINED purposes:

- Encodings with { coproc == 0b1111 , CRn == c9 , opc1 == {0 - 7}, opc2 == {0 - 7}, CRm == { c0 -c2 , c5 -c8 }} are reserved for IMPLEMENTATION DEFINED branch predictor, cache, and TCM operations.
- Encodings with { coproc == 0b1111 , CRn == c9 , opc1 == {0 - 7}, opc2 == {0 - 7}, CRm == c15 } are reserved for IMPLEMENTATION DEFINED performance monitors.

Note

These are distinct from the OPTIONAL Arm Performance Monitors Extension, the registers for which use the encoding space { coproc == 0b1111 , CRn == c9 , opc1 == {0 - 7}, opc2 == {0 - 7}, CRm == { c12 -c14 }}.

## G7.3.1.3.2 Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c10 }

In the AArch32 encoding space, for 32-bit encodings with { coproc == 0b1111 , CRn == c10 }, the following encodings are reserved for IMPLEMENTATION DEFINED purposes:

- Encodings with { coproc == 0b1111 , CRn == c10 , opc == {0 - 7}, CRm == { c0 , c1 , c4 , c8 }} are reserved for IMPLEMENTATION DEFINED TLB lockdown operations.

G7.3.1.3.3 Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c11 }

In the AArch32 encoding space, for 32-bit encodings with { coproc == 0b1111 , CRn == c11 }, the following encodings are reserved for IMPLEMENTATION DEFINED purposes:

- Encodings with { coproc == 0b1111 , CRn == c11 , opc == {0 - 7}, CRm == { c0 -c8 , c15 }} are reserved for IMPLEMENTATION DEFINED DMA operations for TCM access.

The remainder of the AArch32 { coproc == 0b1111 , CRn == c11 } encoding space is UNDEFINED.

<!-- formula-not-decoded -->

The AArch32 System register encodings are reserved with ( coproc == 0b1111 , CRn == c15 ) for IMPLEMENTATION DEFINED purposes, and there are no restrictions on the use of these encodings. The documentation of the Arm implementation must describe fully any registers implemented in the { coproc == 0b1111 , CRn == c15 } encoding space. Normally, for processor implementations by Arm, this information is included in the Technical Reference Manual for the processor.

Typically, an implementation uses the { coproc == 0b1111 , CRn == c15 } encodings to provide test features, and any required configuration options that are not covered by this Manual.

This reservation means that the AArch32 64-bit encodings with { coproc == 0b1111 , CRm == c15 } are also reserved for IMPLEMENTATION DEFINED purposes, without any restrictions on the use of these encodings.

## G7.3.2 Full list of AArch32 VMSA System registers in the ( coproc == 0b1111 ) encoding space

Table G7-3 shows the System registers in the ( coproc == 0b1111 ) encoding space in the AArch32 VMSA, in the order of the { CRn , opc1 , CRm , opc2 } parameter values used in MCR or MRC accesses to the 32-bit registers:

- For MCR or MRC accesses to the 32-bit registers, CRn is the primary identifier of the target System register for the access. This applies, also, to MCR or MRC instructions that provide 32-bit accesses to a single word of a 64-bit System register.
- For MCRR or MRRC accesses to the 64-bit registers, CRm is the primary identifier of the target System register for the access. Table G7-3 orders the 64-bit registers with the 32-bit registers accessed using the same primary register identifier. For example, the 64-bit encoding of TTBR0, that is accessed with ( CRm == c2 ), is listed with the 32-bit registers that are accessed with ( CRn == c2 ).

Table G7-3 AArch32 VMSA ( coproc == 0b1111) register summary, in MCR/MRC parameter order

| Name     | CRn   | opc1   | CRm   | opc2       | Source   |
|----------|-------|--------|-------|------------|----------|
| MIDR     | c0    | 0      | c0    | 0          | v8.0     |
| CTR      |       |        |       | 1          | v8.0     |
| TCMTR    |       |        |       | 2          | v8.0     |
| TLBTR    |       |        |       | 3          | v8.0     |
| MIDR     |       |        |       | 4, 6 a , 7 | v8.0     |
| MPIDR    |       |        |       | 5          | v8.0     |
| REVIDR   |       |        |       | 6 a        | v8.0     |
| ID_PFR0  |       |        | c1    | 0          | v8.0     |
| ID_PFR1  |       |        |       | 1          | v8.0     |
| ID_DFR0  |       |        |       | 2          | v8.0     |
| ID_AFR0  |       |        |       | 3          | v8.0     |
| ID_MMFR0 |       |        |       | 4          | v8.0     |
| ID_MMFR1 |       |        |       | 5          | v8.0     |

| Name               | CRn   | opc1   | CRm   | opc2   | Source   |
|--------------------|-------|--------|-------|--------|----------|
| ID_MMFR2           |       |        |       | 6      | v8.0     |
| ID_MMFR3           |       |        |       | 7      | v8.0     |
| ID_ISAR0           |       |        | c2    | 0      | v8.0     |
| ID_ISAR1           |       |        |       | 1      | v8.0     |
| ID_ISAR2           |       |        |       | 2      | v8.0     |
| ID_ISAR3           |       |        |       | 3      | v8.0     |
| ID_ISAR4           |       |        |       | 4      | v8.0     |
| ID_ISAR5           |       |        |       | 5      | v8.0     |
| ID_MMFR4           |       |        |       | 6      | v8.0     |
| ID_ISAR6           |       |        |       | 7      | v8.0     |
| ID_PFR2            |       |        | c3    | 4      | v8.0     |
| ID_DFR1            |       |        |       | 5      | v8.6     |
| ID_MMFR5           |       |        |       | 6      | v8.6     |
| CCSIDR             |       | 1      | c0    | 0      | v8.0     |
| CLIDR              |       |        |       | 1      | v8.0     |
| CCSIDR2            |       |        |       | 2      | v8.3 b   |
| AIDR               |       |        |       | 7      | v8.0     |
| CSSELR             | c0    | 2      | c0    | 0      | v8.0     |
| VPIDR c            |       | 4      | c0    | 0      | v8.0     |
| VMPIDR c           |       |        |       | 5      | v8.0     |
| SCTLR              | c1    | 0      | c0    | 0      | v8.0     |
| ACTLR              |       |        |       | 1      | v8.0     |
| CPACR              |       |        |       | 2      | v8.0     |
| ACTLR2             |       |        |       | 3      | v8.0     |
| SCR d              |       |        | c1    | 0      | v8.0     |
| SDER d             |       |        |       | 1      | v8.0     |
| NSACR d            |       |        |       | 2      | v8.0     |
| TRFCR              |       |        | c2    | 1      | v8.4     |
| SDCR               |       |        | c3    | 1      | v8.0     |
| HSCTLR c           |       | 4      | c0    | 0      | v8.0     |
| HACTLR c           |       |        |       | 1      | v8.0     |
| HACTLR2 c          |       |        |       | 3      | v8.0     |
| HCR c              |       |        | c1    | 0      | v8.0     |
| HDCR c             |       |        |       | 1      | v8.0     |
| HCPTR c            |       |        |       | 2      | v8.0     |
| HSTR c             |       |        |       | 3      | v8.0     |
| HCR2 c             |       |        |       | 4      | v8.0     |
| HACR c             |       |        |       | 7      | v8.0     |
| HTRFCR             |       |        | c2    | 1      | v8.4     |
| TTBR0, 32-bit view | c2    | 0      | c0    | 0      | v8.0     |
| TTBR0, 64-bit view | -     | 0      | c2    | -      | v8.0     |

| Name                  | CRn   | opc1   | CRm   | opc2   | Source   |
|-----------------------|-------|--------|-------|--------|----------|
| TTBR1, 32-bit view    | c2    | 0      | c0    | 1      | v8.0     |
| TTBR1, 64-bit view    | -     | 1      | c2    | -      | v8.0     |
| TTBCR                 | c2    | 0      | c0    | 2      | v8.0     |
| TTBCR2                |       |        |       | 3      | v8.2     |
| HTCR c                |       | 4      | c0    | 2      | v8.0     |
| VTCR c                |       |        | c1    | 2      | v8.0     |
| HTTBR c , 64-bit view | -     | 4      | c2    | -      | v8.0     |
| VTTBR c . 64-bit view | -     | 6      | c2    | -      | v8.0     |
| DACR                  | c3    | 0      | c0    | 0      | v8.0     |
| ICC_PMR ICV_PMR       | c4    | 0      | c6    | 0      | GIC e    |
| DSPSR f               | c4    | 3      | c5    | 0      | v8.0     |
| DLR                   |       |        |       | 1      | v8.0     |
| DFSR                  | c5    | 0      | c0    | 0      | v8.0     |
| IFSR                  |       |        |       | 1      | v8.0     |
| ADFSR                 |       |        | c1    | 0      | v8.0     |
| AIFSR                 |       |        |       | 1      | v8.0     |
| ERRIDR                |       |        | c3    | 0      | RAS g    |
| ERRSELR               |       |        |       | 1      | RAS g    |
| ERXFR                 |       |        | c4    | 0      | RAS g    |
| ERXCTLR               |       |        |       | 1      | RAS g    |
| ERXSTATUS             |       |        |       | 2      | RAS g    |
| ERXADDR               |       |        |       | 3      | RAS g    |
| ERXFR2                |       |        |       | 4      | RAS g    |
| ERXCTLR2              |       |        |       | 5      | RAS g    |
| ERXADDR2              |       |        |       | 7      | RAS g    |
| ERXMISC0              |       |        | c5    | 0      | RAS g    |
| ERXMISC1              |       |        |       | 1      | RAS g    |
| ERXMISC4              |       |        |       | 2      | RAS g    |
| ERXMISC5              |       |        |       | 3      | RAS g    |
| ERXMISC2              |       |        |       | 4      | RAS g    |
| ERXMISC3              |       |        |       | 5      | RAS g    |
| ERXMISC6              |       |        |       | 6      | RAS g    |
| ERXMISC7              |       |        |       | 7      | RAS g    |
| HADFSR c              |       | 4      | c1    | 0      | v8.0     |
| HAIFSR                |       |        |       | 1      | v8.0     |
| HSR c                 |       |        | c2    | 0      | v8.0     |
| VDFSR                 |       |        |       | 3      | RAS g    |
| DFAR                  | c6    | 0      | c0    | 0      | v8.0     |
| IFAR                  |       |        |       | 2      | v8.0     |
| HDFAR c               |       | 4      | c0    | 0      | v8.0     |

| Name             | CRn   | opc1   | CRm   | opc2   | Source   |
|------------------|-------|--------|-------|--------|----------|
| HIFAR c          |       |        |       | 2      | v8.0     |
| HPFAR c          | c6    | 4      | c0    | 4      | v8.0     |
| ICIALLUIS        | c7    | 0      | c1    | 0      | v8.0     |
| BPIALLIS         |       |        |       | 6      | v8.0     |
| CFPRCTX          |       |        | c3    | 4      | v8.0 h   |
| DVPRCTX          |       |        |       | 5      | v8.0 h   |
| COSPRCTX         |       |        |       | 6      | v8.9     |
| CPPRCTX          |       |        |       | 7      | v8.0 h   |
| PAR, 32-bit view |       |        | c4    | 0      | v8.0     |
| PAR, 64-bit view | -     | 0      | c7    | -      | v8.0     |
| ICIALLU          | c7    | 0      | c5    | 0      | v8.0     |
| ICIMVAU          |       |        |       | 1      | v8.0     |
| CP15ISB i        |       |        |       | 4      | v8.0     |
| BPIALL           |       |        |       | 6      | v8.0     |
| BPIMVA           |       |        |       | 7      | v8.0     |
| DCIMVAC          |       |        | c6    | 1      | v8.0     |
| DCISW            |       |        |       | 2      | v8.0     |
| ATS1CPR          |       |        | c8    | 0      | v8.0     |
| ATS1CPW          |       |        |       | 1      | v8.0     |
| ATS1CUR          |       |        |       | 2      | v8.0     |
| ATS1CUW          |       |        |       | 3      | v8.0     |
| ATS12NSOPR d     |       |        |       | 4      | v8.0     |
| ATS12NSOPW d     |       |        |       | 5      | v8.0     |
| ATS12NSOUR d     |       |        |       | 6      | v8.0     |
| ATS12NSOUW d     |       |        |       | 7      | v8.0     |
| DCCMVAC          |       |        | c10   | 1      | v8.0     |
| DCCSW            |       |        |       | 2      | v8.0     |
| CP15DSB i        |       |        |       | 4      | v8.0     |
| CP15DMB i        |       |        |       | 5      | v8.0     |
| DCCMVAU          | c7    | 0      | c11   | 1      | v8.0     |
| DCCIMVAC         |       |        | c14   | 1      | v8.0     |
| DCCISW           |       |        |       | 2      | v8.0     |
| ATS1HR c         |       | 4      | c8    | 0      | v8.0     |
| ATS1HW c         |       |        |       | 1      | v8.0     |
| TLBIALLIS        | c8    | 0      | c3    | 0      | v8.0     |
| TLBIMVAIS        |       |        |       | 1      | v8.0     |
| TLBIASIDIS       |       |        |       | 2      | v8.0     |
| TLBIMVAAIS       |       |        |       | 3      | v8.0     |
| TLBIMVALIS       |       |        |       | 5      | v8.0     |
| TLBIMVAALIS      |       |        |       | 7      | v8.0     |
| ITLBIALL         |       |        | c5    | 0      | v8.0     |

| Name                        | CRn   | opc1   | CRm     | opc2   | Source   |
|-----------------------------|-------|--------|---------|--------|----------|
| ITLBIMVA                    |       |        |         | 1      | v8.0     |
| ITLBIASID                   |       |        |         | 2      | v8.0     |
| DTLBIALL                    |       |        | c6      | 0      | v8.0     |
| DTLBIMVA                    |       |        |         | 1      | v8.0     |
| DTLBIASID                   |       |        |         | 2      | v8.0     |
| TLBIALL                     |       |        | c7      | 0      | v8.0     |
| TLBIMVA                     |       |        |         | 1      | v8.0     |
| TLBIASID                    |       |        |         | 2      | v8.0     |
| TLBIMVAA                    |       |        |         | 3      | v8.0     |
| TLBIMVAL                    |       |        |         | 5      | v8.0     |
| TLBIMVAAL                   |       |        |         | 7      | v8.0     |
| TLBIIPAS2IS                 |       | 4      | c0      | 1      | v8.0     |
| TLBIIPAS2LIS                |       |        |         | 5      | v8.0     |
| TLBIALLHIS c                |       |        | c3      | 0      | v8.0     |
| TLBIMVAHIS c                |       |        |         | 1      | v8.0     |
| TLBIALLNSNHIS c             |       |        |         | 4      | v8.0     |
| TLBIMVALHIS                 |       |        |         | 5      | v8.0     |
| TLBIIPAS2                   |       |        | c4      | 1      | v8.0     |
| TLBIIPAS2L                  |       |        |         | 5      | v8.0     |
| TLBIALLH c                  | c8    | 4      | c7      | 0      | v8.0     |
| TLBIMVAH c                  |       |        |         | 1      | v8.0     |
| TLBIALLNSNH c               |       |        |         | 4      | v8.0     |
| TLBIMVALH                   |       |        |         | 5      | v8.0     |
| Reserved j                  | c9    | 0 - 7  | c0 - c2 | 0 - 7  | -        |
| Reserved j                  |       |        | c5 - c8 | 0 - 7  | -        |
| PMCR k                      |       | 0      | c12     | 0      | v8.0     |
| PMCNTENSET k                |       |        |         | 1      | v8.0     |
| PMCNTENCLR k                |       |        |         | 2      | v8.0     |
| PMOVSR k                    |       |        |         | 3      | v8.0     |
| PMSWINC k                   |       |        |         | 4      | v8.0     |
| PMSELR k                    |       |        |         | 5      | v8.0     |
| PMCEID0 k                   |       |        |         | 6      | v8.0     |
| PMCEID1 k                   |       |        |         | 7      | v8.0     |
| PMCCNTR k , 32-bit view     |       |        | c13     | 0      | v8.0     |
| PMCCNTR_EL0 k , 64-bit view | -     | 0      | c9      | -      | v8.0     |
| PMXEVTYPER k                | c9    | 0      | c13     | 1      | v8.0     |
| PMXEVCNTR k                 |       |        |         | 2      | v8.0     |
| PMUSERENR k                 |       |        | c14     | 0      | v8.0     |
| PMINTENSET k                |       |        |         | 1      | v8.0     |
| PMINTENCLR k                |       |        |         | 2      | v8.0     |
| PMOVSSET c , k              |       |        |         | 3      | v8.0     |

| Name                   | CRn   | opc1   | CRm            | opc2   | Source   |
|------------------------|-------|--------|----------------|--------|----------|
| PMCEID2 k              |       |        |                | 4      | v8.1     |
| PMCEID3 k              |       |        |                | 5      | v8.1     |
| PMMIR                  |       |        |                | 6      | v8.4     |
| Reserved l             |       | 0 - 7  | c15            | 0 - 7  | -        |
| Reserved m             | c10   | 0      | c0 - c1        | 0 - 7  | -        |
| PRRR n                 |       |        | c2             | 0      | v8.0     |
| MAIR0 n                |       |        |                |        | v8.0     |
| NMRR n                 |       |        |                | 1      | v8.0     |
| MAIR1 n                |       |        |                |        | v8.0     |
| AMAIR0                 |       |        | c3             | 0      | v8.0     |
| AMAIR1                 |       |        |                | 1      | v8.0     |
| Reserved m             |       |        | c4, c8         | 0 - 7  | -        |
| Reserved m             |       | 1- 3   | c0, c1, c4, c8 | 0 - 7  | -        |
| Reserved m             |       | 4      | c0, c1         | 0 - 7  | -        |
| HMAIR0 c               |       |        | c2             | 0      | v8.0     |
| HMAIR1 c               |       |        |                | 1      | v8.0     |
| HAMAIR0 c              |       |        | c3             | 0      | v8.0     |
| HAMAIR1 c              |       |        |                | 1      | v8.0     |
| Reserved m             |       |        | c4, c8         | 0 - 7  | -        |
| Reserved m             |       | 5 - 7  | c0, c1, c4, c8 | 0 - 7  | -        |
| Reserved o             | c11   | 0-7    | c0-c8          | 0 - 7  | -        |
| Reserved o             |       |        | c15            | 0 - 7  | -        |
| ICC_SGI1R, 64-bit view | -     | 0      | c12            | -      | GIC e    |
| VBAR                   | c12   | 0      | c0             | 0      | v8.0     |
| MVBAR d                |       |        |                | 1      | v8.0     |
| RVBAR                  |       |        |                |        | v8.0     |
| RMR p                  |       |        |                | 2      | v8.0     |
| ISR d                  |       |        | c1             | 0      | v8.0     |
| DISR                   |       |        |                | 1      | RAS g    |
| VDISR                  |       | 4      | c1             | 1      | RAS g    |
| ICC_IAR0 ICV_IAR0      |       | 0      | c8             | 0      | GIC e    |
| ICC_EOIR0 ICV_EOIR0    |       |        |                | 1      | GIC e    |
| ICC_HPPIR0 ICV_HPPIR0  |       |        |                | 2      | GIC e    |
| ICC_BPR0 ICV_BPR0      | c12   | 0      | c8             | 3      | GIC e    |
| ICC_AP0R0 ICV_AP0R0    |       |        |                | 4      | GIC e    |
| ICC_AP0R1 ICV_AP0R1    |       |        |                | 5      | GIC e    |

| Name                    | CRn   | opc1   | CRm   | opc2   | Source   |
|-------------------------|-------|--------|-------|--------|----------|
| ICC_AP0R2 ICV_AP0R2     |       |        |       | 6      | GIC e    |
| ICC_AP0R3 ICV_AP0R3     |       |        |       | 7      | GIC e    |
| ICC_AP1R0 ICV_AP1R0     |       |        | c9    | 0      | GIC e    |
| ICC_AP1R1 ICV_AP1R1     |       |        |       | 1      | GIC e    |
| ICC_AP1R2 ICV_AP1R2     |       |        |       | 2      | GIC e    |
| ICC_AP1R3 ICV_AP1R3     |       |        |       | 3      | GIC e    |
| ICC_DIR ICV_DIR         |       |        | c11   | 1      | GIC e    |
| ICC_RPR ICV_RPR         |       |        |       | 3      | GIC e    |
| ICC_IAR1 ICV_IAR1       |       |        | c12   | 0      | GIC e    |
| ICC_EOIR1 ICV_EOIR1     |       |        |       | 1      | GIC e    |
| ICC_HPPIR1 ICV_HPPIR1   |       |        |       | 2      | GIC e    |
| ICC_BPR1 ICV_BPR1       |       |        |       | 3      | GIC e    |
| ICC_CTLR ICV_CTLR       |       |        |       | 4      | GIC e    |
| ICC_SRE                 |       |        |       | 5      | GIC e    |
| ICC_IGRPEN0 ICV_IGRPEN0 |       |        |       | 6      | GIC e    |
| ICC_IGRPEN1 ICV_IGRPEN1 |       |        |       | 7      | GIC e    |
| ICC_ASGI1R, 64-bit view | -     | 1      | c12   | -      | GIC e    |
| ICC_SGI0R, 64-bit view  | -     | 2      | c12   | -      | GIC e    |
| HVBAR c                 | c12   | 4      | c0    | 0      | v8.0 e   |
| HRMR p                  |       |        |       | 2      | v8.0 e   |
| ICH_AP0R0               |       |        | c8    | 0      | GIC e    |
| ICH_AP0R1               |       |        |       | 1      | GIC e    |
| ICH_AP0R2               |       |        |       | 2      | GIC e    |
| ICH_AP0R3               | c12   | 4      | c8    | 3      | GIC e    |
| ICH_AP1R0               |       |        | c9    | 0      | GIC e    |
| ICH_AP1R1               |       |        |       | 1      | GIC e    |
| ICH_AP1R2               |       |        |       | 2      | GIC e    |
| ICH_AP1R3               |       |        |       | 3      | GIC e    |
| ICC_HSRE                |       |        |       | 5      | GIC e    |
| ICH_HCR                 |       |        | c11   | 0      | GIC e    |
| ICH_VTR                 |       |        |       | 1      | GIC e    |

| Name                                        | CRn   | opc1   | CRm   | opc2   | Source   |
|---------------------------------------------|-------|--------|-------|--------|----------|
| ICH_MISR                                    |       |        |       | 2      | GIC e    |
| ICH_EISR                                    |       |        |       | 3      | GIC e    |
| ICH_ELRSR                                   |       |        |       | 5      | GIC e    |
| ICH_VMCR                                    |       |        |       | 7      | GIC e    |
| ICH_LR, for n == 0 to 7                     |       |        | c12   | 0-7    | GIC e    |
| ICH_LR, for n == 8 to 15                    |       |        | c13   | 0-7    | GIC e    |
| ICH_LRC, for n == 0 to 7                    |       |        | c14   | 0-7    | GIC e    |
| ICH_LRC, for n == 8 to 15                   |       |        | c15   | 0-7    | GIC e    |
| ICC_MCTLR                                   |       | 6      | c12   | 4      | GIC e    |
| ICC_MSRE                                    |       |        |       | 5      | GIC e    |
| ICC_MGRPEN1                                 |       |        |       | 7      | GIC e    |
| FCSEIDR                                     | c13   | 0      | c0    | 0      | v8.0     |
| CONTEXTIDR                                  |       |        |       | 1      | v8.0     |
| TPIDRURW                                    |       |        |       | 2      | v8.0     |
| TPIDRURO                                    |       |        |       | 3      | v8.0     |
| TPIDRPRW                                    |       |        |       | 4      | v8.0     |
| AMCR                                        |       |        | c2    | 0      | AMU q    |
| AMCFGR                                      |       |        | c2    | 1      | AMU q    |
| AMCGCR                                      |       |        | c2    | 2      | AMU q    |
| AMUSERENR                                   |       |        | c2    | 3      | AMU q    |
| AMCNTENCLR0                                 |       |        | c2    | 4      | AMU q    |
| AMCNTENSET0                                 |       |        | c2    | 5      | AMU q    |
| AMCNTENCLR1                                 |       |        | c3    | 0      | AMU q    |
| AMCNTENSET1                                 |       |        | c3    | 1      | AMU q    |
| AMEVTYPER0<n>, for n == 0 to 7              |       |        | c6    | 0-7    | AMU q    |
| AMEVTYPER0<n>, for n == 8 to 15             |       |        | c7    |        | AMU q    |
| AMEVTYPER1<n>, for n == 0 to 7              |       |        | c14   |        | AMU q    |
| AMEVTYPER1<n>, for n == 8 to 15             |       |        | c15   |        | AMU q    |
| AMEVCNTR0<n>, for n == 0 to 7, 64-bit view  | -     | 0-7    | c0    | -      | AMU q    |
| AMEVCNTR0<n>, for n == 8 to 15, 64-bit view | -     |        | c1    |        | AMU q    |
| AMEVCNTR1<n> for n == 0 to 7, 64-bit view   | -     |        | c4    |        | AMU q    |
| AMEVCNTR1<n>, for n == 8 to 15, 64-bit view | -     |        | c5    |        | AMU q    |
| HTPIDR c                                    | c13   | 4      | c0    | 2      | v8.0     |
| CNTPCT r , 64-bit view                      | -     | 0      | c14   | -      | v8.0     |
| CNTFRQ r                                    | c14   | 0      | c0    | 0      | v8.0     |
| CNTKCTL r                                   |       |        | c1    | 0      | v8.0     |
| CNTP_TVAL r                                 |       |        | c2    | 0      | v8.0     |
| CNTP_CTL r                                  |       |        |       | 1      | v8.0     |
| CNTV_TVAL r                                 |       |        | c3    | 0      | v8.0     |
| CNTV_CTL r                                  |       |        |       | 1      | v8.0     |
| PMEVCNTR<n>, for n == 0 to 7 k              |       |        | c8    | 0-7    | v8.0     |

| Name                              | CRn   | opc1   | CRm    | opc2   | Source   |
|-----------------------------------|-------|--------|--------|--------|----------|
| PMEVCNTR<n>, for n == 8 to 15 k   |       |        | c9     | 0-7    | v8.0     |
| PMEVCNTR<n>, for n == 16 to 23 k  |       |        | c10    | 0-7    | v8.0     |
| PMEVCNTR<n>, for n == 24 to 30 k  |       |        | c11    | 0-6    | v8.0     |
| PMEVTYPER<n>, for n == 0 to 7 k   |       |        | c12    | 0-7    | v8.0     |
| PMEVTYPER<n>, for n == 8 to 15 k  |       |        | c13    | 0-7    | v8.0     |
| PMEVTYPER<n>, for n == 16 to 23 k |       |        | c14    | 0-7    | v8.0     |
| PMEVTYPER<n>, for n == 17 to 30 k |       |        | c15    | 0-6    | v8.0     |
| PMCCFILTR k                       |       |        | c15    | 7      | v8.0     |
| CNTVCT r , 64-bit view            | -     | 1      | c14    | -      | v8.0     |
| CNTP_CVAL r , 64-bit view         | -     | 2      | c14    | -      | v8.0     |
| CNTV_CVAL r , 64-bit view         | -     | 3      | c14    | -      | v8.0     |
| CNTVOFF s , 64-bit view           | -     | 4      | c14    | -      | v8.0     |
| CNTHCTL r                         | c14   | 4      | c1     | 0      | v8.0     |
| CNTHP_TVAL r                      | c14   | 4      | c2     | 0      | v8.0     |
| CNTHP_CTL r                       |       |        |        | 1      | v8.0     |
| CNTHP_CVAL r , 64-bit view        | -     | 6      | c14    | -      | v8.0     |
| CNTPCTSS r , 64-bit view          | -     | 8      | c14    | -      | v8.6     |
| CNTVCTSS r , 64-bit view          | -     | 9      | c14    | -      | v8.6     |
| Reserved t                        | c15   | 0-7    | c0-c15 | 0-7    | -        |

- a. REVIDR is an optional register. If it is not implemented, the encoding with opc2 set to 6 is an alias of MIDR.
- b. When FEAT\_CCIDX is implemented, CCSIDR2 is implemented.
- c. Implemented only as part of EL2 when EL2 is using AArch32. Otherwise, encoding is unallocated and UNDEFINED.
- d. Implemented only as part of EL3 when EL3 is using AArch32. Otherwise, encoding is unallocated and UNDEFINED.
- e. GIC System register, see About the GIC System registers. As that subsection describes, each ICV\_* register uses the same encoding as the corresponding ICC\_* register.
- f. This register is accessible only in Debug state.
- g. RAS Extension System registers, see RAS registers.
- h. When FEAT\_SPECRES is implemented, the execution and data prediction restriction instructions are implemented, see Execution and data prediction restriction System instructions.
- i. For performance reasons, Arm deprecates any use of these memory barrier operations.
- j. Reserved for IMPLEMENTATION DEFINED branch predictor, cache, and TCM operations, see Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c9 }.
- k. Performance Monitors Extension System register, see Performance Monitors registers.
- l. Reserved for IMPLEMENTATION DEFINED performance monitors, see Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c9 }.
- m. Reserved for IMPLEMENTATION DEFINED TLB lockdown operations, see Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c10 }.
- n. When an implementation is using the Long descriptor translation table format, these encodings access the MAIR0 and MAIR1 registers. Otherwise, they use PRRR and NMRR.
- o. Reserved for IMPLEMENTATION DEFINED DMA operations for TCM access, see Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c11 }.
- p. Only one of RMR and HRMR is implemented, corresponding to the highest implemented Exception level, and the register is implemented only if that Exception level is using AArch32.
- q. Activity Monitors System register, see Activity Monitors registers.
- r. Generic Timer System register, see Generic Timer registers.

- s. Implemented as RW as part of the Generic Timer on an implementation that includes EL2 and when EL2 is using AArch32. For more information, see The virtual offset register.

t. Reserved for IMPLEMENTATION DEFINED purposes, see Reserved 32-bit encodings with { coproc == 0b1111 , CRn == c15 }.

## G7.3.2.1 About the GIC System registers

From version 3 of the GIC architecture specification, the specification defines three groups of System registers, identified by the prefix of the register name:

- ICC\_ GIC physical CPU interface System registers.

- ICH\_ GIC virtual interface control System registers.

- ICV\_ GIC Virtual CPU interface System registers.

Note

These registers are in addition to the GIC memory-mapped register groups GICC\_, GICD\_, GICH\_, GICR\_, GICV\_, and GITS\_.

In AArch32, the GIC System registers are all in the ( coproc == 0b1111 ) encoding space with ( CRn == c12 ). The ICV\_* registers have the same { CRn , opc1 , CRm , op2 } encodings as the corresponding ICC\_* registers. For these encodings, GIC register configuration fields determine which register is accessed.

When implemented, the GIC System registers form part of an Arm processor implementation, and therefore these registers are included in the register summaries. However, the registers are defined only in the GIC Architecture Specification.

For more information, see the ARM ® Generic Interrupt Controller Architecture Specification, GIC architecture version 3 and version 4 (ARM IHI 0069).

## Chapter G8 AArch32 System Register Descriptions

This chapter describes each of the AArch32 System registers.

It contains the following sections:

- About the AArch32 System registers.
- General system control registers.
- Debug registers.
- Performance Monitors registers.
- Activity Monitors registers.
- RAS registers.
- Generic Timer registers.