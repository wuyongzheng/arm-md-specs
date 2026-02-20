## C5.10 A64 IMPLEMENTATION DEFINED System instructions

This section lists the A64 IMPLEMENTATION DEFINED System instructions.

## C5.10.1 SYS|SYSL|SYSP S1\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;, IMPLEMENTATION DEFINED System instructions

The SYS|SYSL|SYSP S1\_&lt;op1&gt; &lt;Cn&gt; &lt;Cm&gt;\_&lt;op2&gt; characteristics are:

## Purpose

This area of the System instruction encoding space is reserved for IMPLEMENTATION DEFINED System instructions.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SYS|SYSL|SYSP S1\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt; are UNDEFINED.

## Attributes

SYS|SYSL|SYSP S1\_&lt;op1&gt; &lt;Cn&gt; &lt;Cm&gt;\_&lt;op2&gt; is a:

- 128-bit System instruction when FEAT\_SYSINSTR128 is implemented.
- 64-bit System instruction otherwise.

## Field descriptions

## When FEAT\_SYSINSTR128 is implemented:

| 127                    |                        | 96                     |
|------------------------|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 95                     |                        | 64                     |
| 63                     |                        | 32                     |
| 31                     | 0                      |                        |

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

## Executing SYS|SYSL|SYSP S1\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt;

Accesses to this instruction use the following encodings in the System instruction encoding space:

SYS #&lt;op1&gt;, &lt;Cn&gt;, &lt;Cm&gt;, #&lt;op2&gt;{, &lt;Xt&gt;}

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b01  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysInstr(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysInstr(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL2 then AArch64.ImpDefSysInstr(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL3 then AArch64.ImpDefSysInstr(op0, op1, CRn, CRm, op2, t);
```

SYSL &lt;Xt&gt;, #&lt;op1&gt;, &lt;Cn&gt;, &lt;Cm&gt;, #&lt;op2&gt;

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b01  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysInstrWithResult(op0, op1, CRn, CRm, op2, elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.ImpDefSysInstrWithResult(op0, op1, CRn, CRm, op2, elsif PSTATE.EL == EL2 then AArch64.ImpDefSysInstrWithResult(op0, op1, CRn, CRm, op2, t); elsif PSTATE.EL == EL3 then AArch64.ImpDefSysInstrWithResult(op0, op1, CRn, CRm, op2, t);
```

```
t); t);
```

When FEAT\_SYSINSTR128 is implemented SYSP #&lt;op1&gt;, &lt;Cn&gt;, &lt;Cm&gt;, #&lt;op2&gt;{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1      | CRn    | CRm     | op2      |
|-------|----------|--------|---------|----------|
| 0b01  | op1[2:0] | 0b1x11 | Cm[3:0] | op2[2:0] |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.TIDCP == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.SystemAccessTrap(EL1, 0x14); elsif ELIsInHost(EL0) && SCTLR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.ImpDefSysInstr128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TIDCP == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.ImpDefSysInstr128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL2 then AArch64.ImpDefSysInstr128(op0, op1, CRn, CRm, op2, t, t2); elsif PSTATE.EL == EL3 then AArch64.ImpDefSysInstr128(op0, op1, CRn, CRm, op2, t, t2);
```

## Chapter C6 A64 Base Instruction Descriptions

This chapter describes the A64 base instructions.

It contains the following sections:

- About the A64 base instructions.
- Alphabetical list of A64 base instructions.