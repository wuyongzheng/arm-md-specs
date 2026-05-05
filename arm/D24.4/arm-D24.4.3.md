## D24.4.3 TRBLIMITR\_EL1, Trace Buffer Limit Address Register

The TRBLIMITR\_EL1 characteristics are:

## Purpose

Defines the top address for the trace buffer, and controls the trace buffer modes and enable.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBLIMITR\_EL1 bits [63:0] are architecturally mapped to External register TRBLIMITR\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBLIMITR\_EL1 are UNDEFINED.

## Attributes

TRBLIMITR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## LIMIT, bits [63:12]

Trace Buffer Limit pointer address. (TRBLIMITR\_EL1.LIMIT « 12) is the address of the last byte in the trace buffer plus one. Bits [11:0] of the Limit pointer address are always zero. If the smallest implemented translation granule is not 4KB, then TRBLIMITR\_EL1[N-1:12] are RES0, where N is the IMPLEMENTATION DEFINED value Log2(smallest implemented translation granule).

The reset behavior of this field is:

· On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:7]

Reserved, RES0.

## XE, bit [6]

## When FEAT\_TRBE\_EXT is implemented:

Trace Buffer Unit External mode enable. Used for save/restore of TRBLIMITR\_EL1.XE.

| XE   | Meaning                                                                 |
|------|-------------------------------------------------------------------------|
| 0b0  | Trace Buffer Unit is not enabled by this control.                       |
| 0b1  | If SelfHostedTraceEnabled() is FALSE, the Trace Buffer Unit is enabled. |

Software must treat this field as UNK/SBZP when the OS Lock is unlocked.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When !OSLockStatus(), access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## nVM, bit [5]

Address mode.

| nVM   | Meaning                                                                                                                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The trace buffer pointers are virtual addresses.                                                                                                                                                                                       |
| 0b1   | The trace buffer pointers are:                                                                                                                                                                                                         |
|       | • Physical address in the owning security state if the owning translation regime has no stage 2 translation. • Intermediate physical addresses in the owning security state if the owning translation regime has stage 2 translations. |

If FEAT\_TRBE\_EXT is implemented and SelfHostedTraceEnabled() == FALSE, then the PE ignores the value of this field and the trace buffer pointers are always physical addresses.

If FEAT\_TRBEv1p1 is implemented, SelfHostedTraceEnabled() == TRUE, and the Effective value of TRFCR\_EL2.DnVM is 1, then the PE ignores the value of this field, and the trace buffer pointers are always virtual addresses.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES1 if all of the following are true:
- FEAT\_TRBE\_EXT is implemented
- !SelfHostedTraceEnabled()
- Otherwise, access to this field is RW.

## TM, bits [4:3]

Trigger mode.

| TM   | Meaning                                                                                       |
|------|-----------------------------------------------------------------------------------------------|
| 0b00 | Stop on trigger. Flush then stop collection and raise maintenance interrupt on Trigger Event. |
| 0b01 | IRQ on trigger. Continue collection and raise maintenance interrupt on Trigger Event.         |
| 0b11 | Ignore trigger. Continue collection and do not raise maintenance interrupt on Trigger Event.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## FM, bits [2:1]

Trace buffer mode.

| FM   | Meaning                                                                                                         |
|------|-----------------------------------------------------------------------------------------------------------------|
| 0b00 | Fill mode. Stop collection and raise maintenance interrupt on current write pointer wrap.                       |
| 0b01 | Wrap mode. Continue collection and raise maintenance interrupt on current write pointer wrap.                   |
| 0b11 | Circular Buffer mode. Continue collection and do not raise maintenance interrupt on current write pointer wrap. |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Trace Buffer Unit enable. Controls whether the Trace Buffer Unit is enabled when SelfHostedTraceEnabled() == TRUE.

| E   | Meaning                                                                |
|-----|------------------------------------------------------------------------|
| 0b0 | Trace Buffer Unit is not enabled by this control.                      |
| 0b1 | If SelfHostedTraceEnabled() is TRUE, the Trace Buffer Unit is enabled. |

If FEAT\_TRBE\_EXT is implemented and SelfHostedTraceEnabled() == FALSE, then

TRBLIMITR\_EL1.XE controls whether the Trace Buffer Unit is enabled.

If FEAT\_TRBE\_EXT is not implemented, then the Trace Buffer Unit is disabled when SelfHostedTraceEnabled() == FALSE.

All output is discarded by the Trace Buffer Unit when the Trace Buffer Unit is disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRBLIMITR\_EL1

The PE might ignore a write to TRBLIMITR\_EL1 if all the following are true:

- TRBLIMITR\_EL1.E == 0b1 .
- Either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- The write does not set TRBLIMITR\_EL1.E to 0.

If FEAT\_TRBE\_EXT is implemented, the PE might ignore a write to TRBLIMITR\_EL1 if all the following are true:

- TRBLIMITR\_EL1.XE == 0b1 .
- The Trace Buffer Unit is using External mode.
- The write does not set TRBLIMITR\_EL1.XE to 0.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBLIMITR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBLIMITR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBLIMITR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBLIMITR_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBLIMITR_EL1;
```

MSR TRBLIMITR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b000 |

```
UNDEFINED; elsif PSTATE.EL == EL0 then
```

```
UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBLIMITR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBLIMITR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBLIMITR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBLIMITR_EL1 = X[t, 64];
```
