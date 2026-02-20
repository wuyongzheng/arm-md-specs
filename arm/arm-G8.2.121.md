## G8.2.121 PAR, Physical Address Register

The PAR characteristics are:

## Purpose

Returns the output address (OA) from an Address translation instruction that executed successfully, or fault information if the instruction did not execute successfully.

## Configuration

PAR is a 64-bit register that can also be accessed as a 32-bit value. If it is accessed as a 32-bit register, accesses read and write bits[31:0] and do not modify bits[63:32].

The Configurations section specifies the cases where each PAR format is used.

PAR is accessed as a 32-bit value:

- When the PE is not in Hyp mode and is using the Short-descriptor translation table format.
- When the PE is in Hyp mode and executes an ATS12NSOPR, ATS12NSOPW, ATS12NSOUR, or ATS12NSOUW instruction and the value of HCR.VM is 0 and the value of TTBCR.EAE is 0.

In these cases, PAR[63:32] is RES0.

Otherwise, the PAR is accessed as a 64-bit value, if any of the following is true:

- When using the Long-descriptor translation table format.
- If the stage 1 address translation is disabled and TTBCR.EAE is set to 1.
- In an implementation that includes EL2, for the result of an ATS1Cxx instruction performed from Hyp mode.

For PL1&amp;0 stage 1 translations, TTBCR.EAE selects the translation table format.

AArch32 System register PAR bits [63:0] are architecturally mapped to AArch64 System register PAR\_EL1[63:0].

This register is banked between PAR and PAR\_S and PAR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to PAR are UNDEFINED.

## Attributes

PAR is a 64-bit register.

This register has the following instances:

- PAR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- PAR\_S, when FEAT\_AA32EL3 is implemented.
- PAR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When the instruction returned a 32-bit value to the PAR, PAR.F==0:

<!-- image -->

This section describes the register value returned by the successful execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

On a successful conversion, the PAR can return a value that indicates the resulting attributes, rather than the values that appear in the Translation table descriptors. More precisely:

- Memory attribute fields are permitted to report the resulting attributes, as determined by any permitted implementation choices and any applicable configuration bits, instead of reporting the values that appear in the Translation table descriptors. This applies to the NOS, SH, Inner, and Outer fields.
- See the NS bit description for constraints on the value it returns.

## Bits [63:32]

Reserved, RES0.

## PA, bits [31:12]

