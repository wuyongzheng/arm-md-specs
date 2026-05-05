## D24.4.40 TRCIDR5, Trace ID Register 5

The TRCIDR5 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR5 bits [31:0] are architecturally mapped to External register TRCIDR5[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR5 are UNDEFINED.

## Attributes

TRCIDR5 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## OE, bit [31]

Indicates support for the ETE Trace Output Enable.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OE   | Meaning                                     |
|------|---------------------------------------------|
| 0b0  | ETE Trace Output Enable is not implemented. |
| 0b1  | ETE Trace Output Enable is implemented.     |

When FEAT\_ETEv1p3 is implemented and when any IMPLEMENTATION DEFINED trace output interface is implemented, this field is 1.

Access to this field is RO.

## NUMCNTR,bits [30:28]

Indicates the number of Counters that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0b000 .

Access to this field is RO.

## NUMSEQSTATE, bits [27:25]

Indicates if the Sequencer is implemented and the number of Sequencer states that are implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMSEQSTATE   | Meaning                                |
|---------------|----------------------------------------|
| 0b000         | The Sequencer is not implemented.      |
| 0b100         | Four Sequencer states are implemented. |

All other values are reserved.

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0b000 .

Access to this field is RO.

## Bit [24]

Reserved, RES0.

## LPOVERRIDE, bit [23]

Indicates support for Low-power Override Mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LPOVERRIDE   | Meaning                                                  |
|--------------|----------------------------------------------------------|
| 0b0          | The trace unit does not support Low-power Override Mode. |
| 0b1          | The trace unit supports Low-power Override Mode.         |

Access to this field is RO.

## ATBTRIG, bit [22]

Indicates if the implementation can support ATB triggers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMCNTR        | Meaning                             |
|----------------|-------------------------------------|
| 0b000 .. 0b100 | The number of Counters implemented. |

| ATBTRIG   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0       | The implementation does not support ATB triggers. |
| 0b1       | The implementation supports ATB triggers.         |

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0.

Access to this field is RO.

## TRACEIDSIZE, bits [21:16]

Indicates the trace ID width.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRACEIDSIZE   | Meaning                                          |
|---------------|--------------------------------------------------|
| 0b000000      | The external trace interface is not implemented. |
| 0b000111      | The implementation supports a 7-bit trace ID.    |

All other values are reserved.

Note

AMBAATBrequires a 7-bit trace ID width.

Access to this field is RO.

## Bits [15:12]

Reserved, RES0.

## NUMEXTINSEL, bits [11:9]

Indicates how many External Input Selector resources are implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMEXTINSEL    | Meaning                                                      |
|----------------|--------------------------------------------------------------|
| 0b000 .. 0b100 | The number of External Input Selector resources implemented. |

All other values are reserved.

Access to this field is RO.

## NUMEXTIN, bits [8:0]

Indicates how many External Inputs are implemented.

All other values are reserved.

Access to this field is RO.

## Accessing TRCIDR5

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR5

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1101 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR5; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR5; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18);
```

| NUMEXTIN    | Meaning                     |
|-------------|-----------------------------|
| 0b111111111 | Unified PMUevent selection. |

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR5;
```
