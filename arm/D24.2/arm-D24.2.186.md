## D24.2.186 SMCR\_EL3, SME Control Register (EL3)

The SMCR\_EL3 characteristics are:

## Purpose

This register controls aspects of Streaming SVE that are visible at all Exception levels.

## Configuration

This register has no effect if the PE is not in Streaming SVE mode.

This register is present only when FEAT\_SME is implemented and EL3 is implemented. Otherwise, direct accesses to SMCR\_EL3 are UNDEFINED.

## Attributes

SMCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## FA64, bit [31]

## When FEAT\_SME\_FA64 is implemented:

Controls whether execution of an A64 instruction is considered legal when executed in Streaming SVE mode.

| FA64   | Meaning                                                                                                           |
|--------|-------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instruction to be treated as legal when executed in Streaming SVE mode.           |
| 0b1    | This control causes all implemented A64 instructions to be treated as legal when executed in Streaming SVE mode . |

Arm recommends that portable SME software should not rely on this optional feature, and that operating systems should provide a means to test for compliance with this recommendation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EZT0, bit [30]

## When FEAT\_SME2 is implemented:

Traps execution at all Exception levels of the LDR, LUTI2, LUTI4, MOVT, STR, and ZERO instructions that access the ZT0 register to EL3.

The exception is reported using ESR\_EL3.EC value 0x1D , with an ISS code of 0x0000004 , at a lower priority than a trap due to PSTATE.SM or PSTATE.ZA.

| EZT0   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b0    | This control causes execution of these instructions at all Exception levels to be trapped. |
| 0b1    | This control does not cause execution of any instruction to be trapped.                    |

Changes to this field only affect whether instructions that access ZT0 are trapped. They do not affect the contents of ZT0, which remain valid so long as PSTATE.ZA is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [29:9]

Reserved, RES0.

## Bits [8:4]

Reserved, RAZ/WI.

## LEN, bits [3:0]

Requests an Effective Streaming SVE vector length (SVL) at EL3 of (LEN+1)*128 bits.

The Streaming SVE vector length can be any power of two from 128 bits to 2048 bits inclusive. An implementation can support any subset of the architecturally permitted lengths.

When the PE is in Streaming SVE mode, the Effective SVE vector length (VL) is equal to SVL.

When FEAT\_SVE is implemented, and the PE is not in Streaming SVE mode, VL is equal to the Effective Non-streaming SVE vector length. See ZCR\_EL3.

For all purposes other than returning the result of a direct read of SMCR\_EL3, the PE selects the Effective Streaming SVE vector length by performing checks in the following order:

1. If the requested length is less than the minimum implemented Streaming SVE vector length, then the Effective length is the minimum implemented Streaming SVE vector length.
2. Otherwise, the Effective length is the highest supported Streaming SVE vector length that is less than or equal to the requested length.

An indirect read of SMCR\_EL3.LEN appears to occur in program order relative to a direct write of the same register, without the need for explicit synchronization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SMCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SMCR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0010 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_SME) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SMCR_EL3;
```

MSR SMCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0010 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_SME) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else SMCR_EL3 = X[t, 64];
```