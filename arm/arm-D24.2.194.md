## D24.2.194 TCR\_EL1, Translation Control Register (EL1)

The TCR\_EL1 characteristics are:

## Purpose

The control register for stage 1 of the EL1&amp;0 translation regime.

## Configuration

AArch64 System register TCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register TTBCR[31:0].

AArch64 System register TCR\_EL1 bits [63:32] are architecturally mapped to AArch32 System register TTBCR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TCR\_EL1 are UNDEFINED.

## Attributes

TCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

Any of the bits in TCR\_EL1, other than the EPDx bits when they have the value 1, and the A1 bit are permitted to be cached in a TLB.

## Bits [63:62]

Reserved, RES0.

## MTX1, bit [61]

## When FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented or FEAT\_MTE\_CANONICAL\_TAGS is implemented:

Extended memory tag checking.

This field controls address generation and tag checking when EL0 and EL1 are using AArch64 where the data address would be translated by tables pointed to by TTBR1\_EL1.

This control has an effect regardless of whether stage 1 of the EL1&amp;0 translation regime is enabled or not.

| MTX1   | Meaning                                                                                                                                                                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on the PE.                                                                                                                                                                                                                                              |
| 0b1    | Bits[59:56] of a 64-bit VA hold a Logical Address Tag, and all of the following apply:                                                                                                                                                                                             |
|        | • Bits[59:56] are treated as 0b1111 when checking if the address is out of range. • If FEAT_PAuth is implemented, bits[59:56] are not part of the PAC field. • ACanonical Tag Check operation is performed on Tag Checked memory accesses to a Canonically Tagged memory location. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MTX0, bit [60]

## When FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented or FEAT\_MTE\_CANONICAL\_TAGS is implemented:

Extended memory tag checking.

This field controls address generation and tag checking when EL0 and EL1 are using AArch64 where the data address would be translated by tables pointed to by TTBR0\_EL1.

This control has an effect regardless of whether stage 1 of the EL1&amp;0 translation regime is enabled or not.

| MTX0   | Meaning                                                                                                                                                                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on the PE.                                                                                                                                                                                                                                              |
| 0b1    | Bits[59:56] of a 64-bit VA hold a Logical Address Tag, and all of the following apply:                                                                                                                                                                                             |
|        | • Bits[59:56] are treated as 0b0000 when checking if the address is out of range. • If FEAT_PAuth is implemented, bits[59:56] are not part of the PAC field. • ACanonical Tag Check operation is performed on Tag Checked memory accesses to a Canonically Tagged memory location. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DS, bit [59]

## When FEAT\_LPA2 is implemented and (FEAT\_D128 is not implemented or TCR2\_EL1.D128 == '0'):

This field affects:

- Whether a 52-bit output address can be described by the translation tables of the 4KB or 16KB translation granules.
- The minimum value of TCR\_EL1.{T0SZ,T1SZ}.

- How and where shareability for Block and Page descriptors are encoded.

| DS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Bits[49:48] of translation descriptors are RES0. Bits[9:8] in Block and Page descriptors encode shareability information in the SH[1:0] field. Bits[9:8] in Table descriptors are ignored by hardware. The minimum value of the TCR_EL1.{T0SZ, T1SZ} fields is 16. Any memory access using a smaller value generates a stage 1 level 0 translation table fault. Output address[51:48] is 0b0000 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 0b1  | Bits[49:48] of translation descriptors hold output address[49:48]. Bits[9:8] of Translation table descriptors hold output address[51:50]. The shareability information of Block and Page descriptors for cacheable locations is determined by: • TCR_EL1.SH0 if the VA is translated using tables pointed to by TTBR0_EL1. • TCR_EL1.SH1 if the VA is translated using tables pointed to by TTBR1_EL1. The minimum value of the TCR_EL1.{T0SZ, T1SZ} fields is 12. Any memory access using a smaller value generates a stage 1 level 0 translation table fault. All calculations of the stage 1 base address are modified for tables of fewer than 8 entries so that the table is aligned to 64 bytes. Bits[5:2] of TTBR0_EL1 or TTBR1_EL1 are used to hold bits[51:48] of the output address in all cases. Note As FEAT_LVA must be implemented if TCR_EL1.DS == 1, the minimum value of the TCR_EL1.{T0SZ, T1SZ} fields is 12, as determined by that extension. For the TLBI Range instructions affecting VA, the format of the argument is changed so that bits[36:0] hold BaseADDR[52:16]. For the 4KB translation granule, bits[15:12] of BaseADDR are treated as 0b0000 . For the 16KB translation granule, bits[15:14] of BaseADDR are treated as 0b00 . Note This forces alignment of the ranges used by the TLBI range instructions. |

