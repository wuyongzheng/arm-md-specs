## D24.2.224 VTCR\_EL2, Virtualization Translation Control Register

The VTCR\_EL2 characteristics are:

## Purpose

The control register for stage 2 of the EL1&amp;0 translation regime.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VTCR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register VTCR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to VTCR\_EL2 are UNDEFINED.

## Attributes

VTCR\_EL2 is a 64-bit register.

## Field descriptions

IsProfile(PROFILE\_A)

<!-- image -->

Unless stated otherwise, any of the bits in VTCR\_EL2 are permitted to be cached in a TLB.

## Bits [63:46]

Reserved, RES0.

## HDBSS, bit [45]

## When FEAT\_HDBSS is implemented:

Enable use of HDBSS.

| HDBSS   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b0     | Hardware tracking of Dirty state Structure is disabled. |

| 0b1   | Hardware tracking of Dirty state Structure is enabled.   |
|-------|----------------------------------------------------------|

If VTCR\_EL2.{HA, HD} is not {1, 1}, the Effective value of this field is 0.

If SCR\_EL3.HDBSSEn is 0, then this field behaves as 0 for all purposes other than a direct read of the value of this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HAFT, bit [44]

## When FEAT\_HAFT is implemented:

Hardware managed Access Flag for Table descriptors.

Enables the Hardware managed Access Flag for Table descriptors.

| HAFT   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | Hardware managed Access Flag for Table descriptors is disabled. |
| 0b1    | Hardware managed Access Flag for Table descriptors is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [43:42]

Reserved, RES0.

## TL0, bit [41]

## When FEAT\_THE is implemented:

Control bit to check for presence of MMU TopLevel0 permission attribute.

| TL0   | Meaning                                                                                   |
|-------|-------------------------------------------------------------------------------------------|
| 0b0   | This bit does not have any effect on stage 2 translations.                                |
| 0b1   | Enables MMUTopLevel0 permission attribute check for TTBR0_EL1 and TTBR1_EL1 translations. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## GCSH, bit [40]

## When FEAT\_THE is implemented and FEAT\_GCS is implemented:

Assured stage 1 translations for Guarded Control Stacks. Enforces use of the AssuredOnly attribute in stage 2 for the memory accessed by privileged Guarded Control Stack data accesses.

| GCSH   | Meaning                                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | For the memory accessed by privileged Guarded Control Stack data accesses, the AssuredOnly attribute in stage 2 is not required to be set. |
| 0b1    | For the memory accessed by privileged Guarded Control Stack data accesses, the AssuredOnly attribute in stage 2 is required to be set.     |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [39]

Reserved, RES0.

## D128, bit [38]

## When FEAT\_D128 is implemented:

Enables VMSAv9-128 translation system for stage 2 translation.

| D128   | Meaning                                                    |
|--------|------------------------------------------------------------|
| 0b0    | Translation system follows VMSAv8-64 translation process.  |
| 0b1    | Translation system follows VMSAv9-128 translation process. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S2POE, bit [37]

## When FEAT\_S2POE is implemented:

Enable Permission Overlay. Enables permission overlay in stage 2 Permission model.

This bit is not permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S2PIE, bit [36]

## When FEAT\_S2PIE is implemented:

Select Permission Model. Enables usage of permission indirection in stage 2 Permission model.

| S2PIE   | Meaning                    |
|---------|----------------------------|
| 0b0     | Direct permission model.   |
| 0b1     | Indirect permission model. |

This field is RES1 when VTCR\_EL2.D128 is set.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TL1, bit [35]

## When FEAT\_THE is implemented:

Control bit to check for presence of MMU TopLevel1 permission attribute.

| TL1   | Meaning                                                                                   |
|-------|-------------------------------------------------------------------------------------------|
| 0b0   | This bit does not have any effect on stage 2 translations.                                |
| 0b1   | Enables MMUTopLevel1 permission attribute check for TTBR0_EL1 and TTBR1_EL1 translations. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

AssuredOnly, bit [34]

| S2POE   | Meaning           |
|---------|-------------------|
| 0b0     | Overlay disabled. |
| 0b1     | Overaly enabled.  |

## When FEAT\_THE is implemented:

AssuredOnly attribute enable for VMSAv8-64. Configures use of bit[58] of the stage 2 translation table Block or Page descriptor.

