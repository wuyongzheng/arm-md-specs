## D24.4.7 TRBSR\_EL1, Trace Buffer Status/syndrome Register (EL1)

The TRBSR\_EL1 characteristics are:

## Purpose

Provides syndrome information to software for a trace buffer management event.

## Configuration

AArch64 System register TRBSR\_EL1 bits [63:0] are architecturally mapped to External register TRBSR\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBSR\_EL1 are UNDEFINED.

## Attributes

TRBSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## MSS2, bits [55:32]

Management event Specific Syndrome 2. Contains syndrome specific to the management event.

The syndrome contents for each management event are described in the following sections.

MSS2 encoding for other trace buffer management events

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer

<!-- image -->

## Bits [23:9]

Reserved, RES0.

## TopLevel, bit [8]

## When FEAT\_THE is implemented:

TopLevel. Indicates if the fault was due to TopLevel.

| TopLevel   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Fault is not due to TopLevel. |
| 0b1        | Fault is due to TopLevel.     |

## Otherwise:

Reserved, RES0.

## AssuredOnly, bit [7]

## When FEAT\_THE is implemented, TRBSR\_EL1.EC == '100101', and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

## Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

## DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

DirtyBit flag. If a write access to memory generates a Data Abort for a Permission fault using Indirect Permission, then this field holds information about the fault.

| DirtyBit   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0        | Permission Fault is not due to dirty state. |
| 0b1        | Permission Fault is due to dirty state.     |

## Otherwise:

Reserved, RES0.

## Bits [4:0]

Reserved, RES0.

MSS2 encoding for Granule Protection Check faults on write to trace buffer

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for trace buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED.

## EC, bits [31:26]

Event class. Top-level description of the cause of the trace buffer management event.

| EC       | Meaning                                                                                                                                                                                                                                                                                                                                                                                                             | MSS                                                                                | MSS2                                                                                 | Applies when            |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------|
| 0b000000 | Other trace buffer management event. All trace buffer management events other than those described by the other defined Event class codes.                                                                                                                                                                                                                                                                          | MSSencoding for other trace buffer management events                               | MSS2 encoding for other trace buffer management events                               |                         |
| 0b011110 | Granule Protection Check fault on write to trace buffer, other than Granule Protection Fault (GPF). That is, any of the following: • Granule Protection Table (GPT) address size fault. • GPT walk fault. • Synchronous External abort on GPT fetch. AGPFontranslation table walk or update is reported as either a Stage 1 or Stage 2 Data Abort, as appropriate. Other GPFs are reported as a Stage 1 Data Abort. | MSSencoding for Granule Protection Check faults on write to trace buffer           | MSS2 encoding for Granule Protection Check faults on write to trace buffer           | FEAT_RME is implemented |
| 0b011111 | Trace buffer management event for an IMPLEMENTATION DEFINED reason.                                                                                                                                                                                                                                                                                                                                                 | MSSencoding for trace buffer management event for an IMPLEMENTATION DEFINED reason | MSS2 encoding for trace buffer management event for an IMPLEMENTATION DEFINED reason |                         |
| 0b100100 | Stage 1 Data Abort on write to trace buffer.                                                                                                                                                                                                                                                                                                                                                                        | MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer            |                         |
| 0b100101 | Stage 2 Data Abort on write to trace buffer.                                                                                                                                                                                                                                                                                                                                                                        | MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer            |                         |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:24]

Reserved, RES0.

## Bit [23]

## When FEAT\_TRBE\_EXT is implemented:

Reserved, UNKNOWN.

## Otherwise:

Reserved, RES0.

## IRQ, bit [22]

Maintenance status. Indicates that a trace buffer management event has been recorded.

| IRQ   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | No trace buffer management event for EL1 has been recorded. |
| 0b1   | Atrace buffer management event for EL1 has been recorded.   |

When FEAT\_TRBE\_EXC is implemented, this field indicates a management event for EL1.

If FEAT\_TRBE\_EXC is implemented and the TRBE Profiling exception for EL1 is enabled, then when this field is 1, a TRBE Profiling exception for EL1 is pending