This field is RES0 for a 64KB translation granule.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

The Effective value of this bit is 0b0 .

Access to this field is RES0.

## TCMA1, bit [58]

## When FEAT\_MTE2 is implemented:

Controls the generation of Unchecked accesses at EL1, and at EL0 if the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, when address[59:55] = 0b11111 .

| TCMA1   | Meaning                                                                           |
|---------|-----------------------------------------------------------------------------------|
| 0b0     | This control has no effect on the generation of Unchecked accesses at EL1 or EL0. |
| 0b1     | All accesses at EL1 and EL0 are Unchecked.                                        |

TCMA1

Note

Software may change this control bit on a context switch.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TCMA0, bit [57]

## When FEAT\_MTE2 is implemented:

Controls the generation of Unchecked accesses at EL1, and at EL0 if the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, when address[59:55] = 0b00000 .

| TCMA0   | Meaning                                                                           |
|---------|-----------------------------------------------------------------------------------|
| 0b0     | This control has no effect on the generation of Unchecked accesses at EL1 or EL0. |
| 0b1     | All accesses at EL1 and EL0 are Unchecked.                                        |

Note

Software may change this control bit on a context switch.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

E0PD1, bit [56]

## When FEAT\_E0PD is implemented:

Faulting control for unprivileged access to any address translated by TTBR1\_EL1.

| E0PD1   | Meaning                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------|
| 0b0     | Unprivileged access to any address translated by TTBR1_EL1 will not generate a fault by this mechanism. |
| 0b1     | Unprivileged access to any address translated by TTBR1_EL1 will generate a level 0 Translation fault.   |

Level 0 Translation faults generated as a result of this field are not counted as TLB misses for performance monitoring. The fault should take the same time to generate, whether the address is present in the TLB or not, to mitigate attacks that use fault timing.

The reset behavior of this field is:

## Meaning

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0PD0, bit [55]

## When FEAT\_E0PD is implemented:

Faulting control for unprivileged access to any address translated by TTBR0\_EL1.

| E0PD0   | Meaning                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------|
| 0b0     | Unprivileged access to any address translated by TTBR0_EL1 will not generate a fault by this mechanism. |
| 0b1     | Unprivileged access to any address translated by TTBR0_EL1 will generate a level 0 Translation fault.   |

Level 0 Translation faults generated as a result of this field are not counted as TLB misses for performance monitoring. The fault should take the same time to generate, whether the address is present in the TLB or not, to mitigate attacks that use fault timing.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NFD1, bit [54]

## When FEAT\_SVE is implemented:

Non-Fault translation timing Disable when using TTBR1\_EL1.

Controls how a TLB miss is reported in response to a non-fault unprivileged access for a virtual address that is translated using TTBR1\_EL1.

If SVE is implemented, the affected access types include:

- All accesses due to an SVE non-fault contiguous load instruction.
- Accesses due to an SVE first-fault gather load instruction that are not for the First active element. Accesses due to an SVE first-fault contiguous load instruction are not affected.
- Accesses due to prefetch instructions might be affected, but the effect is not architecturally visible.

| NFD1   | Meaning                                                                                                                                                                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Does not affect the handling of a TLB miss on accesses translated using TTBR1_EL1.                                                                                                                                                                                                                                                                   |
| 0b1    | ATLBmiss on a virtual address that is translated using TTBR1_EL1 due to the specified access types causes the access to fail without taking an exception. The amount of time that the failure takes to be handled should not predictively leak whether it was caused by a TLB miss or a Permission fault, to mitigate attacks that use fault timing. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NFD0, bit [53]

## When FEAT\_SVE is implemented:

Non-Fault translation timing Disable when using TTBR0\_EL1.

Controls how a TLB miss is reported in response to a non-fault unprivileged access for a virtual address that is translated using TTBR0\_EL1.

If SVE is implemented, the affected access types include:

