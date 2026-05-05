## D24.4.39 TRCIDR4, Trace ID Register 4

The TRCIDR4 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR4 bits [31:0] are architecturally mapped to External register TRCIDR4[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR4 are UNDEFINED.

## Attributes

TRCIDR4 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMVMIDC,bits [31:28]

Indicates the number of Virtual Context Identifier Comparators that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMVMIDC         | Meaning                                                                      |
|------------------|------------------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Virtual Context Identifier Comparators in this implementation. |

All other values are reserved.

If the PE does not implement EL2 then this field is 0b0000 .

Access to this field is RO.

## NUMCIDC, bits [27:24]

Indicates the number of Context Identifier Comparators that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMCIDC          | Meaning                                                              |
|------------------|----------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Context Identifier Comparators in this implementation. |

All other values are reserved. Access to this field is RO.

## NUMSSCC, bits [23:20]

Indicates the number of Single-shot Comparator Controls that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMSSCC          | Meaning                                                               |
|------------------|-----------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Single-shot Comparator Controls in this implementation. |

All other values are reserved.

Access to this field is RO.

## NUMRSPAIR, bits [19:16]

Indicates the number of resource selector pairs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMRSPAIR        | Meaning                                                                  |
|------------------|--------------------------------------------------------------------------|
| 0b0000           | This implementation has zero resource selector pairs.                    |
| 0b0001 .. 0b1111 | The number of resource selector pairs in this implementation, minus one. |

All other values are reserved.

Access to this field is RO.

## NUMPC,bits [15:12]

Indicates the number of PE Comparator Inputs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMPC            | Meaning                                                    |
|------------------|------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of PE Comparator Inputs in this implementation. |

All other values are reserved.

Access to this field is RO.

## Bits [11:9]

Reserved, RES0.

## SUPPDAC, bit [8]

## When TRCIDR4.NUMACPAIRS != '0000':

Indicates whether data address comparisons are implemented. Data address comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SUPPDAC   | Meaning                                   |
|-----------|-------------------------------------------|
| 0b0       | Data address comparisons not implemented. |
| 0b1       | Data address comparisons implemented.     |

This field reads as 0b0 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## NUMDVC,bits [7:4]

Indicates the number of data value comparators. Data value comparators are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMDVC           | Meaning                                                      |
|------------------|--------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of data value comparators in this implementation. |

All other values are reserved.

This field reads as 0b0000 .

Access to this field is RO.

## NUMACPAIRS, bits [3:0]

Indicates the number of Address Comparator pairs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMACPAIRS       | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Address Comparator pairs in this implementation. |

All other values are reserved.

Access to this field is RO.

## Accessing TRCIDR4

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR4

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1100 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR4; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR4; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR4;
```
