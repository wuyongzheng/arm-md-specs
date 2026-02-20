## D24.2.142 PAR\_EL1, Physical Address Register

The PAR\_EL1 characteristics are:

## Purpose

Returns the output address (OA) from an Address translation instruction that executed successfully, or fault information if the instruction did not execute successfully.

## Configuration

AArch64 System register PAR\_EL1 is a 128-bit register that can also be accessed as a 64-bit value. If it is accessed as a 64-bit register, accesses read and write bits [63:0] and do not modify bits [127:64].

Single stage AT Instructions (ATS1*) report their result using the 128-bit format of PAR\_EL1 if the translation system that they target uses VMSAv9-128.

ATS12* Instructions report their result using the 128-bit format PAR\_EL1 if either of the following is true:

- if stage 2 translations are enabled and the stage 2 translation system uses VMSAv9-128.
- if stage 2 translations are disabled and the stage 1 translation system uses VMSAv9-128.

Otherwise, 64-bit format of PAR\_EL1 is used.

AArch64 System register PAR\_EL1 bits [63:0] are architecturally mapped to AArch32 System register PAR[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to PAR\_EL1 are UNDEFINED.

## Attributes

PAR\_EL1 is a:

- 128-bit register when FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '1', and GetPAR\_EL1\_F() == '0'.
- 128-bit register when FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '1', and GetPAR\_EL1\_F() == '1'.
- 128-bit register when FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '0', and GetPAR\_EL1\_F() == '0'.
- 128-bit register when FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '0', and GetPAR\_EL1\_F() == '1'.
- 64-bit register when FEAT\_D128 is not implemented and GetPAR\_EL1\_F() == '0'.
- 64-bit register when FEAT\_D128 is not implemented and GetPAR\_EL1\_F() == '1'.

## Field descriptions

When FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '1', and GetPAR\_EL1\_F() == '0':

<!-- image -->

This section describes the register value returned by the successful execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

On a successful conversion, the PAR\_EL1 can return a value that indicates the resulting attributes, rather than the values that appear in the Translation table descriptors. More precisely:

- The PAR\_EL1.{ATTR, SH} fields are permitted to report the resulting attributes, as determined by any permitted implementation choices and any applicable configuration bits, instead of reporting the values that appear in the Translation table descriptors.
- See the PAR\_EL1.NS bit description for constraints on the value it returns.

## Bits [127:120]

Reserved, RES0.

## PA, bits [119:76]

Output address. The output address (OA) corresponding to the supplied input address. This field returns address bits[55:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [75:65]

Reserved, RES0.

## D128, bit [64]

Indicates if the PAR\_EL1 uses the 128-bit format.

| D128   | Meaning                                                           |
|--------|-------------------------------------------------------------------|
| 0b1    | PAR_EL1 uses the 128-bit format. PAR_EL1[127:0] holds valid data. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ATTR, bits [63:56]

Memory attributes for the returned output address. This field uses the same encoding as the Attr&lt;n&gt; fields in MAIR\_EL1, MAIR\_EL2, and MAIR\_EL3.

If FEAT\_MTE\_PERM is implemented and the instruction performed a stage 2 translation, the following additional encoding is defined:

| ATTR       | Meaning                                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------|
| 0b11100000 | Tagged NoTagAccess Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. |
|            | Note This encoding in MAIR_ELx is Reserved.                                                                       |

The value returned in this field can be the resulting attribute that is actually implemented by the implementation, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

Note

The attributes presented are consistent with the stages of translation applied in the address translation instruction. If the instruction performed a stage 1 translation only, the attributes are from the stage 1 translation. If the instruction performed a stage 1 and stage 2 translation, the attributes are from the combined stage 1 and stage 2 translation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [55:52, 6:4]

Reserved, RES0.

## Bits [51:12]

Reserved, RES0.

## NSE, bit [11]

## When FEAT\_RME is implemented:

Reports the NSE attribute for a translation table descriptor from the EL3 translation regime.

For a description of the values derived by evaluating NS and NSE together, see PAR\_EL1.NS.

For a result from a Secure, Non-secure, or Realm translation regime, this bit is unknown.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## IMPLEMENTATIONDEFINED, bit [10]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS, bit [9]

## When FEAT\_RME is implemented:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime, a Realm translation regime, and the EL3 translation regime.

For a result from an EL3 translation regime, NS and NSE are evaluated together to report the physical address space:

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |

| NSE   | NS   | Meaning   |
|-------|------|-----------|
| 0b1   | 0b1  | Realm.    |

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

For a result from an S1E1 or S1E0 operation on the Realm EL1&amp;0 translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime.

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [8:7]

Shareability attribute, for the returned output address.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

The value

0b01 is reserved.

Note

This field returns the value 0b10 for:

- Any type of Device memory.
- Normal memory with both Inner Non-cacheable and Outer Non-cacheable attributes.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [3:1]

Reserved, RES0.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                                     |
|-----|---------------------------------------------|
| 0b0 | Address translation completed successfully. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '1', and GetPAR\_EL1\_F() == '1':

<!-- image -->

This section describes the register value returned by a fault on the execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

## Bits [127:65]

Reserved, RES0.

## D128, bit [64]

Indicates if the PAR\_EL1 uses the 128-bit format.

| D128   | Meaning                                                           |
|--------|-------------------------------------------------------------------|
| 0b1    | PAR_EL1 uses the 128-bit format. PAR_EL1[127:0] holds valid data. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [63:56]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [55:52]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [51:48]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [47:16]

Reserved, RES0.

## DirtyBit, bit [15]

## When FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented:

DirtyBit flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation that is using Indirect Permissions, and dirty state is managed by software, then this field holds information about the fault.

| DirtyBit   | Meaning                                         |
|------------|-------------------------------------------------|
| 0b0        | The Permission Fault is not due to dirty state. |
| 0b1        | The Permission Fault is due to dirty state.     |

For any other fault or Access, this field is RES0.

Note

At stage 1, dirty state is indicated by the nDirty bit in Block and Page descriptors. At stage 2, dirty state is indicated by the Dirty bit in Block and Page descriptors.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Overlay, bit [14]

## When FEAT\_S1POE is implemented or FEAT\_S2POE is implemented:

Overlay flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation, then this field holds information about the fault.

| Overlay   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0       | The Data Abort is not due to Overlay Permissions. |
| 0b1       | The Data Abort is due to Overlay Permissions.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TopLevel, bit [13]

## When FEAT\_THE is implemented:

Fault due to TopLevel. Indicates if the fault was due to TopLevel.

| TopLevel   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Fault is not due to TopLevel. |
| 0b1        | Fault is due to TopLevel.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

AssuredOnly, bit [12]

## When FEAT\_THE is implemented:

AssuredOnly flag.

If PAR\_EL1.S indicates a stage 2 fault, then this field holds information about the fault.

| AssuredOnly   | Meaning                                   |
|---------------|-------------------------------------------|
| 0b0           | The Data Abort is not due to AssuredOnly. |
| 0b1           | The Data Abort is due to AssuredOnly.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [11]

Reserved, RES1.

## Bit [10]

Reserved, RES0.

## S, bit [9]

Indicates the translation stage at which the translation aborted:

| S   | Meaning                                                            |
|-----|--------------------------------------------------------------------|
| 0b0 | Translation aborted because of a fault in the stage 1 translation. |
| 0b1 | Translation aborted because of a fault in the stage 2 translation. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PTW, bit [8]

If this bit is set to 1, it indicates the translation aborted because of a stage 2 fault during a stage 1 translation table walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [7]

Reserved, RES0.

## FST, bits [6:1]

Fault status code, as shown in the Data Abort ESR encoding.

| FST      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
| 0b001000 | Access flag fault, level 0.                                                                                                   | FEAT_LPA2 is implemented                                 |
| 0b001100 | Permission fault, level 0.                                                                                                    | FEAT_LPA2 is implemented                                 |
| 0b001101 | Permission fault, level 1.                                                                                                    |                                                          |
| 0b001110 | Permission fault, level 2.                                                                                                    |                                                          |
| 0b001111 | Permission fault, level 3.                                                                                                    |                                                          |
| 0b011011 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level -1. | FEAT_LPA2 is implemented and FEAT_RAS is not implemented |
| 0b011100 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 0.  | FEAT_RAS is not implemented                              |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 1.  | FEAT_RAS is not implemented                              |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 2.  | FEAT_RAS is not implemented                              |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 3.  | FEAT_RAS is not implemented                              |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2.                         | FEAT_D128 is implemented and FEAT_RME is implemented     |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1.                         | FEAT_RME is implemented and FEAT_LPA2 is implemented     |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.                          | FEAT_RME is implemented                                  |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.                          | FEAT_RME is implemented                                  |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.                          | FEAT_RME is implemented                                  |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.                          | FEAT_RME is implemented                                  |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.                              | FEAT_RME is implemented                                  |

| FST      | Meaning                                                                                                                 | Applies when                |
|----------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 0b101001 | Address size fault, level -1.                                                                                           | FEAT_LPA2 is implemented    |
| 0b101010 | Translation fault, level -2.                                                                                            | FEAT_D128 is implemented    |
| 0b101011 | Translation fault, level -1.                                                                                            | FEAT_LPA2 is implemented    |
| 0b101100 | Address Size fault, level -2.                                                                                           | FEAT_D128 is implemented    |
| 0b110000 | TLB conflict abort.                                                                                                     |                             |
| 0b110001 | Unsupported atomic hardware update fault.                                                                               | FEAT_HAFDBS is implemented  |
| 0b111101 | Section Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format. | FEAT_AA32EL1 is implemented |
| 0b111110 | Page Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format.    | FEAT_AA32EL1 is implemented |

## Note

The encodings for FST do not include Synchronous External abort on translation table walk or hardware update of translation table, because these MMU faults are reported as a Data Abort exception instead of being recorded in PAR\_EL1. See Exceptions to reporting the fault in PAR\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                      |
|-----|------------------------------|
| 0b1 | Address translation aborted. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '0', and GetPAR\_EL1\_F() == '0':

<!-- image -->

IMPLEMENTATION DEFINED

This section describes the register value returned by the successful execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

On a successful conversion, the PAR\_EL1 can return a value that indicates the resulting attributes, rather than the values that appear in the Translation table descriptors. More precisely:

- The PAR\_EL1.{ATTR, SH} fields are permitted to report the resulting attributes, as determined by any permitted implementation choices and any applicable configuration bits, instead of reporting the values that appear in the Translation table descriptors.
- See the PAR\_EL1.NS bit description for constraints on the value it returns.

## Bits [127:65]

Reserved, RES0.

## D128, bit [64]

Indicates if the PAR\_EL1 uses the 128-bit format.

| D128   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | PAR_EL1 uses the 64-bit format. PAR_EL1[63:0] holds valid data. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ATTR, bits [63:56]

Memory attributes for the returned output address. This field uses the same encoding as the Attr&lt;n&gt; fields in MAIR\_EL1, MAIR\_EL2, and MAIR\_EL3.

If FEAT\_MTE\_PERM is implemented and the instruction performed a stage 2 translation, the following additional encoding is defined:

| ATTR       | Meaning                                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------|
| 0b11100000 | Tagged NoTagAccess Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. |

| Note                                   |
|----------------------------------------|
| This encoding in MAIR_ELx is Reserved. |

The value returned in this field can be the resulting attribute that is actually implemented by the implementation, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

Note

The attributes presented are consistent with the stages of translation applied in the address translation instruction. If the instruction performed a stage 1 translation only, the attributes are from the stage 1 translation. If the instruction performed a stage 1 and stage 2 translation, the attributes are from the combined stage 1 and stage 2 translation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [55:52, 6:4]

Reserved, RES0.

## PA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

Extension to PA[47:12]. For more information, see PA[47:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA[47:12], bits [47:12]

Output address. The output address (OA) corresponding to the supplied input address. This field returns address bits[47:12].

When FEAT\_LPA is implemented and 52-bit addresses are in use, PA[51:48] forms the upper part of the address value. Otherwise, when 52-bit addresses are not in use, PA[51:48] is RES0.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSE, bit [11]

## When FEAT\_RME is implemented:

Reports the NSE attribute for a translation table entry from the EL3 translation regime.

For a description of the values derived by evaluating NS and NSE together, see PAR\_EL1.NS.

For a result from a Secure, Non-secure, or Realm translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## IMPLEMENTATIONDEFINED, bit [10]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS, bit [9]

## When FEAT\_RME is implemented:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime, a Realm translation regime, and the EL3 translation regime.

For a result from an EL3 translation regime, NS and NSE are evaluated together to report the physical address space:

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

For a result from an S1E1 or S1E0 operation on the Realm EL1&amp;0 translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime.

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [8:7]

Shareability attribute, for the returned output address.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

The value

0b01 is reserved.

## Note

This field returns the value 0b10 for:

- Any type of Device memory.
- Normal memory with both Inner Non-cacheable and Outer Non-cacheable attributes.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [3:1]

Reserved, RES0.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                                     |
|-----|---------------------------------------------|
| 0b0 | Address translation completed successfully. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_D128 is implemented, GetPAR\_EL1\_D128() == '0', and GetPAR\_EL1\_F() == '1':

<!-- image -->

This section describes the register value returned by a fault on the execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

## Bits [127:65]

Reserved, RES0.

## D128, bit [64]

Indicates if the PAR\_EL1 uses the 128-bit format.

| D128   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | PAR_EL1 uses the 64-bit format. PAR_EL1[63:0] holds valid data. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [63:56]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [55:52]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [51:48]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [47:16]

Reserved, RES0.

## DirtyBit, bit [15]

## When FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented:

DirtyBit flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation that is using Indirect Permissions, and dirty state is managed by software, then this field holds information about the fault.

| DirtyBit   | Meaning                                                         |
|------------|-----------------------------------------------------------------|
| 0b0        | The Permission Fault is not due to nDirty State or Dirty State. |
| 0b1        | The Permission Fault is due to nDirty State or Dirty State.     |

For any other fault or Access, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Overlay, bit [14]

## When FEAT\_S1POE is implemented or FEAT\_S2POE is implemented:

Overlay flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation, then this field holds information about the fault.

| Overlay   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0       | The Data Abort is not due to Overlay Permissions. |
| 0b1       | The Data Abort is due to Overlay Permissions.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TopLevel, bit [13]

## When FEAT\_THE is implemented:

Fault due to TopLevel. Indicates if the fault was due to TopLevel.

| TopLevel   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Fault is not due to TopLevel. |
| 0b1        | Fault is due to TopLevel.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

AssuredOnly, bit [12]

## When FEAT\_THE is implemented:

AssuredOnly flag.

If PAR\_EL1.S indicates a stage 2 fault, then this field holds information about the fault.

| AssuredOnly   | Meaning                                   |
|---------------|-------------------------------------------|
| 0b0           | The Data Abort is not due to AssuredOnly. |
| 0b1           | The Data Abort is due to AssuredOnly.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [11]

Reserved, RES1.

## Bit [10]

Reserved, RES0.

## S, bit [9]

Indicates the translation stage at which the translation aborted:

| S   | Meaning                                                            |
|-----|--------------------------------------------------------------------|
| 0b0 | Translation aborted because of a fault in the stage 1 translation. |
| 0b1 | Translation aborted because of a fault in the stage 2 translation. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PTW, bit [8]

If this bit is set to 1, it indicates the translation aborted because of a stage 2 fault during a stage 1 translation table walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [7]

Reserved, RES0.

## FST, bits [6:1]

Fault status code, as shown in the Data Abort exception ESR encoding.

| FST      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
| 0b001000 | Access flag fault, level 0.                                                                                                   | FEAT_LPA2 is implemented                                 |
| 0b001100 | Permission fault, level 0.                                                                                                    | FEAT_LPA2 is implemented                                 |
| 0b001101 | Permission fault, level 1.                                                                                                    |                                                          |
| 0b001110 | Permission fault, level 2.                                                                                                    |                                                          |
| 0b001111 | Permission fault, level 3.                                                                                                    |                                                          |
| 0b011011 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level -1. | FEAT_LPA2 is implemented and FEAT_RAS is not implemented |
| 0b011100 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 0.  | FEAT_RAS is not implemented                              |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 1.  | FEAT_RAS is not implemented                              |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 2.  | FEAT_RAS is not implemented                              |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 3.  | FEAT_RAS is not implemented                              |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2.                         | FEAT_D128 is implemented and FEAT_RME is implemented     |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1.                         | FEAT_RME is implemented and FEAT_LPA2 is implemented     |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.                          | FEAT_RME is implemented                                  |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.                          | FEAT_RME is implemented                                  |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.                          | FEAT_RME is implemented                                  |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.                          | FEAT_RME is implemented                                  |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.                              | FEAT_RME is implemented                                  |

| FST      | Meaning                                                                                                                 | Applies when                |
|----------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 0b101001 | Address size fault, level -1.                                                                                           | FEAT_LPA2 is implemented    |
| 0b101010 | Translation fault, level -2.                                                                                            | FEAT_D128 is implemented    |
| 0b101011 | Translation fault, level -1.                                                                                            | FEAT_LPA2 is implemented    |
| 0b101100 | Address Size fault, level -2.                                                                                           | FEAT_D128 is implemented    |
| 0b110000 | TLB conflict abort.                                                                                                     |                             |
| 0b110001 | Unsupported atomic hardware update fault.                                                                               | FEAT_HAFDBS is implemented  |
| 0b111101 | Section Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format. | FEAT_AA32EL1 is implemented |
| 0b111110 | Page Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format.    | FEAT_AA32EL1 is implemented |

## Note

The encodings for FST do not include Synchronous External abort on translation table walk or hardware update of translation table, because these MMU faults are reported as a Data Abort exception instead of being recorded in PAR\_EL1. See Exceptions to reporting the fault in PAR\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                      |
|-----|------------------------------|
| 0b1 | Address translation aborted. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_D128 is not implemented and GetPAR\_EL1\_F() == '0':

<!-- image -->

IMPLEMENTATION DEFINED

This section describes the register value returned by the successful execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

On a successful conversion, the PAR\_EL1 can return a value that indicates the resulting attributes, rather than the values that appear in the Translation table descriptors. More precisely:

- The PAR\_EL1.{ATTR, SH} fields are permitted to report the resulting attributes, as determined by any permitted implementation choices and any applicable configuration bits, instead of reporting the values that appear in the Translation table descriptors.
- See the PAR\_EL1.NS bit description for constraints on the value it returns.

## ATTR, bits [63:56]

Memory attributes for the returned output address. This field uses the same encoding as the Attr&lt;n&gt; fields in MAIR\_EL1, MAIR\_EL2, and MAIR\_EL3.

If FEAT\_MTE\_PERM is implemented and the instruction performed a stage 2 translation, the following additional encoding is defined:

## ATTR

## Meaning

0b11100000

Tagged NoTagAccess Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory.

Note

This encoding in MAIR\_ELx is Reserved.

The value returned in this field can be the resulting attribute that is actually implemented by the implementation, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

Note

The attributes presented are consistent with the stages of translation applied in the address translation instruction. If the instruction performed a stage 1 translation only, the attributes are from the stage 1 translation. If the instruction performed a stage 1 and stage 2 translation, the attributes are from the combined stage 1 and stage 2 translation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [55:52, 6:4]

Reserved, RES0.

## PA[51:48], bits [51:48]

## When FEAT\_LPA is implemented:

Extension to PA[47:12]. For more information, see PA[47:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PA[47:12], bits [47:12]

Output address. The output address (OA) corresponding to the supplied input address. This field returns address bits[47:12].

When FEAT\_LPA is implemented and 52-bit addresses are in use, PA[51:48] forms the upper part of the address value. Otherwise, when 52-bit addresses are not in use, PA[51:48] is RES0.

For implementations with fewer than 48 physical address bits, the corresponding upper bits in this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSE, bit [11]

## When FEAT\_RME is implemented:

Reports the NSE attribute for a translation table entry from the EL3 translation regime.

For a description of the values derived by evaluating NS and NSE together, see PAR\_EL1.NS.

For a result from a Secure, Non-secure, or Realm translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## IMPLEMENTATIONDEFINED, bit [10]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS, bit [9]

## When FEAT\_RME is implemented:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime, a Realm translation regime, and the EL3 translation regime.

For a result from an EL3 translation regime, NS and NSE are evaluated together to report the physical address space:

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

For a result from an S1E1 or S1E0 operation on the Realm EL1&amp;0 translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Non-secure. The NS attribute for a translation table entry from a Secure translation regime.

For a result from a Secure translation regime, when SCR\_EL3.EEL2 is 1, this bit distinguishes between the Secure and Non-secure intermediate physical address space of the translation for the instructions:

- In AArch64 state: AT S1E1R, AT S1E1W, AT S1E1RP, AT S1E1WP, AT S1E0R, and AT S1E0W.
- In AArch32 state: ATS1CPR, ATS1CPW, ATS1CPRP, ATS1CPWP, ATS1CUR, and ATS1CUW.

Otherwise, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [8:7]

Shareability attribute, for the returned output address.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

The value 0b01

is reserved.

## Note

This field returns the value 0b10 for:

- Any type of Device memory.
- Normal memory with both Inner Non-cacheable and Outer Non-cacheable attributes.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [3:1]

Reserved, RES0.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                                     |
|-----|---------------------------------------------|
| 0b0 | Address translation completed successfully. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_D128 is not implemented and GetPAR\_EL1\_F() == '1':

<!-- image -->

This section describes the register value returned by a fault on the execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

## IMPLEMENTATIONDEFINED, bits [63:56]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [55:52]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [51:48]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [47:16]

Reserved, RES0.

## DirtyBit, bit [15]

## When FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented:

DirtyBit flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation that is using Indirect Permissions, and dirty state is managed by software, then this field holds information about the fault.

| DirtyBit   | Meaning                                                         |
|------------|-----------------------------------------------------------------|
| 0b0        | The Permission Fault is not due to nDirty State or Dirty State. |
| 0b1        | The Permission Fault is due to nDirty State or Dirty State.     |

For any other fault or Access, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Overlay, bit [14]

## When FEAT\_S1POE is implemented or FEAT\_S2POE is implemented:

Overlay flag.

If PAR\_EL1.FST indicates a Permission fault for a stage of translation, then this field holds information about the fault.

| Overlay   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0       | The Data Abort is not due to Overlay Permissions. |
| 0b1       | The Data Abort is due to Overlay Permissions.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TopLevel, bit [13]

## When FEAT\_THE is implemented:

Fault due to TopLevel. Indicates if the fault was due to TopLevel.

| TopLevel   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Fault is not due to TopLevel. |
| 0b1        | Fault is due to TopLevel.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

AssuredOnly, bit [12]

## When FEAT\_THE is implemented:

AssuredOnly flag.

If PAR\_EL1.S indicates a stage 2 fault, then this field holds information about the fault.

| AssuredOnly   | Meaning                                   |
|---------------|-------------------------------------------|
| 0b0           | The Data Abort is not due to AssuredOnly. |
| 0b1           | The Data Abort is due to AssuredOnly.     |

For any other fault, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [11]

Reserved, RES1.

## Bit [10]

Reserved, RES0.

## S, bit [9]

Indicates the translation stage at which the translation aborted:

| S   | Meaning                                                            |
|-----|--------------------------------------------------------------------|
| 0b0 | Translation aborted because of a fault in the stage 1 translation. |
| 0b1 | Translation aborted because of a fault in the stage 2 translation. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PTW, bit [8]

If this bit is set to 1, it indicates the translation aborted because of a stage 2 fault during a stage 1 translation table walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [7]

Reserved, RES0.

FST, bits [6:1]

Fault status code, as shown in the Data Abort exception ESR encoding.

| FST      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
| 0b001000 | Access flag fault, level 0.                                                                                                   | FEAT_LPA2 is implemented                                 |
| 0b001100 | Permission fault, level 0.                                                                                                    | FEAT_LPA2 is implemented                                 |
| 0b001101 | Permission fault, level 1.                                                                                                    |                                                          |
| 0b001110 | Permission fault, level 2.                                                                                                    |                                                          |
| 0b001111 | Permission fault, level 3.                                                                                                    |                                                          |
| 0b011011 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level -1. | FEAT_LPA2 is implemented and FEAT_RAS is not implemented |
| 0b011100 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 0.  | FEAT_RAS is not implemented                              |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 1.  | FEAT_RAS is not implemented                              |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 2.  | FEAT_RAS is not implemented                              |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level 3.  | FEAT_RAS is not implemented                              |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2.                         | FEAT_D128 is implemented and FEAT_RME is implemented     |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1.                         | FEAT_RME is implemented and FEAT_LPA2 is implemented     |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.                          | FEAT_RME is implemented                                  |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.                          | FEAT_RME is implemented                                  |

| FST      | Meaning                                                                                                                 | Applies when                |
|----------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.                    | FEAT_RME is implemented     |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.                    | FEAT_RME is implemented     |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.                        | FEAT_RME is implemented     |
| 0b101001 | Address size fault, level -1.                                                                                           | FEAT_LPA2 is implemented    |
| 0b101010 | Translation fault, level -2.                                                                                            | FEAT_D128 is implemented    |
| 0b101011 | Translation fault, level -1.                                                                                            | FEAT_LPA2 is implemented    |
| 0b101100 | Address Size fault, level -2.                                                                                           | FEAT_D128 is implemented    |
| 0b110000 | TLB conflict abort.                                                                                                     |                             |
| 0b110001 | Unsupported atomic hardware update fault.                                                                               | FEAT_HAFDBS is implemented  |
| 0b111101 | Section Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format. | FEAT_AA32EL1 is implemented |
| 0b111110 | Page Domain fault, from an AArch32 stage 1 EL1&0 translation regime using Short-descriptor translation table format.    | FEAT_AA32EL1 is implemented |

Note

The encodings for FST do not include Synchronous External abort on translation table walk or hardware update of translation table, because these MMU faults are reported as a Data Abort exception instead of being recorded in PAR\_EL1. See Exceptions to reporting the fault in PAR\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                      |
|-----|------------------------------|
| 0b1 | Address translation aborted. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PAR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0111 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.PAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = PAR_EL1<63:0>; elsif PSTATE.EL == EL2 then X[t, 64] = PAR_EL1<63:0>; elsif PSTATE.EL == EL3 then X[t, 64] = PAR_EL1<63:0>;
```

MSR PAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0111 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.PAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else PAR_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL2 then PAR_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL3 then PAR_EL1<63:0> = X[t, 64];
```

When FEAT\_D128 is implemented MRRS &lt;Xt&gt;, &lt;Xt+1&gt;, PAR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0111 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.PAR_EL1 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else X[t, t2, 128] = PAR_EL1<127:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else X[t, t2, 128] = PAR_EL1<127:0>; elsif PSTATE.EL == EL3 then X[t, t2, 128] = PAR_EL1<127:0>;
```

When FEAT\_D128 is implemented MSRR PAR\_EL1, &lt;Xt&gt;, &lt;Xt+1&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0111 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.PAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else PAR_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else PAR_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL3 then PAR_EL1<127:0> = X[t, t2, 128];
```