- All accesses due to an SVE non-fault contiguous load instruction.
- Accesses due to an SVE first-fault gather load instruction that are not for the First active element. Accesses due to an SVE first-fault contiguous load instruction are not affected.
- Accesses due to prefetch instructions might be affected, but the effect is not architecturally visible.

| NFD0   | Meaning                                                                                                                                                                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Does not affect the handling of a TLB miss on accesses translated using TTBR0_EL1.                                                                                                                                                                                                                                                                   |
| 0b1    | ATLBmiss on a virtual address that is translated using TTBR0_EL1 due to the specified access types causes the access to fail without taking an exception. The amount of time that the failure takes to be handled should not predictively leak whether it was caused by a TLB miss or a Permission fault, to mitigate attacks that use fault timing. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBID1, bit [52]

## When FEAT\_PAuth is implemented:

Controls the use of the top byte of instruction addresses for address matching.

For the purpose of this field, all cache maintenance and address translation instructions that perform address translation are treated as data accesses.

For more information, see 'Address tagging'.

| TBID1   | Meaning                                                |
|---------|--------------------------------------------------------|
| 0b0     | TCR_EL1.TBI1 applies to Instruction and Data accesses. |
| 0b1     | TCR_EL1.TBI1 applies to Data accesses only.            |

This affects addresses where the address would be translated by tables pointed to by TTBR1\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBID0, bit [51]

## When FEAT\_PAuth is implemented:

Controls the use of the top byte of instruction addresses for address matching.

For the purpose of this field, all cache maintenance and address translation instructions that perform address translation are treated as data accesses.

For more information, see 'Address tagging'.

| TBID0   | Meaning                                                |
|---------|--------------------------------------------------------|
| 0b0     | TCR_EL1.TBI0 applies to Instruction and Data accesses. |
| 0b1     | TCR_EL1.TBI0 applies to Data accesses only.            |

This affects addresses where the address would be translated by tables pointed to by TTBR0\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU162, bit [50]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[62] of the stage 1 translation table Block or Page entry for translations using TTBR1\_EL1.

| HWU162   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR1_EL1, bit[62] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR1_EL1, bit[62] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD1 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD1 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU161, bit [49]

When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[61] of the stage 1 translation table Block or Page entry for translations using TTBR1\_EL1.

| HWU161   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR1_EL1, bit[61] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR1_EL1, bit[61] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD1 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD1 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU160, bit [48]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[60] of the stage 1 translation table Block or Page entry for translations using TTBR1\_EL1.

| HWU160   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR1_EL1, bit[60] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR1_EL1, bit[60] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD1 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD1 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU159, bit [47]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[59] of the stage 1 translation table Block or Page entry for translations using TTBR1\_EL1.

| HWU159   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR1_EL1, bit[59] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR1_EL1, bit[59] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD1 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD1 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU062, bit [46]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[62] of the stage 1 translation table Block or Page entry for translations using TTBR0\_EL1.

| HWU062   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR0_EL1, bit[62] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR0_EL1, bit[62] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD0 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD0 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU061, bit [45]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[61] of the stage 1 translation table Block or Page entry for translations using TTBR0\_EL1.

| HWU061   | Meaning                                                                                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR0_EL1, bit[61] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |

| HWU061   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1      | For translations using TTBR0_EL1, bit[61] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD0 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD0 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU060, bit [44]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[60] of the stage 1 translation table Block or Page entry for translations using TTBR0\_EL1.

| HWU060   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR0_EL1, bit[60] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR0_EL1, bit[60] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD0 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD0 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU059, bit [43]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[59] of the stage 1 translation table Block or Page entry for translations using TTBR0\_EL1.

| HWU059   | Meaning                                                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For translations using TTBR0_EL1, bit[59] of each stage 1 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose.                                |
| 0b1      | For translations using TTBR0_EL1, bit[59] of each stage 1 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose if the value of TCR_EL1.HPD0 is 1. |

The Effective value of this field is 0 if the value of TCR\_EL1.HPD0 is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPD1, bit [42]

## When FEAT\_HPDS is implemented:

Hierarchical Permission Disables. This affects the hierarchical control bits, APTable, PXNTable, and UXNTable, except NSTable, in the translation tables pointed to by TTBR1\_EL1.

| HPD1   | Meaning                                |
|--------|----------------------------------------|
| 0b0    | Hierarchical permissions are enabled.  |
| 0b1    | Hierarchical permissions are disabled. |