| AssuredOnly   | Meaning                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------|
| 0b0           | Bit[58] of each stage 2 translation Block or Page descriptor does not indicate AssuredOnly attribute. |
| 0b1           | Bit[58] of each stage 2 translation Block or Page descriptor indicates AssuredOnly attribute.         |

This field is RES0 when VTCR\_EL2.D128 is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SL2, bit [33]

## When FEAT\_LPA2 is implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the stage 2 translation lookup controlled by VTCR\_EL2.

If VTCR\_EL2.DS == 1, then VTCR\_EL2.SL2, in combination with VTCR\_EL2.SL0, gives encodings for the stage 2 translation table walk initial lookup level.

If VTCR\_EL2.DS == 0, then VTCR\_EL2.SL2 is RES0.

If the translation granule size is not 4KB, then this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DS, bit [32]

## When FEAT\_LPA2 is implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

This field affects:

- Whether a 52-bit output address can be described by the translation tables of the 4KB or 16KB translation granules.
- The minimum value of VTCR\_EL2.T0SZ and VSTCR\_EL2.T0SZ.
- How and where shareability for Block and Page descriptors are encoded.

| DS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Bits[49:48] of translation descriptors are RES0. Bits[9:8] in Block and Page descriptors encode shareability information in the SH[1:0] field. Bits[9:8] in Table descriptors are ignored by hardware. The minimum value of VTCR_EL2.T0SZ is 16. Any memory access using a smaller value generates a stage 2 level 0 translation table fault. The minimum value of VSTCR_EL2.T0SZ is 16. Any memory access using a smaller value generates a stage 2 level 0 translation table fault. Output address[51:48] is 0000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0b1  | Bits[49:48] of translation descriptors hold output address[49:48]. Bits[9:8] in translation descriptors hold output address[51:50]. The shareability information of Block and Page descriptors for cacheable locations is determined by VTCR_EL2.SH0. The minimum value of VTCR_EL2.T0SZ is 12. Any memory access using a smaller value generates a stage 2 level 0 translation table fault. The minimum value of VSTCR_EL2.T0SZ is 12. Any memory access using a smaller value generates a stage 2 level 0 translation table fault. Note As FEAT_LPA must be implemented if VTCR_EL2.DS == 1, the minimum values of VTCR_EL2.T0SZ and VSTCR_EL2.T0SZ are 12, as determined by that extension. For the TLBI range instructions affecting IPA, the format of the argument is changed so that bits[36:0] hold BaseADDR[52:16]. For the 4KB translation granule, bits[15:12] of BaseADDR are treated as 0000. For the 16KB translation granule, bits[15:14] of BaseADDR are treated as 00. Note This forces alignment of the ranges used by the TLBI range instructions. |

This field is RES0 for a 64KB translation granule.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [31]

Reserved, RES1.

## NSA, bit [30]

## When FEAT\_SEL2 is implemented:

Non-secure stage 2 translation output address space for the Secure EL1&amp;0 translation regime.

| NSA   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | All stage 2 translations for the Non-secure IPA space of the Secure EL1&0 translation regime access the Secure PA space.     |
| 0b1   | All stage 2 translations for the Non-secure IPA space of the Secure EL1&0 translation regime access the Non-secure PA space. |

This bit behaves as 1 for all purposes other than reading back the value of the bit when one of the following is true:

- The value of VTCR\_EL2.NSW is 1.
- The value of VSTCR\_EL2.SA is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSW, bit [29]

## When FEAT\_SEL2 is implemented:

Non-secure stage 2 translation table address space for the Secure EL1&amp;0 translation regime.

| NSW   | Meaning                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | All stage 2 translation table walks for the Non-secure IPA space of the Secure EL1&0 translation regime are to the Secure PA space.     |
| 0b1   | All stage 2 translation table walks for the Non-secure IPA space of the Secure EL1&0 translation regime are to the Non-secure PA space. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU62, bit [28]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[62] of the stage 2 translation table Block or Page entry.

| HWU62   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[62] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[62] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU61, bit [27]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[61] of the stage 2 translation table Block or Page entry.

| HWU61   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[61] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[61] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU60, bit [26]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[60] of the stage 2 translation table Block or Page entry.

| HWU60   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[60] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[60] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU59, bit [25]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[59] of the stage 2 translation table Block or Page entry.

