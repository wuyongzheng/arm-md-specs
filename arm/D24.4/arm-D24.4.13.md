## D24.4.13 TRCAUTHSTATUS, Trace Authentication Status Register

The TRCAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

For additional information, see the CoreSight Architecture Specification.

## Configuration

AArch64 System register TRCAUTHSTATUS bits [31:0] are architecturally mapped to External register TRCAUTHSTATUS[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCAUTHSTATUS are UNDEFINED.

## Attributes

TRCAUTHSTATUS is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:28]

Reserved, RES0.

## RTNID, bits [27:26]

Root non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RTNID.

## RTID, bits [25:24]

Root invasive debug.

## Bits [23:16]

Reserved, RES0.

## RLNID, bits [15:14]

Realm non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RLNID.

| RTID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

## RLID, bits [13:12]

Realm invasive debug.

## HNID, bits [11:10]

Hyp Non-invasive Debug. Indicates whether a separate enable control for EL2 non-invasive debug features is implemented and enabled.

| HNID   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b00   | Separate Hyp non-invasive debug enable not implemented, or EL2 non-invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                                                                                   |
| 0b11   | Implemented and enabled.                                                                                    |

All other values are reserved.

This field reads as 0b00 .

## HID, bits [9:8]

Hyp Invasive Debug. Indicates whether a separate enable control for EL2 invasive debug features is implemented and enabled.

| HID   | Meaning                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------|
| 0b00  | Separate Hyp invasive debug enable not implemented, or EL2 invasive debug features not implemented. |
| 0b10  | Implemented and disabled.                                                                           |
| 0b11  | Implemented and enabled.                                                                            |

All other values are reserved.

This field reads as 0b00 .

## SNID, bits [7:6]

Secure Non-invasive Debug. Indicates whether Secure non-invasive debug features are implemented and enabled.

| SNID   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b00   | Secure non-invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                           |

| RLID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

| SNID   | Meaning                  |
|--------|--------------------------|
| 0b11   | Implemented and enabled. |

All other values are reserved.

When Secure state is implemented, this field reads as 0b10 or 0b11 depending whether Secure non-invasive debug is enabled.

When Secure state is not implemented, this field reads as 0b00 .

## SID, bits [5:4]

Secure Invasive Debug. Indicates whether Secure invasive debug features are implemented and enabled.

| SID   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b00  | Secure invasive debug features not implemented. |
| 0b10  | Implemented and disabled.                       |
| 0b11  | Implemented and enabled.                        |

All other values are reserved.

This field reads as 0b00 .

## NSNID, bits [3:2]

Non-secure Non-invasive Debug. Indicates whether Non-secure non-invasive debug features are implemented and enabled.

| NSNID   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b00    | Non-secure non-invasive debug features not implemented. |
| 0b10    | Implemented and disabled.                               |
| 0b11    | Implemented and enabled.                                |

All other values are reserved.

When Non-secure state is implemented, this field reads as 0b11 .

When Non-secure state is not implemented, this field reads as 0b00 .

## NSID, bits [1:0]

Non-secure Invasive Debug. Indicates whether Non-secure invasive debug features are implemented and enabled.

| NSID   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b00   | Non-secure invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                           |

| NSID   | Meaning                  |
|--------|--------------------------|
| 0b11   | Implemented and enabled. |

All other values are reserved.

This field reads as 0b00 .

## Accessing TRCAUTHSTATUS

For implementations that support multiple access mechanisms, different access mechanisms can return different values for reads of TRCAUTHSTATUS if the authentication signals have changed and that change has not yet been synchronized by a Context synchronization event. This scenario can happen if, for example, the external debugger view is implemented separately from the system instruction view to allow for separate power domains, and so observes changes on the signals differently.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCAUTHSTATUS

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1110 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCAUTHSTATUS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCAUTHSTATUS; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

```
else X[t, 64] = TRCAUTHSTATUS; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCAUTHSTATUS;
```