When disabled, the permissions are treated as if the bits are zero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPD0, bit [41]

## When FEAT\_HPDS is implemented:

Hierarchical Permission Disables. This affects the hierarchical control bits, APTable, PXNTable, and UXNTable, except NSTable, in the translation tables pointed to by TTBR0\_EL1.

| HPD0   | Meaning                                |
|--------|----------------------------------------|
| 0b0    | Hierarchical permissions are enabled.  |
| 0b1    | Hierarchical permissions are disabled. |

When disabled, the permissions are treated as if the bits are zero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HD, bit [40]

## When FEAT\_HAFDBS is implemented:

Hardware management of dirty state in stage 1 translations from EL0 and EL1.

| HD   | Meaning                                              |
|------|------------------------------------------------------|
| 0b0  | Stage 1 hardware management of dirty state disabled. |
| 0b1  | Stage 1 hardware management of dirty state enabled.  |

When the Effective value of TCR\_EL1.HA is 0, this field behaves as 0 for all purposes other than a direct read of the value of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HA, bit [39]

## When FEAT\_HAFDBS is implemented:

Hardware Access flag update in stage 1 translations from EL0 and EL1.

| HA   | Meaning                              |
|------|--------------------------------------|
| 0b0  | Stage 1 Access flag update disabled. |
| 0b1  | Stage 1 Access flag update enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBI1, bit [38]

Top Byte ignored. Indicates whether the top byte of an address is used for address match for the TTBR1\_EL1 region, or ignored and used for tagged addresses.

| TBI1   | Meaning                                      |
|--------|----------------------------------------------|
| 0b0    | Top Byte used in the address calculation.    |
| 0b1    | Top Byte ignored in the address calculation. |

This affects addresses generated in EL0 and EL1 using AArch64 where the address would be translated by tables pointed to by TTBR1\_EL1. It has an effect whether the EL1&amp;0 translation regime is enabled or not.

If FEAT\_PAuth is implemented and TCR\_EL1.TBID1 is 1, then this field only applies to Data accesses.

Otherwise, if the value of TBI1 is 1 and bit [55] of the target address to be stored to the PC is 1, then bits[63:56] of that target address are also set to 1 before the address is stored in the PC, in the following cases:

- Abranch or procedure return within EL0 or EL1.
- An exception taken to EL1.
- An exception return to EL0 or EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TBI0, bit [37]

Top Byte ignored. Indicates whether the top byte of an address is used for address match for the TTBR0\_EL1 region, or ignored and used for tagged addresses.

| TBI0   | Meaning                                      |
|--------|----------------------------------------------|
| 0b0    | Top Byte used in the address calculation.    |
| 0b1    | Top Byte ignored in the address calculation. |

This affects addresses generated in EL0 and EL1 using AArch64 where the address would be translated by tables pointed to by TTBR0\_EL1. It has an effect whether the EL1&amp;0 translation regime is enabled or not.

If FEAT\_PAuth is implemented and TCR\_EL1.TBID0 is 1, then this field only applies to Data accesses.

Otherwise, if the value of TBI0 is 1 and bit [55] of the target address to be stored to the PC is 0, then bits[63:56] of that target address are also set to 0 before the address is stored in the PC, in the following cases:

- Abranch or procedure return within EL0 or EL1.
- An exception taken to EL1.
- An exception return to EL0 or EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## AS, bit [36]

ASID Size.

| AS   | Meaning                                                                                                                                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | 8 bit - the upper 8 bits of TTBR0_EL1 and TTBR1_EL1 are ignored by hardware for every purpose except reading back the register, and are treated as if they are all zeros for when used for allocation and matching entries in the TLB. |
| 0b1  | 16 bit - the upper 16 bits of TTBR0_EL1 and TTBR1_EL1 are used for allocation and matching in the TLB.                                                                                                                                 |

If the implementation has only 8 bits of ASID, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [35]

Reserved, RES0.

## IPS, bits [34:32]

Intermediate Physical Address Size.

| IPS   | Meaning         |
|-------|-----------------|
| 0b000 | 32 bits, 4GB.   |
| 0b001 | 36 bits, 64GB.  |
| 0b010 | 40 bits, 1TB.   |
| 0b011 | 42 bits, 4TB.   |
| 0b100 | 44 bits, 16TB.  |
| 0b101 | 48 bits, 256TB. |
| 0b110 | 52 bits, 4PB.   |
| 0b111 | 56 bits, 64PB.  |

