## D24.2.212 TTBR1\_EL1, Translation Table Base Register 1 (EL1)

The TTBR1\_EL1 characteristics are:

## Purpose

Holds the base address of the translation table for the initial lookup for stage 1 of the translation of an address from the higher V A range in the EL1&amp;0 stage 1 translation regime, and other information for this translation regime.

## Configuration

TTBR1\_EL1 is a 128-bit register that can also be accessed as a 64-bit value. If it is accessed as a 64-bit register, accesses read and write bits [63:0] and do not modify bits [127:64].

AArch64 System register TTBR1\_EL1 bits [63:0] are architecturally mapped to AArch32 System register TTBR1[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TTBR1\_EL1 are UNDEFINED.

## Attributes

TTBR1\_EL1 is a:

- 128-bit register when FEAT\_D128 is implemented and TCR2\_EL1.D128 == '1'.
- 64-bit register when FEAT\_D128 is not implemented or TCR2\_EL1.D128 == '0'.

## Field descriptions

When FEAT\_D128 is implemented and TCR2\_EL1.D128 == '1':

<!-- image -->

## Bits [127:88]

Reserved, RES0.

## BADDR, bits [87:80, 47:5]

Translation table base address:

- Bits A[55:x] of the stage 1 translation table base address bits are in register bits[87:80, 47:x].
- Bits A[(x-1):0] of the stage 1 translation table base address are zero.

Address bit x is the minimum address bit required to align the translation table to the size of the table. x is calculated based on LOG2(StartTableSize), as described in VMSAv9-128. The smallest permitted value of x is 5.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [79:64]

Reserved, RES0.

## ASID, bits [63:48]

An ASID for the translation table base address. The TCR\_EL1.A1 field selects either TTBR0\_EL1.ASID or TTBR1\_EL1.ASID.

If the implementation has only 8 bits of ASID, then the upper 8 bits of this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:3]

Reserved, RES0.

## SKL, bits [2:1]

Skip Level associated with translation table walks using TTBR1\_EL1.

This determines the number of levels to be skipped from the regular start level of the stage 1 EL1&amp;0 translation table walks using TTBR1\_EL1.

| SKL   | Meaning                                     |
|-------|---------------------------------------------|
| 0b00  | Skip 0 level from the regular start level.  |
| 0b01  | Skip 1 level from the regular start level.  |
| 0b10  | Skip 2 levels from the regular start level. |
| 0b11  | Skip 3 levels from the regular start level. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

## When FEAT\_TTCNP is implemented:

Common not Private. This bit indicates whether each entry that is pointed to by TBR1\_EL1 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of TTBR1\_EL1.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by TTBR1_EL1, for the current translation regime and ASID, are permitted to differ from corresponding entries for TTBR1_EL1 for other PEs in the Inner Shareable domain. This is not affected by: |
|       | • The value of TTBR1_EL1.CnP on those other PEs.                                                                                                                                                                                           |
|       | • The value of the current ASID.                                                                                                                                                                                                           |
|       | • If EL2 is implemented and enabled in the current Security state, the value of the current VMID.                                                                                                                                          |

| CnP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | The translation table entries pointed to by TTBR1_EL1 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of TTBR1_EL1.CnP is 1 and all of the following apply: • The translation table entries are pointed to by TTBR1_EL1. • The translation tables relate to the same translation regime. • The ASID is the same as the current ASID. • If EL2 is implemented and enabled in the current Security state, the value of the current VMID. |

This bit is permitted to be cached in a TLB.

When a TLB combines entries from stage 1 translation and stage 2 translation into a single entry, that entry can only be shared between different PEs if the value of the CnP bit is 1 for both stage 1 and stage 2.

<!-- image -->

Note

If the value of the TTBR1\_EL1.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those TTBR1\_EL1s do not point to the same translation table entries when the other conditions specified for the case when the value of CnP is 1 apply, then the results of translations are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## When FEAT\_D128 is not implemented or TCR2\_EL1.D128 == '0':

<!-- image -->

## ASID, bits [63:48]

An ASID for the translation table base address. The TCR\_EL1.A1 field selects either TTBR0\_EL1.ASID or TTBR1\_EL1.ASID.

If the implementation has only 8 bits of ASID, then the upper 8 bits of this field are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## BADDR[47:1], bits [47:1]

Translation table base address:

- Bits A[47:x] of the stage 1 translation table base address bits are in register bits[47:x].
- Bits A[(x-1):0] of the stage 1 translation table base address are zero.

Address bit x is the minimum address bit required to align the translation table to the size of the table. The AArch64 Virtual Memory System Architecture chapter describes how x is calculated based on the value of TCR\_EL1.T1SZ, the translation stage, and the translation granule size.

The BADDR field represents a 52-bit address if any of the following apply:

- The value of TCR\_EL1.IPS represents an OA size of 52 bits.
- The Effective value of TCR\_EL1.DS is 1.

When TTBR1\_EL1.BADDR represents a 52-bit addresses, all of the following apply:

- Bits A[51:48] of the stage 1 translation table base address bits are in register bits[5:2].
- Register bit[1] is RES0.
- The smallest permitted value of x is 6.
- When x&gt;6, register bits[(x-1):6] are RES0.

