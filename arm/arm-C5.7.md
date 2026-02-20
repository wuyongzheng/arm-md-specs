## C5.7 A64 System instructions for the Branch Record Buffer Extension

This section lists the A64 System instructions for the Branch Record Buffer Extension.

## C5.7.1 BRB IALL, Invalidate the Branch Record Buffer

The BRB IALL characteristics are:

## Purpose

Invalidates all Branch records in the Branch Record Buffer.

## Configuration

This system instruction is present only when FEAT\_BRBE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to BRB IALL are UNDEFINED.

## Attributes

BRBIALL is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing BRB IALL

Rt should be encoded as 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

BRB IALL

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b001 | 0b0111 | 0b0010 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_BRBE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.nBRBIALL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
else BRB_IALL(); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRB_IALL(); elsif PSTATE.EL == EL3 then BRB_IALL();
```

## C5.7.2 BRB INJ, Branch Record Injection into the Branch Record Buffer

The BRB INJ characteristics are:

## Purpose

Injects the Branch Record held in BRBINFINJ\_EL1, BRBSRCINJ\_EL1, and BRBTGTINJ\_EL1 into the Branch Record Buffer.

## Configuration

This system instruction is present only when FEAT\_BRBE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to BRB INJ are UNDEFINED.

## Attributes

BRBINJ is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing BRB INJ

Rt should be encoded as 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

BRB INJ

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b001 | 0b0111 | 0b0010 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_BRBE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.nBRBINJ == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); else BRB_INJ(); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRB_INJ(); elsif PSTATE.EL == EL3 then BRB_INJ();
```