## D24.2.155 RCWSMASK\_EL1, Software Read Check Write Instruction Mask (EL1)

The RCWSMASK\_EL1 characteristics are:

## Purpose

Contains the software mask used by RCWS instructions.

## Configuration

RCWSMASK\_EL1is a 128-bit register that can also be accessed as a 64-bit value. If it is accessed as a 64-bit register, accesses read and write bits [63:0] and do not modify bits [127:64].

This register is present only when FEAT\_THE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to RCWSMASK\_EL1 are UNDEFINED.

## Attributes

RCWSMASK\_EL1is a:

- 128-bit register when FEAT\_D128 is implemented.
- 64-bit register otherwise.

## Field descriptions

When FEAT\_D128 is implemented:

RCWSMASK

127

96

RCWSMASK

95

64

RCWSMASK

63

32

RCWSMASK

31

0

## RCWSMASK,bits [127:0]

Software Mask used to decide which bit-fields are writable to the 128-bit Descriptor by RCWS instructions.

If RCWSMASK\_EL1 is indirectly read by 128-bit variants of RCWS instructions:

- The Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[n], except as follows:
- If n &gt;= 17, and n &lt;= 55, the Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[16].
- If n is in {126:125, 120:119, 114, 107:101, 90:56, 1:0}, the Effective value of RCWSMASK[n] is 0.
- If n &gt;= 121, n &lt;= 124, and FEAT\_S1POE is not implemented, the Effective value of RCWSMASK[n] is 0.
- If FEAT\_MEC is not implemented, the Effective value of RCWSMASK bit RCWSMASK\_EL1[108] is 0.

If RCWSMASK\_EL1 is indirectly read by 64-bit variants of RCWS instructions:

- The Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[n], except as follows:
- If n &gt;= 18, and n &lt;= 49, the Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[17].
- If n == 52 and Protection is enabled, the Effective value of RCWSMASK[52] is 0.

RCWSMASK\_EL1register bits {126:125, 120:119, 114, 107:101, 90:64, 49:18, 0} are RES0.

If FEAT\_S1POE is not implemented, RCWSMASK\_EL1 register bits {124:121} are RES0.

If FEAT\_MEC is not implemented, RCWSMASK\_EL1[108] is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

| 63       | 32       |          |
|----------|----------|----------|
| RCWSMASK | RCWSMASK | RCWSMASK |
| 31       | 0        |          |
| RCWSMASK | RCWSMASK | RCWSMASK |

## RCWSMASK,bits [63:0]

Software Mask used to decide which bit-fields are writable to the 64-bit Descriptor by RCWS Instruction.

The Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[n], except as follows

- If n &gt;= 18, and n &lt;= 49, the Effective value of RCWSMASK[n] is the same as RCWSMASK\_EL1[17].
- If n == 52 and Protection is enabled, the Effective value of RCWSMASK[52] is 0.

RCWSMASK\_EL1register bits {49:18, 0} are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing RCWSMASK\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RCWSMASK_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_THE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nRCWSMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
else
```

```
X[t, 64] = RCWSMASK_EL1<63:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = RCWSMASK_EL1<63:0>; elsif PSTATE.EL == EL3 then X[t, 64] = RCWSMASK_EL1<63:0>;
```

MSR RCWSMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_THE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nRCWSMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else RCWSMASK_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else RCWSMASK_EL1<63:0> = X[t, 64]; elsif PSTATE.EL == EL3 then RCWSMASK_EL1<63:0> = X[t, 64];
```

When FEAT\_D128 is implemented MRRS &lt;Xt&gt;, &lt;Xt+1&gt;, RCWSMASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_THE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nRCWSMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else X[t, t2, 128] = RCWSMASK_EL1<127:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else X[t, t2, 128] = RCWSMASK_EL1<127:0>; elsif PSTATE.EL == EL3 then X[t, t2, 128] = RCWSMASK_EL1<127:0>;
```

When FEAT\_D128 is implemented MSRR RCWSMASK\_EL1, &lt;Xt&gt;, &lt;Xt+1&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_THE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nRCWSMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.D128En == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else RCWSMASK_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.RCWMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.D128En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.RCWMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); elsif HaveEL(EL3) && SCR_EL3.D128En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else RCWSMASK_EL1<127:0> = X[t, t2, 128]; elsif PSTATE.EL == EL3 then RCWSMASK_EL1<127:0> = X[t, t2, 128];
```