| HWU59   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[59] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |

| HWU59   | Meaning                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------|
| 0b1     | Bit[59] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [24:23]

Reserved, RES0.

## HD, bit [22]

## When FEAT\_HAFDBS is implemented:

Hardware management of dirty state in stage 2 translations when EL2 is enabled in the current Security state.

| HD   | Meaning                                              |
|------|------------------------------------------------------|
| 0b0  | Stage 2 hardware management of dirty state disabled. |
| 0b1  | Stage 2 hardware management of dirty state enabled.  |

When the Effective value of VTCR\_EL2.HA is 0, this field behaves as 0 for all purposes other than a direct read of the value of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HA, bit [21]

## When FEAT\_HAFDBS is implemented:

Hardware Access flag update in stage 2 translations when EL2 is enabled in the current Security state.

| HA   | Meaning                              |
|------|--------------------------------------|
| 0b0  | Stage 2 Access flag update disabled. |
| 0b1  | Stage 2 Access flag update enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [20]

Reserved, RES0.

## VS, bit [19]

## When FEAT\_VMID16 is implemented:

VMIDSize.

| VS   | Meaning                                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | 8-bit VMID. The upper 8 bits of VTTBR_EL2 are ignored by the hardware, and treated as if they are all zeros, for every purpose except when reading back the register. |
| 0b1  | 16-bit VMID. The upper 8 bits of VTTBR_EL2 are used for allocation and matching in the TLB.                                                                           |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PS, bits [18:16]

Physical address Size for the second stage of translation.

| PS    | Meaning         |
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

| Descriptor Format   | ID_AA64MMFR0_EL1.PARange   | Translation Granule   | DS 1 &#124; Represented OA size &#124;   |
|---------------------|----------------------------|-----------------------|------------------------------------------|
| Any                 | 0b0101                     | Any                   | Any 48 bits, 256TB                       |
| VMSAv8-64           | 0b011x                     | 4KB or 16KB           | 0 48 bits, 256TB                         |
| VMSAv8-64           | 0b011x                     | 4KB or 16KB           | 1 52 bits, 4PB                           |

| Descriptor Format   | ID_AA64MMFR0_EL1.PARange   | Translation Granule   | DS 1 &#124; Represented   | OA size &#124;   |
|---------------------|----------------------------|-----------------------|---------------------------|------------------|
| VMSAv8-64           | 0b011x                     | 64KB                  | N/A                       | 52 bits, 4PB     |
| VMSAv9-128          | 0b011x                     | Any                   | N/A                       | 52 bits, 4PB     |

The following table captures the output address size represented by the value 0b111 :

| Descriptor Format   | ID_AA64MMFR0_EL1.PARange   | Translation Granule   | Represented OA size         |
|---------------------|----------------------------|-----------------------|-----------------------------|
| Any                 | 0b0110                     | Any                   | OAsize represented by 0b110 |
| VMSAv8-64           | 0b0111                     | Any                   | OAsize represented by 0b110 |
| VMSAv9-128          | 0b0111                     | Any                   | 56 bits, 64PB               |

If 52-bit PA is supported, and the translation table descriptors cannot express an OA larger than 48-bits, then bits[51:48] of every translation table base address are treated as 0b0000 for the stage of translation controlled by VTCR\_EL2.

If 56-bit PA is supported, and the translation table descriptors cannot express an OA larger than 52-bits, then bits[55:52] of every translation table base address are treated as 0b0000 for the stage of translation controlled by VTCR\_EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TG0, bits [15:14]

Granule size for the VTTBR\_EL2.

Other values are reserved.

If FEAT\_GTG is implemented, ID\_AA64MMFR0\_EL1.{TGran4\_2, TGran16\_2, TGran64\_2} indicate which granule sizes are supported for stage 2 translation.

If FEAT\_GTG is not implemented, ID\_AA64MMFR0\_EL1.{TGran4, TGran16, TGran64} indicate which granule sizes are supported.

If the value is programmed to either a reserved value or a size that has not been implemented, then the hardware will treat the field as if it has been programmed to an IMPLEMENTATION DEFINED choice of the sizes that has been implemented for all purposes other than the value read back from this register.

It is IMPLEMENTATION DEFINED whether the value read back is the value programmed or the value that corresponds to the size chosen.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