The values 0b110 and 0b111 represent different output address sizes depending on implementation choices and translation configuration.

The following table captures the output address size represented by the value 0b110 :

| Descriptor Format   | ID_AA64MMFR0_EL1.PARange   | Translation Granule   | DS 1 &#124; Represented OA size &#124;   | DS 1 &#124; Represented OA size &#124;   |
|---------------------|----------------------------|-----------------------|------------------------------------------|------------------------------------------|
| Any                 | 0b0101                     | Any                   | Any                                      | 48 bits, 256TB                           |
| VMSAv8-64           | 0b011x                     | 4KB or 16KB           | 0                                        | 48 bits, 256TB                           |
| VMSAv8-64           | 0b011x                     | 4KB or 16KB           | 1                                        | 52 bits, 4PB                             |
| VMSAv8-64           | 0b011x                     | 64KB                  | N/A                                      | 52 bits, 4PB                             |
| VMSAv9-128          | 0b011x                     | Any                   | N/A                                      | 52 bits, 4PB                             |

The following table captures the output address size represented by the value 0b111 :

| Descriptor Format   | ID_AA64MMFR0_EL1.PARange   | Translation Granule   | Represented OA size         |
|---------------------|----------------------------|-----------------------|-----------------------------|
| Any                 | 0b0110                     | Any                   | OAsize represented by 0b110 |
| VMSAv8-64           | 0b0111                     | Any                   | OAsize represented by 0b110 |
| VMSAv9-128          | 0b0111                     | Any                   | 56 bits, 64PB               |

If 52-bit PA is supported, and the translation table descriptors cannot express an OA larger than 48-bits, then bits[51:48] of every translation table base address are treated as 0b0000 for the stage of translation controlled by TCR\_EL1.

If 56-bit PA is supported, and the translation table descriptors cannot express an OA larger than 52-bits, then bits[55:52] of every translation table base address are treated as 0b0000 for the stage of translation controlled by TCR\_EL1.

If the output address size represented by this field is larger than the supported PA size expressed in ID\_AA64MMFR0\_EL1.PARange, then the output address size is treated as being the same as the supported PA size. Arm strongly recommends that software avoids configuring this field to a value representing an output address size larger than the supported PA size.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TG1, bits [31:30]

Granule size for the TTBR1\_EL1.

Other values are reserved.

If the value is programmed to either a reserved value or a size that has not been implemented, then the hardware will treat the field as if it has been programmed to an IMPLEMENTATION DEFINED choice of the sizes that has been implemented for all purposes other than the value read back from this register.

It is IMPLEMENTATION DEFINED whether the value read back is the value programmed or the value that corresponds to the size chosen.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH1, bits [29:28]

Shareability attribute for memory associated with translation table walks using TTBR1\_EL1.

| SH1   | Meaning          |
|-------|------------------|
| 0b00  | Non-shareable.   |
| 0b10  | Outer Shareable. |
| 0b11  | Inner Shareable. |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ORGN1, bits [27:26]

Outer cacheability attribute for memory associated with translation table walks using TTBR1\_EL1.

| ORGN1   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

| TG1   | Meaning   |
|-------|-----------|
| 0b01  | 16KB.     |
| 0b10  | 4KB.      |
| 0b11  | 64KB.     |

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN1, bits [25:24]

Inner cacheability attribute for memory associated with translation table walks using TTBR1\_EL1.

| IRGN1   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EPD1, bit [23]

Translation table walk disable for translations using TTBR1\_EL1. This bit controls whether a translation table walk is performed on a TLB miss, for an address that is translated using TTBR1\_EL1. The encoding of this bit is:

| EPD1   | Meaning                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Perform translation table walks using TTBR1_EL1.                                                                                 |
| 0b1    | ATLBmiss on an address that is translated using TTBR1_EL1 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A1, bit [22]

Selects whether TTBR0\_EL1 or TTBR1\_EL1 defines the ASID. The encoding of this bit is:

| A1   | Meaning                          |
|------|----------------------------------|
| 0b0  | TTBR0_EL1.ASID defines the ASID. |
| 0b1  | TTBR1_EL1.ASID defines the ASID. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T1SZ, bits [21:16]

The size offset of the memory region addressed by TTBR1\_EL1. The region size is 2 (64-T1SZ) bytes.

