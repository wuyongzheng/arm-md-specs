## D24.2.184 SMCR\_EL1, SME Control Register (EL1)

The SMCR\_EL1 characteristics are:

## Purpose

This register controls aspects of Streaming SVE that are visible at Exception levels EL1 and EL0.

## Configuration

This register has no effect if the PE is not in Streaming SVE mode.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this register has no effect on execution at EL0.

This register is present only when FEAT\_SME is implemented. Otherwise, direct accesses to SMCR\_EL1 are UNDEFINED.

## Attributes

SMCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## FA64, bit [31]

## When FEAT\_SME\_FA64 is implemented:

Controls whether execution of an A64 instruction at EL1 is considered legal when executed in Streaming SVE mode.

When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, controls whether execution of an A64 instruction at EL0 is considered legal when executed in Streaming SVE mode.

| FA64   | Meaning                                                                                                                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instruction to be treated as legal when executed in Streaming SVE mode.                                                                                                                         |
| 0b1    | This control causes all implemented A64 instructions to be treated as legal when executed in Streaming SVE mode at EL1 and EL0, if they are treated as legal at more privileged Exception levels in the current Security state. |

Arm recommends that portable SME software should not rely on this optional feature, and that operating systems should provide a means to test for compliance with this recommendation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EZT0, bit [30]

## When FEAT\_SME2 is implemented:

Traps execution at EL1 and EL0 of the LDR, LUTI2, LUTI4, MOVT, STR, and ZERO instructions that access the ZT0 register to EL1, or to EL2 when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1.

The exception is reported using ESR\_EL1.EC or ESR\_EL2.EC value 0x1D , with an ISS code of 0x0000004 , at a lower priority than a trap due to PSTATE.SM or PSTATE.ZA.

| EZT0   | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0    | This control causes execution of these instructions at EL1 and EL0 to be trapped. |
| 0b1    | This control does not cause execution of any instruction to be trapped.           |

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

Requests an Effective Streaming SVE vector length (SVL) at EL1 of (LEN+1)*128 bits. This field also defines the Effective Streaming SVE vector length at EL0 when EL2 is not implemented, or EL2 is not enabled in the current Security state, or the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

The Streaming SVE vector length can be any power of two from 128 bits to 2048 bits inclusive. An implementation can support any subset of the architecturally permitted lengths.

When the PE is in Streaming SVE mode, the Effective SVE vector length (VL) is equal to SVL.

When FEAT\_SVE is implemented, and the PE is not in Streaming SVE mode, VL is equal to the Effective Non-streaming SVE vector length. See ZCR\_EL1.

For all purposes other than returning the result of a direct read of SMCR\_EL1, the PE selects the Effective Streaming SVE vector length by performing checks in the following order:

1. If the requested length is less than the minimum implemented Streaming SVE vector length, then the Effective length is the minimum implemented Streaming SVE vector length.
2. If EL2 is implemented and enabled in the current Security state, and the requested length is greater than the Effective length at EL2, then the Effective length at EL2 is used.
3. If EL3 is implemented and the requested length is greater than the Effective length at EL3, then the Effective length at EL3 is used.

4. Otherwise, the Effective length is the highest supported Streaming SVE vector length that is less than or equal to the requested length.

An indirect read of SMCR\_EL1.LEN appears to occur in program order relative to a direct write of the same register, without the need for explicit synchronization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SMCR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name SMCR\_EL1 or SMCR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SMCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SME) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif CPACR_EL1.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x1F0]; else X[t, 64] = SMCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); elsif ELIsInHost(EL2) then X[t, 64] = SMCR_EL2; else X[t, 64] = SMCR_EL1;
```

```
elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SMCR_EL1;
```

MSR SMCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SME) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif CPACR_EL1.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x1F0] = X[t, 64]; else SMCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); elsif ELIsInHost(EL2) then SMCR_EL2 = X[t, 64]; else SMCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else SMCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SMCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SME) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x1F0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SMCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SMCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR SMCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SME) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x1F0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED;
```

```
elsif CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else SMCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else SMCR_EL1 = X[t, 64]; else UNDEFINED;
```