If FEAT\_TRBE\_EXC is not implemented or the TRBE Profiling exception for EL1 is disabled, then this field drives the TRBIRQ trace buffer interrupt request signal.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## TRG, bit [21]

Triggered.

| TRG   | Meaning                                                                          |
|-------|----------------------------------------------------------------------------------|
| 0b0   | No Detected Trigger has been observed since this field was last cleared to zero. |
| 0b1   | ADetected Trigger has been observed since this field was last cleared to zero.   |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## WRAP, bit [20]

Wrapped.

| WRAP   | Meaning                                                                              |
|--------|--------------------------------------------------------------------------------------|
| 0b0    | The current write pointer has not wrapped since this field was last cleared to zero. |
| 0b1    | The current write pointer has wrapped since this field was last cleared to zero.     |

For each byte of trace the Trace Buffer Unit Accepts and writes to the trace buffer at the address in the current write pointer, if the current write pointer is equal to the Limit pointer minus one, the current write pointer is wrapped by setting it to the Base pointer, and this field is set to 1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [19]

Reserved, RES0.

## EA, bit [18]

## When Armv9.3:

Reserved, RES0.

## When the PE sets this bit as the result of an External abort:

External Abort.

| EA   | Meaning                                                                    |
|------|----------------------------------------------------------------------------|
| 0b0  | An External abort has not been asserted.                                   |
| 0b1  | An External abort has been asserted and detected by the Trace Buffer Unit. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S, bit [17]

Stopped.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [16]

Reserved, RES0.

## MSS, bits [15:0]

Management Event Specific Syndrome. Contains syndrome specific to the trace buffer management event.

The syndrome contents for each trace buffer management event are described in the following sections.

MSSencoding for other trace buffer management events

<!-- image -->

## Bits [15:6]

Reserved, RES0.

| S   | Meaning                          |
|-----|----------------------------------|
| 0b0 | Collection has not been stopped. |
| 0b1 | Collection is stopped.           |

## BSC, bits [5:0]

Trace buffer status code

| BSC      | Meaning                                                                                                                                       | Applies when                 |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| 0b000000 | Collection not stopped, or access not allowed.                                                                                                |                              |
| 0b000001 | Trace buffer filled. Collection stopped because the current write pointer wrapped to the base pointer and the trace buffer mode is Fill mode. |                              |
| 0b000010 | Trigger Event. Collection stopped because of a Trigger Event. See TRBTRG_EL1 for more information.                                            |                              |
| 0b000011 | Manual Stop. Collection stopped because of a Manual Stop event. See TRBCR.ManStop for more information.                                       | FEAT_TRBE_EXT is implemented |
| 0b000100 | Buffer size. The requested trace buffer size was too large.                                                                                   |                              |

All other values are reserved.

## MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer

<!-- image -->

Bits [15:6]

Reserved, RES0.

FSC, bits [5:0]

Fault status code

