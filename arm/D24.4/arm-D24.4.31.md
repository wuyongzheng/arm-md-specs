## D24.4.31 TRCIDR0, Trace ID Register 0

The TRCIDR0 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR0 bits [31:0] are architecturally mapped to External register TRCIDR0[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR0 are UNDEFINED.

## Attributes

TRCIDR0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:31]

Reserved, RES0.

## COMMTRANS,bit [30]

Transaction Start element behavior.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| COMMTRANS   | Meaning                                         |
|-------------|-------------------------------------------------|
| 0b0         | Transaction Start elements are P0 elements.     |
| 0b1         | Transaction Start elements are not P0 elements. |

Access to this field is RO.

## COMMOPT,bit [29]

Indicates the contents and encodings of Cycle count packets.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## ITE, bit [22]

Indicates whether Instrumentation Trace is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| COMMOPT   | Meaning        |
|-----------|----------------|
| 0b0       | Commit mode 0. |
| 0b1       | Commit mode 1. |

The Commit mode defines the contents and encodings of Cycle Count packets, in particular how Commit elements are indicated by these packets. See the descriptions of these packets for more details.

Accessing this field has the following behavior:

- Access to this field is RAO/WI if all of the following are true:
- TRCIDR0.TRCCCI == '1'
- UInt(TRCIDR8.MAXSPEC) == 0x0
- When TRCIDR0.TRCCCI == '0', access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## TSSIZE, bits [28:24]

Indicates that the trace unit implements Global timestamping and the size of the timestamp value.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TSSIZE   | Meaning                                                        |
|----------|----------------------------------------------------------------|
| 0b00000  | Global timestamping not implemented.                           |
| 0b01000  | Global timestamping implemented with a 64-bit timestamp value. |

All other values are reserved.

This field reads as 0b01000 .

Access to this field is RO.

## TSMARK,bit [23]

Indicates whether Timestamp Marker elements are generated.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TSMARK   | Meaning                                      |
|----------|----------------------------------------------|
| 0b0      | Timestamp Marker elements are not generated. |
| 0b1      | Timestamp Marker elements are generated.     |

| ITE   | Meaning                                |
|-------|----------------------------------------|
| 0b0   | Instrumentation Trace not implemented. |
| 0b1   | Instrumentation Trace implemented.     |

This field has the value 1 if FEAT\_ITE is implemented.

Access to this field is RO.

## Bits [21:18]

Reserved, RES0.

## TRCEXDATA, bit [17]

## When TRCIDR0.TRCDATA != '00':

Indicates if the trace unit implements tracing of data transfers for exceptions and exception returns. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCEXDATA   | Meaning                                                                         |
|-------------|---------------------------------------------------------------------------------|
| 0b0         | Tracing of data transfers for exceptions and exception returns not implemented. |
| 0b1         | Tracing of data transfers for exceptions and exception returns implemented.     |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## QSUPP, bits [16:15]

Indicates that the trace unit implements Q element support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| QSUPP   | Meaning                                                                                  |
|---------|------------------------------------------------------------------------------------------|
| 0b00    | Qelement support is not implemented.                                                     |
| 0b01    | Qelement support is implemented, and only supports Qelements with instruction counts.    |
| 0b10    | Qelement support is implemented, and only supports Qelements without instruction counts. |
| 0b11    | Qelement support is implemented, and supports:                                           |
|         | • Qelements with instruction counts. • Qelements without instruction counts.             |

Access to this field is RO.

## QFILT, bit [14]

Indicates if the trace unit implements Q element filtering.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| QFILT   | Meaning                                |
|---------|----------------------------------------|
| 0b0     | Qelement filtering is not implemented. |
| 0b1     | Qelement filtering is implemented.     |

If TRCIDR0.QSUPP == 0b00 then this field is 0.

Access to this field is RO.

## CONDTYPE, bits [13:12]

## When TRCIDR0.TRCCOND == '1':

Indicates how conditional instructions are traced. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CONDTYPE   | Meaning                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------|
| 0b00       | Conditional instructions are traced with an indication of whether they pass or fail their condition code check. |
| 0b01       | Conditional instructions are traced with an indication of the APSR condition flags.                             |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## NUMEVENT,bits [11:10]

## When TRCIDR4.NUMRSPAIR == '0000':

Indicates the number of ETEEvents implemented.

| NUMEVENT   | Meaning                              |
|------------|--------------------------------------|
| 0b00       | The trace unit supports 0 ETEEvents. |

All other values are reserved.

Access to this field is RO.

## When TRCIDR4.NUMRSPAIR != '0000':

Indicates the number of ETEEvents implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMEVENT   | Meaning                              |
|------------|--------------------------------------|
| 0b00       | The trace unit supports 1 ETEEvent.  |
| 0b01       | The trace unit supports 2 ETEEvents. |
| 0b10       | The trace unit supports 3 ETEEvents. |
| 0b11       | The trace unit supports 4 ETEEvents. |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## RETSTACK, bit [9]

Indicates if the trace unit supports the return stack.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RETSTACK   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Return stack not implemented. |
| 0b1        | Return stack implemented.     |

Access to this field is RO.

## Bit [8]

Reserved, RES0.

## TRCCCI, bit [7]

Indicates if the trace unit implements cycle counting.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCCCI   | Meaning                         |
|----------|---------------------------------|
| 0b0      | Cycle counting not implemented. |
| 0b1      | Cycle counting implemented.     |

This field reads as 1.

Access to this field is RO.

## TRCCOND,bit [6]

Indicates if the trace unit implements conditional instruction tracing. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCCOND   | Meaning                                          |
|-----------|--------------------------------------------------|
| 0b0       | Conditional instruction tracing not implemented. |
| 0b1       | Conditional instruction tracing implemented.     |

This field reads as 0.

Access to this field is RO.

## TRCBB, bit [5]

Indicates if the trace unit implements branch broadcasting.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCBB   | Meaning                              |
|---------|--------------------------------------|
| 0b0     | Branch broadcasting not implemented. |
| 0b1     | Branch broadcasting implemented.     |

This field reads as 1.

Access to this field is RO.

## TRCDATA, bits [4:3]

Indicates if the trace unit implements data tracing. Data tracing is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCDATA   | Meaning                       |
|-----------|-------------------------------|
| 0b00      | Data tracing not implemented. |
| 0b11      | Data tracing implemented.     |

All other values are reserved.

This field reads as 0b00 .

Access to this field is RO.

## INSTP0, bits [2:1]

Indicates if load and store instructions are P0 instructions. Load and store instructions as P0 instructions is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| INSTP0   | Meaning                                              |
|----------|------------------------------------------------------|
| 0b00     | Load and store instructions are not P0 instructions. |
| 0b11     | Load and store instructions are P0 instructions.     |

All other values are reserved.

When FEAT\_ETE is implemented, the only permitted value is 0b00 .

Access to this field is RO.

## Bit [0]

Reserved, RES1.

## Accessing TRCIDR0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR0;
```
