## D24.2.227 ZCR\_EL2, SVE Control Register (EL2)

The ZCR\_EL2 characteristics are:

## Purpose

This register controls aspects of SVE visible at Exception levels EL2, EL1, and EL0.

## Configuration

This register has no effect when EL2 is not enabled in the current Security state, or when FEAT\_SME is implemented and the PE is in Streaming SVE mode.

This register is present only when FEAT\_SVE is implemented. Otherwise, direct accesses to ZCR\_EL2 are UNDEFINED.

## Attributes

ZCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:9]

Reserved, RES0.

## Bits [8:4]

Reserved, RAZ/WI.

## LEN, bits [3:0]

Requests an Effective Non-streaming SVE vector length at EL2 of (LEN+1)*128 bits. This field also defines the Effective Non-streaming SVE vector length at EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

The Non-streaming SVE vector length can be any power of two from 128 bits to 2048 bits inclusive. An implementation can support a subset of the architecturally permitted lengths. An implementation is required to support all lengths that are powers of two, from 128 bits up to its maximum implemented Non-streaming SVE vector length.

When FEAT\_SME is not implemented, or the PE is not in Streaming SVE mode, the Effective SVE vector length (VL) is equal to the Effective Non-streaming SVE vector length.

When FEAT\_SME is implemented and the PE is in Streaming SVE mode, VL is equal to the Effective Streaming SVE vector length. See SMCR\_EL2.

For all purposes other than returning the result of a direct read of ZCR\_EL2, the PE selects the Effective Non-streaming SVE vector length by performing checks in the following order:

1. If EL3 is implemented and the requested length is greater than the Effective length at EL3, then the Effective length at EL3 is used.
2. Otherwise, the Effective length is the highest supported Non-streaming SVE vector length that is less than or equal to the requested length.

An indirect read of ZCR\_EL2.LEN appears to occur in program order relative to a direct write of the same register, without the need for explicit synchronization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ZCR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name ZCR\_EL2 or ZCR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ZCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); else X[t, 64] = ZCR_EL2; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else X[t, 64] = ZCR_EL2;
```

MSR ZCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); else ZCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else ZCR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, ZCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED; elsif CPACR_EL1.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x19); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x1E0]; else X[t, 64] = ZCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED;
```

```
elsif !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); elsif ELIsInHost(EL2) then X[t, 64] = ZCR_EL2; else X[t, 64] = ZCR_EL1; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else X[t, 64] = ZCR_EL1;
```

MSR ZCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED; elsif CPACR_EL1.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x19); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x1E0] = X[t, 64]; else ZCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.EZ == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TZ == '1' then AArch64.SystemAccessTrap(EL2, 0x19); elsif ELIsInHost(EL2) && CPTR_EL2.ZEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x19); elsif HaveEL(EL3) && CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x19); elsif ELIsInHost(EL2) then ZCR_EL2 = X[t, 64];
```

```
else ZCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else ZCR_EL1 = X[t, 64];
```