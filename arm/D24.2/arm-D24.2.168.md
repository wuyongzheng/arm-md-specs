## D24.2.168 S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;, IMPLEMENTATION DEFINED Registers

The S3\_&lt;op1&gt; &lt;Cn&gt; &lt;Cm&gt;\_&lt;op2&gt; characteristics are:

## Purpose

This area of the instruction set space is reserved for IMPLEMENTATION DEFINED registers.

## Configuration

When FEAT\_SYSREG128 is implemented, each register in this space is a 128-bit register that can also be accessed as a 64-bit value. If it is accessed as a 64-bit register, accesses read and write bits [63:0] and do not modify bits [127:64].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt; are UNDEFINED.

## Attributes

<!-- formula-not-decoded -->

- 128-bit register when FEAT\_SYSREG128 is implemented.
- 64-bit register otherwise.

## Field descriptions

## When FEAT\_SYSREG128 is implemented:

| 127                    | 96                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 95                     | 64                     |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 63                     | 32                     |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [127:0]

IMPLEMENTATION DEFINED.

## Otherwise:

<!-- image -->

| 63                     | 32   |
|------------------------|------|
| IMPLEMENTATION DEFINED |      |
| 31                     | 0    |
| IMPLEMENTATION DEFINED |      |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Accessing S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, S3\_&lt;op1&gt;\_C&lt;Cn&gt;\_C&lt;Cm&gt;\_&lt;op2&gt;

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b11  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysRegRead(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysRegRead(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL2 then AArch64.ImpDefSysRegRead(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL3 then AArch64.ImpDefSysRegRead(op0, op1, CRn, CRm, op2, t);
```

MSR S3\_&lt;op1&gt;\_C&lt;Cn&gt;\_C&lt;Cm&gt;\_&lt;op2&gt;, &lt;Xt&gt;

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b11  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysRegWrite(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysRegWrite(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL2 then AArch64.ImpDefSysRegWrite(op0, op1, CRn, CRm, op2, t);
```

```
elsif PSTATE.EL == EL3 then AArch64.ImpDefSysRegWrite(op0, op1, CRn, CRm, op2, t);
```

When FEAT\_SYSREG128 is implemented MRRS &lt;Xt&gt;, &lt;Xt+1&gt;, S3\_&lt;op1&gt;\_C&lt;Cn&gt;\_C&lt;Cm&gt;\_&lt;op2&gt;

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b11  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.SystemAccessTrap(EL1, 0x14); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif !ELIsInHost(EL0) && (!IsSCTLR2EL1Enabled() || SCTLR2_EL1.EnIDCP128 == '0') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.SystemAccessTrap(EL1, 0x14); elsif ELIsInHost(EL0) && (!IsSCTLR2EL2Enabled() || SCTLR2_EL2.EnIDCP128 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && !ELIsInHost(EL0) && (!IsHCRXEL2Enabled() || HCRX_EL2.EnIDCP128 == '0') ↪ → then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else AArch64.ImpDefSysRegRead128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.EnIDCP128 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else AArch64.ImpDefSysRegRead128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else
```

```
AArch64.ImpDefSysRegRead128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL3 then AArch64.ImpDefSysRegRead128(op0, op1, CRn, CRm, op2, t, t2);
```

When FEAT\_SYSREG128 is implemented MSRR S3\_&lt;op1&gt;\_C&lt;Cn&gt;\_C&lt;Cm&gt;\_&lt;op2&gt;, &lt;Xt&gt;, &lt;Xt+1&gt;

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b11  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.SystemAccessTrap(EL1, 0x14); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif !ELIsInHost(EL0) && (!IsSCTLR2EL1Enabled() || SCTLR2_EL1.EnIDCP128 == '0') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.SystemAccessTrap(EL1, 0x14); elsif ELIsInHost(EL0) && (!IsSCTLR2EL2Enabled() || SCTLR2_EL2.EnIDCP128 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && !ELIsInHost(EL0) && (!IsHCRXEL2Enabled() || HCRX_EL2.EnIDCP128 == '0') ↪ → then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else AArch64.ImpDefSysRegWrite128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.EnIDCP128 == '0') then AArch64.SystemAccessTrap(EL2, 0x14); elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14); else AArch64.ImpDefSysRegWrite128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnIDCP128 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnIDCP128 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x14);
```

```
else t2);
```

```
AArch64.ImpDefSysRegWrite128(op0, op1, CRn, CRm, op2, t, elsif PSTATE.EL == EL3 then AArch64.ImpDefSysRegWrite128(op0, op1, CRn, CRm, op2, t, t2);
```