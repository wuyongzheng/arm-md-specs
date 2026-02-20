## D24.2.211 TTBR0\_EL3, Translation Table Base Register 0 (EL3)

The TTBR0\_EL3 characteristics are:

## Purpose

Holds the base address of the translation table for the initial lookup for stage 1 of an address translation in the EL3 translation regime, and other information for this translation regime.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TTBR0\_EL3 are UNDEFINED.

## Attributes

TTBR0\_EL3 is a 64-bit register.

## Field descriptions

When FEAT\_D128 is implemented and TCR\_EL3.D128 == '1':

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## BADDR, bits [55:5]

- Bits A[55:x] of the stage 1 translation table base address bits are in register bits[55:x].
- Bits A[(x-1):0] of the stage 1 translation table base address are zero.

Address bit x is the minimum address bit required to align the translation table to the size of the table. x is calculated based on LOG2(StartTableSize), as described in VMSAv9-128. The smallest permitted value of x is 5.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:3]

Reserved, RES0.

## SKL, bits [2:1]

Skip Level associated with translation table walks using TTBR0\_EL3.

This determines the number of levels to be skipped from the regular start level of the stage 1 EL3 translation table walks using TTBR0\_EL3.

| SKL   | Meaning                                    |
|-------|--------------------------------------------|
| 0b00  | Skip 0 level from the regular start level. |

| SKL   | Meaning                                     |
|-------|---------------------------------------------|
| 0b01  | Skip 1 level from the regular start level.  |
| 0b10  | Skip 2 levels from the regular start level. |
| 0b11  | Skip 3 levels from the regular start level. |

## The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

Common not Private. This bit indicates whether each entry that is pointed to by TTBR0\_EL3 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of TTBR0\_EL3.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by TTBR0_EL3, for the current translation regime, are permitted to differ from corresponding entries for TTBR0_EL3 for other PEs in the Inner Shareable domain. This is not affected by the value of TTBR0_EL3.CnP on those other PEs. |
| 0b1   | The translation table entries pointed to by TTBR0_EL3 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of TTBR0_EL3.CnP is 1 and the translation table entries are pointed to by TTBR0_EL3.                   |

This bit is permitted to be cached in a TLB.

<!-- image -->

Note

If the value of the TTBR0\_EL3.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those TTBR0\_EL3s do not point to the same translation table entries the results of translations using TTBR0\_EL3 are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_D128 is not implemented or TCR\_EL3.D128 == '0':

<!-- image -->

Bits [63:48]

Reserved, RES0.

BADDR, bits [47:1]

- Bits A[47:x] of the stage 1 translation table base address bits are in register bits[47:x].

- Bits A[(x-1):0] of the stage 1 translation table base address are zero.

Address bit x is the minimum address bit required to align the translation table to the size of the table. The AArch64 Virtual Memory System Architecture chapter describes how x is calculated based on the value of TCR\_EL3.T0SZ, the translation stage, and the translation granule size.

The BADDR field represents a 52-bit address if any of the following apply:

- The value of TCR\_EL3.PS represents an OA size of 52 bits.
- The Effective value of TCR\_EL3.DS is 1.

When TTBR0\_EL3.BADDR represents a 52-bit addresses, all of the following apply:

- Bits A[51:48] of the stage 1 translation table base address bits are in register bits[5:2].
- Register bit[1] is RES0.
- The smallest permitted value of x is 6.
- When x&gt;6, register bits[(x-1):6] are RES0.

Otherwise, all of the following apply:

- Register bits[(x-1):1] are RES0.
- If 52-bit PA is supported, then bits A[51:48] of the stage 1 translation table base address are treated as 0b0000 .

## Note

If BADDR represents a 52-bit address, and the translation table has fewer than eight entries, the table must be aligned to 64 bytes. Otherwise the translation table must be aligned to the size of the table.

For the 64KB granule, if 52-bit PA is not supported, and the value of TCR\_EL3.PS is 0b110 or 0b111 , one of the following IMPLEMENTATION DEFINED behaviors occur:

- BADDRuses the extended format to represent a 52-bit base address.
- BADDRdoes not use the extended format.

When the value of ID\_AA64MMFR0\_EL1.PARange indicates that the implementation supports a 56 bit PA size, bits A[55:52] of the stage 1 translation table base address are zero.

If any register bit[47:1] that is defined as RES0 has the value 1 when a translation table walk is done using TTBR0\_EL3, then the translation table base address might be misaligned, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Bits A[(x-1):0] of the stage 1 translation table base address are treated as if all the bits are zero. The value read back from the corresponding register bits is either the value written to the register or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

## When FEAT\_TTCNP is implemented:

Common not Private. This bit indicates whether each entry that is pointed to by TTBR0\_EL3 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of TTBR0\_EL3.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by TTBR0_EL3, for the current translation regime, are permitted to differ from corresponding entries for TTBR0_EL3 for other PEs in the Inner Shareable domain. This is not affected by the value of TTBR0_EL3.CnP on those other PEs. |
| 0b1   | The translation table entries pointed to by TTBR0_EL3 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of TTBR0_EL3.CnP is 1 and the translation table entries are pointed to by TTBR0_EL3.                   |

This bit is permitted to be cached in a TLB.

Note

If the value of the TTBR0\_EL3.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those TTBR0\_EL3s do not point to the same translation table entries the results of translations using TTBR0\_EL3 are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TTBR0\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0000 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = TTBR0_EL3;
```

MSR TTBR0\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0000 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.TTBR0_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else TTBR0_EL3 = X[t, 64];
```