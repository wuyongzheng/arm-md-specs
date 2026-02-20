## D24.2.44 DCZID\_EL0, Data Cache Zero ID Register

The DCZID\_EL0 characteristics are:

## Purpose

Indicates the block size that is written with byte values of 0 by the DC ZV A (Data Cache Zero by Address) System instruction.

If FEAT\_MTE is implemented, this register indicates the granularity at which the DC GV A and DC GZV A instructions write.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DCZID\_EL0 are UNDEFINED.

## Attributes

DCZID\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## DZP, bit [4]

Data Zero Prohibited. This field indicates whether use of DC ZV A instructions is permitted or prohibited.

If FEAT\_MTE is implemented, this field indicates whether use of the DC GV A and DC GZVA instructions are permitted or prohibited.

| DZP   | Meaning                      |
|-------|------------------------------|
| 0b0   | Instructions are permitted.  |
| 0b1   | Instructions are prohibited. |

The value read from this field is governed by the current Exception level and the values of the following fields:

- The Effective value of HCR\_EL2.TDZ.
- When the Effective value of HCR\_EL2.{E2H, TGE} != '11', SCTLR\_EL1.DZE.
- When the Effective value of HCR\_EL2.{E2H, TGE} == '11', SCTLR\_EL2.DZE.

## BS, bits [3:0]

Log2 of the block size in words written by a DC ZV A instruction. The maximum size supported is 2KB, indicated by value 0b1001 .

If FEAT\_MTE2 is implemented, then this field determines the block size written by a DC GV A or DC GZVA instruction and the minimum size supported is 16 bytes, indicated by value 0b0010 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing DCZID\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DCZID\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0000 | 0b0000 | 0b111 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.DCZID_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = DCZID_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.DCZID_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = DCZID_EL0; elsif PSTATE.EL == EL2 then X[t, 64] = DCZID_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = DCZID_EL0;
```