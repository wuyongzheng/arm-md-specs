## D23.3 Moves to and from non-debug System registers, Special-purpose registers

The instructions that move data to and from non-debug System registers are encoded with op0 == 0b11 , except that some of this encoding space is reserved for IMPLEMENTATION DEFINED functionality. The encoding of these instructions is:

<!-- image -->

The value of CRn provides the next level of decode of these instructions, as follows: CRn == { 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0101 , 0b0110 , 0b0111 , 0b1001 , 0b1010 , 0b1100 , 0b1101 , 0b1110 See Instructions for accessing non-debug System registers. CRn == { 0b0100 } See Instructions for accessing Special-purpose registers. CRn =={ 0b1011 , 0b1111 } See Reserved encodings for IMPLEMENTATION DEFINED registers.

## D23.3.1 Instructions for accessing non-debug System registers

The A64 instructions for accessing System registers are:

```
MSR <System_register>, Xt ; Write to 64-bit System register MSRR <System_register>, Xt ; Write to 128-bit System register MRS Xt, <System_register> ; Read from 64-bit System register MRRS Xt, <System_register> ; Read from 128-bit System register
```

Where &lt;System\_register&gt; is the register name, for example MIDR\_EL1.

This section includes only the System register access encodings for which both:

- op0 is 0b11 .
- The value of CRn is one of { 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0100 , 0b0101 , 0b0110 , 0b0111 , 0b1001 , 0b1010 , 0b1100 , 0b1101 , 0b1110 }.

## Note

- These encodings access the registers that are equivalent to the AArch32 System registers in the ( coproc == 0b1111 ) encoding space. For more information, see Mapping of the System registers between the Execution states.
- While this group is described as accessing the non-debug System registers, its correct characterization is by the { op0 , CRn } values given in this subsection, and the group includes the debug registers DLR\_EL0, DSPSR\_EL0, MDCR\_EL2, MDCR\_EL3, and SDER32\_EL3, which are described in Debug registers. These registers are exceptions to the standard encoding of debug registers, which has op0 == 0b10 . See Instructions for accessing debug System registers for more information.

Direct accesses to some regions of the system register encoding space have a defined behavior even if no register is currently allocated or implemented for the encodings in those regions. The Feature ID space is the System register space in AArch64 with op0==3, op1=={0, 1, 3}, CRn==0, CRm=={0-7}, op2=={0-7} . The properties for this space are that:

- For unused encodings in the part of the space that has op1 == 0 and CRm == {2-7} , the following apply:

```
}
```

- -If FEAT\_FGT is not implemented, it is IMPLEMENTATION DEFINED whether direct reads can be trapped by HCR\_EL2.TID3.
- -If FEAT\_FGT is implemented, direct reads can be trapped by HCR\_EL2.TID3.
- -If FEAT\_IDTE3 is implemented, direct reads can be trapped by SCR\_EL3.TID3.
- -Direct reads that are not trapped behave as Reserved, RES0 to ensure correct behavior if the encodings are used for ID registers in the future.
- For unused encodings in the part of the space that has either op1 == 0 and CRm == 0 , or op1 == {1, 3} , the following apply:
- -If FEAT\_IDST is not implemented, direct reads are UNDEFINED and therefore generate exceptions reported with EC syndrome value 0x00 .
- -If FEAT\_IDST is not implemented, direct reads are UNDEFINED and therefore generate exceptions reported with EC syndrome value 0x00 .
- -If FEAT\_IDST is implemented, direct reads generate exceptions reported with EC syndrome value 0x18 .
- -
- The behavior for direct reads is consistent with the pseudocode function UnimplementedIDRegister() .

The instruction encoding for these accesses is:

<!-- image -->

op0

See text for permitted values of CRn

Table D23-2 shows the encodings of the register access instructions.

See the register descriptions for information about the control that determines whether these accesses are permitted.

Table D23-2 Instruction encodings for non-debug System register access in the (op0==0b11) encoding space

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic     | Accesses             |
|-------|--------|--------|-------|----------|--------------|----------------------|
| 0b000 | 0b0000 | 0b0000 | 0b000 | RO       | MIDR_EL1     | MIDR_EL1 VPIDR_EL2   |
| 0b000 | 0b0000 | 0b0000 | 0b101 | RO       | MPIDR_EL1    | MPIDR_EL1 VMPIDR_EL2 |
| 0b000 | 0b0000 | 0b0000 | 0b110 | RO       | REVIDR_EL1   | REVIDR_EL1           |
| 0b000 | 0b0000 | 0b0001 | 0b000 | RO       | ID_PFR0_EL1  | ID_PFR0_EL1          |
| 0b000 | 0b0000 | 0b0001 | 0b001 | RO       | ID_PFR1_EL1  | ID_PFR1_EL1          |
| 0b000 | 0b0000 | 0b0001 | 0b010 | RO       | ID_DFR0_EL1  | ID_DFR0_EL1          |
| 0b000 | 0b0000 | 0b0001 | 0b011 | RO       | ID_AFR0_EL1  | ID_AFR0_EL1          |
| 0b000 | 0b0000 | 0b0001 | 0b100 | RO       | ID_MMFR0_EL1 | ID_MMFR0_EL1         |
| 0b000 | 0b0000 | 0b0001 | 0b101 | RO       | ID_MMFR1_EL1 | ID_MMFR1_EL1         |
| 0b000 | 0b0000 | 0b0001 | 0b110 | RO       | ID_MMFR2_EL1 | ID_MMFR2_EL1         |
| 0b000 | 0b0000 | 0b0001 | 0b111 | RO       | ID_MMFR3_EL1 | ID_MMFR3_EL1         |
| 0b000 | 0b0000 | 0b0010 | 0b000 | RO       | ID_ISAR0_EL1 | ID_ISAR0_EL1         |
| 0b000 | 0b0000 | 0b0010 | 0b001 | RO       | ID_ISAR1_EL1 | ID_ISAR1_EL1         |
| 0b000 | 0b0000 | 0b0010 | 0b010 | RO       | ID_ISAR2_EL1 | ID_ISAR2_EL1         |

| op1         | CRn    | CRm    | op2   | Access   | Mnemonic         | Accesses              |
|-------------|--------|--------|-------|----------|------------------|-----------------------|
| 0b000       | 0b0000 | 0b0010 | 0b011 | RO       | ID_ISAR3_EL1     | ID_ISAR3_EL1          |
| 0b000       | 0b0000 | 0b0010 | 0b100 | RO       | ID_ISAR4_EL1     | ID_ISAR4_EL1          |
| 0b000       | 0b0000 | 0b0010 | 0b101 | RO       | ID_ISAR5_EL1     | ID_ISAR5_EL1          |
| 0b000       | 0b0000 | 0b0010 | 0b110 | RO       | ID_MMFR4_EL1     | ID_MMFR4_EL1          |
| 0b000       | 0b0000 | 0b0010 | 0b111 | RO       | ID_ISAR6_EL1     | ID_ISAR6_EL1          |
| 0b000       | 0b0000 | 0b0011 | 0b000 | RO       | MVFR0_EL1        | MVFR0_EL1             |
| 0b000       | 0b0000 | 0b0011 | 0b001 | RO       | MVFR1_EL1        | MVFR1_EL1             |
| 0b000       | 0b0000 | 0b0011 | 0b010 | RO       | MVFR2_EL1        | MVFR2_EL1             |
| 0b000       | 0b0000 | 0b0011 | 0b100 | RO       | ID_PFR2_EL1      | ID_PFR2_EL1           |
| 0b000       | 0b0000 | 0b0011 | 0b101 | RO       | ID_DFR1_EL1      | ID_DFR1_EL1           |
| 0b000       | 0b0000 | 0b0011 | 0b110 | RO       | ID_MMFR5_EL1     | ID_MMFR5_EL1          |
| 0b000       | 0b0000 | 0b0100 | 0b000 | RO       | ID_AA64PFR0_EL1  | ID_AA64PFR0_EL1       |
| 0b000       | 0b0000 | 0b0100 | 0b001 | RO       | ID_AA64PFR1_EL1  | ID_AA64PFR1_EL1       |
| 0b000       | 0b0000 | 0b0100 | 0b010 | RO       | ID_AA64PFR2_EL1  | ID_AA64PFR2_EL1       |
| 0b000       | 0b0000 | 0b0100 | 0b100 | RO       | ID_AA64ZFR0_EL1  | ID_AA64ZFR0_EL1       |
| 0b000       | 0b0000 | 0b0100 | 0b101 | RO       | ID_AA64SMFR0_EL1 | ID_AA64SMFR0_EL1      |
| 0b000       | 0b0000 | 0b0100 | 0b111 | RO       | ID_AA64FPFR0_EL1 | ID_AA64FPFR0_EL1      |
| 0b000       | 0b0000 | 0b0101 | 0b000 | RO       | ID_AA64DFR0_EL1  | ID_AA64DFR0_EL1       |
| 0b000       | 0b0000 | 0b0101 | 0b001 | RO       | ID_AA64DFR1_EL1  | ID_AA64DFR1_EL1       |
| 0b000       | 0b0000 | 0b0101 | 0b010 | RO       | ID_AA64DFR2_EL1  | ID_AA64DFR2_EL1       |
| 0b000       | 0b0000 | 0b0101 | 0b100 | RO       | ID_AA64AFR0_EL1  | ID_AA64AFR0_EL1       |
| 0b000       | 0b0000 | 0b0101 | 0b101 | RO       | ID_AA64AFR1_EL1  | ID_AA64AFR1_EL1       |
| 0b000       | 0b0000 | 0b0110 | 0b000 | RO       | ID_AA64ISAR0_EL1 | ID_AA64ISAR0_EL1      |
| 0b000       | 0b0000 | 0b0110 | 0b001 | RO       | ID_AA64ISAR1_EL1 | ID_AA64ISAR1_EL1      |
| 0b000       | 0b0000 | 0b0110 | 0b010 | RO       | ID_AA64ISAR2_EL1 | ID_AA64ISAR2_EL1      |
| 0b000       | 0b0000 | 0b0110 | 0b011 | RO       | ID_AA64ISAR3_EL1 | ID_AA64ISAR3_EL1      |
| 0b000       | 0b0000 | 0b0111 | 0b000 | RO       | ID_AA64MMFR0_EL1 | ID_AA64MMFR0_EL1      |
| 0b000       | 0b0000 | 0b0111 | 0b001 | RO       | ID_AA64MMFR1_EL1 | ID_AA64MMFR1_EL1      |
| 0b000       | 0b0000 | 0b0111 | 0b010 | RO       | ID_AA64MMFR2_EL1 | ID_AA64MMFR2_EL1      |
| 0b000       | 0b0000 | 0b0111 | 0b011 | RO       | ID_AA64MMFR3_EL1 | ID_AA64MMFR3_EL1      |
| 0b000       | 0b0000 | 0b0111 | 0b100 | RO       | ID_AA64MMFR4_EL1 | ID_AA64MMFR4_EL1      |
| 0b000       | 0b0001 | 0b0000 | 0b000 | RW       | SCTLR_EL1        | SCTLR_EL1 SCTLR_EL2   |
| 0b000       | 0b0001 | 0b0000 | 0b001 | RW       | ACTLR_EL1        | ACTLR_EL1 ACTLR_EL2   |
| 0b000       | 0b0001 | 0b0000 | 0b010 | RW       | CPACR_EL1        | CPACR_EL1 CPTR_EL2    |
| 0b000       | 0b0001 | 0b0000 | 0b011 | RW       | SCTLR2_EL1       | SCTLR2_EL1 SCTLR2_EL2 |
| 0b000 0b000 | 0b0001 | 0b0000 | 0b101 | RW       | RGSR_EL1         | RGSR_EL1              |
|             | 0b0001 | 0b0000 | 0b110 | RW       | GCR_EL1          | GCR_EL1               |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses                      |
|-------|--------|--------|-------|----------|-----------------|-------------------------------|
| 0b000 | 0b0001 | 0b0010 | 0b000 | RW       | ZCR_EL1         | ZCR_EL1 ZCR_EL2               |
| 0b000 | 0b0001 | 0b0010 | 0b001 | RW       | TRFCR_EL1       | TRFCR_EL1 TRFCR_EL2           |
| 0b000 | 0b0001 | 0b0010 | 0b011 | RW       | TRCITECR_EL1    | TRCITECR_EL1 TRCITECR_EL2     |
| 0b000 | 0b0001 | 0b0010 | 0b100 | RW       | SMPRI_EL1       | SMPRI_EL1                     |
| 0b000 | 0b0001 | 0b0010 | 0b110 | RW       | SMCR_EL1        | SMCR_EL1 SMCR_EL2             |
| 0b000 | 0b0001 | 0b0100 | 0b000 | RW       | SCTLRMASK_EL1   | SCTLRMASK_EL1 SCTLRMASK_EL2   |
| 0b000 | 0b0001 | 0b0100 | 0b001 | RW       | ACTLRMASK_EL1   | ACTLRMASK_EL1 ACTLRMASK_EL2   |
| 0b000 | 0b0001 | 0b0100 | 0b010 | RW       | CPACRMASK_EL1   | CPACRMASK_EL1 CPTRMASK_EL2    |
| 0b000 | 0b0001 | 0b0100 | 0b011 | RW       | SCTLR2MASK_EL1  | SCTLR2MASK_EL1 SCTLR2MASK_EL2 |
| 0b000 | 0b0001 | 0b0100 | 0b100 | RW       | CPACRALIAS_EL1  | CPACR_EL1                     |
| 0b000 | 0b0001 | 0b0100 | 0b101 | RW       | ACTLRALIAS_EL1  | ACTLR_EL1                     |
| 0b000 | 0b0001 | 0b0100 | 0b110 | RW       | SCTLRALIAS_EL1  | SCTLR_EL1                     |
| 0b000 | 0b0001 | 0b0100 | 0b111 | RW       | SCTLR2ALIAS_EL1 | SCTLR2_EL1                    |
| 0b000 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL1       | TTBR0_EL1 TTBR0_EL2           |
| 0b000 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL1       | TTBR0_EL1 TTBR0_EL2           |
| 0b000 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL1       | TTBR1_EL1 TTBR1_EL2           |
| 0b000 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL1       | TTBR1_EL1 TTBR1_EL2           |
| 0b000 | 0b0010 | 0b0000 | 0b010 | RW       | TCR_EL1         | TCR_EL1 TCR_EL2               |
| 0b000 | 0b0010 | 0b0000 | 0b011 | RW       | TCR2_EL1        | TCR2_EL1 TCR2_EL2             |
| 0b000 | 0b0010 | 0b0001 | 0b000 | RW       | APIAKeyLo_EL1   | APIAKeyLo_EL1                 |
| 0b000 | 0b0010 | 0b0001 | 0b001 | RW       | APIAKeyHi_EL1   | APIAKeyHi_EL1                 |
| 0b000 | 0b0010 | 0b0001 | 0b010 | RW       | APIBKeyLo_EL1   | APIBKeyLo_EL1                 |
| 0b000 | 0b0010 | 0b0001 | 0b011 | RW       | APIBKeyHi_EL1   | APIBKeyHi_EL1                 |
| 0b000 | 0b0010 | 0b0010 | 0b000 | RW       | APDAKeyLo_EL1   | APDAKeyLo_EL1                 |
| 0b000 | 0b0010 | 0b0010 | 0b001 | RW       | APDAKeyHi_EL1   | APDAKeyHi_EL1                 |
| 0b000 | 0b0010 | 0b0010 | 0b010 | RW       | APDBKeyLo_EL1   | APDBKeyLo_EL1                 |
| 0b000 | 0b0010 | 0b0010 | 0b011 | RW       | APDBKeyHi_EL1   | APDBKeyHi_EL1                 |
| 0b000 | 0b0010 | 0b0011 | 0b000 | RW       | APGAKeyLo_EL1   | APGAKeyLo_EL1                 |
| 0b000 | 0b0010 | 0b0011 | 0b001 | RW       | APGAKeyHi_EL1   | APGAKeyHi_EL1                 |
| 0b000 | 0b0010 | 0b0101 | 0b000 | RW       | GCSCR_EL1       | GCSCR_EL1                     |
| 0b000 | 0b0010 | 0b0101 | 0b001 | RW       | GCSPR_EL1       | GCSPR_EL1 GCSPR_EL2           |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic      | Accesses                  |
|-------|--------|--------|-------|----------|---------------|---------------------------|
| 0b000 | 0b0010 | 0b0101 | 0b010 | RW       | GCSCRE0_EL1   | GCSCRE0_EL1               |
| 0b000 | 0b0010 | 0b0111 | 0b010 | RW       | TCRMASK_EL1   | TCRMASK_EL1 TCRMASK_EL2   |
| 0b000 | 0b0010 | 0b0111 | 0b011 | RW       | TCR2MASK_EL1  | TCR2MASK_EL1 TCR2MASK_EL2 |
| 0b000 | 0b0010 | 0b0111 | 0b110 | RW       | TCRALIAS_EL1  | TCR_EL1                   |
| 0b000 | 0b0010 | 0b0111 | 0b111 | RW       | TCR2ALIAS_EL1 | TCR2_EL1                  |
| 0b000 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL1      | SPSR_EL1 SPSR_EL2         |
| 0b000 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL1       | ELR_EL1 ELR_EL2           |
| 0b000 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL0        | SP_EL0                    |
| 0b000 | 0b0100 | 0b0010 | 0b000 | RW       | SPSel         | SPSel                     |
| 0b000 | 0b0100 | 0b0010 | 0b010 | RO       | CurrentEL     | CurrentEL                 |
| 0b000 | 0b0100 | 0b0010 | 0b011 | RW       | PAN           | PAN                       |
| 0b000 | 0b0100 | 0b0010 | 0b100 | RW       | UAO           | UAO                       |
| 0b000 | 0b0100 | 0b0011 | 0b000 | RW       | ALLINT        | ALLINT                    |
| 0b000 | 0b0100 | 0b0011 | 0b001 | RW       | PM            | PM                        |
| 0b000 | 0b0100 | 0b0110 | 0b000 | RW       | ICC_PMR_EL1   | ICC_PMR_EL1 ICV_PMR_EL1   |
| 0b000 | 0b0101 | 0b0001 | 0b000 | RW       | AFSR0_EL1     | AFSR0_EL1 AFSR0_EL2       |
| 0b000 | 0b0101 | 0b0001 | 0b001 | RW       | AFSR1_EL1     | AFSR1_EL1 AFSR1_EL2       |
| 0b000 | 0b0101 | 0b0010 | 0b000 | RW       | ESR_EL1       | ESR_EL1 ESR_EL2           |
| 0b000 | 0b0101 | 0b0011 | 0b000 | RO       | ERRIDR_EL1    | ERRIDR_EL1                |
| 0b000 | 0b0101 | 0b0011 | 0b001 | RW       | ERRSELR_EL1   | ERRSELR_EL1               |
| 0b000 | 0b0101 | 0b0011 | 0b010 | RO       | ERXGSR_EL1    | ERXGSR_EL1                |
| 0b000 | 0b0101 | 0b0100 | 0b000 | RO       | ERXFR_EL1     | ERXFR_EL1                 |
| 0b000 | 0b0101 | 0b0100 | 0b001 | RW       | ERXCTLR_EL1   | ERXCTLR_EL1               |
| 0b000 | 0b0101 | 0b0100 | 0b010 | RW       | ERXSTATUS_EL1 | ERXSTATUS_EL1             |
| 0b000 | 0b0101 | 0b0100 | 0b011 | RW       | ERXADDR_EL1   | ERXADDR_EL1               |
| 0b000 | 0b0101 | 0b0100 | 0b100 | RO       | ERXPFGF_EL1   | ERXPFGF_EL1               |
| 0b000 | 0b0101 | 0b0100 | 0b101 | RW       | ERXPFGCTL_EL1 | ERXPFGCTL_EL1             |
| 0b000 | 0b0101 | 0b0100 | 0b110 | RW       | ERXPFGCDN_EL1 | ERXPFGCDN_EL1             |
| 0b000 | 0b0101 | 0b0101 | 0b000 | RW       | ERXMISC0_EL1  | ERXMISC0_EL1              |
| 0b000 | 0b0101 | 0b0101 | 0b001 | RW       | ERXMISC1_EL1  | ERXMISC1_EL1              |
| 0b000 | 0b0101 | 0b0101 | 0b010 | RW       | ERXMISC2_EL1  | ERXMISC2_EL1              |
| 0b000 | 0b0101 | 0b0101 | 0b011 | RW       | ERXMISC3_EL1  | ERXMISC3_EL1              |
| 0b000 | 0b0101 | 0b0110 | 0b000 | RW       | TFSR_EL1      | TFSR_EL1                  |
| 0b000 | 0b0101 | 0b0110 | 0b001 | RW       | TFSRE0_EL1    | TFSRE0_EL1                |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic       | Accesses            |
|-------|--------|--------|-------|----------|----------------|---------------------|
| 0b000 | 0b0110 | 0b0000 | 0b000 | RW       | FAR_EL1        | FAR_EL1 FAR_EL2     |
| 0b000 | 0b0110 | 0b0000 | 0b101 | RW       | PFAR_EL1       | PFAR_EL1            |
| 0b000 | 0b0111 | 0b0100 | 0b000 | RW       | PAR_EL1        | PAR_EL1             |
| 0b000 | 0b0111 | 0b0100 | 0b000 | RW       | PAR_EL1        | PAR_EL1             |
| 0b000 | 0b1001 | 0b1001 | 0b000 | RW       | PMSCR_EL1      | PMSCR_EL1 PMSCR_EL2 |
| 0b000 | 0b1001 | 0b1001 | 0b001 | RW       | PMSNEVFR_EL1   | PMSNEVFR_EL1        |
| 0b000 | 0b1001 | 0b1001 | 0b010 | RW       | PMSICR_EL1     | PMSICR_EL1          |
| 0b000 | 0b1001 | 0b1001 | 0b011 | RW       | PMSIRR_EL1     | PMSIRR_EL1          |
| 0b000 | 0b1001 | 0b1001 | 0b100 | RW       | PMSFCR_EL1     | PMSFCR_EL1          |
| 0b000 | 0b1001 | 0b1001 | 0b101 | RW       | PMSEVFR_EL1    | PMSEVFR_EL1         |
| 0b000 | 0b1001 | 0b1001 | 0b110 | RW       | PMSLATFR_EL1   | PMSLATFR_EL1        |
| 0b000 | 0b1001 | 0b1001 | 0b111 | RO       | PMSIDR_EL1     | PMSIDR_EL1          |
| 0b000 | 0b1001 | 0b1010 | 0b000 | RW       | PMBLIMITR_EL1  | PMBLIMITR_EL1       |
| 0b000 | 0b1001 | 0b1010 | 0b001 | RW       | PMBPTR_EL1     | PMBPTR_EL1          |
| 0b000 | 0b1001 | 0b1010 | 0b011 | RW       | PMBSR_EL1      | PMBSR_EL1 PMBSR_EL2 |
| 0b000 | 0b1001 | 0b1010 | 0b100 | RW       | PMSDSFR_EL1    | PMSDSFR_EL1         |
| 0b000 | 0b1001 | 0b1010 | 0b101 | RW       | PMBMAR_EL1     | PMBMAR_EL1          |
| 0b000 | 0b1001 | 0b1010 | 0b111 | RO       | PMBIDR_EL1     | PMBIDR_EL1          |
| 0b000 | 0b1001 | 0b1011 | 0b000 | RW       | TRBLIMITR_EL1  | TRBLIMITR_EL1       |
| 0b000 | 0b1001 | 0b1011 | 0b001 | RW       | TRBPTR_EL1     | TRBPTR_EL1          |
| 0b000 | 0b1001 | 0b1011 | 0b010 | RW       | TRBBASER_EL1   | TRBBASER_EL1        |
| 0b000 | 0b1001 | 0b1011 | 0b011 | RW       | TRBSR_EL1      | TRBSR_EL1 TRBSR_EL2 |
| 0b000 | 0b1001 | 0b1011 | 0b100 | RW       | TRBMAR_EL1     | TRBMAR_EL1          |
| 0b000 | 0b1001 | 0b1011 | 0b101 | RW       | TRBMPAM_EL1    | TRBMPAM_EL1         |
| 0b000 | 0b1001 | 0b1011 | 0b110 | RW       | TRBTRG_EL1     | TRBTRG_EL1          |
| 0b000 | 0b1001 | 0b1011 | 0b111 | RO       | TRBIDR_EL1     | TRBIDR_EL1          |
| 0b000 | 0b1001 | 0b1101 | 0b011 | RW       | PMSSCR_EL1     | PMSSCR_EL1          |
| 0b000 | 0b1001 | 0b1110 | 0b001 | RW       | PMINTENSET_EL1 | PMINTENSET_EL1      |
| 0b000 | 0b1001 | 0b1110 | 0b010 | RW       | PMINTENCLR_EL1 | PMINTENCLR_EL1      |
| 0b000 | 0b1001 | 0b1110 | 0b100 | RW       | PMUACR_EL1     | PMUACR_EL1          |
| 0b000 | 0b1001 | 0b1110 | 0b101 | RW       | PMECR_EL1      | PMECR_EL1           |
| 0b000 | 0b1001 | 0b1110 | 0b110 | RO       | PMMIR_EL1      | PMMIR_EL1           |
| 0b000 | 0b1001 | 0b1110 | 0b111 | RW       | PMIAR_EL1      | PMIAR_EL1           |
| 0b000 | 0b1010 | 0b0010 | 0b000 | RW       | MAIR_EL1       | MAIR_EL1 MAIR_EL2   |
| 0b000 | 0b1010 | 0b0010 | 0b001 | RW       | MAIR2_EL1      | MAIR2_EL1 MAIR2_EL2 |
| 0b000 | 0b1010 | 0b0010 | 0b010 | RW       | PIRE0_EL1      | PIRE0_EL1 PIRE0_EL2 |

| op1   | CRn    | CRm    | op2         | Access   | Mnemonic        | Accesses                        |
|-------|--------|--------|-------------|----------|-----------------|---------------------------------|
| 0b000 | 0b1010 | 0b0010 | 0b011       | RW       | PIR_EL1         | PIR_EL1 PIR_EL2                 |
| 0b000 | 0b1010 | 0b0010 | 0b100       | RW       | POR_EL1         | POR_EL1 POR_EL2                 |
| 0b000 | 0b1010 | 0b0010 | 0b101       | RW       | S2POR_EL1       | S2POR_EL1                       |
| 0b000 | 0b1010 | 0b0011 | 0b000       | RW       | AMAIR_EL1       | AMAIR_EL1 AMAIR_EL2             |
| 0b000 | 0b1010 | 0b0011 | 0b001       | RW       | AMAIR2_EL1      | AMAIR2_EL1 AMAIR2_EL2           |
| 0b000 | 0b1010 | 0b0100 | 0b000       | RW       | LORSA_EL1       | LORSA_EL1                       |
| 0b000 | 0b1010 | 0b0100 | 0b001       | RW       | LOREA_EL1       | LOREA_EL1                       |
| 0b000 | 0b1010 | 0b0100 | 0b010       | RW       | LORN_EL1        | LORN_EL1                        |
| 0b000 | 0b1010 | 0b0100 | 0b011       | RW       | LORC_EL1        | LORC_EL1                        |
| 0b000 | 0b1010 | 0b0100 | 0b100       | RO       | MPAMIDR_EL1     | MPAMIDR_EL1                     |
| 0b000 | 0b1010 | 0b0100 | 0b101       | RO       | MPAMBWIDR_EL1   | MPAMBWIDR_EL1                   |
| 0b000 | 0b1010 | 0b0100 | 0b111       | RO       | LORID_EL1       | LORID_EL1                       |
| 0b000 | 0b1010 | 0b0101 | 0b000       | RW       | MPAM1_EL1       | MPAM1_EL1 MPAM2_EL2             |
| 0b000 | 0b1010 | 0b0101 | 0b001       | RW       | MPAM0_EL1       | MPAM0_EL1                       |
| 0b000 | 0b1010 | 0b0101 | 0b011       | RW       | MPAMSM_EL1      | MPAMSM_EL1                      |
| 0b000 | 0b1010 | 0b0101 | 0b100       | RW       | MPAMBW1_EL1     | MPAMBW1_EL1 MPAMBW2_EL2         |
| 0b000 | 0b1010 | 0b0101 | 0b101       | RW       | MPAMBW0_EL1     | MPAMBW0_EL1                     |
| 0b000 | 0b1010 | 0b0101 | 0b111       | RW       | MPAMBWSM_EL1    | MPAMBWSM_EL1                    |
| 0b000 | 0b1100 | 0b0000 | 0b000       | RW       | VBAR_EL1        | VBAR_EL1 VBAR_EL2               |
| 0b000 | 0b1100 | 0b0000 | 0b001       | RO       | RVBAR_EL1       | RVBAR_EL1                       |
| 0b000 | 0b1100 | 0b0000 | 0b010       | RW       | RMR_EL1         | RMR_EL1                         |
| 0b000 | 0b1100 | 0b0001 | 0b000       | RO       | ISR_EL1         | ISR_EL1                         |
| 0b000 | 0b1100 | 0b0001 | 0b001       | RW       | DISR_EL1        | DISR_EL1 VDISR_EL2 VDISR_EL3    |
| 0b000 | 0b1100 | 0b1000 | 0b000       | RO       | ICC_IAR0_EL1    | ICC_IAR0_EL1 ICV_IAR0_EL1       |
| 0b000 | 0b1100 | 0b1000 | 0b001       | WO       | ICC_EOIR0_EL1   | ICC_EOIR0_EL1 ICV_EOIR0_EL1     |
| 0b000 | 0b1100 | 0b1000 | 0b010       | RO       | ICC_HPPIR0_EL1  | ICC_HPPIR0_EL1 ICV_HPPIR0_EL1   |
| 0b000 | 0b1100 | 0b1000 | 0b011       | RW       | ICC_BPR0_EL1    | ICC_BPR0_EL1 ICV_BPR0_EL1       |
| 0b000 | 0b1100 | 0b1000 | 0b1 :m[1:0] | RW       | ICC_AP0R<m>_EL1 | ICC_AP0R<n>_EL1 ICV_AP0R<n>_EL1 |
| 0b000 | 0b1100 | 0b1001 | 0b0 :m[1:0] | RW       | ICC_AP1R<m>_EL1 | ICC_AP1R<n>_EL1 ICV_AP1R<n>_EL1 |
| 0b000 | 0b1100 | 0b1001 | 0b101       | RO       | ICC_NMIAR1_EL1  | ICC_NMIAR1_EL1 ICV_NMIAR1_EL1   |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses                        |
|-------|--------|--------|-------|----------|-----------------|---------------------------------|
| 0b000 | 0b1100 | 0b1011 | 0b001 | WO       | ICC_DIR_EL1     | ICC_DIR_EL1 ICV_DIR_EL1         |
| 0b000 | 0b1100 | 0b1011 | 0b011 | RO       | ICC_RPR_EL1     | ICC_RPR_EL1 ICV_RPR_EL1         |
| 0b000 | 0b1100 | 0b1011 | 0b101 | WO       | ICC_SGI1R_EL1   | ICC_SGI1R_EL1                   |
| 0b000 | 0b1100 | 0b1011 | 0b110 | WO       | ICC_ASGI1R_EL1  | ICC_ASGI1R_EL1                  |
| 0b000 | 0b1100 | 0b1011 | 0b111 | WO       | ICC_SGI0R_EL1   | ICC_SGI0R_EL1                   |
| 0b000 | 0b1100 | 0b1100 | 0b000 | RO       | ICC_IAR1_EL1    | ICC_IAR1_EL1 ICV_IAR1_EL1       |
| 0b000 | 0b1100 | 0b1100 | 0b001 | WO       | ICC_EOIR1_EL1   | ICC_EOIR1_EL1 ICV_EOIR1_EL1     |
| 0b000 | 0b1100 | 0b1100 | 0b010 | RO       | ICC_HPPIR1_EL1  | ICC_HPPIR1_EL1 ICV_HPPIR1_EL1   |
| 0b000 | 0b1100 | 0b1100 | 0b011 | RW       | ICC_BPR1_EL1    | ICC_BPR1_EL1 ICV_BPR1_EL1       |
| 0b000 | 0b1100 | 0b1100 | 0b100 | RW       | ICC_CTLR_EL1    | ICC_CTLR_EL1 ICV_CTLR_EL1       |
| 0b000 | 0b1100 | 0b1100 | 0b101 | RW       | ICC_SRE_EL1     | ICC_SRE_EL1                     |
| 0b000 | 0b1100 | 0b1100 | 0b110 | RW       | ICC_IGRPEN0_EL1 | ICC_IGRPEN0_EL1 ICV_IGRPEN0_EL1 |
| 0b000 | 0b1100 | 0b1100 | 0b111 | RW       | ICC_IGRPEN1_EL1 | ICC_IGRPEN1_EL1 ICV_IGRPEN1_EL1 |
| 0b000 | 0b1101 | 0b0000 | 0b001 | RW       | CONTEXTIDR_EL1  | CONTEXTIDR_EL1 CONTEXTIDR_EL2   |
| 0b000 | 0b1101 | 0b0000 | 0b011 | RW       | RCWSMASK_EL1    | RCWSMASK_EL1                    |
| 0b000 | 0b1101 | 0b0000 | 0b011 | RW       | RCWSMASK_EL1    | RCWSMASK_EL1                    |
| 0b000 | 0b1101 | 0b0000 | 0b100 | RW       | TPIDR_EL1       | TPIDR_EL1                       |
| 0b000 | 0b1101 | 0b0000 | 0b101 | RW       | ACCDATA_EL1     | ACCDATA_EL1                     |
| 0b000 | 0b1101 | 0b0000 | 0b110 | RW       | RCWMASK_EL1     | RCWMASK_EL1                     |
| 0b000 | 0b1101 | 0b0000 | 0b110 | RW       | RCWMASK_EL1     | RCWMASK_EL1                     |
| 0b000 | 0b1101 | 0b0000 | 0b111 | RW       | SCXTNUM_EL1     | SCXTNUM_EL1 SCXTNUM_EL2         |
| 0b000 | 0b1110 | 0b0001 | 0b000 | RW       | CNTKCTL_EL1     | CNTHCTL_EL2 CNTKCTL_EL1         |
| 0b001 | 0b0000 | 0b0000 | 0b000 | RO       | CCSIDR_EL1      | CCSIDR_EL1                      |
| 0b001 | 0b0000 | 0b0000 | 0b001 | RO       | CLIDR_EL1       | CLIDR_EL1                       |
| 0b001 | 0b0000 | 0b0000 | 0b010 | RO       | CCSIDR2_EL1     | CCSIDR2_EL1                     |
| 0b001 | 0b0000 | 0b0000 | 0b100 | RO       | GMID_EL1        | GMID_EL1                        |
| 0b001 | 0b0000 | 0b0000 | 0b110 | RO       | SMIDR_EL1       | SMIDR_EL1                       |
| 0b001 | 0b0000 | 0b0000 | 0b111 | RO       | AIDR_EL1        | AIDR_EL1                        |
| 0b010 | 0b0000 | 0b0000 | 0b000 | RW       | CSSELR_EL1      | CSSELR_EL1                      |
| 0b011 | 0b0000 | 0b0000 | 0b001 | RO       | CTR_EL0         | CTR_EL0                         |
| 0b011 | 0b0000 | 0b0000 | 0b111 | RO       | DCZID_EL0       | DCZID_EL0                       |
| 0b011 | 0b0010 | 0b0100 | 0b000 | RO       | RNDR            | RNDR                            |
| 0b011 | 0b0010 | 0b0100 | 0b001 | RO       | RNDRRS          | RNDRRS                          |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses        |
|-------|--------|--------|-------|----------|-----------------|-----------------|
| 0b011 | 0b0010 | 0b0101 | 0b001 | RW       | GCSPR_EL0       | GCSPR_EL0       |
| 0b011 | 0b0100 | 0b0010 | 0b000 | RW       | NZCV            | NZCV            |
| 0b011 | 0b0100 | 0b0010 | 0b001 | RW       | DAIF            | DAIF            |
| 0b011 | 0b0100 | 0b0010 | 0b010 | RW       | SVCR            | SVCR            |
| 0b011 | 0b0100 | 0b0010 | 0b101 | RW       | DIT             | DIT             |
| 0b011 | 0b0100 | 0b0010 | 0b110 | RW       | SSBS            | SSBS            |
| 0b011 | 0b0100 | 0b0010 | 0b111 | RW       | TCO             | TCO             |
| 0b011 | 0b0100 | 0b0100 | 0b000 | RW       | FPCR            | FPCR            |
| 0b011 | 0b0100 | 0b0100 | 0b001 | RW       | FPSR            | FPSR            |
| 0b011 | 0b0100 | 0b0100 | 0b010 | RW       | FPMR            | FPMR            |
| 0b011 | 0b0100 | 0b0101 | 0b000 | RW       | DSPSR_EL0       | DSPSR_EL0       |
| 0b011 | 0b0100 | 0b0101 | 0b001 | RW       | DLR_EL0         | DLR_EL0         |
| 0b011 | 0b1001 | 0b0100 | 0b000 | RW       | PMICNTR_EL0     | PMICNTR_EL0     |
| 0b011 | 0b1001 | 0b0110 | 0b000 | RW       | PMICFILTR_EL0   | PMICFILTR_EL0   |
| 0b011 | 0b1001 | 0b1100 | 0b000 | RW       | PMCR_EL0        | PMCR_EL0        |
| 0b011 | 0b1001 | 0b1100 | 0b001 | RW       | PMCNTENSET_EL0  | PMCNTENSET_EL0  |
| 0b011 | 0b1001 | 0b1100 | 0b010 | RW       | PMCNTENCLR_EL0  | PMCNTENCLR_EL0  |
| 0b011 | 0b1001 | 0b1100 | 0b011 | RW       | PMOVSCLR_EL0    | PMOVSCLR_EL0    |
| 0b011 | 0b1001 | 0b1100 | 0b100 | WO       | PMSWINC_EL0     | PMSWINC_EL0     |
| 0b011 | 0b1001 | 0b1100 | 0b101 | RW       | PMSELR_EL0      | PMSELR_EL0      |
| 0b011 | 0b1001 | 0b1100 | 0b110 | RO       | PMCEID0_EL0     | PMCEID0_EL0     |
| 0b011 | 0b1001 | 0b1100 | 0b111 | RO       | PMCEID1_EL0     | PMCEID1_EL0     |
| 0b011 | 0b1001 | 0b1101 | 0b000 | RW       | PMCCNTR_EL0     | PMCCNTR_EL0     |
| 0b011 | 0b1001 | 0b1101 | 0b001 | RW       | PMXEVTYPER_EL0  | PMXEVTYPER_EL0  |
| 0b011 | 0b1001 | 0b1101 | 0b010 | RW       | PMXEVCNTR_EL0   | PMXEVCNTR_EL0   |
| 0b011 | 0b1001 | 0b1101 | 0b100 | WO       | PMZR_EL0        | PMZR_EL0        |
| 0b011 | 0b1001 | 0b1110 | 0b000 | RW       | PMUSERENR_EL0   | PMUSERENR_EL0   |
| 0b011 | 0b1001 | 0b1110 | 0b011 | RW       | PMOVSSET_EL0    | PMOVSSET_EL0    |
| 0b011 | 0b1010 | 0b0010 | 0b100 | RW       | POR_EL0         | POR_EL0         |
| 0b011 | 0b1101 | 0b0000 | 0b010 | RW       | TPIDR_EL0       | TPIDR_EL0       |
| 0b011 | 0b1101 | 0b0000 | 0b011 | RW       | TPIDRRO_EL0     | TPIDRRO_EL0     |
| 0b011 | 0b1101 | 0b0000 | 0b101 | RW       | TPIDR2_EL0      | TPIDR2_EL0      |
| 0b011 | 0b1101 | 0b0000 | 0b111 | RW       | SCXTNUM_EL0     | SCXTNUM_EL0     |
| 0b011 | 0b1101 | 0b0010 | 0b000 | RW       | AMCR_EL0        | AMCR_EL0        |
| 0b011 | 0b1101 | 0b0010 | 0b001 | RO       | AMCFGR_EL0      | AMCFGR_EL0      |
| 0b011 | 0b1101 | 0b0010 | 0b010 | RO       | AMCGCR_EL0      | AMCGCR_EL0      |
| 0b011 | 0b1101 | 0b0010 | 0b011 | RW       | AMUSERENR_EL0   | AMUSERENR_EL0   |
| 0b011 | 0b1101 | 0b0010 | 0b100 | RW       | AMCNTENCLR0_EL0 | AMCNTENCLR0_EL0 |
| 0b011 | 0b1101 | 0b0010 | 0b101 | RW       | AMCNTENSET0_EL0 | AMCNTENSET0_EL0 |
| 0b011 | 0b1101 | 0b0010 | 0b110 | RO       | AMCG1IDR_EL0    | AMCG1IDR_EL0    |

| op1   | CRn    | CRm          | op2    | Access   | Mnemonic          | Accesses                                     |
|-------|--------|--------------|--------|----------|-------------------|----------------------------------------------|
| 0b011 | 0b1101 | 0b0011       | 0b000  | RW       | AMCNTENCLR1_EL0   | AMCNTENCLR1_EL0                              |
| 0b011 | 0b1101 | 0b0011       | 0b001  | RW       | AMCNTENSET1_EL0   | AMCNTENSET1_EL0                              |
| 0b011 | 0b1101 | 0b010 :m[3]  | m[2:0] | RW       | AMEVCNTR0<m>_EL0  | AMEVCNTR0<n>_EL0                             |
| 0b011 | 0b1101 | 0b011 :m[3]  | m[2:0] | RO       | AMEVTYPER0<m>_EL0 | AMEVTYPER0<n>_EL0                            |
| 0b011 | 0b1101 | 0b110 :m[3]  | m[2:0] | RW       | AMEVCNTR1<m>_EL0  | AMEVCNTR1<n>_EL0                             |
| 0b011 | 0b1101 | 0b111 :m[3]  | m[2:0] | RW       | AMEVTYPER1<m>_EL0 | AMEVTYPER1<n>_EL0                            |
| 0b011 | 0b1110 | 0b0000       | 0b000  | RW       | CNTFRQ_EL0        | CNTFRQ_EL0                                   |
| 0b011 | 0b1110 | 0b0000       | 0b001  | RO       | CNTPCT_EL0        | CNTPCT_EL0                                   |
| 0b011 | 0b1110 | 0b0000       | 0b010  | RO       | CNTVCT_EL0        | CNTVCT_EL0                                   |
| 0b011 | 0b1110 | 0b0000       | 0b101  | RO       | CNTPCTSS_EL0      | CNTPCTSS_EL0                                 |
| 0b011 | 0b1110 | 0b0000       | 0b110  | RO       | CNTVCTSS_EL0      | CNTVCTSS_EL0                                 |
| 0b011 | 0b1110 | 0b0010       | 0b000  | RW       | CNTP_TVAL_EL0     | CNTHPS_TVAL_EL2 CNTHP_TVAL_EL2 CNTP_TVAL_EL0 |
| 0b011 | 0b1110 | 0b0010       | 0b001  | RW       | CNTP_CTL_EL0      | CNTHPS_CTL_EL2 CNTHP_CTL_EL2 CNTP_CTL_EL0    |
| 0b011 | 0b1110 | 0b0010       | 0b010  | RW       | CNTP_CVAL_EL0     | CNTHPS_CVAL_EL2 CNTHP_CVAL_EL2 CNTP_CVAL_EL0 |
| 0b011 | 0b1110 | 0b0011       | 0b000  | RW       | CNTV_TVAL_EL0     | CNTHVS_TVAL_EL2 CNTHV_TVAL_EL2 CNTV_TVAL_EL0 |
| 0b011 | 0b1110 | 0b0011       | 0b001  | RW       | CNTV_CTL_EL0      | CNTHVS_CTL_EL2 CNTHV_CTL_EL2 CNTV_CTL_EL0    |
| 0b011 | 0b1110 | 0b0011       | 0b010  | RW       | CNTV_CVAL_EL0     | CNTHVS_CVAL_EL2 CNTHV_CVAL_EL2 CNTV_CVAL_EL0 |
| 0b011 | 0b1110 | 0b10 :m[4:3] | m[2:0] | RW       | PMEVCNTR<m>_EL0   | PMEVCNTR<n>_EL0                              |
| 0b011 | 0b1110 | 0b1111       | 0b111  | RW       | PMCCFILTR_EL0     | PMCCFILTR_EL0                                |
| 0b011 | 0b1110 | 0b11 :m[4:3] | m[2:0] | RW       | PMEVTYPER<m>_EL0  | PMEVTYPER<n>_EL0                             |
| 0b100 | 0b0000 | 0b0000       | 0b000  | RW       | VPIDR_EL2         | VPIDR_EL2                                    |
| 0b100 | 0b0000 | 0b0000       | 0b101  | RW       | VMPIDR_EL2        | VMPIDR_EL2                                   |
| 0b100 | 0b0001 | 0b0000       | 0b000  | RW       | SCTLR_EL2         | SCTLR_EL2                                    |
| 0b100 | 0b0001 | 0b0000       | 0b001  | RW       | ACTLR_EL2         | ACTLR_EL2                                    |
| 0b100 | 0b0001 | 0b0000       | 0b011  | RW       | SCTLR2_EL2        | SCTLR2_EL2                                   |
| 0b100 | 0b0001 | 0b0001       | 0b000  | RW       | HCR_EL2           | HCR_EL2                                      |
| 0b100 | 0b0001 | 0b0001       | 0b001  | RW       | MDCR_EL2          | MDCR_EL2                                     |
| 0b100 | 0b0001 | 0b0001       | 0b010  | RW       | CPTR_EL2          | CPTR_EL2                                     |
| 0b100 | 0b0001 | 0b0001       | 0b011  | RW       | HSTR_EL2          | HSTR_EL2                                     |
| 0b100 | 0b0001 | 0b0001       | 0b100  | RW       | HFGRTR_EL2        | HFGRTR_EL2                                   |
| 0b100 | 0b0001 | 0b0001       | 0b101  | RW       | HFGWTR_EL2        | HFGWTR_EL2                                   |
| 0b100 | 0b0001 | 0b0001       | 0b110  | RW       | HFGITR_EL2        | HFGITR_EL2                                   |
| 0b100 | 0b0001 | 0b0001       | 0b111  | RW       | HACR_EL2          | HACR_EL2                                     |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic       | Accesses       |
|-------|--------|--------|-------|----------|----------------|----------------|
| 0b100 | 0b0001 | 0b0010 | 0b000 | RW       | ZCR_EL2        | ZCR_EL2        |
| 0b100 | 0b0001 | 0b0010 | 0b001 | RW       | TRFCR_EL2      | TRFCR_EL2      |
| 0b100 | 0b0001 | 0b0010 | 0b010 | RW       | HCRX_EL2       | HCRX_EL2       |
| 0b100 | 0b0001 | 0b0010 | 0b011 | RW       | TRCITECR_EL2   | TRCITECR_EL2   |
| 0b100 | 0b0001 | 0b0010 | 0b101 | RW       | SMPRIMAP_EL2   | SMPRIMAP_EL2   |
| 0b100 | 0b0001 | 0b0010 | 0b110 | RW       | SMCR_EL2       | SMCR_EL2       |
| 0b100 | 0b0001 | 0b0011 | 0b001 | RW       | SDER32_EL2     | SDER32_EL2     |
| 0b100 | 0b0001 | 0b0100 | 0b000 | RW       | SCTLRMASK_EL2  | SCTLRMASK_EL2  |
| 0b100 | 0b0001 | 0b0100 | 0b001 | RW       | ACTLRMASK_EL2  | ACTLRMASK_EL2  |
| 0b100 | 0b0001 | 0b0100 | 0b010 | RW       | CPTRMASK_EL2   | CPTRMASK_EL2   |
| 0b100 | 0b0001 | 0b0100 | 0b011 | RW       | SCTLR2MASK_EL2 | SCTLR2MASK_EL2 |
| 0b100 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL2      | TTBR0_EL2      |
| 0b100 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL2      | TTBR0_EL2      |
| 0b100 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL2      | TTBR1_EL2      |
| 0b100 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL2      | TTBR1_EL2      |
| 0b100 | 0b0010 | 0b0000 | 0b010 | RW       | TCR_EL2        | TCR_EL2        |
| 0b100 | 0b0010 | 0b0000 | 0b011 | RW       | TCR2_EL2       | TCR2_EL2       |
| 0b100 | 0b0010 | 0b0001 | 0b000 | RW       | VTTBR_EL2      | VTTBR_EL2      |
| 0b100 | 0b0010 | 0b0001 | 0b000 | RW       | VTTBR_EL2      | VTTBR_EL2      |
| 0b100 | 0b0010 | 0b0001 | 0b010 | RW       | VTCR_EL2       | VTCR_EL2       |
| 0b100 | 0b0010 | 0b0010 | 0b000 | RW       | VNCR_EL2       | VNCR_EL2       |
| 0b100 | 0b0010 | 0b0011 | 0b010 | RW       | HDBSSBR_EL2    | HDBSSBR_EL2    |
| 0b100 | 0b0010 | 0b0011 | 0b011 | RW       | HDBSSPROD_EL2  | HDBSSPROD_EL2  |
| 0b100 | 0b0010 | 0b0011 | 0b100 | RW       | HACDBSBR_EL2   | HACDBSBR_EL2   |
| 0b100 | 0b0010 | 0b0011 | 0b101 | RW       | HACDBSCONS_EL2 | HACDBSCONS_EL2 |
| 0b100 | 0b0010 | 0b0101 | 0b000 | RW       | GCSCR_EL2      | GCSCR_EL2      |
| 0b100 | 0b0010 | 0b0101 | 0b001 | RW       | GCSPR_EL2      | GCSPR_EL2      |
| 0b100 | 0b0010 | 0b0110 | 0b000 | RW       | VSTTBR_EL2     | VSTTBR_EL2     |
| 0b100 | 0b0010 | 0b0110 | 0b010 | RW       | VSTCR_EL2      | VSTCR_EL2      |
| 0b100 | 0b0010 | 0b0111 | 0b010 | RW       | TCRMASK_EL2    | TCRMASK_EL2    |
| 0b100 | 0b0010 | 0b0111 | 0b011 | RW       | TCR2MASK_EL2   | TCR2MASK_EL2   |
| 0b100 | 0b0011 | 0b0000 | 0b000 | RW       | DACR32_EL2     | DACR32_EL2     |
| 0b100 | 0b0011 | 0b0001 | 0b000 | RW       | HDFGRTR2_EL2   | HDFGRTR2_EL2   |
| 0b100 | 0b0011 | 0b0001 | 0b001 | RW       | HDFGWTR2_EL2   | HDFGWTR2_EL2   |
| 0b100 | 0b0011 | 0b0001 | 0b010 | RW       | HFGRTR2_EL2    | HFGRTR2_EL2    |
| 0b100 | 0b0011 | 0b0001 | 0b011 | RW       | HFGWTR2_EL2    | HFGWTR2_EL2    |
| 0b100 | 0b0011 | 0b0001 | 0b100 | RW       | HDFGRTR_EL2    | HDFGRTR_EL2    |
| 0b100 | 0b0011 | 0b0001 | 0b101 | RW       | HDFGWTR_EL2    | HDFGWTR_EL2    |
| 0b100 | 0b0011 | 0b0001 | 0b110 | RW       | HAFGRTR_EL2    | HAFGRTR_EL2    |
| 0b100 | 0b0011 | 0b0001 | 0b111 | RW       | HFGITR2_EL2    | HFGITR2_EL2    |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic      | Accesses          |
|-------|--------|--------|-------|----------|---------------|-------------------|
| 0b100 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL2      | SPSR_EL1 SPSR_EL2 |
| 0b100 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL2       | ELR_EL1 ELR_EL2   |
| 0b100 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL1        | SP_EL1            |
| 0b100 | 0b0100 | 0b0011 | 0b000 | RW       | SPSR_irq      | SPSR_irq          |
| 0b100 | 0b0100 | 0b0011 | 0b001 | RW       | SPSR_abt      | SPSR_abt          |
| 0b100 | 0b0100 | 0b0011 | 0b010 | RW       | SPSR_und      | SPSR_und          |
| 0b100 | 0b0100 | 0b0011 | 0b011 | RW       | SPSR_fiq      | SPSR_fiq          |
| 0b100 | 0b0101 | 0b0000 | 0b001 | RW       | IFSR32_EL2    | IFSR32_EL2        |
| 0b100 | 0b0101 | 0b0001 | 0b000 | RW       | AFSR0_EL2     | AFSR0_EL2         |
| 0b100 | 0b0101 | 0b0001 | 0b001 | RW       | AFSR1_EL2     | AFSR1_EL2         |
| 0b100 | 0b0101 | 0b0010 | 0b000 | RW       | ESR_EL2       | ESR_EL1 ESR_EL2   |
| 0b100 | 0b0101 | 0b0010 | 0b011 | RW       | VSESR_EL2     | VSESR_EL2         |
| 0b100 | 0b0101 | 0b0011 | 0b000 | RW       | FPEXC32_EL2   | FPEXC32_EL2       |
| 0b100 | 0b0101 | 0b0110 | 0b000 | RW       | TFSR_EL2      | TFSR_EL1 TFSR_EL2 |
| 0b100 | 0b0110 | 0b0000 | 0b000 | RW       | FAR_EL2       | FAR_EL1 FAR_EL2   |
| 0b100 | 0b0110 | 0b0000 | 0b100 | RW       | HPFAR_EL2     | HPFAR_EL2         |
| 0b100 | 0b0110 | 0b0000 | 0b101 | RW       | PFAR_EL2      | PFAR_EL2          |
| 0b100 | 0b1001 | 0b1001 | 0b000 | RW       | PMSCR_EL2     | PMSCR_EL2         |
| 0b100 | 0b1001 | 0b1010 | 0b011 | RW       | PMBSR_EL2     | PMBSR_EL2         |
| 0b100 | 0b1001 | 0b1011 | 0b011 | RW       | TRBSR_EL2     | TRBSR_EL2         |
| 0b100 | 0b1010 | 0b0001 | 0b001 | RW       | MAIR2_EL2     | MAIR2_EL2         |
| 0b100 | 0b1010 | 0b0010 | 0b000 | RW       | MAIR_EL2      | MAIR_EL2          |
| 0b100 | 0b1010 | 0b0010 | 0b010 | RW       | PIRE0_EL2     | PIRE0_EL2         |
| 0b100 | 0b1010 | 0b0010 | 0b011 | RW       | PIR_EL2       | PIR_EL2           |
| 0b100 | 0b1010 | 0b0010 | 0b100 | RW       | POR_EL2       | POR_EL2           |
| 0b100 | 0b1010 | 0b0010 | 0b101 | RW       | S2PIR_EL2     | S2PIR_EL2         |
| 0b100 | 0b1010 | 0b0011 | 0b000 | RW       | AMAIR_EL2     | AMAIR_EL2         |
| 0b100 | 0b1010 | 0b0011 | 0b001 | RW       | AMAIR2_EL2    | AMAIR2_EL2        |
| 0b100 | 0b1010 | 0b0100 | 0b000 | RW       | MPAMHCR_EL2   | MPAMHCR_EL2       |
| 0b100 | 0b1010 | 0b0100 | 0b001 | RW       | MPAMVPMV_EL2  | MPAMVPMV_EL2      |
| 0b100 | 0b1010 | 0b0101 | 0b000 | RW       | MPAM2_EL2     | MPAM2_EL2         |
| 0b100 | 0b1010 | 0b0101 | 0b100 | RW       | MPAMBW2_EL2   | MPAMBW2_EL2       |
| 0b100 | 0b1010 | 0b0101 | 0b110 | RW       | MPAMBWCAP_EL2 | MPAMBWCAP_EL2     |
| 0b100 | 0b1010 | 0b0110 | 0b000 | RW       | MPAMVPM0_EL2  | MPAMVPM0_EL2      |
| 0b100 | 0b1010 | 0b0110 | 0b001 | RW       | MPAMVPM1_EL2  | MPAMVPM1_EL2      |
| 0b100 | 0b1010 | 0b0110 | 0b010 | RW       | MPAMVPM2_EL2  | MPAMVPM2_EL2      |
| 0b100 | 0b1010 | 0b0110 | 0b011 | RW       | MPAMVPM3_EL2  | MPAMVPM3_EL2      |

| op1   | CRn    | CRm         | op2         | Access   | Mnemonic            | Accesses            |
|-------|--------|-------------|-------------|----------|---------------------|---------------------|
| 0b100 | 0b1010 | 0b0110      | 0b100       | RW       | MPAMVPM4_EL2        | MPAMVPM4_EL2        |
| 0b100 | 0b1010 | 0b0110      | 0b101       | RW       | MPAMVPM5_EL2        | MPAMVPM5_EL2        |
| 0b100 | 0b1010 | 0b0110      | 0b110       | RW       | MPAMVPM6_EL2        | MPAMVPM6_EL2        |
| 0b100 | 0b1010 | 0b0110      | 0b111       | RW       | MPAMVPM7_EL2        | MPAMVPM7_EL2        |
| 0b100 | 0b1010 | 0b1000      | 0b000       | RW       | MECID_P0_EL2        | MECID_P0_EL2        |
| 0b100 | 0b1010 | 0b1000      | 0b001       | RW       | MECID_A0_EL2        | MECID_A0_EL2        |
| 0b100 | 0b1010 | 0b1000      | 0b010       | RW       | MECID_P1_EL2        | MECID_P1_EL2        |
| 0b100 | 0b1010 | 0b1000      | 0b011       | RW       | MECID_A1_EL2        | MECID_A1_EL2        |
| 0b100 | 0b1010 | 0b1000      | 0b111       | RO       | MECIDR_EL2          | MECIDR_EL2          |
| 0b100 | 0b1010 | 0b1001      | 0b000       | RW       | VMECID_P_EL2        | VMECID_P_EL2        |
| 0b100 | 0b1010 | 0b1001      | 0b001       | RW       | VMECID_A_EL2        | VMECID_A_EL2        |
| 0b100 | 0b1100 | 0b0000      | 0b000       | RW       | VBAR_EL2            | VBAR_EL2            |
| 0b100 | 0b1100 | 0b0000      | 0b001       | RO       | RVBAR_EL2           | RVBAR_EL2           |
| 0b100 | 0b1100 | 0b0000      | 0b010       | RW       | RMR_EL2             | RMR_EL2             |
| 0b100 | 0b1100 | 0b0001      | 0b001       | RW       | VDISR_EL2           | VDISR_EL2           |
| 0b100 | 0b1100 | 0b1000      | 0b0 :m[1:0] | RW       | ICH_AP0R<m>_EL2     | ICH_AP0R<n>_EL2     |
| 0b100 | 0b1100 | 0b1001      | 0b0 :m[1:0] | RW       | ICH_AP1R<m>_EL2     | ICH_AP1R<n>_EL2     |
| 0b100 | 0b1100 | 0b1001      | 0b101       | RW       | ICC_SRE_EL2         | ICC_SRE_EL2         |
| 0b100 | 0b1100 | 0b1011      | 0b000       | RW       | ICH_HCR_EL2         | ICH_HCR_EL2         |
| 0b100 | 0b1100 | 0b1011      | 0b001       | RO       | ICH_VTR_EL2         | ICH_VTR_EL2         |
| 0b100 | 0b1100 | 0b1011      | 0b010       | RO       | ICH_MISR_EL2        | ICH_MISR_EL2        |
| 0b100 | 0b1100 | 0b1011      | 0b011       | RO       | ICH_EISR_EL2        | ICH_EISR_EL2        |
| 0b100 | 0b1100 | 0b1011      | 0b101       | RO       | ICH_ELRSR_EL2       | ICH_ELRSR_EL2       |
| 0b100 | 0b1100 | 0b1011      | 0b111       | RW       | ICH_VMCR_EL2        | ICH_VMCR_EL2        |
| 0b100 | 0b1100 | 0b110 :m[3] | m[2:0]      | RW       | ICH_LR<m>_EL2       | ICH_LR<n>_EL2       |
| 0b100 | 0b1101 | 0b0000      | 0b001       | RW       | CONTEXTIDR_EL2      | CONTEXTIDR_EL2      |
| 0b100 | 0b1101 | 0b0000      | 0b010       | RW       | TPIDR_EL2           | TPIDR_EL2           |
| 0b100 | 0b1101 | 0b0000      | 0b111       | RW       | SCXTNUM_EL2         | SCXTNUM_EL2         |
| 0b100 | 0b1101 | 0b100 :m[3] | m[2:0]      | RW       | AMEVCNTVOFF0<m>_EL2 | AMEVCNTVOFF0<n>_EL2 |
| 0b100 | 0b1101 | 0b101 :m[3] | m[2:0]      | RW       | AMEVCNTVOFF1<m>_EL2 | AMEVCNTVOFF1<n>_EL2 |
| 0b100 | 0b1110 | 0b0000      | 0b011       | RW       | CNTVOFF_EL2         | CNTVOFF_EL2         |
| 0b100 | 0b1110 | 0b0000      | 0b110       | RW       | CNTPOFF_EL2         | CNTPOFF_EL2         |
| 0b100 | 0b1110 | 0b0001      | 0b000       | RW       | CNTHCTL_EL2         | CNTHCTL_EL2         |
| 0b100 | 0b1110 | 0b0010      | 0b000       | RW       | CNTHP_TVAL_EL2      | CNTHP_TVAL_EL2      |
| 0b100 | 0b1110 | 0b0010      | 0b001       | RW       | CNTHP_CTL_EL2       | CNTHP_CTL_EL2       |
| 0b100 | 0b1110 | 0b0010      | 0b010       | RW       | CNTHP_CVAL_EL2      | CNTHP_CVAL_EL2      |
| 0b100 | 0b1110 | 0b0011      | 0b000       | RW       | CNTHV_TVAL_EL2      | CNTHV_TVAL_EL2      |
| 0b100 | 0b1110 | 0b0011      | 0b001       | RW       | CNTHV_CTL_EL2       | CNTHV_CTL_EL2       |
| 0b100 | 0b1110 | 0b0011      | 0b010       | RW       | CNTHV_CVAL_EL2      | CNTHV_CVAL_EL2      |
| 0b100 | 0b1110 | 0b0100      | 0b000       | RW       | CNTHVS_TVAL_EL2     | CNTHVS_TVAL_EL2     |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses        |
|-------|--------|--------|-------|----------|-----------------|-----------------|
| 0b100 | 0b1110 | 0b0100 | 0b001 | RW       | CNTHVS_CTL_EL2  | CNTHVS_CTL_EL2  |
| 0b100 | 0b1110 | 0b0100 | 0b010 | RW       | CNTHVS_CVAL_EL2 | CNTHVS_CVAL_EL2 |
| 0b100 | 0b1110 | 0b0101 | 0b000 | RW       | CNTHPS_TVAL_EL2 | CNTHPS_TVAL_EL2 |
| 0b100 | 0b1110 | 0b0101 | 0b001 | RW       | CNTHPS_CTL_EL2  | CNTHPS_CTL_EL2  |
| 0b100 | 0b1110 | 0b0101 | 0b010 | RW       | CNTHPS_CVAL_EL2 | CNTHPS_CVAL_EL2 |
| 0b101 | 0b0001 | 0b0000 | 0b000 | RW       | SCTLR_EL12      | SCTLR_EL1       |
| 0b101 | 0b0001 | 0b0000 | 0b001 | RW       | ACTLR_EL12      | ACTLR_EL1       |
| 0b101 | 0b0001 | 0b0000 | 0b010 | RW       | CPACR_EL12      | CPACR_EL1       |
| 0b101 | 0b0001 | 0b0000 | 0b011 | RW       | SCTLR2_EL12     | SCTLR2_EL1      |
| 0b101 | 0b0001 | 0b0010 | 0b000 | RW       | ZCR_EL12        | ZCR_EL1         |
| 0b101 | 0b0001 | 0b0010 | 0b001 | RW       | TRFCR_EL12      | TRFCR_EL1       |
| 0b101 | 0b0001 | 0b0010 | 0b011 | RW       | TRCITECR_EL12   | TRCITECR_EL1    |
| 0b101 | 0b0001 | 0b0010 | 0b110 | RW       | SMCR_EL12       | SMCR_EL1        |
| 0b101 | 0b0001 | 0b0100 | 0b000 | RW       | SCTLRMASK_EL12  | SCTLRMASK_EL1   |
| 0b101 | 0b0001 | 0b0100 | 0b001 | RW       | ACTLRMASK_EL12  | ACTLRMASK_EL1   |
| 0b101 | 0b0001 | 0b0100 | 0b010 | RW       | CPACRMASK_EL12  | CPACRMASK_EL1   |
| 0b101 | 0b0001 | 0b0100 | 0b011 | RW       | SCTLR2MASK_EL12 | SCTLR2MASK_EL1  |
| 0b101 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL12      | TTBR0_EL1       |
| 0b101 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL12      | TTBR0_EL1       |
| 0b101 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL12      | TTBR1_EL1       |
| 0b101 | 0b0010 | 0b0000 | 0b001 | RW       | TTBR1_EL12      | TTBR1_EL1       |
| 0b101 | 0b0010 | 0b0000 | 0b010 | RW       | TCR_EL12        | TCR_EL1         |
| 0b101 | 0b0010 | 0b0000 | 0b011 | RW       | TCR2_EL12       | TCR2_EL1        |
| 0b101 | 0b0010 | 0b0101 | 0b000 | RW       | GCSCR_EL12      | GCSCR_EL1       |
| 0b101 | 0b0010 | 0b0101 | 0b001 | RW       | GCSPR_EL12      | GCSPR_EL1       |
| 0b101 | 0b0010 | 0b0111 | 0b010 | RW       | TCRMASK_EL12    | TCRMASK_EL1     |
| 0b101 | 0b0010 | 0b0111 | 0b011 | RW       | TCR2MASK_EL12   | TCR2MASK_EL1    |
| 0b101 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL12       | SPSR_EL1        |
| 0b101 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL12        | ELR_EL1         |
| 0b101 | 0b0101 | 0b0001 | 0b000 | RW       | AFSR0_EL12      | AFSR0_EL1       |
| 0b101 | 0b0101 | 0b0001 | 0b001 | RW       | AFSR1_EL12      | AFSR1_EL1       |
| 0b101 | 0b0101 | 0b0010 | 0b000 | RW       | ESR_EL12        | ESR_EL1         |
| 0b101 | 0b0101 | 0b0110 | 0b000 | RW       | TFSR_EL12       | TFSR_EL1        |
| 0b101 | 0b0110 | 0b0000 | 0b000 | RW       | FAR_EL12        | FAR_EL1         |
| 0b101 | 0b0110 | 0b0000 | 0b101 | RW       | PFAR_EL12       | PFAR_EL1        |
| 0b101 | 0b1001 | 0b1001 | 0b000 | RW       | PMSCR_EL12      | PMSCR_EL1       |
| 0b101 | 0b1001 | 0b1010 | 0b011 | RW       | PMBSR_EL12      | PMBSR_EL1       |
| 0b101 | 0b1001 | 0b1011 | 0b011 | RW       | TRBSR_EL12      | TRBSR_EL1       |
| 0b101 | 0b1010 | 0b0010 | 0b000 | RW       | MAIR_EL12       | MAIR_EL1        |
| 0b101 | 0b1010 | 0b0010 | 0b001 | RW       | MAIR2_EL12      | MAIR2_EL1       |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses       |
|-------|--------|--------|-------|----------|-----------------|----------------|
| 0b101 | 0b1010 | 0b0010 | 0b010 | RW       | PIRE0_EL12      | PIRE0_EL1      |
| 0b101 | 0b1010 | 0b0010 | 0b011 | RW       | PIR_EL12        | PIR_EL1        |
| 0b101 | 0b1010 | 0b0010 | 0b100 | RW       | POR_EL12        | POR_EL1        |
| 0b101 | 0b1010 | 0b0011 | 0b000 | RW       | AMAIR_EL12      | AMAIR_EL1      |
| 0b101 | 0b1010 | 0b0011 | 0b001 | RW       | AMAIR2_EL12     | AMAIR2_EL1     |
| 0b101 | 0b1010 | 0b0101 | 0b000 | RW       | MPAM1_EL12      | MPAM1_EL1      |
| 0b101 | 0b1010 | 0b0101 | 0b100 | RW       | MPAMBW1_EL12    | MPAMBW1_EL1    |
| 0b101 | 0b1100 | 0b0000 | 0b000 | RW       | VBAR_EL12       | VBAR_EL1       |
| 0b101 | 0b1101 | 0b0000 | 0b001 | RW       | CONTEXTIDR_EL12 | CONTEXTIDR_EL1 |
| 0b101 | 0b1101 | 0b0000 | 0b111 | RW       | SCXTNUM_EL12    | SCXTNUM_EL1    |
| 0b101 | 0b1110 | 0b0001 | 0b000 | RW       | CNTKCTL_EL12    | CNTKCTL_EL1    |
| 0b101 | 0b1110 | 0b0010 | 0b000 | RW       | CNTP_TVAL_EL02  | CNTP_TVAL_EL0  |
| 0b101 | 0b1110 | 0b0010 | 0b001 | RW       | CNTP_CTL_EL02   | CNTP_CTL_EL0   |
| 0b101 | 0b1110 | 0b0010 | 0b010 | RW       | CNTP_CVAL_EL02  | CNTP_CVAL_EL0  |
| 0b101 | 0b1110 | 0b0011 | 0b000 | RW       | CNTV_TVAL_EL02  | CNTV_TVAL_EL0  |
| 0b101 | 0b1110 | 0b0011 | 0b001 | RW       | CNTV_CTL_EL02   | CNTV_CTL_EL0   |
| 0b101 | 0b1110 | 0b0011 | 0b010 | RW       | CNTV_CVAL_EL02  | CNTV_CVAL_EL0  |
| 0b110 | 0b0001 | 0b0000 | 0b000 | RW       | SCTLR_EL3       | SCTLR_EL3      |
| 0b110 | 0b0001 | 0b0000 | 0b001 | RW       | ACTLR_EL3       | ACTLR_EL3      |
| 0b110 | 0b0001 | 0b0000 | 0b011 | RW       | SCTLR2_EL3      | SCTLR2_EL3     |
| 0b110 | 0b0001 | 0b0001 | 0b000 | RW       | SCR_EL3         | SCR_EL3        |
| 0b110 | 0b0001 | 0b0001 | 0b001 | RW       | SDER32_EL3      | SDER32_EL3     |
| 0b110 | 0b0001 | 0b0001 | 0b010 | RW       | CPTR_EL3        | CPTR_EL3       |
| 0b110 | 0b0001 | 0b0001 | 0b101 | RW       | FGWTE3_EL3      | FGWTE3_EL3     |
| 0b110 | 0b0001 | 0b0010 | 0b000 | RW       | ZCR_EL3         | ZCR_EL3        |
| 0b110 | 0b0001 | 0b0010 | 0b110 | RW       | SMCR_EL3        | SMCR_EL3       |
| 0b110 | 0b0001 | 0b0011 | 0b001 | RW       | MDCR_EL3        | MDCR_EL3       |
| 0b110 | 0b0010 | 0b0000 | 0b000 | RW       | TTBR0_EL3       | TTBR0_EL3      |
| 0b110 | 0b0010 | 0b0000 | 0b010 | RW       | TCR_EL3         | TCR_EL3        |
| 0b110 | 0b0010 | 0b0001 | 0b100 | RW       | GPTBR_EL3       | GPTBR_EL3      |
| 0b110 | 0b0010 | 0b0001 | 0b101 | RW       | GPCBW_EL3       | GPCBW_EL3      |
| 0b110 | 0b0010 | 0b0001 | 0b110 | RW       | GPCCR_EL3       | GPCCR_EL3      |
| 0b110 | 0b0010 | 0b0101 | 0b000 | RW       | GCSCR_EL3       | GCSCR_EL3      |
| 0b110 | 0b0010 | 0b0101 | 0b001 | RW       | GCSPR_EL3       | GCSPR_EL3      |
| 0b110 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL3        | SPSR_EL3       |
| 0b110 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL3         | ELR_EL3        |
| 0b110 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL2          | SP_EL2         |
| 0b110 | 0b0101 | 0b0001 | 0b000 | RW       | AFSR0_EL3       | AFSR0_EL3      |
| 0b110 | 0b0101 | 0b0001 | 0b001 | RW       | AFSR1_EL3       | AFSR1_EL3      |
| 0b110 | 0b0101 | 0b0010 | 0b000 | RW       | ESR_EL3         | ESR_EL3        |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic        | Accesses        |
|-------|--------|--------|-------|----------|-----------------|-----------------|
| 0b110 | 0b0101 | 0b0010 | 0b011 | RW       | VSESR_EL3       | VSESR_EL3       |
| 0b110 | 0b0101 | 0b0110 | 0b000 | RW       | TFSR_EL3        | TFSR_EL3        |
| 0b110 | 0b0110 | 0b0000 | 0b000 | RW       | FAR_EL3         | FAR_EL3         |
| 0b110 | 0b0110 | 0b0000 | 0b101 | RW       | MFAR_EL3        | MFAR_EL3        |
| 0b110 | 0b1001 | 0b1010 | 0b011 | RW       | PMBSR_EL3       | PMBSR_EL3       |
| 0b110 | 0b1001 | 0b1011 | 0b011 | RW       | TRBSR_EL3       | TRBSR_EL3       |
| 0b110 | 0b1010 | 0b0001 | 0b001 | RW       | MAIR2_EL3       | MAIR2_EL3       |
| 0b110 | 0b1010 | 0b0010 | 0b000 | RW       | MAIR_EL3        | MAIR_EL3        |
| 0b110 | 0b1010 | 0b0010 | 0b011 | RW       | PIR_EL3         | PIR_EL3         |
| 0b110 | 0b1010 | 0b0010 | 0b100 | RW       | POR_EL3         | POR_EL3         |
| 0b110 | 0b1010 | 0b0011 | 0b000 | RW       | AMAIR_EL3       | AMAIR_EL3       |
| 0b110 | 0b1010 | 0b0011 | 0b001 | RW       | AMAIR2_EL3      | AMAIR2_EL3      |
| 0b110 | 0b1010 | 0b0101 | 0b000 | RW       | MPAM3_EL3       | MPAM3_EL3       |
| 0b110 | 0b1010 | 0b0101 | 0b100 | RW       | MPAMBW3_EL3     | MPAMBW3_EL3     |
| 0b110 | 0b1010 | 0b1010 | 0b001 | RW       | MECID_RL_A_EL3  | MECID_RL_A_EL3  |
| 0b110 | 0b1100 | 0b0000 | 0b000 | RW       | VBAR_EL3        | VBAR_EL3        |
| 0b110 | 0b1100 | 0b0000 | 0b001 | RO       | RVBAR_EL3       | RVBAR_EL3       |
| 0b110 | 0b1100 | 0b0000 | 0b010 | RW       | RMR_EL3         | RMR_EL3         |
| 0b110 | 0b1100 | 0b0001 | 0b001 | RW       | VDISR_EL3       | VDISR_EL3       |
| 0b110 | 0b1100 | 0b1100 | 0b100 | RW       | ICC_CTLR_EL3    | ICC_CTLR_EL3    |
| 0b110 | 0b1100 | 0b1100 | 0b101 | RW       | ICC_SRE_EL3     | ICC_SRE_EL3     |
| 0b110 | 0b1100 | 0b1100 | 0b111 | RW       | ICC_IGRPEN1_EL3 | ICC_IGRPEN1_EL3 |
| 0b110 | 0b1101 | 0b0000 | 0b010 | RW       | TPIDR_EL3       | TPIDR_EL3       |
| 0b110 | 0b1101 | 0b0000 | 0b111 | RW       | SCXTNUM_EL3     | SCXTNUM_EL3     |
| 0b111 | 0b1110 | 0b0010 | 0b000 | RW       | CNTPS_TVAL_EL1  | CNTPS_TVAL_EL1  |
| 0b111 | 0b1110 | 0b0010 | 0b001 | RW       | CNTPS_CTL_EL1   | CNTPS_CTL_EL1   |
| 0b111 | 0b1110 | 0b0010 | 0b010 | RW       | CNTPS_CVAL_EL1  | CNTPS_CVAL_EL1  |

## D23.3.1.1 About the GIC System registers

From version 3 of the GIC architecture, the specification defines three groups of System registers, identified by the prefix of the register name:

- ICC\_ GIC physical CPU interface System registers.

ICH\_ GIC virtual interface control System registers.

ICV\_ GIC Virtual CPU interface System registers.

Note

These registers are in addition to the GIC memory-mapped register groups GICC\_, GICD\_, GICH\_, GICR\_, GICV\_, and GITS\_.

When implemented, the GIC System registers form part of an Arm processor implementation, and therefore these registers are included in the register summaries. However, the registers are defined only in the GIC Architecture Specification.

As Table D23-2 shows, the ICV\_* registers have the same { op0 , op1 , CRn , CRm , op2 } encodings as the corresponding ICC\_* registers. For these encodings, GIC register configuration fields determine which register is accessed.

For more information, see the Arm ® Generic Interrupt Controller Architecture Specification, GIC architecture version 3 and version 4 (ARM IHI 0069).

## D23.3.2 Reserved encodings for IMPLEMENTATION DEFINED registers

The System register encoding space with op0 == 0b11 reserves the following encodings for IMPLEMENTATION DEFINED registers:

<!-- image -->

The value of L defines the access type and the use of Rt as follows:

- 0 Write the value in Rt to the IMPLEMENTATION DEFINED register.
- 1 Read the value of the IMPLEMENTATION DEFINED register to Rt .

For more information about these encodings, see S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;, IMPLEMENTATION DEFINED Registers.

As that section describes, any IMPLEMENTATION DEFINED registers are accessed in a similar way to architecturally-defined System registers, using MRS , MRRS , MSR , and MSRR instructions, see:

- MRS.
- MRRS.
- MSR(immediate).
- MSR(register).
- MSRR.

The Arm architecture guarantees not to define any register name prefixed with IMP\_ as part of the standard Arm architecture.

Note

Arm strongly recommends that any register names created in the IMPLEMENTATION DEFINED register spaces be prefixed with IMP\_ and postfixed with \_ELx , where appropriate.

## Chapter D24 AArch64 System Register Descriptions

This chapter defines the AArch64 System registers. It contains the following sections:

- About the AArch64 System registers.
- General system control registers.
- Debug registers.
- Trace registers.
- Performance Monitors registers.
- Activity Monitors registers.
- Statistical Profiling Extension registers.
- Branch Record Buffer Extension registers.
- RAS registers.
- Generic Timer registers.
- Guarded Control Stack registers.
- MPAMregisters.