| FSC      | Meaning                                                                        | Applies when   |
|----------|--------------------------------------------------------------------------------|----------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register. |                |
| 0b000001 | Address size fault, level 1.                                                   |                |
| 0b000010 | Address size fault, level 2.                                                   |                |
| 0b000011 | Address size fault, level 3.                                                   |                |
| 0b000100 | Translation fault, level 0.                                                    |                |
| 0b000101 | Translation fault, level 1.                                                    |                |
| 0b000110 | Translation fault, level 2.                                                    |                |
| 0b000111 | Translation fault, level 3.                                                    |                |
| 0b001001 | Access flag fault, level 1.                                                    |                |
| 0b001010 | Access flag fault, level 2.                                                    |                |
| 0b001011 | Access flag fault, level 3.                                                    |                |

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b001000 | Access flag fault, level 0.                                                                                                   | FEAT_LPA2 is implemented                                 |
| 0b001100 | Permission fault, level 0.                                                                                                    | FEAT_LPA2 is implemented                                 |
| 0b001101 | Permission fault, level 1.                                                                                                    |                                                          |
| 0b001110 | Permission fault, level 2.                                                                                                    |                                                          |
| 0b001111 | Permission fault, level 3.                                                                                                    |                                                          |
| 0b010000 | Synchronous External abort, not on translation table walk or hardware update of translation table.                            |                                                          |
| 0b010001 | Asynchronous External abort.                                                                                                  |                                                          |
| 0b010010 | Synchronous External abort on translation table walk or hardware update of translation table, level -2.                       | FEAT_D128 is implemented                                 |
| 0b010011 | Synchronous External abort on translation table walk or hardware update of translation table, level -1.                       | FEAT_LPA2 is implemented                                 |
| 0b010100 | Synchronous External abort on translation table walk or hardware update of translation table, level 0.                        |                                                          |
| 0b010101 | Synchronous External abort on translation table walk or hardware update of translation table, level 1.                        |                                                          |
| 0b010110 | Synchronous External abort on translation table walk or hardware update of translation table, level 2.                        |                                                          |
| 0b010111 | Synchronous External abort on translation table walk or hardware update of translation table, level 3.                        |                                                          |
| 0b011011 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level -1. | FEAT_LPA2 is implemented and FEAT_RAS is not implemented |
| 0b100001 | Alignment fault.                                                                                                              |                                                          |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2.                         | FEAT_D128 is implemented and FEAT_RME is implemented     |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1.                         | FEAT_RME is implemented and FEAT_LPA2 is implemented     |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.                          | FEAT_RME is implemented                                  |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.                          | FEAT_RME is implemented                                  |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.                          | FEAT_RME is implemented                                  |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.                          | FEAT_RME is implemented                                  |

| FSC      | Meaning                                                                                          | Applies when               |
|----------|--------------------------------------------------------------------------------------------------|----------------------------|
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table. | FEAT_RME is implemented    |
| 0b101001 | Address size fault, level -1.                                                                    | FEAT_LPA2 is implemented   |
| 0b101010 | Translation fault, level -2.                                                                     | FEAT_D128 is implemented   |
| 0b101011 | Translation fault, level -1.                                                                     | FEAT_LPA2 is implemented   |
| 0b101100 | Address Size fault, level -2.                                                                    | FEAT_D128 is implemented   |
| 0b110000 | TLB conflict abort.                                                                              |                            |
| 0b110001 | Unsupported atomic hardware update fault.                                                        | FEAT_HAFDBS is implemented |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## MSSencoding for Granule Protection Check faults on write to trace buffer

<!-- image -->

## Bits [15:0]

Reserved, RES0.

MSSencoding for trace buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing TRBSR\_EL1

The PE might ignore a write to TRBSR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TRBSR\_EL1 or TRBSR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b011 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} && (EffectiveTRFCR_EL2_EE() != '00' && TRFCR_EL1.EE != '00') ↪ → then X[t, 64] = NVMem[0x860]; elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); elsif EffectiveTRFCR_EL2_EE() != '00' && ELIsInHost(EL2) then X[t, 64] = TRBSR_EL2; else X[t, 64] = TRBSR_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBSR_EL1;
```

MSR TRBSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b011 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} && (EffectiveTRFCR_EL2_EE() != '00' && TRFCR_EL1.EE != '00') ↪ → then NVMem[0x860] = X[t, 64]; elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); elsif EffectiveTRFCR_EL2_EE() != '00' && ELIsInHost(EL2) then TRBSR_EL2 = X[t, 64]; else TRBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBSR_EL1 = X[t, 64];
```

When FEAT\_TRBE\_EXC is implemented and FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRBSR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1011 | 0b011 |

```
UNDEFINED; elsif PSTATE.EL == EL0 then
```

```
UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x860]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && ↪ → EDSCR2.TTA == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBSR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && ↪ → EDSCR2.TTA == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBSR_EL1; else UNDEFINED;
```

When FEAT\_TRBE\_EXC is implemented and FEAT\_VHE is implemented MSR TRBSR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1011 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TRBE_EXC) && IsFeatureImplemented(FEAT_VHE)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x860] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && ↪ → EDSCR2.TTA == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else TRBSR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && ↪ → EDSCR2.TTA == '1' then Halt(DebugHalt_SoftwareAccess); else TRBSR_EL1 = X[t, 64]; else UNDEFINED;
```