| TG0   | Meaning   |
|-------|-----------|
| 0b00  | 4KB.      |
| 0b01  | 64KB.     |
| 0b10  | 16KB.     |

## SH0, bits [13:12]

Shareability attribute for memory associated with translation table walks using VTTBR\_EL2 or VSTTBR\_EL2.

| SH0   | Meaning          |
|-------|------------------|
| 0b00  | Non-shareable.   |
| 0b10  | Outer Shareable. |
| 0b11  | Inner Shareable. |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ORGN0, bits [11:10]

Outer cacheability attribute for memory associated with translation table walks using VTTBR\_EL2 or VSTTBR\_EL2.

| ORGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN0, bits [9:8]

Inner cacheability attribute for memory associated with translation table walks using VTTBR\_EL2 or VSTTBR\_EL2.

| IRGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

SL0, bits [7:6]

## When FEAT\_TTST is implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the stage 2 translation lookup, controlled by VTCR\_EL2. The meaning of this field depends on the value of VTCR\_EL2.TG0.

| SL0   | Meaning                                                                                                                                                                                                                                                                                                                                                              |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | If VTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 2. • If FEAT_LPA2 is implemented and VTCR_EL2.SL2 is 0b0 , start at level 2. • If FEAT_LPA2 is implemented and VTCR_EL2.SL2 is 0b1 , start at level -1. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 3.                                    |
| 0b01  | If VTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 1. • If FEAT_LPA2 is implemented and VTCR_EL2.SL2 is 0b0 , start at level 1. • If FEAT_LPA2 is implemented, the combination of VTCR_EL2.SL0 == 01 and VTCR_EL2.SL2 == 1 is reserved. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 2.       |
| 0b10  | If VTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 0. • If FEAT_LPA2 is implemented and VTCR_EL2.SL2 is 0b0 , start at level 0. • If FEAT_LPA2 is implemented, the combination of VTCR_EL2.SL0 == 10 and VTCR_EL2.SL2 == 1 is reserved. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 1.       |
| 0b11  | If VTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 3. • If FEAT_LPA2 is implemented and VTCR_EL2.SL2 is 0b0 , start at level 3. • If FEAT_LPA2 is implemented, the combination of VTCR_EL2.SL0 == 11 and VTCR_EL2.SL2 == 1 is reserved. If VTCR_EL2.TG0 is 0b10 (16KB granule) and FEAT_LPA2 is implemented, start at level 0. |

If this field is programmed to a value that is not consistent with the programming of VTCR\_EL2.T0SZ, then a stage 2 level 0 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_TTST is not implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the stage 2 translation lookup, controlled by VTCR\_EL2. The meaning of this field depends on the value of VTCR\_EL2.TG0.

| SL0   | Meaning                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | If VTCR_EL2.TG0 is 0b00 (4KB granule), start at level 2. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 3. |
| 0b01  | If VTCR_EL2.TG0 is 0b00 (4KB granule), start at level 1. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 2. |
| 0b10  | If VTCR_EL2.TG0 is 0b00 (4KB granule), start at level 0. If VTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 1. |

All other values are reserved. If this field is programmed to a reserved value, or to a value that is not consistent with the programming of VTCR\_EL2.T0SZ, then a stage 2 level 0 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## T0SZ, bits [5:0]

The size offset of the memory region addressed by VTTBR\_EL2. The region size is 2 (64-T0SZ) bytes.

The maximum and minimum possible values for T0SZ depend on the level of translation table and the memory translation granule size, as described in 'The AArch64 Virtual Memory System Architecture'.

If this field is programmed to a value that is not consistent with the programming of SL0, then a stage 2 level 0 Translation fault is generated.

Note

For the 4KB translation granule, if FEAT\_LPA2 is implemented, VTCR\_EL2.DS is 1, and this field is less than 16, the translation table walk begins with a level -1 initial lookup. For the 16KB translation granule, if FEAT\_LPA2 is implemented, VTCR\_EL2.DS is 1, and this field is less than

17, the translation table walk begins with a level 0 initial lookup.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VTCR\_EL2

Unless stated otherwise, any of the bits in VTCR\_EL2 are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, VTCR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x040];
```

elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);

else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VTCR\_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = VTCR\_EL2;

MSR VTCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x040] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VTCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then VTCR_EL2 = X[t, 64];
```