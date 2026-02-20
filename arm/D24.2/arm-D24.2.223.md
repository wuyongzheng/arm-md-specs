## D24.2.223 VSTTBR\_EL2, Virtualization Secure Translation Table Base Register

The VSTTBR\_EL2 characteristics are:

## Purpose

The base register for stage 2 translation tables to translate Secure IPAs in the Secure EL1&amp;0 translation regime. Holds the base address of the translation table for the initial lookup for stage 2 of an address translation for a Secure IPA in the Secure EL1&amp;0 translation regime, and other information for this translation stage.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SEL2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to VSTTBR\_EL2 are UNDEFINED.

## Attributes

VSTTBR\_EL2 is a 64-bit register.

## Field descriptions

When FEAT\_D128 is implemented and VTCR\_EL2.D128 == '1':

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## BADDR, bits [55:5]

- Bits A[55:x] of the stage 2 translation table base address bits are in register bits[55:x].
- Bits A[(x-1):0] of the stage 2 translation table base address are zero.

Address bit x is the minimum address bit required to align the translation table to the size of the table. x is calculated based on LOG2(StartTableSize), as described in VMSAv9-128. The smallest permitted value of x is 5.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:3]

Reserved, RES0.

## SKL, bits [2:1]

Skip Level. Skip Level determines the number of levels to be skipped from the regular start level of the Secure stage 2 translation table walk.

| SKL   | Meaning                                     |
|-------|---------------------------------------------|
| 0b00  | Skip 0 level from the regular start level.  |
| 0b01  | Skip 1 level from the regular start level.  |
| 0b10  | Skip 2 levels from the regular start level. |
| 0b11  | Skip 3 levels from the regular start level. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

Common not Private, for stage 2 of the Secure EL1&amp;0 translation regime. In an implementation that includes FEAT\_TTCNP, indicates whether each entry that is pointed to by VSTTBR\_EL2 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of VSTTBR\_EL2.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by VSTTBR_EL2 are permitted to differ from the entries for VSTTBR_EL2 for other PEs in the Inner Shareable domain. This is not affected by the value of the current VMID.                            |
| 0b1   | The translation table entries pointed to by VSTTBR_EL2 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of VSTTBR_EL2.CnP is 1 and the VMIDis the same as the current VMID. |

This bit is permitted to be cached in a TLB.

Note

If the value of VSTTBR\_EL2.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those VSTTBR\_EL2s do not point to the same translation table entries when using the current VMID, then the results of translations using VSTTBR\_EL2 are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

When this register has an architecturally-defined reset value, this field resets to a value that is architecturally UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0':

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## BADDR, bits [47:1]

The BADDR field represents a 52-bit address if any of the following apply:

- The value of VTCR\_EL2.PS represents an OA size of 52 bits.
- The Effective value of VTCR\_EL2.DS is 1.

When VSTTBR\_EL2.BADDR represents a 52-bit addresses, all of the following apply:

- Register bits[47:x] hold bits[47:x] of the stage 2 translation table base address, where x is determined by the size of the translation table at the start level.
- The smallest permitted value of x is 6.
- Register bits[5:2] hold bits[51:48] of the stage 2 translation table base address.
- Bits[x:0] of the translation table base address are zero.
- When x&gt;6 register bits[(x-1):6] are RES0.
- Register bit[1] is RES0.

Otherwise, all of the following apply:

- Register bits[47:x] hold bits[47:x] of the stage 2 translation table base address.
- Register bits[(x-1):1] are RES0.
- If 52-bit PA is supported, then bits[51:48] of the stage 2 translation table base address are treated as 0b0000 .

Note

If BADDR represents a 52-bit address, and the translation table has fewer than eight entries, the table must be aligned to 64 bytes. Otherwise the translation table must be aligned to the size of the table.

For the 64KB granule, if 52-bit PA is not supported, and the value of VTCR\_EL2.PS is 0b110 or 0b111 , one of the following IMPLEMENTATION DEFINED behaviors occur:

- BADDRuses the extended format to represent a 52-bit base address.
- BADDRdoes not use the extended format.

When the value of ID\_AA64MMFR0\_EL1.PARange indicates that the implementation supports a 56 bit PA size, bits [55:52] of the stage 2 translation table base address are zero.

If any VSTTBR\_EL2[47:1] bit that is defined as RES0 has the value 1 when a translation table walk is performed using VSTTBR\_EL2, then the translation table base address might be misaligned, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Bits[x-1:0] of the translation table base address are treated as if all the bits are zero. The value read back from the corresponding register bits is either the value written to the register or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

The AArch64 Virtual Memory System Architecture chapter describes how x is calculated based on the value of VSTCR\_EL2.T0SZ, the stage of translation, and the translation granule size.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

Common not Private, for stage 2 of the Secure EL1&amp;0 translation regime. In an implementation that includes FEAT\_TTCNP, indicates whether each entry that is pointed to by VSTTBR\_EL2 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of VSTTBR\_EL2.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by VSTTBR_EL2 are permitted to differ from the entries for VSTTBR_EL2 for other PEs in the Inner Shareable domain. This is not affected by the value of the current VMID.                            |
| 0b1   | The translation table entries pointed to by VSTTBR_EL2 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of VSTTBR_EL2.CnP is 1 and the VMIDis the same as the current VMID. |

This bit is permitted to be cached in a TLB.

Note

If the value of VSTTBR\_EL2.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those VSTTBR\_EL2s do not point to the same translation table entries when using the current VMID, then the results of translations using VSTTBR\_EL2 are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

When this register has an architecturally-defined reset value, this field resets to a value that is architecturally UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VSTTBR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VSTTBR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0110 | 0b000 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(IsFeatureImplemented(FEAT_SEL2) && UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x030]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else X[t, 64] = VSTTBR_EL2; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = VSTTBR_EL2;
```

MSR VSTTBR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x030] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else VSTTBR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else VSTTBR_EL2 = X[t, 64];
```