The maximum and minimum possible values for T1SZ depend on the level of translation table and the memory translation granule size, as described in the AArch64 Virtual Memory System Architecture chapter.

Note

For the 4KB translation granule, if FEAT\_LPA2 is implemented, TCR\_EL1.DS is 1, and this field is less than 16, the translation table walk begins with a level -1 initial lookup. For the 16KB translation granule, if FEAT\_LPA2 is implemented, TCR\_EL1.DS is 1, and this field is less than 17, the translation table walk begins with a level 0 initial lookup.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TG0, bits [15:14]

Granule size for the TTBR0\_EL1.

## Other values are reserved.

If the value is programmed to either a reserved value or a size that has not been implemented, then the hardware will treat the field as if it has been programmed to an IMPLEMENTATION DEFINED choice of the sizes that has been implemented for all purposes other than the value read back from this register.

It is IMPLEMENTATION DEFINED whether the value read back is the value programmed or the value that corresponds to the size chosen.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH0, bits [13:12]

Shareability attribute for memory associated with translation table walks using TTBR0\_EL1.

| SH0   | Meaning         |
|-------|-----------------|
| 0b00  | Non-shareable   |
| 0b10  | Outer Shareable |
| 0b11  | Inner Shareable |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ORGN0, bits [11:10]

Outer cacheability attribute for memory associated with translation table walks using TTBR0\_EL1.

| TG0   | Meaning   |
|-------|-----------|
| 0b00  | 4KB       |
| 0b01  | 64KB      |
| 0b10  | 16KB      |

| ORGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN0, bits [9:8]

Inner cacheability attribute for memory associated with translation table walks using TTBR0\_EL1.

| IRGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EPD0, bit [7]

Translation table walk disable for translations using TTBR0\_EL1. This bit controls whether a translation table walk is performed on a TLB miss, for an address that is translated using TTBR0\_EL1. The encoding of this bit is:

| EPD0   | Meaning                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Perform translation table walks using TTBR0_EL1.                                                                                 |
| 0b1    | ATLBmiss on an address that is translated using TTBR0_EL1 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [6]

Reserved, RES0.

## T0SZ, bits [5:0]

The size offset of the memory region addressed by TTBR0\_EL1. The region size is 2 (64-T0SZ) bytes.

The maximum and minimum possible values for T0SZ depend on the level of translation table and the memory translation granule size, as described in the AArch64 Virtual Memory System Architecture chapter.

Note

For the 4KB translation granule, if FEAT\_LPA2 is implemented, TCR\_EL1.DS is 1, and this field is less than 16, the translation table walk begins with a level -1 initial lookup.

For the 16KB translation granule, if FEAT\_LPA2 is implemented, TCR\_EL1.DS is 1, and this field is less than 17, the translation table walk begins with a level 0 initial lookup.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing TCR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TCR\_EL1 or TCR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to TCR\_EL1 are masked by TCRMASK\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.TCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x120]; else X[t, 64] = TCR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = TCR_EL2; else X[t, 64] = TCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCR_EL1;
```

MSR TCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.TCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x120] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then TCR_EL1 = (X[t, 64] AND NOT EffectiveTCRMASK_EL1()) OR (TCR_EL1 AND EffectiveTCRMASK_EL1()); else TCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then TCR_EL2 = (X[t, 64] AND NOT EffectiveTCRMASK_EL2()) OR (TCR_EL2 AND EffectiveTCRMASK_EL2()); else TCR_EL2 = X[t, 64]; else TCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x120]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = TCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x120] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then TCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TCR_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_SRMASK is implemented MRS &lt;Xt&gt;, TCRALIAS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nTCRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x120]; else X[t, 64] = TCR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = TCR_EL2; else X[t, 64] = TCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCR_EL1;
```

When FEAT\_SRMASK is implemented MSR TCRALIAS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nTCRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x120] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then TCR_EL1 = (X[t, 64] AND NOT EffectiveTCRMASK_EL1()) OR (TCR_EL1 AND ↪ → EffectiveTCRMASK_EL1()); else TCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then TCR_EL2 = (X[t, 64] AND NOT EffectiveTCRMASK_EL2()) OR (TCR_EL2 AND ↪ → EffectiveTCRMASK_EL2()); else TCR_EL2 = X[t, 64]; else TCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCR_EL1 = X[t, 64];
```