Output address. The output address (OA) corresponding to the supplied input address. This field returns address bits[31:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LPAE, bit [11]

When updating the PAR with the result of the translation operation, this bit is set as follows:

| LPAE   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0    | Short-descriptor translation table format used. This means the PAR returned a 32-bit value. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NOS, bit [10]

Not Outer Shareable. When the returned value of PAR.SH is 1, indicates the Shareability attribute for the physical memory region:

| NOS   | Meaning                           |
|-------|-----------------------------------|
| 0b0   | Memory region is Outer Shareable. |
| 0b1   | Memory region is Inner Shareable. |

When the returned value of PAR.SH is 0 the value returned to this field is UNKNOWN.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

NS, bit [9]

Non-secure. The NS attribute for a translation table entry from a Secure translation regime.

For a result from a Secure translation regime, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bit [8]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bit [7]

Shareability. Indicates whether the physical memory region is Non-shareable:

| SH   | Meaning                                                                                              |
|------|------------------------------------------------------------------------------------------------------|
| 0b0  | Memory is Non-shareable.                                                                             |
| 0b1  | Memory is shareable, and PAR.NOS indicates whether the region is Outer Shareable or Inner Shareable. |

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Inner[2:0], bits [6:4]

Inner cacheability attribute for the region. Permitted values are:

| Inner[2:0]   | Meaning                        |
|--------------|--------------------------------|
| 0b000        | Non-cacheable.                 |
| 0b001        | Device-nGnRnE.                 |
| 0b011        | Device-nGnRE.                  |
| 0b101        | Write-Back, Write-Allocate.    |
| 0b110        | Write-Through.                 |
| 0b111        | Write-Back, no Write-Allocate. |

The values

0b010 and 0b100 are reserved.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Outer[1:0], bits [3:2]

Outer cacheability attribute for the region. Permitted values are:

| Outer[1:0]   | Meaning                           |
|--------------|-----------------------------------|
| 0b00         | Non-cacheable.                    |
| 0b01         | Write-Back, Write-Allocate.       |
| 0b10         | Write-Through, no Write-Allocate. |
| 0b11         | Write-Back, no Write-Allocate.    |

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SS, bit [1]

Supersection. Used to indicate if the result is a Supersection:

| SS   | Meaning                                                                                                                                                                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Result is not a Supersection. PAR[31:12] contains OA[31:12].                                                                                                                                                                                                                                                  |
| 0b1  | Result is a Supersection, and: • PAR[31:24] contains OA[31:24]. • PAR[23:16] contains OA[39:32]. • PAR[15:12] contains 0b0000 . If an implementation supports less than 40 bits of physical address, the bits in the PAR field that correspond to physical address bits that are not implemented are UNKNOWN. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                                     |
|-----|---------------------------------------------|
| 0b0 | Address translation completed successfully. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When the instruction returned a 32-bit value to the PAR, PAR.F==1:

<!-- image -->

This section describes the register value returned by a fault on the execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

## Bits [63:32]

Reserved, RES0.

## IMPLEMENTATIONDEFINED, bits [31:16]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:12]

Reserved, RES0.

## LPAE, bit [11]

When updating the PAR with the result of the translation operation, this bit is set as follows:

| LPAE   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0    | Short-descriptor translation table format used. This means the PAR returned a 32-bit value. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [10:7]

Reserved, RES0.

## FS[5], bit [6]

Fault status bits, External abort type. Provides an IMPLEMENTATION DEFINED classification of an External abort. Values are as in the DFSR.ExT field when using the Short-descriptor translation table format.

In an implementation that does not provide any classification of External aborts, this bit is RES0.

For aborts other than External aborts this bit always returns 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

FS[4:0], bits [5:1]

Fault status bits. Values are as in the DFSR.FS field when using the Short-descriptor translation table format.

| FS[4:0]   | Meaning                                                                          | Applies when                |
|-----------|----------------------------------------------------------------------------------|-----------------------------|
| 0b00001   | Alignment fault.                                                                 |                             |
| 0b00011   | Access flag fault, level 1.                                                      |                             |
| 0b00100   | Fault on instruction cache maintenance.                                          |                             |
| 0b00101   | Translation fault, level 1.                                                      |                             |
| 0b00110   | Access flag fault, level 2.                                                      |                             |
| 0b00111   | Translation fault, level 2.                                                      |                             |
| 0b01001   | Domain fault, level 1.                                                           |                             |
| 0b01011   | Domain fault, level 2.                                                           |                             |
| 0b01100   | Synchronous External abort, on translation table walk, level 1.                  |                             |
| 0b01101   | Permission fault, level 1.                                                       |                             |
| 0b01110   | Synchronous External abort, on translation table walk, level 2.                  |                             |
| 0b01111   | Permission fault, level 2.                                                       |                             |
| 0b10000   | TLB conflict abort.                                                              |                             |
| 0b11001   | Synchronous parity or ECC error on memory access, not on translation table walk. | FEAT_RAS is not implemented |
| 0b11100   | Synchronous parity or ECC error on translation table walk, level 1.              | FEAT_RAS is not implemented |
| 0b11110   | Synchronous parity or ECC error on translation table walk, level 2.              | FEAT_RAS is not implemented |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                      |
|-----|------------------------------|
| 0b1 | Address translation aborted. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When the instruction returned a 64-bit value to the PAR, PAR.F==0:

<!-- image -->

This section describes the register value returned by the successful execution of an Address translation instruction. Software might subsequently write a different value to the register, and that write does not affect the operation of the PE.

On a successful conversion, the PAR can return a value that indicates the resulting attributes, rather than the values that appear in the Translation table descriptors. More precisely:

- Memory attribute fields are permitted to report the resulting attributes, as determined by any permitted implementation choices and any applicable configuration bits, instead of reporting the values that appear in the Translation table descriptors. This applies to the ATTR and SH fields.
- See the NS bit description for constraints on the value it returns.

## ATTR, bits [63:56]

Memory attributes for the returned output address. This field uses the same encoding as the Attr&lt;n&gt; fields in MAIR0 and MAIR1.

The value returned in this field can be the resulting attribute, as determined by any permitted implementation choices and any applicable configuration bits, instead of the value that appears in the Translation table descriptor.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [55:40]

Reserved, RES0.

## PA, bits [39:12]

Output address. The output address (OA) corresponding to the supplied input address. This field returns address bits[39:12].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LPAE, bit [11]

When updating the PAR with the result of the translation operation, this bit is set as follows:

| LPAE   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b1    | Long-descriptor translation table format used. This means the PAR returned a 64-bit value. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bit [10]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS, bit [9]

Non-secure. The NS attribute for a translation table entry from a Secure translation regime.

For a result from a Secure translation regime, this bit reflects the Security state of the physical address space of the translation. This means it reflects the effect of the NSTable bits of earlier levels of the translation table walk if those NSTable bits have an effect on the translation.

For a result from a Non-secure translation regime, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [8:7]

Shareability attribute, for the returned output address. Permitted values are:

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

## Bits [6:1]

Reserved, RES0.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                                     |
|-----|---------------------------------------------|
| 0b0 | Address translation completed successfully. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When the instruction returned a 64-bit value to the PAR, PAR.F==1:

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

## Bits [47:12]

Reserved, RES0.

## LPAE, bit [11]

When updating the PAR with the result of the translation operation, this bit is set as follows:

| LPAE   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b1    | Long-descriptor translation table format used. This means the PAR returned a 64-bit value. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [10]

Reserved, RES0.

## FSTAGE, bit [9]

Indicates the translation stage at which the translation aborted:

| FSTAGE   | Meaning                                                            |
|----------|--------------------------------------------------------------------|
| 0b0      | Translation aborted because of a fault in the stage 1 translation. |
| 0b1      | Translation aborted because of a fault in the stage 2 translation. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S2WLK, bit [8]

If this bit is set to 1, it indicates the translation aborted because of a stage 2 fault during a stage 1 translation table walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [7]

Reserved, RES0.

## FST, bits [6:1]

Fault status field. Values are as in the DFSR.STATUS and IFSR.STATUS fields when using the Long-descriptor translation table format.

| FST      | Meaning                                                | Applies when   |
|----------|--------------------------------------------------------|----------------|
| 0b000000 | Address size fault in translation table base register. |                |
| 0b000001 | Address size fault, level 1.                           |                |
| 0b000010 | Address size fault, level 2.                           |                |
| 0b000011 | Address size fault, level 3.                           |                |
| 0b000101 | Translation fault, level 1.                            |                |
| 0b000110 | Translation fault, level 2.                            |                |
| 0b000111 | Translation fault, level 3.                            |                |
| 0b001001 | Access flag fault, level 1.                            |                |
| 0b001010 | Access flag fault, level 2.                            |                |
| 0b001011 | Access flag fault, level 3.                            |                |
| 0b001101 | Permission fault, level 1.                             |                |
| 0b001110 | Permission fault, level 2.                             |                |
| 0b001111 | Permission fault, level 3.                             |                |

| FST      | Meaning                                                                              | Applies when                |
|----------|--------------------------------------------------------------------------------------|-----------------------------|
| 0b010101 | Synchronous External abort on translation table walk, level 1.                       |                             |
| 0b010110 | Synchronous External abort on translation table walk, level 2.                       |                             |
| 0b010111 | Synchronous External abort on translation table walk, level 3.                       |                             |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented |
| 0b110000 | TLB conflict abort.                                                                  |                             |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [0]

Indicates whether the instruction performed a successful address translation.

| F   | Meaning                      |
|-----|------------------------------|
| 0b1 | Address translation aborted. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PAR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0100 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = PAR_NS<31:0>; else R[t] = PAR<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = PAR_NS<31:0>; else R[t] = PAR<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = PAR_S<31:0>; else R[t] = PAR_NS<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0100 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then PAR_NS<31:0> = R[t]; else PAR<31:0> = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then PAR_NS<31:0> = R[t]; else PAR<31:0> = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then PAR_S<31:0> = R[t]; else PAR_NS<31:0> = R[t];
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0111 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = PAR_NS; else R[t, t2] = PAR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = PAR_NS; else R[t, t2] = PAR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t, t2] = PAR_S; else R[t, t2] = PAR_NS;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0111 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then PAR_NS = R[t, t2]; else PAR = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then PAR_NS = R[t, t2]; else PAR = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then PAR_S = R[t, t2]; else PAR_NS = R[t, t2];
```