Otherwise, all of the following apply:

- Register bits[(x-1):1] are RES0.
- If 52-bit PA is supported, then bits A[51:48] of the stage 1 translation table base address are treated as 0b0000 .

## Note

If BADDR represents a 52-bit address, and the translation table has fewer than eight entries, the table must be aligned to 64 bytes. Otherwise the translation table must be aligned to the size of the table.

For the 64KB granule, if 52-bit PA is not supported, and the value of TCR\_EL1.IPS is 0b110 or 0b111 , one of the following IMPLEMENTATION DEFINED behaviors occur:

- BADDRuses the extended format to represent a 52-bit base address.
- BADDRdoes not use the extended format.

When the value of ID\_AA64MMFR0\_EL1.PARange indicates that the implementation supports a 56 bit PA size, bits A[55:52] of the stage 1 translation table base address are zero.

If any register bit[47:1] that is defined as RES0 has the value 1 when a translation table walk is done using TTBR1\_EL1, then the translation table base address might be misaligned, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Bits A[(x-1):0] of the stage 1 translation table base address are treated as if all the bits are zero. The value read back from the corresponding register bits is either the value written to the register or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

## When FEAT\_TTCNP is implemented:

Common not Private. This bit indicates whether each entry that is pointed to by TBR1\_EL1 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of TTBR1\_EL1.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by TTBR1_EL1, for the current translation regime and ASID, are permitted to differ from corresponding entries for TTBR1_EL1 for other PEs in the Inner Shareable domain. This is not affected by: |
|       | • The value of TTBR1_EL1.CnP on those other PEs.                                                                                                                                                                                           |
|       | • The value of the current ASID.                                                                                                                                                                                                           |
|       | • If EL2 is implemented and enabled in the current Security state, the value of the current VMID.                                                                                                                                          |

| CnP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | The translation table entries pointed to by TTBR1_EL1 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of TTBR1_EL1.CnP is 1 and all of the following apply: • The translation table entries are pointed to by TTBR1_EL1. • The translation tables relate to the same translation regime. • The ASID is the same as the current ASID. • If EL2 is implemented and enabled in the current Security state, the value of the current VMID. |

This bit is permitted to be cached in a TLB.

When a TLB combines entries from stage 1 translation and stage 2 translation into a single entry, that entry can only be shared between different PEs if the value of the CnP bit is 1 for both stage 1 and stage 2.

Note

If the value of the TTBR1\_EL1.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those TTBR1\_EL1s do not point to the same translation table entries when the other conditions specified for the case when the value of CnP is 1 apply, then the results of translations are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TTBR1\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TTBR1\_EL1 or TTBR1\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TTBR1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.TTBR1_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x210]; else X[t, 64] = TTBR1_EL1<63:0>;
```

```
elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = TTBR1_EL2<63:0>; else X[t, 64] = TTBR1_EL1<63:0>; elsif PSTATE.EL == EL3 then X[t, 64] = TTBR1_EL1<63:0>;
```

MSR TTBR1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.TTBR1_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x210] = X[t, 64]; else TTBR1_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then TTBR1_EL2<63:0> = X[t, 64]; else TTBR1_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL3 then TTBR1_EL1<63:0> = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TTBR1\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x210]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = TTBR1_EL1<63:0>;
```

```
else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TTBR1_EL1<63:0>; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TTBR1\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x210] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then TTBR1_EL1<63:0> = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TTBR1_EL1<63:0> = X[t, 64]; else UNDEFINED;
```

When FEAT\_D128 is implemented MRRS &lt;Xt&gt;, &lt;Xt+1&gt;, TTBR1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.TTBR1_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14);
```

```
elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, t2, 128] = NVMem128[0x210]; else X[t, t2, 128] = TTBR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif ELIsInHost(EL2) then X[t, t2, 128] = TTBR1_EL2; else X[t, t2, 128] = TTBR1_EL1; elsif PSTATE.EL == EL3 then X[t, t2, 128] = TTBR1_EL1;
```

When FEAT\_D128 is implemented MSRR TTBR1\_EL1, &lt;Xt&gt;, &lt;Xt+1&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.TTBR1_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem128[0x210] = X[t, t2, 128]; else TTBR1_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14);
```

```
elsif ELIsInHost(EL2) then TTBR1_EL2<127:0> = X[t, t2, 128]; else TTBR1_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL3 then TTBR1_EL1<127:0> = X[t, t2, 128];
```

When FEAT\_D128 is implemented and FEAT\_VHE is implemented MRRS &lt;Xt&gt;, &lt;Xt+1&gt;, TTBR1\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, t2, 128] = NVMem128[0x210]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else X[t, t2, 128] = TTBR1_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, t2, 128] = TTBR1_EL1; else UNDEFINED;
```

When FEAT\_D128 is implemented and FEAT\_VHE is implemented MSRR TTBR1\_EL12, &lt;Xt&gt;, &lt;Xt+1&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem128[0x210] = X[t, t2, 128];
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else TTBR1_EL1<127:0> = X[t, t2, 128]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TTBR1_EL1<127:0> = X[t, t2, 128]; else UNDEFINED;
```