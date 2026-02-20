## D24.4 Trace registers

This section lists the Trace registers in AArch64.

## D24.4.1 TRBBASER\_EL1, Trace Buffer Base Address Register

The TRBBASER\_EL1 characteristics are:

## Purpose

Defines the base address for the trace buffer.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBBASER\_EL1 bits [63:0] are architecturally mapped to External register TRBBASER\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBBASER\_EL1 are UNDEFINED.

## Attributes

TRBBASER\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## BASE, bits [63:12]

Trace Buffer Base pointer address. (TRBBASER\_EL1.BASE « 12) is the address of the first byte in the trace buffer. Bits [11:0] of the Base pointer address are always zero. If the smallest implemented translation granule is not 4KB, then TRBBASER\_EL1[N-1:12] are RES0, where N is the IMPLEMENTATION DEFINED value Log2(smallest implemented translation granule).

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing TRBBASER\_EL1

The PE might ignore a write to TRBBASER\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBBASER\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBBASER_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1;
```

MSR TRBBASER\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBBASER_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64];
```

## D24.4.2 TRBIDR\_EL1, Trace Buffer ID Register

The TRBIDR\_EL1 characteristics are:

## Purpose

Describes constraints on using the Trace Buffer Unit to software, including whether the Trace Buffer Unit can be programmed at the current Exception level.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBIDR\_EL1 bits [63:0] are architecturally mapped to External register TRBIDR\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBIDR\_EL1 are UNDEFINED.

## Attributes

TRBIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## MaxBuffSize, bits [47:32]

Maximum supported trace buffer size. Reserved for software use.

Reads as 0x0000

The only permitted value is 0x0000 , indicating there is no limit to the maximum buffer size.

Note

Permitted values relate to the values an implementation is permitted to set this field to. A hypervisor might trap accesses to this register and use other values to describe limitations of its virtualization support to a guest operating system, as follows:

- MaxBuffSize bits[8:0] encodes a mantissa value, M .
- MaxBuffSize bits[13:9] encodes an exponent value, E .
- MaxBuffSize bits[15:14] are reserved.

The maximum buffer size, in bytes, is expressed using the following function:

if IsZero(E), then UInt(M:Zeros(12)) else UInt('1':M:Zeros(UInt(E)+11))

For example:

- Avalue of 0x0001 means a maximum buffer size of 4KB.
- Avalue of 0x3FFF means a maximum buffer size of 4092TB.

Access to this field is RO.

## Bits [31:16]

Reserved, RES0.

## MPAM,bits [15:12]

## When FEAT\_TRBE\_EXT is implemented:

FEAT\_MPAMv0p1 or FEAT\_MPAMv1p0 extensions. Indicates Memory Partitioning and Monitoring (MPAM) support in the Trace Buffer Unit when using External mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MPAM   | Meaning                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Trace Buffer External Mode is not implemented or the version of MPAMsupported by this field is not implemented by the PE.    |
| 0b0001 | FEAT_MPAMv0p1 or FEAT_MPAMv1p0 is implemented by the Trace Buffer Unit, using default PARTID and PMGvalues in External mode. |
| 0b0010 | Trace Buffer MPAMextensions implemented, using FEAT_MPAMv0p1 or FEAT_MPAMv1p0.                                               |

When FEAT\_TRBE\_EXT is not implemented by the PE, or if FEAT\_MPAMv0p1 and FEAT\_MPAMv1p0 are not implemented by the PE, the only permitted value is 0b0000 .

When FEAT\_TRBE\_EXT is implemented by the PE, and at least one of FEAT\_MPAMv0p1 and FEAT\_MPAMv1p0 are implemented by the PE, the value 0b0000 is not permitted.

FEAT\_TRBE\_MPAM implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## EA, bits [11:8]

External Abort handling. Describes how the PE manages External aborts on writes made by the Trace Buffer Unit to the trace buffer.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EA     | Meaning                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not described.                                                                                                   |
| 0b0001 | The PE ignores External aborts on writes made by the Trace Buffer Unit.                                          |
| 0b0010 | An External abort on a write made by the Trace Buffer Unit generates an asynchronous SError exception at the PE. |

All other values are reserved.

From Armv9.3, the value 0b0000 is not permitted.

The behavior described by this field does not apply for External aborts on a translation table walk, translation table update, or GPT walk made by the Trace Buffer Unit that are reported as MMU faults using TRBSR\_ELx. For more information, see 'External aborts'.

Access to this field is RO.

## AddrMode, bits [7:6]

Address Modes. Describes the addressing modes available for the trace buffer.

| AddrMode   | Meaning                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------|
| 0b00       | Virtual and physical address modes are supported.                                                     |
| 0b01       | Only virtual address mode is supported.                                                               |
| 0b10       | Reserved for software use under virtualization, to show that only physical address mode is supported. |

Other values are reserved.

If the Effective value of TRFCR\_EL2.DnVM is 1 and the value returned for TRBIDR\_EL1.P is 0, then this field reads as 0b01 . Otherwise, this field reads as 0b00 .

Note

A hypervisor might trap accesses to this register to describe limitations of its virtualization support to a guest operating system.

## F, bit [5]

Flag updates. Describes how address translations performed by the Trace Buffer Unit manage the Access flag and dirty state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F   | Meaning                                                                                                                                                                                                    |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is always disabled for all translation stages.                                                           |
| 0b1 | Hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is controlled in the same way as explicit memory accesses in the trace buffer owning translation regime. |

## Note

If hardware management of the Access flag is disabled for a stage of translation, an access to a Page or Block with the Access flag bit not set in the descriptor will generate an Access Flag fault.

If hardware management of the dirty state is disabled for a stage of translation, an access to a Page or Block will ignore the Dirty Bit Modifier in the descriptor and might generate a Permission fault, depending on the values of the access permission bits in the descriptor.

From Armv9.3, the value 0 is not permitted.

Access to this field is RO.

## P, bit [4]

Programming not allowed. When read at EL3, this field reads as zero. Otherwise, indicates that the trace buffer owning Exception level is a higher Exception level or the trace buffer owning Security state is not the current Security state.

All other values are reserved. Access to this field is RO.

| P   | Meaning                  |
|-----|--------------------------|
| 0b0 | Programming is allowed.  |
| 0b1 | Programming not allowed. |

The value read from this field depends on the current Exception level and the Effective values of MDCR\_EL3.NSTB, MDCR\_EL3.NSTBE, and MDCR\_EL2.E2TB:

- If EL3 is implemented, MDCR\_EL3.NSTB is 0b0x , and either FEAT\_RME is not implemented, or Secure state is implemented and MDCR\_EL3.NSTBE is 0, then this field reads as one from:
- Non-secure EL1 and Non-secure EL2.
- If FEAT\_RME is implemented, Realm EL1 and Realm EL2.
- If Secure EL2 is implemented and enabled, and MDCR\_EL2.E2TB is 0b00 , Secure EL1.
- If EL3 is implemented, MDCR\_EL3.NSTB is 0b1x and either FEAT\_RME is not implemented or MDCR\_EL3.NSTBE is 0, then this field reads as one from:
- If Secure state is implemented, Secure EL1.
- If Secure EL2 is implemented, Secure EL2.
- If EL2 is implemented and MDCR\_EL2.E2TB is 0b00 , Non-secure EL1.
- If FEAT\_RME is implemented, Realm EL1 and Realm EL2.
- If FEAT\_RME is implemented, and MDCR\_EL3.{NSTB, NSTBE} is { 0b1x , 1}, then this field reads as one from:
- Non-secure EL1 and Non-secure EL2.
- If Secure state is implemented, Secure EL1 and Secure EL2.
- If MDCR\_EL2.E2TB is 0b00 , Realm EL1.
- If EL3 is not implemented, EL2 is implemented, and MDCR\_EL2.E2TB is 0b00 , then this field reads as one from EL1.

Otherwise, this field reads as zero.

## Align, bits [3:0]

Defines the minimum alignment constraint for writes to TRBPTR\_EL1 and TRBTRG\_EL1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Align   | Meaning     |
|---------|-------------|
| 0b0000  | Byte.       |
| 0b0001  | Halfword.   |
| 0b0010  | Word.       |
| 0b0011  | Doubleword. |
| 0b0100  | 16 bytes.   |
| 0b0101  | 32 bytes.   |
| 0b0110  | 64 bytes.   |
| 0b0111  | 128 bytes.  |
| 0b1000  | 256 bytes.  |
| 0b1001  | 512 bytes.  |
| 0b1010  | 1KB.        |
| 0b1011  | 2KB.        |

## Accessing TRBIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b111 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBIDR_EL1; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBIDR_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBIDR_EL1;
```

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

## D24.4.4 TRBMAR\_EL1, Trace Buffer Memory Attribute Register

The TRBMAR\_EL1 characteristics are:

## Purpose

Controls Trace Buffer Unit accesses to memory.

If the trace buffer pointers specify virtual addresses, the address properties are defined by the translation tables and this register is ignored.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBMAR\_EL1 bits [63:0] are architecturally mapped to External register TRBMAR\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBMAR\_EL1 are UNDEFINED.

## Attributes

TRBMAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |    |    |    |    |    |    |    |    |    |
|------|----|----|----|----|----|----|----|----|----|
|      | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 31   |    |    |    |    |    |    |    |    |    |
| RES0 |    |    |    |    |    |    |    |    |    |

## Bits [63:12]

Reserved, RES0.

PAS, bits [11:10]

## When FEAT\_TRBE\_EXT is implemented:

Physical address specifier. Defines the PAS attribute for memory addressed by the buffer in External mode.

| PAS   | Meaning     | Applies when               |
|-------|-------------|----------------------------|
| 0b00  | Secure.     | FEAT_Secure is implemented |
| 0b01  | Non-secure. |                            |
| 0b10  | Root.       | FEAT_RME is implemented    |
| 0b11  | Realm.      | FEAT_RME is implemented    |

## All other values are reserved.

If the Trace Buffer Unit is using external mode and either TRBMAR\_EL1.PAS is set to a reserved value, or the IMPLEMENTATION DEFINED authentication interface prohibits invasive debug of the Security state corresponding to the physical address space selected by TRBMAR\_EL1.PAS, then when the Trace Buffer Unit receives trace data from the trace unit, it does not write the trace data to memory and generates a trace buffer management event. That is, if any of the following apply:

- ExternalInvasiveDebugEnabled() == FALSE.
- TRBMAR\_EL1.PAS is 0b00 , and either ExternalSecureInvasiveDebugEnabled() == FALSE or Secure state is not implemented.
- TRBMAR\_EL1.PAS is 0b10 , and either ExternalRootInvasiveDebugEnabled() == FALSE or FEAT\_RME is not implemented.
- TRBMAR\_EL1.PAS is 0b11 , and either ExternalRealmInvasiveDebugEnabled() == FALSE or FEAT\_RME is not implemented.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SH, bits [9:8]

Trace buffer shareability domain. Defines the shareability domain for Normal memory used by the trace buffer.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

All other values are reserved.

This field is ignored when TRBMAR\_EL1.Attr specifies any of the following memory types:

- Any Device memory type.
- Normal memory, Inner Non-cacheable, Outer Non-cacheable.

All Device and Normal Inner Non-cacheable Outer Non-cacheable memory regions are always treated as Outer Shareable.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_TRBE\_EXT is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_TRBE\_EXT is not implemented, this field resets to an architecturally UNKNOWN value.

## Attr, bits [7:0]

Trace buffer memory type and attributes. Defines the memory type and, for Normal memory, the cacheability attributes, for memory addressed by the trace buffer.

The encoding of this field is the same as that of a MAIR\_ELx.Attr&lt;n&gt; field, as follows:

| Attr        | Meaning                                                                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 dd00 | Device memory. See encoding of 'dd' for the type of Device memory.                                                                                     |
| 0b0000 dd01 | If FEAT_XS is implemented: Device memory with the XS attribute set to 0. See encoding of 'dd' for the type of Device memory. Otherwise, UNPREDICTABLE. |

| Attr        |                                                                       | Meaning                                                                                                                                                                                                          |
|-------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 dd1x | 0b0000 dd1x                                                           | UNPREDICTABLE.                                                                                                                                                                                                   |
| 0booooiiii  | where oooo != 0000 and iiii != 0000                                   | Normal memory. See encoding of 'oooo' and 'iiii' for the type of Normal memory.                                                                                                                                  |
| 0b01000000  | 0b01000000                                                            | If FEAT_XS is implemented: Normal Inner Non-cacheable, Outer Non-cacheable memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE.                                                                      |
| 0b10100000  | 0b10100000                                                            | If FEAT_XS is implemented: Normal Inner Write-through Cacheable, Outer Write-through Cacheable, Read-Allocate, No-Write Allocate, Non-transient memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE. |
| 0b11110000  | 0b11110000                                                            | If FEAT_MTE2 is implemented: Tagged Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. Otherwise, UNPREDICTABLE.                                                     |
| 0bxxxx0000  | where xxxx != 0000 and xxxx != 0100 and xxxx != 1010 and xxxx != 1111 | UNPREDICTABLE.                                                                                                                                                                                                   |

dd is encoded as follows:

oooo is encoded as follows:

| 'oooo'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Outer Write-Through Transient.     |
| 0b0100   |              | Normal memory, Outer Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Outer Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Outer Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Outer Write-Back Non-transient.    |

R encodes the Outer Read-Allocate policy and W encodes the Outer Write-Allocate policy.

iiii is encoded as follows:

| 'iiii'   | Meaning                                       |
|----------|-----------------------------------------------|
| 0b0000   | See encoding of Attr.                         |
| 0b00 RW  | Normal memory, Inner Write-Through Transient. |

| 'dd'   | Meaning               |
|--------|-----------------------|
| 0b00   | Device-nGnRnE memory. |
| 0b01   | Device-nGnRE memory.  |
| 0b10   | Device-nGRE memory.   |
| 0b11   | Device-GRE memory.    |

| 'iiii'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0100   |              | Normal memory, Inner Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Inner Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Inner Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Inner Write-Back Non-transient.    |

R encodes the Inner Read-Allocate policy and W encodes the Inner Write-Allocate policy.

In oooo and iiii , R and W are encoded as follows:

| 'R' or 'W'   | Meaning      |
|--------------|--------------|
| 0b0          | No Allocate. |
| 0b1          | Allocate.    |

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_TRBE\_EXT is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_TRBE\_EXT is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing TRBMAR\_EL1

The PE might ignore a write to TRBMAR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRBMAR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b100 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBMAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMAR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMAR_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMAR_EL1;
```

MSR TRBMAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b100 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBMAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBMAR_EL1 = X[t, 64];
```

## D24.4.5 TRBMPAM\_EL1, Trace Buffer MPAM Configuration Register

The TRBMPAM\_EL1 characteristics are:

## Purpose

Defines the PARTID, PMG, and MPAM\_SP values used by the trace buffer unit in external mode.

## Configuration

AArch64 System register TRBMPAM\_EL1 bits [63:0] are architecturally mapped to External register TRBMPAM\_EL1[63:0].

This register is present only when FEAT\_TRBE\_MPAM is implemented. Otherwise, direct accesses to TRBMPAM\_EL1 are UNDEFINED.

## Attributes

TRBMPAM\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:27]

Reserved, RES0.

## EN, bit [26]

Enable. Enables use of non-default MPAM values.

| EN   | Meaning                                 |
|------|-----------------------------------------|
| 0b0  | Use default MPAMvalues.                 |
| 0b1  | Use TRBMPAM_EL1.{PARTID, PMG, MPAM_SP}. |

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## MPAM\_SP, bits [25:24]

Partition Identifier space. Selects the PARTID space.

| MPAM_SP   | Meaning                                   | Applies when               |
|-----------|-------------------------------------------|----------------------------|
| 0b00      | PARTID is in the Secure PARTID space.     | FEAT_Secure is implemented |
| 0b01      | PARTID is in the Non-secure PARTID space. |                            |
| 0b10      | PARTID is in the Root PARTID space.       | FEAT_RME is implemented    |
| 0b11      | PARTID is in the Realm PARTID space.      | FEAT_RME is implemented    |

If the Trace Buffer Unit is using external mode and either TRBMPAM\_EL1.MPAM\_SP is set to reserved value, or the IMPLEMENTATION DEFINED authentication interface prohibits invasive debug of the Security state corresponding to the Partition Identifier space selected by TRBMPAM\_EL1.MPAM\_SP, then when the Trace Buffer Unit receives trace data from the trace unit, it does not write the trace data to memory and generates a trace buffer management event.

The interface prohibits invasive debug of the Security state if any of the following apply:

- ExternalInvasiveDebugEnabled() == FALSE.
- Secure state is implemented, ExternalSecureInvasiveDebugEnabled() == FALSE and TRBMPAM\_EL1.MPAM\_SP is 0b00 .
- FEAT\_RME is implemented, ExternalRootInvasiveDebugEnabled() == FALSE, and TRBMPAM\_EL1.MPAM\_SP is 0b10 .
- FEAT\_RME is implemented, ExternalRealmInvasiveDebugEnabled() == FALSE, and TRBMPAM\_EL1.MPAM\_SP is 0b11 .

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## PMG, bits [23:16]

Performance Monitoring Group. Selects the PMG.

Only sufficient low-order bits are required to represent the TRBDEVID1.PMG\_MAX. Higher-order bits are RES0.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## PARTID, bits [15:0]

Partition Identifier. Selects the PARTID.

Only sufficient low-order bits are required to represent the TRBDEVID1.PARTID\_MAX. Higher-order bits are RES0.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBMPAM\_EL1

The PE might ignore a write to TRBMPAM\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBMPAM\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b101 |

```
if !IsFeatureImplemented(FEAT_TRBE_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRBMPAM_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1;
```

MSR TRBMPAM\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b101 |

```
if !IsFeatureImplemented(FEAT_TRBE_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRBMPAM_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64];
```

## D24.4.6 TRBPTR\_EL1, Trace Buffer Write Pointer Register

The TRBPTR\_EL1 characteristics are:

## Purpose

Defines the current write pointer for the trace buffer.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBPTR\_EL1 bits [63:0] are architecturally mapped to External register TRBPTR\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBPTR\_EL1 are UNDEFINED.

## Attributes

TRBPTR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |     |
|------|------|-----|
| PTR  | PTR  | PTR |
| 31   | 0    |     |
| PTR  | PTR  | PTR |

## PTR, bits [63:0]

Trace Buffer current write pointer address.

Defines the virtual address of the next entry to be written to the trace buffer.

If TRBIDR\_EL1.Align is not zero, then it is IMPLEMENTATION DEFINED whether bits [M-1:0] are RES0 or read/write, where M is an integer between 1 and TRBIDR\_EL1.Align inclusive.

The architecture places restrictions on the values that software can write to the pointer. For more information, see Restrictions on Programming the Trace Buffer Unit.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBPTR\_EL1

The PE might ignore a write to TRBPTR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBPTR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBPTR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBPTR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBPTR_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBPTR_EL1;
```

MSR TRBPTR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBPTR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBPTR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBPTR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBPTR_EL1 = X[t, 64];
```

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

## D24.4.8 TRBSR\_EL2, Trace Buffer Syndrome Register (EL2)

The TRBSR\_EL2 characteristics are:

## Purpose

Provides syndrome information to software for a trace buffer management event.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_TRBE\_EXC is implemented. Otherwise, direct accesses to TRBSR\_EL2 are UNDEFINED.

## Attributes

TRBSR\_EL2 is a 64-bit register.

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

Bits [23:9]

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

## When FEAT\_THE is implemented, TRBSR\_EL2.EC == '100101', and GetTRBSR\_EL2\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetTRBSR\_EL2\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetTRBSR\_EL2\_FSC() IN {'0011xx'}:

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

## Bits [25:23]

Reserved, RES0.

## IRQ, bit [22]

Maintenance status. Indicates that a trace buffer management event has been recorded.

| IRQ   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | No trace buffer management event for EL2 has been recorded. |
| 0b1   | Atrace buffer management event for EL2 has been recorded.   |

When FEAT\_TRBE\_EXC is implemented, this field indicates a management event for EL2.

If the TRBE Profiling exception for EL2 is enabled, then when this field is 1, a TRBE Profiling exception for EL2 is pending

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

Bit [19]

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

| 15   | 6 5   |
|------|-------|
| RES0 | BSC   |

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Trace buffer status code

| S   | Meaning                          |
|-----|----------------------------------|
| 0b0 | Collection has not been stopped. |
| 0b1 | Collection is stopped.           |

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

| FSC      | Meaning                                                                        | Applies when             |
|----------|--------------------------------------------------------------------------------|--------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register. |                          |
| 0b000001 | Address size fault, level 1.                                                   |                          |
| 0b000010 | Address size fault, level 2.                                                   |                          |
| 0b000011 | Address size fault, level 3.                                                   |                          |
| 0b000100 | Translation fault, level 0.                                                    |                          |
| 0b000101 | Translation fault, level 1.                                                    |                          |
| 0b000110 | Translation fault, level 2.                                                    |                          |
| 0b000111 | Translation fault, level 3.                                                    |                          |
| 0b001001 | Access flag fault, level 1.                                                    |                          |
| 0b001010 | Access flag fault, level 2.                                                    |                          |
| 0b001011 | Access flag fault, level 3.                                                    |                          |
| 0b001000 | Access flag fault, level 0.                                                    | FEAT_LPA2 is implemented |
| 0b001100 | Permission fault, level 0.                                                     | FEAT_LPA2 is implemented |
| 0b001101 | Permission fault, level 1.                                                     |                          |
| 0b001110 | Permission fault, level 2.                                                     |                          |

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
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
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.                              | FEAT_RME is implemented                                  |
| 0b101001 | Address size fault, level -1.                                                                                                 | FEAT_LPA2 is implemented                                 |
| 0b101010 | Translation fault, level -2.                                                                                                  | FEAT_D128 is implemented                                 |
| 0b101011 | Translation fault, level -1.                                                                                                  | FEAT_LPA2 is implemented                                 |

| FSC      | Meaning                                   | Applies when               |
|----------|-------------------------------------------|----------------------------|
| 0b101100 | Address Size fault, level -2.             | FEAT_D128 is implemented   |
| 0b110000 | TLB conflict abort.                       |                            |
| 0b110001 | Unsupported atomic hardware update fault. | FEAT_HAFDBS is implemented |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

MSSencoding for Granule Protection Check faults on write to trace buffer

<!-- image -->

## Bits [15:0]

Reserved, RES0.

MSSencoding for trace buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing TRBSR\_EL2

The PE might ignore a write to TRBSR\_EL2 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name TRBSR\_EL2 or TRBSR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBSR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1011 | 0b011 |

```
if !IsFeatureImplemented(FEAT_TRBE_EXC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TRBEE == '00' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TRBEE == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRBSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TRBSR_EL2;
```

MSR TRBSR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1011 | 0b011 |

```
if !IsFeatureImplemented(FEAT_TRBE_EXC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TRBEE == '00' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TRBEE == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
TRBSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TRBSR_EL2 = X[t, 64];
```

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

## D24.4.9 TRBSR\_EL3, Trace Buffer Syndrome Register (EL3)

The TRBSR\_EL3 characteristics are:

## Purpose

Provides syndrome information to software for a trace buffer management event.

## Configuration

This register is present only when FEAT\_TRBE\_EXC is implemented and EL3 is implemented. Otherwise, direct accesses to TRBSR\_EL3 are UNDEFINED.

## Attributes

TRBSR\_EL3 is a 64-bit register.

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

Bits [23:9]

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

## When FEAT\_THE is implemented, TRBSR\_EL3.EC == '100101', and GetTRBSR\_EL3\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetTRBSR\_EL3\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetTRBSR\_EL3\_FSC() IN {'0011xx'}:

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

## Bits [25:23]

Reserved, RES0.

## IRQ, bit [22]

Maintenance status. Indicates that a trace buffer management event has been recorded.

| IRQ   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | No trace buffer management event for EL3 has been recorded. |
| 0b1   | Atrace buffer management event for EL3 has been recorded.   |

When FEAT\_TRBE\_EXC is implemented, this field indicates a management event for EL3.

If the TRBE Profiling exception for EL3 is enabled, then when this field is 1, a TRBE Profiling exception for EL3 is pending

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

Bit [19]

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

| 15   | 6 5   |
|------|-------|
| RES0 | BSC   |

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Trace buffer status code

| S   | Meaning                          |
|-----|----------------------------------|
| 0b0 | Collection has not been stopped. |
| 0b1 | Collection is stopped.           |

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

| FSC      | Meaning                                                                        | Applies when             |
|----------|--------------------------------------------------------------------------------|--------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register. |                          |
| 0b000001 | Address size fault, level 1.                                                   |                          |
| 0b000010 | Address size fault, level 2.                                                   |                          |
| 0b000011 | Address size fault, level 3.                                                   |                          |
| 0b000100 | Translation fault, level 0.                                                    |                          |
| 0b000101 | Translation fault, level 1.                                                    |                          |
| 0b000110 | Translation fault, level 2.                                                    |                          |
| 0b000111 | Translation fault, level 3.                                                    |                          |
| 0b001001 | Access flag fault, level 1.                                                    |                          |
| 0b001010 | Access flag fault, level 2.                                                    |                          |
| 0b001011 | Access flag fault, level 3.                                                    |                          |
| 0b001000 | Access flag fault, level 0.                                                    | FEAT_LPA2 is implemented |
| 0b001100 | Permission fault, level 0.                                                     | FEAT_LPA2 is implemented |
| 0b001101 | Permission fault, level 1.                                                     |                          |
| 0b001110 | Permission fault, level 2.                                                     |                          |

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
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
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.                              | FEAT_RME is implemented                                  |
| 0b101001 | Address size fault, level -1.                                                                                                 | FEAT_LPA2 is implemented                                 |
| 0b101010 | Translation fault, level -2.                                                                                                  | FEAT_D128 is implemented                                 |
| 0b101011 | Translation fault, level -1.                                                                                                  | FEAT_LPA2 is implemented                                 |

| FSC      | Meaning                                   | Applies when               |
|----------|-------------------------------------------|----------------------------|
| 0b101100 | Address Size fault, level -2.             | FEAT_D128 is implemented   |
| 0b110000 | TLB conflict abort.                       |                            |
| 0b110001 | Unsupported atomic hardware update fault. | FEAT_HAFDBS is implemented |

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

## Accessing TRBSR\_EL3

The PE might ignore a write to TRBSR\_EL3 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1001 | 0b1011 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TRBE_EXC) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = TRBSR_EL3;
```

MSR TRBSR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1001 | 0b1011 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TRBE_EXC) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then TRBSR_EL3 = X[t, 64];
```

## D24.4.10 TRBTRG\_EL1, Trace Buffer Trigger Counter Register

The TRBTRG\_EL1 characteristics are:

## Purpose

Specifies the number of bytes of trace to capture following a Detected Trigger before a Trigger Event.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBTRG\_EL1 bits [63:0] are architecturally mapped to External register TRBTRG\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBTRG\_EL1 are UNDEFINED.

## Attributes

TRBTRG\_EL1 is a 64-bit register.

## Field descriptions

RES0

63

32

TRG

31

0

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TRG, bits [31:0]

Trigger count.

Specifies the number of bytes of trace to capture following a Detected Trigger before a Trigger Event.

TRBTRG\_EL1 decrements by 1 for every byte of trace written to the trace buffer when all of the following are true:

- TRBTRG\_EL1 is nonzero.
- TRBSR\_EL1.TRG is 1.

The architecture places restrictions on the values that software can write to the counter.

Note

As a result of the restrictions an implementation might treat some of TRG[M:0] as RES0, where M is defined by TRBIDR\_EL1.Align.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBTRG\_EL1

The PE might ignore a write to TRBTRG\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.

- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBTRG\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b110 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBTRG_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBTRG_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBTRG_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBTRG_EL1;
```

MSR TRBTRG\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b110 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBTRG_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBTRG_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBTRG_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBTRG_EL1 = X[t, 64];
```

## D24.4.11 TRCACATR&lt;n&gt;, Trace Address Comparator Access Type Register &lt;n&gt;, n = 0 - 15

The TRCACATR&lt;n&gt; characteristics are:

## Purpose

Defines the type of access for the corresponding TRCACVR&lt;n&gt; Register. This register configures the context type, Exception levels, alignment, masking that is applied by the Address Comparator, and how the Address Comparator behaves when it is one half of an Address Range Comparator.

## Configuration

AArch64 System register TRCACATR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCACATR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and (UInt(TRCIDR4.NUMACPAIRS) * 2) &gt; n. Otherwise, direct accesses to TRCACATR&lt;n&gt; are UNDEFINED.

## Attributes

TRCACATR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:19]

Reserved, RES0.

EXLEVEL\_RL\_EL2, bit [18]

## When FEAT\_RME is implemented:

Realm EL2 address comparison control. Controls whether a comparison can occur at EL2 in Realm state.

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator performs comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator does not perform comparisons in Realm EL2. |

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator does not perform comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator performs comparisons in Realm EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL1, bit [17]

## When FEAT\_RME is implemented:

Realm EL1 address comparison control. Controls whether a comparison can occur at EL1 in Realm state.

| EXLEVEL_RL_EL1   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator performs comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator does not perform comparisons in Realm EL1. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator does not perform comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator performs comparisons in Realm EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL0, bit [16]

## When FEAT\_RME is implemented:

Realm EL0 address comparison control. Controls whether a comparison can occur at EL0 in Realm state.

| EXLEVEL_RL_EL0   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator performs comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator does not perform comparisons in Realm EL0. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator does not perform comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator performs comparisons in Realm EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [15]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [14]

## When Non-secure EL2 is implemented:

Non-secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Non-secure state.

| EXLEVEL_NS_EL2   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL2.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL1, bit [13]

## When Non-secure EL1 is implemented:

Non-secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Non-secure state.

| EXLEVEL_NS_EL1   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL1.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL0, bit [12]

## When Non-secure EL0 is implemented:

Non-secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Non-secure state.

| EXLEVEL_NS_EL0   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL0.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL3, bit [11]

## When EL3 is implemented:

EL3 address comparison control. Controls whether a comparison can occur at EL3.

| EXLEVEL_S_EL3   | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons at EL3.         |
| 0b1             | The Address Comparator does not perform comparisons at EL3. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL2, bit [10]

## When Secure EL2 is implemented:

Secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Secure state.

| EXLEVEL_S_EL2   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL2.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL1, bit [9]

## When Secure EL1 is implemented:

Secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Secure state.

| EXLEVEL_S_EL1   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL1.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL0, bit [8]

## When Secure EL0 is implemented:

Secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Secure state.

| EXLEVEL_S_EL0   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL0.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [7]

Reserved, RES0.

CONTEXT, bits [6:4]

When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Selects a Context Identifier Comparator or Virtual Context Identifier Comparator:

| CONTEXT   | Meaning       | Applies when                                            |
|-----------|---------------|---------------------------------------------------------|
| 0b000     | Comparator 0. |                                                         |
| 0b001     | Comparator 1. | UInt(TRCIDR4.NUMCIDC) > 1 or UInt(TRCIDR4.NUMVMIDC) > 1 |
| 0b010     | Comparator 2. | UInt(TRCIDR4.NUMCIDC) > 2 or UInt(TRCIDR4.NUMVMIDC) > 2 |
| 0b011     | Comparator 3. | UInt(TRCIDR4.NUMCIDC) > 3 or UInt(TRCIDR4.NUMVMIDC) > 3 |
| 0b100     | Comparator 4. | UInt(TRCIDR4.NUMCIDC) > 4 or UInt(TRCIDR4.NUMVMIDC) > 4 |
| 0b101     | Comparator 5. | UInt(TRCIDR4.NUMCIDC) > 5 or UInt(TRCIDR4.NUMVMIDC) > 5 |
| 0b110     | Comparator 6. | UInt(TRCIDR4.NUMCIDC) > 6 or UInt(TRCIDR4.NUMVMIDC) > 6 |
| 0b111     | Comparator 7. | UInt(TRCIDR4.NUMCIDC) > 7 or UInt(TRCIDR4.NUMVMIDC) > 7 |

The width of this field is dependent on the maximum number of Context Identifier Comparators or Virtual Context Identifier Comparators implemented. Unimplemented bits are RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CONTEXTTYPE, bits [3:2]

## When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Controls whether the Address Comparator is dependent on a Context Identifier Comparator, a Virtual Context Identifier Comparator, or both comparisons.

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                              | Applies when               |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 0b00          | The Address Comparator is not dependent on the Context Identifier Comparators or Virtual Context Identifier Comparators.                                                                                                                             |                            |
| 0b01          | The Address Comparator is dependent on the Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Context Identifier Comparator and the address comparison match.                 | TRCIDR4.NUMCIDC != '0000'  |
| 0b10          | The Address Comparator is dependent on the Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Virtual Context Identifier Comparator and the address comparison match. | TRCIDR4.NUMVMIDC != '0000' |

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                                                                                               | Applies when                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b11          | The Address Comparator is dependent on the Context Identifier Comparator and Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if the Context Identifier Comparator, the Virtual Context Identifier Comparator, and address comparison all match. | TRCIDR4.NUMCIDC != '0000' and TRCIDR4.NUMVMIDC != '0000' |

If TRCIDR4.NUMCIDC == 0b0000 , then bit [2] is RES0.

If TRCIDR4.NUMVMIDC == 0b0000 , then bit [3] is RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [1:0]

Reserved, RES0.

## Accessing TRCACATR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCBBCTLR.RANGE[n/2] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0100 and TRCRSCTLR&lt;a&gt;.SAC[n] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0101 and TRCRSCTLR&lt;a&gt;.ARC[n/2] == 1.
- TRCVIIECTLR.EXCLUDE[n/2] == 1.
- TRCVIIECTLR.INCLUDE[n/2] == 1.
- TRCVISSCTLR.START[n] == 1.
- TRCVISSCTLR.STOP[n] == 1.
- TRCSSCCR&lt;&gt;.ARC[n/2] == 1.
- TRCSSCCR&lt;&gt;.SAC[n] == 1.
- TRCQCTLR.RANGE[n/2] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCACATR<m> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b01 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then
```

```
AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m];
```

MSR TRCACATR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b01 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64];
```

## D24.4.12 TRCACVR&lt;n&gt;, Trace Address Comparator Value Register &lt;n&gt;, n = 0 - 15

The TRCACVR&lt;n&gt; characteristics are:

## Purpose

Contains the address value.

## Configuration

AArch64 System register TRCACVR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCACVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and (UInt(TRCIDR4.NUMACPAIRS) * 2) &gt; n. Otherwise, direct accesses to TRCACVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCACVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDRESS, bits [63:0]

Address Value.

The Address Comparators can support implementations that use multiple address widths. When the trace unit compares the ADDRESS field with an address that has a width less than this field, then the address must be zero-extended to the ADDRESS field width. The trace unit then compares all implemented bits. For example, in a system that supports both 32-bit and 64-bit addresses, when the PE is in AArch32 state the comparator must zero-extend the 32-bit address and compare against the full 64 bits that are stored in TRCACVR.ADDRESS. This requires that the trace analyzer always programs all implemented bits of TRCACVR.ADDRESS.

The result of writing a value other than all zeros or all ones to ADDRESS at bits[63:P] is an UNKNOWN value, where P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The result of writing a value of all zeros or all ones to ADDRESS at bits[63:P] is the written value, and a read of the register returns the written value.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCACVR&lt;n&gt;

Must be programmed if any of the following are true:

```
· TRCBBCTLR.RANGE[n/2] == 1. · TRCRSCTLR<a>.GROUP == 0b0100 and TRCRSCTLR<a>.SAC[n] == 1. · TRCRSCTLR<a>.GROUP == 0b0101 and TRCRSCTLR<a>.ARC[n/2] == 1.
```

- TRCVIIECTLR.EXCLUDE[n/2] == 1.
- TRCVIIECTLR.INCLUDE[n/2] == 1. · TRCVISSCTLR.START[n] == 1. · TRCVISSCTLR.STOP[n] == 1. · TRCSSCCR&lt;&gt;.ARC[n/2] == 1. · TRCSSCCR&lt;&gt;.SAC[n] == 1. · TRCQCTLR.RANGE[n/2] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCACVR<m> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b00 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACVR[m];
```

MSR TRCACVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b00 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACVR[m] = X[t, 64];
```

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

## D24.4.14 TRCAUXCTLR, Trace Auxiliary Control Register

The TRCAUXCTLR characteristics are:

## Purpose

The function of this register is IMPLEMENTATION DEFINED.

## Configuration

AArch64 System register TRCAUXCTLR bits [31:0] are architecturally mapped to External register TRCAUXCTLR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCAUXCTLR are UNDEFINED.

## Attributes

TRCAUXCTLRis a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
|                        | 0                      |
| 31                     |                        |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## Bits [63:32]

Reserved, RES0.

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

This field reads as an IMPLEMENTATION DEFINED value and writes to this field have IMPLEMENTATION DEFINED behavior.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to 0x00000000 .

## Accessing TRCAUXCTLR

If this register is nonzero then it might cause the behavior of a trace unit to contradict this architecture specification. See the documentation of the specific implementation for information about the IMPLEMENTATION DEFINED support for this register.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCAUXCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCAUXCTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCAUXCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCAUXCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCAUXCTLR;
```

MSR TRCAUXCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then
```

```
UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCAUXCTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCAUXCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCAUXCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCAUXCTLR = X[t, 64];
```

## D24.4.15 TRCBBCTLR, Trace Branch Broadcast Control Register

The TRCBBCTLR characteristics are:

## Purpose

Controls the regions in the memory map where branch broadcasting is active.

## Configuration

AArch64 System register TRCBBCTLR bits [31:0] are architecturally mapped to External register TRCBBCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, TRCIDR0.TRCBB == '1', and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCBBCTLR are UNDEFINED.

## Attributes

TRCBBCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:9]

Reserved, RES0.

## MODE,bit [8]

Mode.

| MODE   | Meaning                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Exclude Mode. Branch broadcasting is not active for instructions in the address ranges defined by TRCBBCTLR.RANGE. If TRCBBCTLR.RANGE == 0x00 then branch broadcasting is active for all instructions.                                                                                                                  |
| 0b1    | Include Mode. Branch broadcasting is active for instructions in the address ranges defined by TRCBBCTLR.RANGE. If TRCBBCTLR.RANGE == 0x00 then the behavior of the trace unit is CONSTRAINED UNPREDICTABLE. That is, the trace unit might or might not consider any instructions to be in a branch broadcasting region. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RANGE[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects whether Address Range Comparator &lt;m&gt; is used with branch broadcasting.

| RANGE[<m>]   | Meaning                                                                       |
|--------------|-------------------------------------------------------------------------------|
| 0b0          | The address range that Address Range Comparator <m> defines, is not selected. |
| 0b1          | The address range that Address Range Comparator <m> defines, is selected.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCBBCTLR

Must be programmed if TRCCONFIGR.BB == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCBBCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1111 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TRCBB == '1' && ↪ → UInt(TRCIDR4.NUMACPAIRS) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCBBCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCBBCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCBBCTLR;
```

MSR TRCBBCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1111 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TRCBB == '1' && ↪ → UInt(TRCIDR4.NUMACPAIRS) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCBBCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED;
```

```
elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCBBCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCBBCTLR = X[t, 64];
```

## D24.4.16 TRCCCCTLR, Trace Cycle Count Control Register

The TRCCCCTLR characteristics are:

## Purpose

Set the threshold value for cycle counting.

## Configuration

AArch64 System register TRCCCCTLR bits [31:0] are architecturally mapped to External register TRCCCCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR0.TRCCCI == '1'. Otherwise, direct accesses to TRCCCCTLR are UNDEFINED.

## Attributes

TRCCCCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## THRESHOLD, bits [11:0]

Sets the threshold value for instruction trace cycle counting.

The minimum threshold value that can be programmed into THRESHOLD is given in TRCIDR3.CCITMIN. If the THRESHOLD value is smaller than the value in TRCIDR3.CCITMIN then the behavior is CONSTRAINED UNPREDICTABLE. That is, cycle counts might or might not be included in the trace and the cycle count threshold is not known.

Writing a value of zero when TRCCONFIGR.CCI enables instruction trace cycle counting results in CONSTRAINED UNPREDICTABLE behavior. That is, cycle counts might or might not be included in the trace and the cycle count threshold is not known.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCCCTLR

Must be programmed if TRCCONFIGR.CCI == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCCCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TRCCCI == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCCCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCCCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCCCTLR;
```

MSR TRCCCCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TRCCCI == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCCCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCCCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCCCTLR = X[t, 64];
```

## D24.4.17 TRCCIDCCTLR0, Trace Context Identifier Comparator Control Register 0

The TRCCIDCCTLR0 characteristics are:

## Purpose

Contains Context identifier mask values for the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3.

## Configuration

AArch64 System register TRCCIDCCTLR0 bits [31:0] are architecturally mapped to External register TRCCIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMCIDC) &gt; 0x0 , and UInt(TRCIDR2.CIDSIZE) &gt; 0. Otherwise, direct accesses to TRCCIDCCTLR0 are UNDEFINED.

## Attributes

TRCCIDCCTLR0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 3:

TRCCIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR3. Each bit in this field corresponds to a byte in TRCCIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMCIDC) &gt; 2:

TRCCIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR2. Each bit in this field corresponds to a byte in TRCCIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 1:

TRCCIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR1. Each bit in this field corresponds to a byte in TRCCIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 0:

TRCCIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR0. Each bit in this field corresponds to a byte in TRCCIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCCIDCCTLR0

If software uses the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCCIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCCIDCVR&lt;n&gt; is not 0x00 , the behavior of the Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCIDCCTLR0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x0 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0;
```

MSR TRCCIDCCTLR0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x0 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64];
```

## D24.4.18 TRCCIDCCTLR1, Trace Context Identifier Comparator Control Register 1

The TRCCIDCCTLR1 characteristics are:

## Purpose

Contains Context identifier mask values for the TRCCIDCVR&lt;n&gt; registers, for n = 4 to 7.

## Configuration

AArch64 System register TRCCIDCCTLR1 bits [31:0] are architecturally mapped to External register TRCCIDCCTLR1[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMCIDC) &gt; 0x4 , and UInt(TRCIDR2.CIDSIZE) &gt; 0. Otherwise, direct accesses to TRCCIDCCTLR1 are UNDEFINED.

## Attributes

TRCCIDCCTLR1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP7[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 7:

TRCCIDCVR7 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR7. Each bit in this field corresponds to a byte in TRCCIDCVR7.

| COMP7[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR7[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR7[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP6[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMCIDC) &gt; 6:

TRCCIDCVR6 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR6. Each bit in this field corresponds to a byte in TRCCIDCVR6.

| COMP6[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR6[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR6[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP5[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 5:

TRCCIDCVR5 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR5. Each bit in this field corresponds to a byte in TRCCIDCVR5.

| COMP5[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR5[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR5[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP4[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 4:

TRCCIDCVR4 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR4. Each bit in this field corresponds to a byte in TRCCIDCVR4.

| COMP4[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR4[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR4[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCCIDCCTLR1

If software uses the TRCCIDCVR&lt;n&gt; registers, for n = 4 to 7, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCCIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCCIDCVR&lt;n&gt; is not 0x00 , the behavior of the Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCIDCCTLR1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x4 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR1; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR1;
```

MSR TRCCIDCCTLR1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x4 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR1 = X[t, 64];
```

## D24.4.19 TRCCIDCVR&lt;n&gt;, Trace Context Identifier Comparator Value Registers &lt;n&gt;, n = 0 - 7

The TRCCIDCVR&lt;n&gt; characteristics are:

## Purpose

Contains a Context identifier value.

## Configuration

AArch64 System register TRCCIDCVR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCCIDCVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMCIDC) &gt; n. Otherwise, direct accesses to TRCCIDCVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCIDCVR&lt;n&gt; is a 64-bit register.

## Field descriptions

VALUE

63

32

VALUE

31

0

<!-- image -->

## VALUE, bits [63:0]

Context identifier value. The width of this field is indicated by TRCIDR2.CIDSIZE. Unimplemented bits are RES0. After a PE Reset, the trace unit assumes that the Context identifier is zero until the PE updates the Context identifier.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCIDCVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCRSCTLR&lt;a&gt;.GROUP == 0b0110 and TRCRSCTLR&lt;a&gt;.CID[n] == 1. · TRCACATR&lt;a&gt;.CONTEXTTYPE == 0b01 or 0b11 and TRCACATR&lt;a&gt;.CONTEXT == n.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCCIDCVR<m> ; Where m = 0-7
```

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b000 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_CONTEXT_IDENTIFIER_COMPARATORS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m];
```

MSR TRCCIDCVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b000 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_CONTEXT_IDENTIFIER_COMPARATORS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64];
```

## D24.4.20 TRCCLAIMCLR, Trace Claim Tag Clear Register

The TRCCLAIMCLR characteristics are:

## Purpose

In conjunction with TRCCLAIMSET, provides Claim Tag bits that can be separately set and cleared to indicate whether functionality is in use by a debug agent.

For additional information, see the CoreSight Architecture Specification.

## Configuration

AArch64 System register TRCCLAIMCLR bits [63:0] are architecturally mapped to AArch64 System register TRCCLAIMSET[63:0].

AArch64 System register TRCCLAIMCLR bits [31:0] are architecturally mapped to External register TRCCLAIMCLR[31:0].

AArch64 System register TRCCLAIMCLR bits [31:0] are architecturally mapped to External register TRCCLAIMSET[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCCLAIMCLR are UNDEFINED.

## Attributes

TRCCLAIMCLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

CLR[&lt;m&gt;] , bits [m], for m = 31 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

| CLR[<m>]   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The number of Claim Tag bits implemented is indicated in TRCCLAIMSET.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

Accessing this field has the following behavior:

- When m &gt;= NUM\_TRC\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing TRCCLAIMCLR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCLAIMCLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMCLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMCLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMCLR;
```

MSR TRCCLAIMCLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCLAIMCLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

```
else TRCCLAIMCLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCLAIMCLR = X[t, 64];
```

## D24.4.21 TRCCLAIMSET, Trace Claim Tag Set Register

The TRCCLAIMSET characteristics are:

## Purpose

In conjunction with TRCCLAIMCLR, provides Claim Tag bits that can be separately set and cleared to indicate whether functionality is in use by a debug agent.

For additional information, see the CoreSight Architecture Specification.

## Configuration

The number of claim tag bits implemented is IMPLEMENTATION DEFINED. Arm recommends that implementations support a minimum of four claim tag bits, that is, SET[3:0] reads as 0b1111 .

AArch64 System register TRCCLAIMSET bits [63:0] are architecturally mapped to AArch64 System register TRCCLAIMCLR[63:0].

AArch64 System register TRCCLAIMSET bits [31:0] are architecturally mapped to External register TRCCLAIMSET[31:0].

AArch64 System register TRCCLAIMSET bits [31:0] are architecturally mapped to External register TRCCLAIMCLR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCCLAIMSET are UNDEFINED.

## Attributes

TRCCLAIMSET is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

SET[&lt;m&gt;] , bits [m], for m = 31 to 0

Claim Tag Set. Indicates whether Claim Tag bit &lt;m&gt; is implemented, and is used to set Claim Tag bit &lt;m&gt; to 1.

| SET[<m>]   | Meaning                                                                              |
|------------|--------------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not implemented. On a write: Ignored.                |
| 0b1        | On a read: Claim Tag bit <m> is implemented. On a write: Set Claim Tag bit <m> to 1. |

Accessing this field has the following behavior:

- When m &gt;= NUM\_TRC\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is RAO/W1S.

## Accessing TRCCLAIMSET

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCLAIMSET

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1000 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMSET; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMSET; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCLAIMSET;
```

MSR TRCCLAIMSET, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1000 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCLAIMSET = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCLAIMSET = X[t, 64]; elsif PSTATE.EL == EL3 then
```

```
if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCLAIMSET = X[t, 64];
```

## D24.4.22 TRCCNTCTLR&lt;n&gt;, Trace Counter Control Register &lt;n&gt;, n = 0 - 3

The TRCCNTCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the operation of Counter &lt;n&gt;.

## Configuration

AArch64 System register TRCCNTCTLR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCCNTCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTCTLR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCNTCTLR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:18]

Reserved, RES0.

## CNTCHAIN, bit [17]

## When (n MOD 2) != 0:

For TRCCNTCTLR3 and TRCCNTCTLR1, this field controls whether the Counter decrements when a reload event occurs for Counter &lt;n-1&gt;.

| CNTCHAIN   | Meaning                                                                                                                                                |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | The Counter does not decrement when a reload event for Counter <n-1> occurs.                                                                           |
| 0b1        | Counter <n> decrements when a reload event for Counter <n-1> occurs. This concatenates Counter <n> and Counter <n-1>, to provide a larger count value. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLDSELF, bit [16]

Controls whether a reload event occurs for the Counter, when the Counter reaches zero.

| RLDSELF   | Meaning                                               |
|-----------|-------------------------------------------------------|
| 0b0       | Normal mode. The Counter is in Normal mode.           |
| 0b1       | Self-reload mode. The Counter is in Self-reload mode. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RLDEVENT\_TYPE, bit [15]

Selects an event, that when it occurs causes a reload event for Counter

Chooses the type of Resource Selector.

| RLDEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.RLDEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.RLDEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## RLDEVENT\_SEL, bits [12:8]

Selects an event, that when it occurs causes a reload event for Counter

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.TYPE controls whether TRCCNTCTLR.RLDEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## CNTEVENT\_TYPE, bit [7]

Selects an event, that when it occurs causes Counter to decrement.

Chooses the type of Resource Selector.

| CNTEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.CNTEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.CNTEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## CNTEVENT\_SEL, bits [4:0]

Selects an event, that when it occurs causes Counter to decrement.

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.TYPE controls whether TRCCNTCTLR.CNTEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTCTLR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCNTCTLR&lt;m&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b01 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m];
```

MSR TRCCNTCTLR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b01 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64];
```

## D24.4.23 TRCCNTRLDVR&lt;n&gt;, Trace Counter Reload Value Register &lt;n&gt;, n = 0 - 3

The TRCCNTRLDVR&lt;n&gt; characteristics are:

## Purpose

This sets or returns the reload count value for Counter &lt;n&gt;.

## Configuration

AArch64 System register TRCCNTRLDVR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCCNTRLDVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTRLDVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCNTRLDVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## VALUE, bits [15:0]

Contains the reload value for Counter &lt;n&gt;. When a reload event occurs for Counter &lt;n&gt; then the trace unit copies the VALUE&lt;n&gt; field into Counter &lt;n&gt;.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTRLDVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCNTRLDVR&lt;m&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTRLDVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTRLDVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTRLDVR[m];
```

MSR TRCCNTRLDVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTRLDVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTRLDVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTRLDVR[m] = X[t, 64];
```

## D24.4.24 TRCCNTVR&lt;n&gt;, Trace Counter Value Register &lt;n&gt;, n = 0 - 3

The TRCCNTVR&lt;n&gt; characteristics are:

## Purpose

This sets or returns the value of Counter &lt;n&gt;.

## Configuration

AArch64 System register TRCCNTVR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCCNTVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCNTVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## VALUE, bits [15:0]

Contains the count value of Counter.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCNTVR&lt;m&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCCNTVRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m];
```

MSR TRCCNTVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCCNTVRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64];
```

## D24.4.25 TRCCONFIGR, Trace Configuration Register

The TRCCONFIGR characteristics are:

## Purpose

Controls the tracing options.

## Configuration

AArch64 System register TRCCONFIGR bits [31:0] are architecturally mapped to External register TRCCONFIGR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCCONFIGR are UNDEFINED.

## Attributes

TRCCONFIGR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:19]

Reserved, RES0.

## ITO, bit [18]

When TRCIDR0.ITE == '1':

Instrumentation Trace Override.

| ITO   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Instrumentation Trace Override disabled. |
| 0b1   | Instrumentation Trace Override enabled.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [17:16]

Reserved, RES0.

## VMIDOPT, bit [15]

## When TRCIDR2.VMIDOPT == '01':

Virtual context identifier selection control.

| VMIDOPT   | Meaning                                                          |
|-----------|------------------------------------------------------------------|
| 0b0       | VTTBR_EL2.VMID is used as the Virtual context identifier.        |
| 0b1       | CONTEXTIDR_EL2.PROCID is used as the Virtual context identifier. |

## When TRCIDR2.VMIDOPT == '00':

Reserved, RES0.

Virtual context identifier selection control.

VTTBR\_EL2.VMID is used as the Virtual context identifier.

## When TRCIDR2.VMIDOPT == '10':

Reserved, RES1.

Virtual context identifier selection control.

CONTEXTIDR\_EL2.PROCID is used as the Virtual context identifier.

## Otherwise:

Reserved, RES0.

QE, bits [14:13]

## When TRCIDR0.QSUPP == '01':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '10':

Qelement generation control.

| QE   | Meaning                                                                                          |
|------|--------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                          |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '11':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled.  |

All other values are reserved.

## Otherwise:

Reserved, RES0.

## RS, bit [12]

## When TRCIDR0.RETSTACK == '1':

Return stack control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TS, bit [11]

## When TRCIDR0.TSSIZE != '00000':

Global timestamp tracing control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

| RS   | Meaning                   |
|------|---------------------------|
| 0b0  | Return stack is disabled. |
| 0b1  | Return stack is enabled.  |

| TS   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Global timestamp tracing is disabled. |
| 0b1  | Global timestamp tracing is enabled.  |

## Otherwise:

Reserved, RES0.

## Bits [10:8]

Reserved, RES0.

## VMID, bit [7]

## When TRCIDR2.VMIDSIZE != '00000':

Virtual context identifier tracing control.

| VMID   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Virtual context identifier tracing is disabled. |
| 0b1    | Virtual context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

CID, bit [6]

## When TRCIDR2.CIDSIZE != '00000':

Context identifier tracing control.

| CID   | Meaning                                 |
|-------|-----------------------------------------|
| 0b0   | Context identifier tracing is disabled. |
| 0b1   | Context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [5]

Reserved, RES0.

CCI, bit [4]

When TRCIDR0.TRCCCI == '1':

Cycle counting instruction tracing control.

| CCI   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Cycle counting instruction tracing is disabled. |
| 0b1   | Cycle counting instruction tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BB, bit [3]

## When TRCIDR0.TRCBB == '1':

Branch broadcasting control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [2:1]

Reserved, RES0.

## Bit [0]

Reserved, RES1.

## Accessing TRCCONFIGR

Must always be programmed.

TRCCONFIGR.QE must be set to 0b00 if TRCCONFIGR.BB is not 0.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCONFIGR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0100 | 0b000 |

| BB   | Meaning                          |
|------|----------------------------------|
| 0b0  | Branch broadcasting is disabled. |
| 0b1  | Branch broadcasting is enabled.  |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR;
```

MSR TRCCONFIGR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then
```

```
UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64];
```

## D24.4.26 TRCDEVARCH, Trace Device Architecture Register

The TRCDEVARCH characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

AArch64 System register TRCDEVARCH bits [31:0] are architecturally mapped to External register TRCDEVARCH[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCDEVARCH are UNDEFINED.

## Attributes

TRCDEVARCHis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ARCHITECT, bits [31:21]

Defines the architect of the component. For Trace, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as 0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the TRCDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Revision. Defines the architecture revision of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

Access to this field is RO.

## ARCHVER,bits [15:12]

Architecture Version. Defines the architecture version of the component.

| ARCHVER   | Meaning   |
|-----------|-----------|
| 0b0101    | ETEv1.    |

ARCHVERand ARCHPART are also defined as a single field, ARCHID, so that ARCHVER is ARCHID[15:12]. This field reads as 0x5 .

Access to this field is RO.

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

| ARCHPART   | Meaning                    |
|------------|----------------------------|
| 0xA13      | Arm PE trace architecture. |

ARCHVERand ARCHPART are also defined as a single field, ARCHID, so that ARCHPART is ARCHID[11:0]. This field reads as 0xA13 .

Access to this field is RO.

## Accessing TRCDEVARCH

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCDEVARCH

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1111 | 0b110 |

| REVISION   | Meaning                |
|------------|------------------------|
| 0b0000     | ETEv1.0, FEAT_ETE.     |
| 0b0001     | ETEv1.1, FEAT_ETEv1p1. |
| 0b0010     | ETEv1.2, FEAT_ETEv1p2. |
| 0b0011     | ETEv1.3, FEAT_ETEv1p3. |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH;
```

## D24.4.27 TRCDEVID, Trace Device Configuration Register

The TRCDEVID characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

AArch64 System register TRCDEVID bits [31:0] are architecturally mapped to External register TRCDEVID[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCDEVID are UNDEFINED.

## Attributes

TRCDEVID is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:0]

Reserved, RES0.

## Accessing TRCDEVID

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCDEVID

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b0010 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVID; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVID; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVID;
```

## D24.4.28 TRCEVENTCTL0R, Trace Event Control 0 Register

The TRCEVENTCTL0R characteristics are:

## Purpose

Controls the generation of ETEEvents.

## Configuration

AArch64 System register TRCEVENTCTL0R bits [31:0] are architecturally mapped to External register TRCEVENTCTL0R[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR4.NUMRSPAIR != '0000'. Otherwise, direct accesses to TRCEVENTCTL0R are UNDEFINED.

## Attributes

TRCEVENTCTL0R is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

EVENT3\_TYPE, bit [31]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 3:

Chooses the type of Resource Selector.

| EVENT3_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT3.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT3.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT3.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [30:29]

Reserved, RES0.

## EVENT3\_SEL, bits [28:24]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 3:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[3] == 1, then Event element 3 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT3.TYPE controls whether TRCEVENTCTL0R.EVENT3.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT2\_TYPE, bit [23]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 2:

Chooses the type of Resource Selector.

| EVENT2_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT2.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT2.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT2.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [22:21]

Reserved, RES0.

## EVENT2\_SEL, bits [20:16]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 2:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[2] == 1, then Event element 2 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT2.TYPE controls whether TRCEVENTCTL0R.EVENT2.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT1\_TYPE, bit [15]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 1:

Chooses the type of Resource Selector.

| EVENT1_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT1.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT1.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT1.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [14:13]

Reserved, RES0.

## EVENT1\_SEL, bits [12:8]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 1:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[1] == 1, then Event element 1 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT1.TYPE controls whether TRCEVENTCTL0R.EVENT1.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT0\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT0_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT0.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT0.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT0.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## EVENT0\_SEL, bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[0] == 1, then Event element 0 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT0.TYPE controls whether TRCEVENTCTL0R.EVENT0.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TRCEVENTCTL0R

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCEVENTCTL0R

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1000 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR4.NUMRSPAIR != '0000') ↪ → then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL0R; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL0R; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL0R;
```

MSR TRCEVENTCTL0R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1000 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR4.NUMRSPAIR != '0000') ↪ → then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL0R = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL0R = X[t, 64]; elsif PSTATE.EL == EL3 then
```

```
if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL0R = X[t, 64];
```

## D24.4.29 TRCEVENTCTL1R, Trace Event Control 1 Register

The TRCEVENTCTL1R characteristics are:

## Purpose

Controls the behavior of the ETEEvents that TRCEVENTCTL0R selects.

## Configuration

AArch64 System register TRCEVENTCTL1R bits [31:0] are architecturally mapped to External register TRCEVENTCTL1R[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCEVENTCTL1R are UNDEFINED.

## Attributes

TRCEVENTCTL1R is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:14]

Reserved, RES0.

OE, bit [13]

When TRCIDR5.OE == '1':

ETE Trace Output Enable control.

| OE   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | Trace output to any IMPLEMENTATION DEFINED trace output interface is disabled. |
| 0b1  | Trace output to any IMPLEMENTATION DEFINED trace output interface is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

LPOVERRIDE, bit [12]

## When TRCIDR5.LPOVERRIDE == '1':

Low-power Override Mode select.

| LPOVERRIDE   | Meaning                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Trace unit Low-power Override Mode is not enabled. That is, the trace unit is permitted to enter low-power state.                                |
| 0b1          | Trace unit Low-power Override Mode is enabled. That is, entry to a low-power state does not affect the trace unit resources or trace generation. |

## Otherwise:

Reserved, RES0.

## ATB, bit [11]

## When TRCIDR5.ATBTRIG == '1':

AMBATrace Bus (ATB) trigger enable.

If a CoreSight ATB interface is implemented then when ETEEvent 0 occurs the trace unit sets:

- ATID == 0x7D .
- ATDATA to the value of TRCTRACEIDR.

If the width of ATDATA is greater than the width of TRCTRACEIDR.TRACEID then the trace unit zeros the upper ATDATA bits.

If ETEEvent 0 is programmed to occur based on program execution, such as an Address Comparator, the ATB trigger might not be inserted into the ATB stream at the same time as any trace generated by that program execution is output by the trace unit. Typically, the generated trace might be buffered in a trace unit which means that the ATB trigger would be output before the associated trace is output.

If ETEEvent 0 is asserted multiple times in close succession, the trace unit is required to generate an ATB trigger for the first assertion, but might ignore one or more of the subsequent assertions. Arm recommends that the window in which ETEEvent 0 is ignored is limited only by the time taken to output an ATB trigger.

| ATB   | Meaning                  |
|-------|--------------------------|
| 0b0   | ATB trigger is disabled. |
| 0b1   | ATB trigger is enabled.  |

## Otherwise:

Reserved, RES0.

## Bits [10:4]

Reserved, RES0.

## INSTEN[&lt;m&gt;] , bits [m], for m = 3 to 0

Event element control.

| INSTEN[<m>]   | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| 0b0           | The trace unit does not generate an Event element <m>.                  |
| 0b1           | The trace unit generates an Event element <m> when ETEEvent <m> occurs. |

Accessing this field has the following behavior:

- When TRCIDR4.NUMRSPAIR == '0000', access to this field is RES0.
- Access to this field is RES0 if all of the following are true:
- TRCIDR4.NUMRSPAIR != '0000'
- m&gt;UInt(TRCIDR0.NUMEVENT)
- Otherwise, access to this field is RW.

## Accessing TRCEVENTCTL1R

Must be programmed.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCEVENTCTL1R

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL1R; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL1R; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEVENTCTL1R;
```

MSR TRCEVENTCTL1R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL1R = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL1R = X[t, 64];
```

```
elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEVENTCTL1R = X[t, 64];
```

## D24.4.30 TRCEXTINSELR&lt;n&gt;, Trace External Input Select Register &lt;n&gt;, n = 0 - 3

The TRCEXTINSELR&lt;n&gt; characteristics are:

## Purpose

Use this to set, or read, which External Inputs are resources to the trace unit.

The name TRCEXTINSELR is an alias of TRCEXTINSELR0.

## Configuration

AArch64 System register TRCEXTINSELR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCEXTINSELR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMEXTINSEL) &gt; n. Otherwise, direct accesses to TRCEXTINSELR&lt;n&gt; are UNDEFINED.

## Attributes

TRCEXTINSELR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32       |
|----------|----------|
| RES0     | 0        |
| 31 16 15 |          |
| RES0     | evtCount |

## Bits [63:16]

Reserved, RES0.

## evtCount, bits [15:0]

PMUevent to select.

The event number as defined by the Arm ARM.

Software must program this field with a PMU event that is supported by the PE being programmed.

There are three ranges of PMU event numbers:

- PMUevent numbers in the range 0x0000 to 0x003F are common architectural and microarchitectural events.
- PMUevent numbers in the range 0x0040 to 0x00BF are Arm recommended common architectural and microarchitectural PMU events.
- PMUevent numbers in the range 0x00C0 to 0x03FF are IMPLEMENTATION DEFINED PMU events.

If evtCount is programmed to a PMU event that is reserved or not supported by the PE, the behavior depends on the PMU event type:

- For the range 0x0000 to 0x003F , then the PMU event is not active, and the value returned by a direct or external read of the evtCount field is the value written to the field.
- For IMPLEMENTATION DEFINED PMU events, it is UNPREDICTABLE what PMU event, if any, is counted, and the value returned by a direct or external read of the evtCount field is UNKNOWN.

UNPREDICTABLE means the PMU event must not expose privileged information.

Arm recommends that the behavior across a family of implementations is defined such that if a given implementation does not include a PMU event from a set of common IMPLEMENTATION DEFINED PMU events, then no PMU event is counted and the value read back on evtCount is the value written.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCEXTINSELR&lt;n&gt;

Must be programmed if any of the following is true: TRCRSCTLR&lt;a&gt;.GROUP == 0b0000 and TRCRSCTLR&lt;a&gt;.EXTIN[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCEXTINSELR<m> ; Where m = 0-3
```

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_EXTERNAL_INPUT_SELECTOR_RESOURCES then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEXTINSELR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else
```

```
X[t, 64] = TRCEXTINSELR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCEXTINSELR[m];
```

MSR TRCEXTINSELR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_EXTERNAL_INPUT_SELECTOR_RESOURCES then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEXTINSELR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEXTINSELR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCEXTINSELR[m] = X[t, 64];
```

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

## D24.4.32 TRCIDR1, Trace ID Register 1

The TRCIDR1 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR1 bits [31:0] are architecturally mapped to External register TRCIDR1[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR1 are UNDEFINED.

## Attributes

TRCIDR1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## DESIGNER, bits [31:24]

Indicates which company designed the trace unit. The permitted values of this field are the same as MIDR\_EL1.Implementer.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [23:16]

Reserved, RES0.

## Bits [15:12]

Reserved, RES1.

## TRCARCHMAJ,bits [11:8]

Major architecture version.

| TRCARCHMAJ   | Meaning                                                                            |
|--------------|------------------------------------------------------------------------------------|
| 0b1111       | If both TRCIDR1.TRCARCHMAJ and TRCIDR1.TRCARCHMIN == 0xF then refer to TRCDEVARCH. |

All other values are reserved.

This field reads as 0b1111 .

Access to this field is RO.

## TRCARCHMIN,bits [7:4]

Minor architecture version.

| TRCARCHMIN   | Meaning                                                                            |
|--------------|------------------------------------------------------------------------------------|
| 0b1111       | If both TRCIDR1.TRCARCHMAJ and TRCIDR1.TRCARCHMIN == 0xF then refer to TRCDEVARCH. |

All other values are reserved.

This field reads as 0b1111 .

Access to this field is RO.

## REVISION, bits [3:0]

Implementation revision.

Returns an IMPLEMENTATION DEFINED value that identifies the revision of the trace unit.

Arm deprecates any use of this field and recommends that implementations set this field to zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCIDR1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1001 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR1; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR1;
```

## D24.4.33 TRCIDR10, Trace ID Register 10

The TRCIDR10 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR10 bits [31:0] are architecturally mapped to External register TRCIDR10[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR10 are UNDEFINED.

## Attributes

TRCIDR10 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMP1KEY, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of P1 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR10

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR10

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10;
```

## D24.4.34 TRCIDR11, Trace ID Register 11

The TRCIDR11 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR11 bits [31:0] are architecturally mapped to External register TRCIDR11[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR11 are UNDEFINED.

## Attributes

TRCIDR11 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMP1SPC, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of special P1 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR11

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR11

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0011 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR11; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR11; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR11;
```

## D24.4.35 TRCIDR12, Trace ID Register 12

The TRCIDR12 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR12 bits [31:0] are architecturally mapped to External register TRCIDR12[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR12 are UNDEFINED.

## Attributes

TRCIDR12 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMCONDKEY,bits [31:0]

## When TRCIDR0.TRCCOND == '1':

Indicates the number of conditional instruction right-hand keys. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR12

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0100 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR12; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR12; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR12;
```

## D24.4.36 TRCIDR13, Trace ID Register 13

The TRCIDR13 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR13 bits [31:0] are architecturally mapped to External register TRCIDR13[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR13 are UNDEFINED.

## Attributes

TRCIDR13 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMCONDSPC,bits [31:0]

## When TRCIDR0.TRCCOND == '1':

Indicates the number of special conditional instruction right-hand keys. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR13

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR13

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0101 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR13; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR13; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR13;
```

## D24.4.37 TRCIDR2, Trace ID Register 2

The TRCIDR2 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR2 bits [31:0] are architecturally mapped to External register TRCIDR2[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR2 are UNDEFINED.

## Attributes

TRCIDR2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## WFXMODE,bit [31]

Indicates whether WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WFXMODE   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | WFI , WFIT , WFE , and WFET instructions are not classified as P0 instructions. |
| 0b1       | WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions.     |

Access to this field is RO.

## VMIDOPT, bits [30:29]

Indicates the options for Virtual context identifier selection.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDOPT   | Meaning                                                                            |
|-----------|------------------------------------------------------------------------------------|
| 0b00      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES0.    |
| 0b01      | Virtual context identifier selection supported. TRCCONFIGR.VMIDOPT is implemented. |
| 0b10      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES1.    |

All other values are reserved.

If TRCIDR2.VMIDSIZE == 0b00000 then this field is 0b00 .

If TRCIDR2.VMIDSIZE != 0b00000 then this field is 0b10 .

Access to this field is RO.

## CCSIZE, bits [28:25]

## When TRCIDR0.TRCCCI == '1':

Indicates the size of the cycle counter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCSIZE   | Meaning                                 |
|----------|-----------------------------------------|
| 0b0000   | The cycle counter is 12 bits in length. |
| 0b0001   | The cycle counter is 13 bits in length. |
| 0b0010   | The cycle counter is 14 bits in length. |
| 0b0011   | The cycle counter is 15 bits in length. |
| 0b0100   | The cycle counter is 16 bits in length. |
| 0b0101   | The cycle counter is 17 bits in length. |
| 0b0110   | The cycle counter is 18 bits in length. |
| 0b0111   | The cycle counter is 19 bits in length. |
| 0b1000   | The cycle counter is 20 bits in length. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DVSIZE, bits [24:20]

## When TRCIDR0.TRCDATA != '00':

Indicates the data value size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DVSIZE   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b00000  | Data value tracing not implemented.                     |
| 0b00100  | Data value tracing has a maximum of 32-bit data values. |
| 0b01000  | Data value tracing has a maximum of 64-bit data values. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

DASIZE, bits [19:15]

## When TRCIDR0.TRCDATA != '00':

Indicates the data address size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DASIZE   | Meaning                                                      |
|----------|--------------------------------------------------------------|
| 0b00000  | Data address tracing not implemented.                        |
| 0b00100  | Data address tracing has a maximum of 32-bit data addresses. |
| 0b01000  | Data address tracing has a maximum of 64-bit data addresses. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## VMIDSIZE, bits [14:10]

Indicates the trace unit Virtual context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDSIZE   | Meaning                                              |
|------------|------------------------------------------------------|
| 0b00000    | Virtual context identifier tracing is not supported. |
| 0b00001    | 8-bit Virtual context identifier size.               |
| 0b00010    | 16-bit Virtual context identifier size.              |
| 0b00100    | 32-bit Virtual context identifier size.              |

All other values are reserved.

If the PE does not implement EL2 then this field is 0b00000 .

If the PE implements EL2 then this field is 0b00100 .

Access to this field is RO.

## CIDSIZE, bits [9:5]

Indicates the Context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CIDSIZE   | Meaning                                      |
|-----------|----------------------------------------------|
| 0b00000   | Context identifier tracing is not supported. |
| 0b00100   | 32-bit Context identifier size.              |

All other values are reserved.

This field reads as 0b00100 .

Access to this field is RO.

## IASIZE, bits [4:0]

Virtual instruction address size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IASIZE   | Meaning                                     |
|----------|---------------------------------------------|
| 0b00100  | Maximum of 32-bit instruction address size. |
| 0b01000  | Maximum of 64-bit instruction address size. |

All other values are reserved.

This field reads as 0b01000 .

Access to this field is RO.

## Accessing TRCIDR2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1010 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then
```

then

```
AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2;
```

## D24.4.38 TRCIDR3, Trace ID Register 3

The TRCIDR3 characteristics are:

## Purpose

Returns the base architecture of the trace unit.

## Configuration

AArch64 System register TRCIDR3 bits [31:0] are architecturally mapped to External register TRCIDR3[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR3 are UNDEFINED.

## Attributes

TRCIDR3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NOOVERFLOW,bit [31]

Indicates if overflow prevention is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NOOVERFLOW   | Meaning                                 |
|--------------|-----------------------------------------|
| 0b0          | Overflow prevention is not implemented. |
| 0b1          | Overflow prevention is implemented.     |

If TRCIDR3.STALLCTL == 0 then this field is 0.

Access to this field is RO.

## NUMPROC,bits [13:12, 30:28]

Indicates the number of PEs available for tracing.

This field reads as 0b00000 .

Access to this field is RO.

## SYSSTALL, bit [27]

Indicates if stalling of the PE is permitted.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYSSTALL   | Meaning                              |
|------------|--------------------------------------|
| 0b0        | Stalling of the PE is not permitted. |
| 0b1        | Stalling of the PE is permitted.     |

The value of this field might be dynamic and change based on system conditions.

If TRCIDR3.STALLCTL == 0 then this field is 0.

Access to this field is RO.

## STALLCTL, bit [26]

Indicates if trace unit implements stalling of the PE.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| STALLCTL   | Meaning                                |
|------------|----------------------------------------|
| 0b0        | Stalling of the PE is not implemented. |
| 0b1        | Stalling of the PE is implemented.     |

Access to this field is RO.

## SYNCPR, bit [25]

Indicates if an implementation has a fixed synchronization period.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYNCPR   | Meaning                                                                    |
|----------|----------------------------------------------------------------------------|
| 0b0      | TRCSYNCPR is read/write so software can change the synchronization period. |
| 0b1      | TRCSYNCPR is read-only so the synchronization period is fixed.             |

| NUMPROC   | Meaning                          |
|-----------|----------------------------------|
| 0b00000   | The trace unit can trace one PE. |

This field reads as 0.

Access to this field is RO.

## TRCERR, bit [24]

Indicates forced tracing of System Error exceptions is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCERR   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0      | Forced tracing of System Error exceptions is not implemented. |
| 0b1      | Forced tracing of System Error exceptions is implemented.     |

This field reads as 1.

Access to this field is RO.

## Bit [23]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [22]

Indicates if Non-secure EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_NS_EL2   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL2 is not implemented. |
| 0b1              | Non-secure EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_NS\_EL1, bit [21]

Indicates if Non-secure EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_NS_EL1   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL1 is not implemented. |
| 0b1              | Non-secure EL1 is implemented.     |

Access to this field is RO.

## EXLEVEL\_NS\_EL0, bit [20]

Indicates if Non-secure EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_NS_EL0   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL0 is not implemented. |
| 0b1              | Non-secure EL0 is implemented.     |

Access to this field is RO.

## EXLEVEL\_S\_EL3, bit [19]

Indicates if EL3 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL3   | Meaning                 |
|-----------------|-------------------------|
| 0b0             | EL3 is not implemented. |
| 0b1             | EL3 is implemented.     |

Access to this field is RO.

## EXLEVEL\_S\_EL2, bit [18]

Indicates if Secure EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL2   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL2 is not implemented. |
| 0b1             | Secure EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_S\_EL1, bit [17]

Indicates if Secure EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## EXLEVEL\_S\_EL0, bit [16]

Indicates if Secure EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL0   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL0 is not implemented. |
| 0b1             | Secure EL0 is implemented.     |

Access to this field is RO.

## Bits [15:14]

Reserved, RES0.

## CCITMIN, bits [11:0]

## When TRCIDR0.TRCCCI == '0':

Indicates the minimum value that can be programmed in TRCCCCTLR.THRESHOLD.

Reads as 0x000

Access to this field is RO.

## When TRCIDR0.TRCCCI == '1':

Indicates the minimum value that can be programmed in TRCCCCTLR.THRESHOLD.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCITMIN        | Meaning                                                          |
|----------------|------------------------------------------------------------------|
| 0x001 .. 0xFFF | The minimum value that can be programmed in TRCCCCTLR.THRESHOLD. |

The minimum value of this field is 0x001 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR3

Accesses to this register use the following encodings in the System register encoding space:

| EXLEVEL_S_EL1   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL1 is not implemented. |
| 0b1             | Secure EL1 is implemented.     |

MRS &lt;Xt&gt;, TRCIDR3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1011 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR3; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR3; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR3;
```

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

## D24.4.41 TRCIDR6, Trace ID Register 6

The TRCIDR6 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR6 bits [31:0] are architecturally mapped to External register TRCIDR6[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR6 are UNDEFINED.

## Attributes

TRCIDR6 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

Reserved, RES0.

## EXLEVEL\_RL\_EL2, bit [2]

Indicates if Realm EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_RL_EL2   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL2 is not implemented. |
| 0b1              | Realm EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_RL\_EL1, bit [1]

Indicates if Realm EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## EXLEVEL\_RL\_EL0, bit [0]

Indicates if Realm EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_RL_EL0   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL0 is not implemented. |
| 0b1              | Realm EL0 is implemented.     |

Access to this field is RO.

## Accessing TRCIDR6

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR6

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6; elsif PSTATE.EL == EL2 then
```

| EXLEVEL_RL_EL1   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL1 is not implemented. |
| 0b1              | Realm EL1 is implemented.     |

```
if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6;
```

## D24.4.42 TRCIDR7, Trace ID Register 7

The TRCIDR7 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR7 bits [31:0] are architecturally mapped to External register TRCIDR7[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR7 are UNDEFINED.

## Attributes

TRCIDR7 is a 64-bit register.

## Field descriptions

<!-- image -->

|   63 |   32 |
|------|------|
|   31 |    0 |

## Bits [63:0]

Reserved, RES0.

## Accessing TRCIDR7

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR7

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR7; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR7; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR7;
```

## D24.4.43 TRCIDR8, Trace ID Register 8

The TRCIDR8 characteristics are:

## Purpose

Returns the maximum speculation depth of the instruction trace element stream.

## Configuration

AArch64 System register TRCIDR8 bits [31:0] are architecturally mapped to External register TRCIDR8[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR8 are UNDEFINED.

## Attributes

TRCIDR8 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |         | 32   |
|------|---------|------|
|      | RES0    |      |
| 31   |         | 0    |
|      | MAXSPEC |      |

## Bits [63:32]

Reserved, RES0.

## MAXSPEC, bits [31:0]

Indicates the maximum speculation depth of the instruction trace element stream. This is the maximum number of P0 elements in the trace element stream that can be speculative at any time.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCIDR8

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR8

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED;
```

```
elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR8; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR8; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR8;
```

## D24.4.44 TRCIDR9, Trace ID Register 9

The TRCIDR9 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR9 bits [31:0] are architecturally mapped to External register TRCIDR9[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR9 are UNDEFINED.

## Attributes

TRCIDR9 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMP0KEY, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of P0 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR9

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR9

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR9; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR9; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR9;
```

## D24.4.45 TRCIMSPEC0, Trace IMP DEF Register 0

The TRCIMSPEC0 characteristics are:

## Purpose

TRCIMSPEC0 shows the presence of any IMPLEMENTATION DEFINED features, and provides an interface to enable the features that are provided.

## Configuration

AArch64 System register TRCIMSPEC0 bits [31:0] are architecturally mapped to External register TRCIMSPEC0[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIMSPEC0 are UNDEFINED.

## Attributes

TRCIMSPEC0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## EN, bits [7:4]

## When TRCIMSPEC0.SUPPORT != '0000':

Enable. Controls whether the IMPLEMENTATION DEFINED features are enabled.

| EN     | Meaning                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The IMPLEMENTATION DEFINED features are not enabled. The trace unit must behave as if the IMPLEMENTATION DEFINED features are not supported. |
| 0b0001 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0010 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0011 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0100 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0101 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0110 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0111 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b1000 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b1001 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |

| EN     | Meaning                                            |
|--------|----------------------------------------------------|
| 0b1010 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1011 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1100 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1101 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1110 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1111 | The trace unit behavior is IMPLEMENTATION DEFINED. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0000' .

## Otherwise:

Reserved, RES0.

## SUPPORT, bits [3:0]

Indicates whether the implementation supports IMPLEMENTATION DEFINED features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SUPPORT   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0000    | No IMPLEMENTATION DEFINED features are supported. |
| 0b0001    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0010    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0011    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0100    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0101    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0110    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0111    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1000    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1001    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1010    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1011    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1100    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1101    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1110    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1111    | IMPLEMENTATION DEFINED features are supported.    |

Use of nonzero values requires written permission from Arm.

Access to this field is RO.

## Accessing TRCIMSPEC0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIMSPEC0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCIMSPECn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0;
```

MSR TRCIMSPEC0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCIMSPECn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64];
```

## D24.4.46 TRCIMSPEC&lt;n&gt;, Trace IMP DEF Register &lt;n&gt;, n = 1 - 7

The TRCIMSPEC&lt;n&gt; characteristics are:

## Purpose

These registers might return information that is specific to an implementation, or enable features specific to an implementation to be programmed. The product Technical Reference Manual describes these registers.

## Configuration

AArch64 System register TRCIMSPEC&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCIMSPEC&lt;n&gt;[31:0].

This register is present only when an implementation implements TRCIMSPEC&lt;n&gt;, FEAT\_ETE is implemented, and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIMSPEC&lt;n&gt; are UNDEFINED.

## Attributes

TRCIMSPEC&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

This field reads as an IMPLEMENTATION DEFINED value and writes to this field have IMPLEMENTATION DEFINED behavior.

## Accessing TRCIMSPEC&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCIMSPEC<m> ; Where m = 1-7
```

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0 :m[2:0] | 0b111 |

```
integer m = UInt(CRm<2:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then
```

```
UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCIMSPECn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC[m];
```

MSR TRCIMSPEC&lt;m&gt;, &lt;Xt&gt; ; Where m = 1-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0 :m[2:0] | 0b111 |

```
integer m = UInt(CRm<2:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCIMSPECn == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC[m] = X[t, 64];
```

## D24.4.47 TRCIT, Trace Instrumentation

The TRCIT characteristics are:

## Purpose

Generates an instrumentation packet in the trace.

## Configuration

This system instruction is present only when FEAT\_ITE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCIT are UNDEFINED.

## Attributes

TRCIT is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| VALUE | VALUE | VALUE |
| 31    | 0     |       |
| VALUE | VALUE | VALUE |

## VALUE, bits [63:0]

Value to be included in the Instrumentation packet.

## Executing TRCIT

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TRCIT &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0010 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL1 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL2 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL3 then AArch64.TRCIT(X[t, 64]);
```

## D24.4.48 TRCITECR\_EL1, Instrumentation Trace Control Register (EL1)

The TRCITECR\_EL1 characteristics are:

## Purpose

Provides EL1 controls for Trace Instrumentation.

## Configuration

This register is present only when FEAT\_ITE is implemented, System register access to the trace unit registers is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCITECR\_EL1 are UNDEFINED.

## Attributes

TRCITECR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32      |
|------|---------|
| RES0 |         |
| RES0 | E1E E0E |

## Bits [63:2]

Reserved, RES0.

## E1E, bit [1]

EL1 Instrumentation Trace Enable.

| E1E   | Meaning                                      |
|-------|----------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL1.     |
| 0b1   | Instrumentation trace not prohibited at EL1. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0E, bit [0]

EL0 Instrumentation Trace Enable.

| E0E   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL0. |

0b1

Instrumentation trace not prohibited at EL0.

This field is ignored by the PE when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRCITECR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TRCITECR\_EL1 or TRCITECR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCITECR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x888]; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL2; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL1;
```

MSR TRCITECR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x888] = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRCITECR_EL2 = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRCITECR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x888]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRCITECR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TRCITECR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x888] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRCITECR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TRCITECR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.4.49 TRCITECR\_EL2, Instrumentation Trace Control Register (EL2)

The TRCITECR\_EL2 characteristics are:

## Purpose

Provides EL2 controls for Trace Instrumentation.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_ITE is implemented, System register access to the trace unit registers is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCITECR\_EL2 are UNDEFINED.

## Attributes

TRCITECR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## E2E, bit [1]

EL2 Instrumentation Trace Enable.

| E2E   | Meaning                                      |
|-------|----------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL2.     |
| 0b1   | Instrumentation trace not prohibited at EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0HE, bit [0]

EL0 Instrumentation Trace Enable.

| E0HE   | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0    | Instrumentation trace prohibited at EL0 when HCR_EL2.TGE == 1. |

| E0HE   | Meaning                                                            |
|--------|--------------------------------------------------------------------|
| 0b1    | Instrumentation trace not prohibited at EL0 when HCR_EL2.TGE == 1. |

This field is ignored by the PE when any of the following are true:

- HCR\_EL2.TGE == 0.
- EL2 is disabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRCITECR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name TRCITECR\_EL2 or TRCITECR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCITECR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRCITECR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL2; MSR TRCITECR_EL2, <Xt>
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRCITECR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, TRCITECR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x888]; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL2; else
```

```
X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL1;
```

MSR TRCITECR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x888] = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRCITECR_EL2 = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL1 = X[t, 64];
```

## D24.4.50 TRCITEEDCR, Instrumentation Trace Extension External Debug Control Register

The TRCITEEDCR characteristics are:

## Purpose

Controls instrumentation trace filtering.

## Configuration

AArch64 System register TRCITEEDCR bits [31:0] are architecturally mapped to External register TRCITEEDCR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and FEAT\_ITE is implemented. Otherwise, direct accesses to TRCITEEDCR are UNDEFINED.

## Attributes

TRCITEEDCR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      | 32    |
|---------|-------|
| RES0 31 | 1 0   |
| RES0    | E1 E0 |

## Bits [63:7]

Reserved, RES0.

## RL, bit [6]

## When FEAT\_RME is implemented:

Instrumentation Trace in Realm state.

| RL   | Meaning                                          |
|------|--------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Realm state. |
| 0b1  | Instrumentation trace permitted in Realm state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Realm state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S, bit [5]

## When Secure state is implemented:

Instrumentation Trace in Secure state.

<!-- image -->

| S   | Meaning                                           |
|-----|---------------------------------------------------|
| 0b0 | Instrumentation trace prohibited in Secure state. |
| 0b1 | Instrumentation trace permitted in Secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, this field is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.E3, and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

When FEAT\_RME is implemented, this field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NS, bit [4]

## When Any of Non-secure EL2, EL1, or EL0 are implemented:

Instrumentation Trace in Non-secure state.

| NS   | Meaning                                               |
|------|-------------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Non-secure state. |
| 0b1  | Instrumentation trace permitted in Non-secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Non-secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E3, bit [3]

## When EL3 is implemented:

Instrumentation Trace Enable at EL3.

| E3   | Meaning                                  |
|------|------------------------------------------|
| 0b0  | Instrumentation trace prohibited at EL3. |
| 0b1  | Instrumentation trace permitted at EL3.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.S to control whether Instrumentation trace is permitted or prohibited at EL3.

When FEAT\_RME is implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO to control whether Instrumentation trace is permitted or prohibited at EL3.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E&lt;m&gt;, bits [m], for m = 2 to 0

Instrumentation Trace Enable at EL&lt;m&gt;.

| E<m>   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | Instrumentation trace prohibited at EL<m>. |
| 0b1    | Instrumentation trace permitted at EL<m>.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This bit is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.NS, TRCITEEDCR.S, and TRCITEEDCR.RL to control whether Instrumentation trace is permitted or prohibited at EL&lt;m&gt; in the specified Security states.

TRCITEEDCR.E&lt;2&gt; is RES0 if EL2 is not implemented in any Security states.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCITEEDCR

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCITEEDCR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_ITE)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR;
```

MSR TRCITEEDCR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_ITE)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64];
```

## D24.4.51 TRCOSLSR, Trace OS Lock Status Register

The TRCOSLSR characteristics are:

## Purpose

Returns the status of the Trace OS Lock.

## Configuration

AArch64 System register TRCOSLSR bits [31:0] are architecturally mapped to External register TRCOSLSR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCOSLSR are UNDEFINED.

## Attributes

TRCOSLSR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## OSLM, bits [4:3, 0]

OS Lock model.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OSLM   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b000  | Trace OS Lock is not implemented.                                                     |
| 0b010  | Trace OS Lock is implemented.                                                         |
| 0b100  | Trace OS Lock is not implemented, and the trace unit is controlled by the PE OS Lock. |

All other values are reserved.

When FEAT\_ETE is implemented, the values 0b000 and 0b010 are not permitted.

Access to this field is RO.

## Bit [2]

Reserved, RES0.

## OSLK, bit [1]

OS Lock status.

| OSLK   | Meaning                  |
|--------|--------------------------|
| 0b0    | The OS Lock is unlocked. |
| 0b1    | The OS Lock is locked.   |

When FEAT\_ETE is implemented, this field indicates the state of the PE OS Lock.

When FEAT\_ETMv4 is implemented, this field indicates the state of the Trace OS Lock.

## Accessing TRCOSLSR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCOSLSR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCOSLSR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR;
```

## D24.4.52 TRCPRGCTLR, Trace Programming Control Register

The TRCPRGCTLR characteristics are:

## Purpose

Enables the trace unit.

## Configuration

AArch64 System register TRCPRGCTLR bits [31:0] are architecturally mapped to External register TRCPRGCTLR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCPRGCTLR are UNDEFINED.

## Attributes

TRCPRGCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
| RES0 |      |
| 31   | 1 0  |
| RES0 | EN   |

## Bits [63:1]

Reserved, RES0.

## EN, bit [0]

Trace unit enable.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

## Accessing TRCPRGCTLR

Must be programmed.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCPRGCTLR

| EN   | Meaning                     |
|------|-----------------------------|
| 0b0  | The trace unit is disabled. |
| 0b1  | The trace unit is enabled.  |

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCPRGCTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCPRGCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCPRGCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCPRGCTLR;
```

MSR TRCPRGCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCPRGCTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCPRGCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCPRGCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCPRGCTLR = X[t, 64];
```

## D24.4.53 TRCQCTLR, Trace Q Element Control Register

The TRCQCTLR characteristics are:

## Purpose

Controls when Q elements are enabled.

## Configuration

AArch64 System register TRCQCTLR bits [31:0] are architecturally mapped to External register TRCQCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR0.QFILT == '1'. Otherwise, direct accesses to TRCQCTLR are UNDEFINED.

## Attributes

TRCQCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:9]

Reserved, RES0.

## MODE,bit [8]

Selects whether the Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit is permitted to generate Q elements or address ranges where the trace unit is not permitted to generate Qelements:

| MODE   | Meaning                                                                                                                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Exclude mode. The Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit must not generate Qelements. If no ranges are selected, Qelements are permitted across the entire memory map. |
| 0b1    | Include Mode. The Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit can generate Qelements. If all the implemented bits in RANGEare set to 0 thenQ elements are disabled.         |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RANGE[&lt;m&gt;] , bits [m], for m = 7 to 0

Specifies whether Address Range Comparator &lt;m&gt; controls Q elements.

| RANGE[<m>]   | Meaning                                                                      |
|--------------|------------------------------------------------------------------------------|
| 0b0          | The address range that Address Range Comparator <m> defines is not selected. |
| 0b1          | The address range that Address Range Comparator <m> defines is selected.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCQCTLR

Must be programmed if TRCCONFIGR.QE != 0b00 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCQCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.QFILT == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

```
else X[t, 64] = TRCQCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCQCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCQCTLR;
```

MSR TRCQCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.QFILT == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCQCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCQCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCQCTLR = X[t, 64];
```

## D24.4.54 TRCRSCTLR&lt;n&gt;, Trace Resource Selection Control Register &lt;n&gt;, n = 2 - 31

The TRCRSCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the selection of the resources in the trace unit.

## Configuration

Resource selector 0 always returns FALSE.

Resource selector 1 always returns TRUE.

Resource selectors are implemented in pairs. Each odd numbered resource selector is part of a pair with the even numbered resource selector that is numbered as one less than it. For example, resource selectors 2 and 3 form a pair.

AArch64 System register TRCRSCTLR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCRSCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and ((UInt(TRCIDR4.NUMRSPAIR) + 1) * 2) &gt; n. Otherwise, direct accesses to TRCRSCTLR&lt;n&gt; are UNDEFINED.

## Attributes

TRCRSCTLR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:22]

Reserved, RES0.

## PAIRINV, bit [21]

When (n MOD 2) == 0:

Controls whether the combined result from a resource selector pair is inverted.

| PAIRINV   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0       | Do not invert the combined output of the 2 resource selectors. |
| 0b1       | Invert the combined output of the 2 resource selectors.        |

If:

- Ais the register TRCRSCTLR&lt;n&gt;.
- Bis the register TRCRSCTLR&lt;n+1&gt;.

Then the combined output of the 2 resource selectors A and B depends on the value of (A.PAIRINV , A.INV , B.INV) as follows:

- 0b000 -&gt; A and B.
- 0b001 -&gt; Reserved.
- 0b010 -&gt; not(A) and B.
- 0b011 -&gt; not(A) and not(B).
- 0b100 -&gt; not(A) or not(B).
- 0b101 -&gt; not(A) or B.
- 0b110 -&gt; Reserved.
- 0b111 -&gt; A or B.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## INV, bit [20]

Controls whether the resource, that TRCRSCTLR&lt;n&gt;.GROUP and TRCRSCTLR&lt;n&gt;.SELECT selects, is inverted.

| INV   | Meaning                                    |
|-------|--------------------------------------------|
| 0b0   | Do not invert the output of this selector. |
| 0b1   | Invert the output of this selector.        |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## GROUP, bits [19:16]

Selects a group of resources.

| GROUP   | Meaning                                 | SELECT                                                     |
|---------|-----------------------------------------|------------------------------------------------------------|
| 0b0000  | External Input Selectors.               | SELECT encoding for External Input Selectors               |
| 0b0001  | PE Comparator Inputs.                   | SELECT encoding for PE Comparator Inputs                   |
| 0b0010  | Counters and Sequencer.                 | SELECT encoding for Counters and Sequencer                 |
| 0b0011  | Single-shot Comparator Controls.        | SELECT encoding for Single-shot Comparator Controls        |
| 0b0100  | Single Address Comparators.             | SELECT encoding for Single Address Comparators             |
| 0b0101  | Address Range Comparators.              | SELECT encoding for Address Range Comparators              |
| 0b0110  | Context Identifier Comparators.         | SELECT encoding for Context Identifier Comparators         |
| 0b0111  | Virtual Context Identifier Comparators. | SELECT encoding for Virtual Context Identifier Comparators |

All other values are reserved.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT, bits [15:0]

Resource Specific Controls. Contains the controls specific to the resource group selected by GROUP, described in the following sections.

## SELECT encoding for External Input Selectors

<!-- image -->

| EXTIN[<m>]   | Meaning           |
|--------------|-------------------|
| 0b0          | Ignore EXTIN <m>. |
| 0b1          | Select EXTIN <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMEXTINSEL.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for PE Comparator Inputs

<!-- image -->

## Bits [15:8]

Reserved, RES0.

PECOMP[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs.

## Bits [15:4]

Reserved, RES0.

## EXTIN[&lt;m&gt;] , bits [m], for m = 3 to 0

Selects one or more External Inputs.

## Bits [15:8]

Reserved, RES0.

## SEQUENCER[&lt;m&gt;] , bits [m+4], for m = 3 to 0

Sequencer states.

| PECOMP[<m>]   | Meaning                         |
|---------------|---------------------------------|
| 0b0           | Ignore PE Comparator Input <m>. |
| 0b1           | Select PE Comparator Input <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Counters and Sequencer

<!-- image -->

| SEQUENCER[<m>]   | Meaning                     |
|------------------|-----------------------------|
| 0b0              | Ignore Sequencer state <m>. |
| 0b1              | Select Sequencer state <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMSEQSTATE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

COUNTERS[&lt;m&gt;] , bits [m], for m = 3 to 0

Counters resources at zero.

## Bits [15:8]

Reserved, RES0.

## SINGLE\_SHOT[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Single-shot Comparator Controls.

| SINGLE_SHOT[<m>]   | Meaning                                    |
|--------------------|--------------------------------------------|
| 0b0                | Ignore Single-shot Comparator Control <m>. |
| 0b1                | Select Single-shot Comparator Control <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMSSCC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single Address Comparators

| COUNTERS[<m>]   | Meaning                     |
|-----------------|-----------------------------|
| 0b0             | Ignore Counter <m>.         |
| 0b1             | Select Counter <m> is zero. |

This bit is RES0 if m &gt;= TRCIDR5.NUMCNTR.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single-shot Comparator Controls

<!-- image -->

## Bits [15:8]

Reserved, RES0.

ARC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Address Range Comparators.

| ARC[<m>]   | Meaning                              |
|------------|--------------------------------------|
| 0b0        | Ignore Address Range Comparator <m>. |
| 0b1        | Select Address Range Comparator <m>. |

<!-- image -->

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators.

| SAC[<m>]   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | Ignore Single Address Comparator <m>. |
| 0b1        | Select Single Address Comparator <m>. |

This bit is RES0 if m &gt;= 2 × TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Address Range Comparators

<!-- image -->

This bit is RES0 if m &gt;= TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

## CID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Context Identifier Comparators.

| CID[<m>]   | Meaning                                   |
|------------|-------------------------------------------|
| 0b0        | Ignore Context Identifier Comparator <m>. |
| 0b1        | Select Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMCIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Virtual Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

VMID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Virtual Context Identifier Comparators.

| VMID[<m>]   | Meaning                                           |
|-------------|---------------------------------------------------|
| 0b0         | Ignore Virtual Context Identifier Comparator <m>. |
| 0b1         | Select Virtual Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMVMIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCRSCTLR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n/2.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n/2.
- TRCEVENTCTL0R.EVENT0.TYPE == 0 and TRCEVENTCTL0R.EVENT0.SEL == n.
- TRCEVENTCTL0R.EVENT0.TYPE == 1 and TRCEVENTCTL0R.EVENT0.SEL == n/2.
- TRCEVENTCTL0R.EVENT1.TYPE == 0 and TRCEVENTCTL0R.EVENT1.SEL == n.
- TRCEVENTCTL0R.EVENT1.TYPE == 1 and TRCEVENTCTL0R.EVENT1.SEL == n/2.
- TRCEVENTCTL0R.EVENT2.TYPE == 0 and TRCEVENTCTL0R.EVENT2.SEL == n.
- TRCEVENTCTL0R.EVENT2.TYPE == 1 and TRCEVENTCTL0R.EVENT2.SEL == n/2.
- TRCEVENTCTL0R.EVENT3.TYPE == 0 and TRCEVENTCTL0R.EVENT3.SEL == n.
- TRCEVENTCTL0R.EVENT3.TYPE == 1 and TRCEVENTCTL0R.EVENT3.SEL == n/2.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 0 and TRCSEQEVR&lt;a&gt;.B.SEL = n.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 1 and TRCSEQEVR&lt;a&gt;.B.SEL = n/2.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 0 and TRCSEQEVR&lt;a&gt;.F.SEL = n.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 1 and TRCSEQEVR&lt;a&gt;.F.SEL = n/2.
- TRCSEQRSTEVR.RST.TYPE == 0 and TRCSEQRSTEVR.RST.SEL == n.
- TRCSEQRSTEVR.RST.TYPE == 1 and TRCSEQRSTEVR.RST.SEL == n/2.
- TRCTSCTLR.EVENT.TYPE == 0 and TRCTSCTLR.EVENT.SEL == n.
- TRCTSCTLR.EVENT.TYPE == 1 and TRCTSCTLR.EVENT.SEL == n/2.
- TRCVICTLR.EVENT.TYPE == 0 and TRCVICTLR.EVENT.SEL == n.
- TRCVICTLR.EVENT.TYPE == 1 and TRCVICTLR.EVENT.SEL == n/2.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCRSCTLR<m> ; Where m = 2-31
```

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b0001 | m[3:0] | 0b00 :m[4] |

```
integer m = UInt(op2<0>:CRm<3:0>); if m >= NUM_TRACE_RESOURCE_SELECTOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED;
```

```
elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m];
```

MSR TRCRSCTLR&lt;m&gt;, &lt;Xt&gt; ; Where m = 2-31

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b0001 | m[3:0] | 0b00 :m[4] |

```
integer m = UInt(op2<0>:CRm<3:0>); if m >= NUM_TRACE_RESOURCE_SELECTOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64];
```

## D24.4.55 TRCRSR, Trace Resources Status Register

The TRCRSR characteristics are:

## Purpose

Use this to set, or read, the status of the resources.

## Configuration

AArch64 System register TRCRSR bits [31:0] are architecturally mapped to External register TRCRSR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCRSR are UNDEFINED.

## Attributes

TRCRSR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:13]

Reserved, RES0.

## TA, bit [12]

Tracing active.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

EVENT[&lt;m&gt;] , bits [m+8], for m = 3 to 0

Untraced status of ETEEvents.

| TA   | Meaning                |
|------|------------------------|
| 0b0  | Tracing is not active. |
| 0b1  | Tracing is active.     |

| EVENT[<m>]   | Meaning                                                                    |
|--------------|----------------------------------------------------------------------------|
| 0b0          | An ETEEvent <m> has not occurred.                                          |
| 0b1          | An ETEEvent <m> has occurred while the resources were in the Paused state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When TRCIDR4.NUMRSPAIR == '0000', access to this field is RES0.
- Access to this field is RES0 if all of the following are true:
- TRCIDR4.NUMRSPAIR != '0000'
- m&gt;UInt(TRCIDR0.NUMEVENT)
- Otherwise, access to this field is RW.

## Bits [7:4]

Reserved, RES0.

## EXTIN[&lt;m&gt;] , bits [m], for m = 3 to 0

The sticky status of the External Input Selectors.

| EXTIN[<m>]   | Meaning                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0          | An event selected by External Input Selector <m> has not occurred.                                                    |
| 0b1          | At least one event selected by External Input Selector <m> has occurred while the resources were in the Paused state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR5.NUMEXTINSEL), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCRSR

Must always be programmed.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCRSR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1010 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSR;
```

MSR TRCRSR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1010 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSR = X[t, 64];
```

## D24.4.56 TRCSEQEVR&lt;n&gt;, Trace Sequencer State Transition Control Register &lt;n&gt;, n = 0 - 2

The TRCSEQEVR&lt;n&gt; characteristics are:

## Purpose

Moves the Sequencer state:

- Backwards, from state n+1 to state n when a programmed resource event occurs.
- Forwards, from state n to state n+1 when a programmed resource event occurs.

## Configuration

AArch64 System register TRCSEQEVR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSEQEVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQEVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSEQEVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## B\_TYPE, bit [15]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Chooses the type of Resource Selector.

| B_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.B.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.B.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.B.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## B\_SEL, bits [12:8]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.B.TYPE controls whether TRCSEQEVR.B.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## F\_TYPE, bit [7]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Chooses the type of Resource Selector.

| F_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.F.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.F.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.F.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## F\_SEL, bits [4:0]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.F.TYPE controls whether TRCSEQEVR.F.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQEVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCSEQEVR<m> ; Where m = 0-2
```

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m];
```

```
elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m];
```

MSR TRCSEQEVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-2

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQEVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQEVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else
```

## D24.4.57 TRCSEQRSTEVR, Trace Sequencer Reset Control Register

The TRCSEQRSTEVR characteristics are:

## Purpose

Moves the Sequencer to state 0 when a programmed resource event occurs.

## Configuration

AArch64 System register TRCSEQRSTEVR bits [31:0] are architecturally mapped to External register TRCSEQRSTEVR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQRSTEVR are UNDEFINED.

## Attributes

TRCSEQRSTEVR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## RST\_TYPE, bit [7]

Reset field. Selects an event that causes the Sequencer to move to state 0.

Chooses the type of Resource Selector.

| RST_TYPE   | Meaning                                                                                                                                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Asingle Resource Selector. TRCSEQRSTEVR.RST.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                     |
| 0b1        | ABoolean-combined pair of Resource Selectors. TRCSEQRSTEVR.RST.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQRSTEVR.RST.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## RST\_SEL, bits [4:0]

Reset field. Selects an event that causes the Sequencer to move to state 0.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQRSTEVR.RST.TYPE controls whether TRCSEQRSTEVR.RST.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQRSTEVR

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSEQRSTEVR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0110 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR5.NUMSEQSTATE != ↪ → '000') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQRSTEVR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQRSTEVR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQRSTEVR;
```

MSR TRCSEQRSTEVR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0110 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR5.NUMSEQSTATE != ↪ → '000') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQRSTEVR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQRSTEVR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQRSTEVR = X[t, 64];
```

## D24.4.58 TRCSEQSTR, Trace Sequencer State Register

The TRCSEQSTR characteristics are:

## Purpose

Use this to set, or read, the Sequencer state.

## Configuration

AArch64 System register TRCSEQSTR bits [31:0] are architecturally mapped to External register TRCSEQSTR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQSTR are UNDEFINED.

## Attributes

TRCSEQSTR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## STATE, bits [1:0]

Set or returns the state of the Sequencer.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQSTR

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

| STATE   | Meaning   |
|---------|-----------|
| 0b00    | State 0.  |
| 0b01    | State 1.  |
| 0b10    | State 2.  |
| 0b11    | State 3.  |

MRS &lt;Xt&gt;, TRCSEQSTR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0111 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR5.NUMSEQSTATE != ↪ → '000') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCSEQSTR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQSTR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQSTR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQSTR;
```

MSR TRCSEQSTR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0111 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR5.NUMSEQSTATE != ↪ → '000') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCSEQSTR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQSTR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQSTR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQSTR = X[t, 64];
```

## D24.4.59 TRCSSCCR&lt;n&gt;, Trace Single-shot Comparator Control Register &lt;n&gt;, n = 0 - 7

The TRCSSCCR&lt;n&gt; characteristics are:

## Purpose

Controls the corresponding Single-shot Comparator Control resource.

## Configuration

AArch64 System register TRCSSCCR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSCCR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCCR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSCCR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:25]

Reserved, RES0.

## RST, bit [24]

Selects the Single-shot Comparator Control mode.

| RST   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | The Single-shot Comparator Control is in single-shot mode. |
| 0b1   | The Single-shot Comparator Control is in multi-shot mode.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## ARC[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Selects one or more Address Range Comparators for Single-shot control.

| ARC[<m>]   | Meaning                                                                    |
|------------|----------------------------------------------------------------------------|
| 0b0        | The Address Range Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Address Range Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators for Single-shot control.

| SAC[<m>]   | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
| 0b0        | The Single Address Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Single Address Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCSSCCR&lt;n&gt;

Must be programmed if any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSCCR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m];
```

MSR TRCSSCCR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64];
```

## D24.4.60 TRCSSCSR&lt;n&gt;, Trace Single-shot Comparator Control Status Register &lt;n&gt;, n = 0 - 7

The TRCSSCSR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

AArch64 System register TRCSSCSR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSCSR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCSR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSCSR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## STATUS, bit [31]

Single-shot Comparator Control status. Indicates if any of the comparators selected by this Single-shot Comparator control have matched. The selected comparators are defined by TRCSSCCR&lt;n&gt;.ARC, TRCSSCCR&lt;n&gt;.SAC, and TRCSSPCICR&lt;n&gt;.PC.

| STATUS   | Meaning                                                                                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | No match has occurred. When the first match occurs, this field takes a value of 1. It remains at 1 until explicitly modified by a write to this register.                                                          |
| 0b1      | One or more matches has occurred. If TRCSSCCR<n>.RST == 0 then: • There is only one match and no more matches are possible. • Software must reset this field to 0 to re-enable the Single-shot Comparator Control. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## PENDING, bit [30]

Single-shot pending status. The Single-shot Comparator Control fired while the resources were in the Paused state.

The reset behavior of this field is:

· On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [29:4]

Reserved, RES0.

## PC, bit [3]

PE Comparator Input support. Indicates if the Single-shot Comparator Control supports PE Comparator Inputs.

| PC   | Meaning                                                                                                                                                                                                                                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support PE Comparator Inputs. Selecting any PE Comparator Inputs using the associated TRCSSPCICR<n> results in CONSTRAINED UNPREDICTABLE behavior of the Single-shot Comparator Control resource. The Single-shot Comparator Control might match unexpectedly or might not match. |
| 0b1  | This Single-shot Comparator Control supports PE Comparator Inputs.                                                                                                                                                                                                                                                             |

Access to this field is RO.

## DV, bit [2]

Data value comparator support. Data value comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| DV   | Meaning                                                                      |
|------|------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data value comparisons. |
| 0b1  | This Single-shot Comparator Control supports data value comparisons.         |

This field reads as 0.

Access to this field is RO.

## DA, bit [1]

Data Address Comparator support. Data address comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| PENDING   | Meaning                           |
|-----------|-----------------------------------|
| 0b0       | No match has occurred.            |
| 0b1       | One or more matches has occurred. |

| DA   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data address comparisons. |
| 0b1  | This Single-shot Comparator Control supports data address comparisons.         |

This field reads as 0.

Access to this field is RO.

## INST, bit [0]

Instruction Address Comparator support. Indicates if the Single-shot Comparator Control supports instruction address comparisons.

| INST   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b0    | This Single-shot Comparator Control does not support instruction address comparisons. |
| 0b1    | This Single-shot Comparator Control supports instruction address comparisons.         |

This field reads as 1.

Access to this field is RO.

## Accessing TRCSSCSR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSCSR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b1 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCSSCSRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m];
```

MSR TRCSSCSR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b1 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCSSCSRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64];
```

## D24.4.61 TRCSSPCICR&lt;n&gt;, Trace Single-shot Processing Element Comparator Input Control Register &lt;n&gt;, n = 0 - 7

The TRCSSPCICR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

AArch64 System register TRCSSPCICR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSPCICR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMSSCC) &gt; n, UInt(TRCIDR4.NUMPC) &gt; 0, and TRCSSCSR&lt;n&gt;.PC == '1'. Otherwise, direct accesses to TRCSSPCICR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSPCICR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## PC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs for Single-shot control.

| PC[<m>]   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | The single PE Comparator Input <m>, is not selected as for Single-shot control. |
| 0b1       | The single PE Comparator Input <m>, is selected as for Single-shot control.     |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSSPCICR&lt;n&gt;

Must be programmed if implemented and any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSPCICR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b011 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m];
```

MSR TRCSSPCICR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b011 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64];
```

## D24.4.62 TRCSTALLCTLR, Trace Stall Control Register

The TRCSTALLCTLR characteristics are:

## Purpose

Enables trace unit functionality that prevents trace unit buffer overflows.

## Configuration

AArch64 System register TRCSTALLCTLR bits [31:0] are architecturally mapped to External register TRCSTALLCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR3.STALLCTL == '1'. Otherwise, direct accesses to TRCSTALLCTLR are UNDEFINED.

## Attributes

TRCSTALLCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:14]

Reserved, RES0.

## NOOVERFLOW,bit [13]

## When TRCIDR3.NOOVERFLOW == '1':

Trace overflow prevention.

| NOOVERFLOW   | Meaning                                            |
|--------------|----------------------------------------------------|
| 0b0          | Trace unit buffer overflow prevention is disabled. |
| 0b1          | Trace unit buffer overflow prevention is enabled.  |

Note

Enabling this feature might cause a significant performance impact.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [12:9]

Reserved, RES0.

## ISTALL, bit [8]

Instruction stall control. Controls if a trace unit can stall the PE when the trace buffer space is less than LEVEL.

| ISTALL   | Meaning                               |
|----------|---------------------------------------|
| 0b0      | The trace unit must not stall the PE. |
| 0b1      | The trace unit can stall the PE.      |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [7:4]

Reserved, RES0.

## LEVEL, bits [3:0]

Threshold level field. The field can support 16 monotonic levels from 0b0000 to 0b1111 .

The value 0b0000 defines the Minimal invasion level. This setting has a greater risk of a trace unit buffer overflow.

The value 0b1111 defines the Maximum invasion level. This setting has a reduced risk of a trace unit buffer overflow.

Note

For some implementations, invasion might occur at the minimal invasion level.

One or more of the least significant bits of LEVEL are permitted to be RES0. Arm recommends that LEVEL[3:2] are fully implemented. Arm strongly recommends that LEVEL[3] is always implemented. If one or more bits are RES0 and are written with a nonzero value, the effective value of LEVEL is rounded down to the nearest power of 2 value which has the RES0 bits as zero. For example, if LEVEL[1:0] are RES0 and a value of 0b1110 is written to LEVEL, the effective value of LEVEL is 0b1100 .

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSTALLCTLR

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSTALLCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1011 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR3.STALLCTL == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSTALLCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSTALLCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSTALLCTLR;
```

MSR TRCSTALLCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1011 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR3.STALLCTL == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSTALLCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSTALLCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSTALLCTLR = X[t, 64];
```

## D24.4.63 TRCSTATR, Trace Status Register

The TRCSTATR characteristics are:

## Purpose

Returns the trace unit status.

## Configuration

AArch64 System register TRCSTATR bits [31:0] are architecturally mapped to External register TRCSTATR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCSTATR are UNDEFINED.

## Attributes

TRCSTATR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## PMSTABLE, bit [1]

Programmers' model stable.

| PMSTABLE   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | The programmers' model is not stable. |
| 0b1        | The programmers' model is stable.     |

Accessing this field has the following behavior:

- When the trace unit is enabled, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## IDLE, bit [0]

Idle status.

## Accessing TRCSTATR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSTATR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0011 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCSTATR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSTATR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSTATR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

| IDLE   | Meaning                     |
|--------|-----------------------------|
| 0b0    | The trace unit is not idle. |
| 0b1    | The trace unit is idle.     |

else

X[t, 64] = TRCSTATR;

## D24.4.64 TRCSYNCPR, Trace Synchronization Period Register

The TRCSYNCPR characteristics are:

## Purpose

Controls how often trace protocol synchronization requests occur.

## Configuration

AArch64 System register TRCSYNCPR bits [31:0] are architecturally mapped to External register TRCSYNCPR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCSYNCPR are UNDEFINED.

## Attributes

TRCSYNCPR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## PERIOD, bits [4:0]

Defines the number of bytes of trace between each periodic trace protocol synchronization request.

| PERIOD   | Meaning                                                                  |
|----------|--------------------------------------------------------------------------|
| 0b00000  | Trace protocol synchronization is disabled.                              |
| 0b01000  | Trace protocol synchronization request occurs after 2 8 bytes of trace.  |
| 0b01001  | Trace protocol synchronization request occurs after 2 9 bytes of trace.  |
| 0b01010  | Trace protocol synchronization request occurs after 2 10 bytes of trace. |
| 0b01011  | Trace protocol synchronization request occurs after 2 11 bytes of trace. |
| 0b01100  | Trace protocol synchronization request occurs after 2 12 bytes of trace. |
| 0b01101  | Trace protocol synchronization request occurs after 2 13 bytes of trace. |
| 0b01110  | Trace protocol synchronization request occurs after 2 14 bytes of trace. |
| 0b01111  | Trace protocol synchronization request occurs after 2 15 bytes of trace. |
| 0b10000  | Trace protocol synchronization request occurs after 2 16 bytes of trace. |
| 0b10001  | Trace protocol synchronization request occurs after 2 17 bytes of trace. |
| 0b10010  | Trace protocol synchronization request occurs after 2 18 bytes of trace. |

| PERIOD   | Meaning                                                                  |
|----------|--------------------------------------------------------------------------|
| 0b10011  | Trace protocol synchronization request occurs after 2 19 bytes of trace. |
| 0b10100  | Trace protocol synchronization request occurs after 2 20 bytes of trace. |

Other values are reserved. If a reserved value is programmed into PERIOD, then the behavior of the synchronization period counter is CONSTRAINED UNPREDICTABLE and one of the following behaviors occurs:

- No trace protocol synchronization requests are generated by this counter.
- Trace protocol synchronization requests occur at the specified period.
- Trace protocol synchronization requests occur at some other UNKNOWN period which can vary.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSYNCPR

Must be programmed if TRCIDR3.SYNCPR == 0.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSYNCPR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSYNCPR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSYNCPR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSYNCPR;
```

MSR TRCSYNCPR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSYNCPR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

```
else TRCSYNCPR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSYNCPR = X[t, 64];
```

## D24.4.65 TRCTRACEIDR, Trace ID Register

The TRCTRACEIDR characteristics are:

## Purpose

Sets the trace ID for instruction trace.

## Configuration

AArch64 System register TRCTRACEIDR bits [31:0] are architecturally mapped to External register TRCTRACEIDR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCTRACEIDR are UNDEFINED.

## Attributes

TRCTRACEIDR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:7]

Reserved, RES0.

## TRACEID, bits [6:0]

Trace ID field. Sets the trace ID value for instruction trace. The width of the field is indicated by the value of TRCIDR5.TRACEIDSIZE. Unimplemented bits are RES0.

If an implementation supports AMBA ATB, then:

- The width of the field is 7 bits.
- Writing a reserved trace ID value does not affect behavior of the trace unit but it might cause UNPREDICTABLE behavior of the trace capture infrastructure.

See the AMBA ATB Protocol Specification for information about which ATID values are reserved.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCTRACEIDR

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCTRACEIDR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTRACEIDR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTRACEIDR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTRACEIDR;
```

MSR TRCTRACEIDR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTRACEIDR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTRACEIDR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTRACEIDR = X[t, 64];
```

## D24.4.66 TRCTSCTLR, Trace Timestamp Control Register

The TRCTSCTLR characteristics are:

## Purpose

Controls the insertion of global timestamps in the trace stream.

## Configuration

AArch64 System register TRCTSCTLR bits [31:0] are architecturally mapped to External register TRCTSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR0.TSSIZE != '00000'. Otherwise, direct accesses to TRCTSCTLR are UNDEFINED.

## Attributes

TRCTSCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## EVENT\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT_TYPE   | Meaning                                                                                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Asingle Resource Selector. TRCTSCTLR.EVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                    |
| 0b1          | ABoolean-combined pair of Resource Selectors. TRCTSCTLR.EVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCTSCTLR.EVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## EVENT\_SEL, bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

Defines the selected Resource Selector or pair of Resource Selectors. TRCTSCTLR.EVENT.TYPE controls whether TRCTSCTLR.EVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TRCTSCTLR

Must be programmed if TRCCONFIGR.TS == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCTSCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TSSIZE != '00000') ↪ → then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTSCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTSCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCTSCTLR;
```

MSR TRCTSCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && TRCIDR0.TSSIZE != '00000') ↪ → then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTSCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTSCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCTSCTLR = X[t, 64];
```

## D24.4.67 TRCVICTLR, Trace ViewInst Main Control Register

The TRCVICTLR characteristics are:

## Purpose

Controls instruction trace filtering.

## Configuration

AArch64 System register TRCVICTLR bits [31:0] are architecturally mapped to External register TRCVICTLR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCVICTLR are UNDEFINED.

## Attributes

TRCVICTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:27]

Reserved, RES0.

## EXLEVEL\_RL\_EL2, bit [26]

## When FEAT\_RME is implemented:

Filter instruction trace for EL2 in Realm state.

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL2 is 0 the trace unit generates instruction trace for EL2 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL2 is 1 the trace unit does not generate instruction trace for EL2 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL2 is 0 the trace unit does not generate instruction trace for EL2 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL2 is 1 the trace unit generates instruction trace for EL2 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL1, bit [25]

## When FEAT\_RME is implemented:

Filter instruction trace for EL1 in Realm state.

| EXLEVEL_RL_EL1   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL1 is 0 the trace unit generates instruction trace for EL1 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL1 is 1 the trace unit does not generate instruction trace for EL1 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL1 is 0 the trace unit does not generate instruction trace for EL1 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL1 is 1 the trace unit generates instruction trace for EL1 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL0, bit [24]

## When FEAT\_RME is implemented:

Filter instruction trace for EL0 in Realm state.

| EXLEVEL_RL_EL0   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL0 is 0 the trace unit generates instruction trace for EL0 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL0 is 1 the trace unit does not generate instruction trace for EL0 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL0 is 0 the trace unit does not generate instruction trace for EL0 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL0 is 1 the trace unit generates instruction trace for EL0 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [23]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [22]

## When Non-secure EL2 is implemented:

Filter instruction trace for EL2 in Non-secure state.

| EXLEVEL_NS_EL2   | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL2 in Non-secure state.         |
| 0b1              | The trace unit does not generate instruction trace for EL2 in Non-secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL1, bit [21]

## When Non-secure EL1 is implemented:

Filter instruction trace for EL1 in Non-secure state.

| EXLEVEL_NS_EL1   | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL1 in Non-secure state.         |
| 0b1              | The trace unit does not generate instruction trace for EL1 in Non-secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL0, bit [20]

## When Non-secure EL0 is implemented:

Filter instruction trace for EL0 in Non-secure state.

| EXLEVEL_NS_EL0   | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL0 in Non-secure state.         |
| 0b1              | The trace unit does not generate instruction trace for EL0 in Non-secure state. |

## The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL3, bit [19]

## When EL3 is implemented:

Filter instruction trace for EL3.

| EXLEVEL_S_EL3   | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL3.         |
| 0b1             | The trace unit does not generate instruction trace for EL3. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL2, bit [18]

## When Secure EL2 is implemented:

Filter instruction trace for EL2 in Secure state.

| EXLEVEL_S_EL2   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL2 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL2 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL1, bit [17]

## When Secure EL1 is implemented:

Filter instruction trace for EL1 in Secure state.

| EXLEVEL_S_EL1   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL1 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL1 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL0, bit [16]

## When Secure EL0 is implemented:

Filter instruction trace for EL0 in Secure state.

| EXLEVEL_S_EL0   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL0 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL0 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:12]

Reserved, RES0.

## TRCERR, bit [11]

When TRCIDR3.TRCERR == '1':

Controls the forced tracing of System Error exceptions.

| TRCERR   | Meaning                                                |
|----------|--------------------------------------------------------|
| 0b0      | Forced tracing of System Error exceptions is disabled. |
| 0b1      | Forced tracing of System Error exceptions is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCRESET, bit [10]

Controls the forced tracing of PE Resets.

| TRCRESET   | Meaning                                  |
|------------|------------------------------------------|
| 0b0        | Forced tracing of PE Resets is disabled. |
| 0b1        | Forced tracing of PE Resets is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SSSTATUS, bit [9]

ViewInst start/stop function status.

| SSSTATUS   | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| 0b0        | Stopped State. The ViewInst start/stop function is in the stopped state. |
| 0b1        | Started State. The ViewInst start/stop function is in the started state. |

Before software enables the trace unit, it must write to this field to set the initial state of the ViewInst start/stop function. If the ViewInst start/stop function is not used then set this field to 1. Arm recommends that the value of this field is set before each trace session begins.

If the trace unit becomes disabled while a start point or stop point is still speculative, then the value of TRCVICTLR.SSSTATUS is UNKNOWN and might represent the result of a speculative start point or stop point.

If software which is running on the PE being traced disables the trace unit, either by clearing TRCPRGCTLR.EN or locking the OS Lock, Arm recommends that a DSB and an ISB instruction are executed before disabling the trace unit to prevent any start points or stop points being speculative at the point of disabling the trace unit. This procedure assumes that all start points or stop points occur before the barrier instructions are executed. The procedure does not guarantee that there are no speculative start points or stop points when disabling, although it helps minimize the probability.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES1 if all of the following are true:
- TRCIDR4.NUMACPAIRS == '0000'
- TRCIDR4.NUMPC == '0000'
- Otherwise, access to this field is RW.

## Bit [8]

Reserved, RES0.

## EVENT\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT_TYPE   | Meaning                                                                                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Asingle Resource Selector. TRCVICTLR.EVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                    |
| 0b1          | ABoolean-combined pair of Resource Selectors. TRCVICTLR.EVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCVICTLR.EVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## Bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

## EVENT\_SEL, bits [4:0]

Defines the selected Resource Selector or pair of Resource Selectors. TRCVICTLR.EVENT.TYPE controls whether TRCVICTLR.EVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## When TRCIDR4.NUMRSPAIR == '0000':

## Reserved, bits [4:0]

This field is reserved:

- Bits [4:1] are RES0.
- Bit [0] is RES1.

## Otherwise:

Reserved, RES0.

## Accessing TRCVICTLR

Must be programmed.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVICTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCVICTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVICTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else
```

```
X[t, 64] = TRCVICTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVICTLR;
```

MSR TRCVICTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCVICTLR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVICTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVICTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess);
```

else

TRCVICTLR = X[t, 64];

## D24.4.68 TRCVIIECTLR, Trace ViewInst Include/Exclude Control Register

The TRCVIIECTLR characteristics are:

## Purpose

Use this to select, or read, the Address Range Comparators for the ViewInst include/exclude function.

## Configuration

AArch64 System register TRCVIIECTLR bits [31:0] are architecturally mapped to External register TRCVIIECTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCVIIECTLR are UNDEFINED.

## Attributes

TRCVIIECTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## EXCLUDE[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Exclude Address Range Comparator &lt;m&gt;. Selects whether Address Range Comparator &lt;m&gt; is in use with the ViewInst exclude function.

| EXCLUDE[<m>]   | Meaning                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| 0b0            | The address range that Address Range Comparator <m> defines, is not selected for the ViewInst exclude function. |
| 0b1            | The address range that Address Range Comparator <m> defines, is selected for the ViewInst exclude function.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.

- Otherwise, access to this field is RW.

## Bits [15:8]

Reserved, RES0.

## INCLUDE[&lt;m&gt;] , bits [m], for m = 7 to 0

Include Address Range Comparator &lt;m&gt;.

Selects whether Address Range Comparator &lt;m&gt; is in use with the ViewInst include function.

Selecting no comparators for the ViewInst include function indicates that all instructions are included by default.

The ViewInst exclude function then indicates which ranges are excluded.

| INCLUDE[<m>]   | Meaning                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| 0b0            | The address range that Address Range Comparator <m> defines, is not selected for the ViewInst include function. |
| 0b1            | The address range that Address Range Comparator <m> defines, is selected for the ViewInst include function.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVIIECTLR

Must be programmed if TRCIDR4.NUMACPAIRS &gt; 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVIIECTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMACPAIRS) > ↪ → 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIIECTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIIECTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIIECTLR;
```

MSR TRCVIIECTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMACPAIRS) > ↪ → 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIIECTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIIECTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIIECTLR = X[t, 64];
```

## D24.4.69 TRCVIPCSSCTLR, Trace ViewInst Start/Stop PE Comparator Control Register

The TRCVIPCSSCTLR characteristics are:

## Purpose

Use this to select, or read, which PE Comparator Inputs can control the ViewInst start/stop function.

## Configuration

AArch64 System register TRCVIPCSSCTLR bits [31:0] are architecturally mapped to External register TRCVIPCSSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMPC) &gt; 0. Otherwise, direct accesses to TRCVIPCSSCTLR are UNDEFINED.

## Attributes

TRCVIPCSSCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## STOP[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Selects whether PE Comparator Input &lt;m&gt; is in use with the ViewInst start/stop function for the purpose of stopping trace.

| STOP[<m>]   | Meaning                                                         |
|-------------|-----------------------------------------------------------------|
| 0b0         | The PE Comparator Input <m> is not selected as a stop resource. |
| 0b1         | The PE Comparator Input <m> is selected as a stop resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMPC), access to this field is RES0.

- Otherwise, access to this field is RW.

## Bits [15:8]

Reserved, RES0.

## START[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects whether PE Comparator Input &lt;m&gt; is in use with the ViewInst start/stop function for the purpose of starting trace.

| START[<m>]   | Meaning                                                          |
|--------------|------------------------------------------------------------------|
| 0b0          | The PE Comparator Input <m> is not selected as a start resource. |
| 0b1          | The PE Comparator Input <m> is selected as a start resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMPC), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVIPCSSCTLR

Must be programmed if TRCIDR4.NUMPC != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVIPCSSCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMPC) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIPCSSCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIPCSSCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVIPCSSCTLR;
```

MSR TRCVIPCSSCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMPC) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIPCSSCTLR = X[t, 64];
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIPCSSCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVIPCSSCTLR = X[t, 64];
```

## D24.4.70 TRCVISSCTLR, Trace ViewInst Start/Stop Control Register

The TRCVISSCTLR characteristics are:

## Purpose

Use this to select, or read, the Single Address Comparators for the ViewInst start/stop function.

## Configuration

AArch64 System register TRCVISSCTLR bits [31:0] are architecturally mapped to External register TRCVISSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCVISSCTLR are UNDEFINED.

## Attributes

TRCVISSCTLR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## STOP[&lt;m&gt;] , bits [m+16], for m = 15 to 0

Selects whether Single Address Comparator &lt;m&gt; is used with the ViewInst start/stop function for the purpose of stopping trace.

| STOP[<m>]   | Meaning                                                               |
|-------------|-----------------------------------------------------------------------|
| 0b0         | The Single Address Comparator <m> is not selected as a stop resource. |
| 0b1         | The Single Address Comparator <m> is selected as a stop resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## START[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects whether Single Address Comparator &lt;m&gt; is used with the ViewInst start/stop function for the purpose of starting trace.

| START[<m>]   | Meaning                                                                |
|--------------|------------------------------------------------------------------------|
| 0b0          | The Single Address Comparator <m> is not selected as a start resource. |
| 0b1          | The Single Address Comparator <m> is selected as a start resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVISSCTLR

Must be programmed if TRCIDR4.NUMACPAIRS &gt; 0b0000 .

For any 2 comparators selected for the ViewInst start/stop function, the comparator containing the lower address must be a lower numbered comparator.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVISSCTLR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMACPAIRS) > ↪ → 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVISSCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVISSCTLR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVISSCTLR;
```

MSR TRCVISSCTLR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMACPAIRS) > ↪ → 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVISSCTLR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVISSCTLR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVISSCTLR = X[t, 64];
```

## D24.4.71 TRCVMIDCCTLR0, Trace Virtual Context Identifier Comparator Control Register 0

The TRCVMIDCCTLR0 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=0-3.

## Configuration

AArch64 System register TRCVMIDCCTLR0 bits [31:0] are architecturally mapped to External register TRCVMIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x0 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR0 are UNDEFINED.

## Attributes

TRCVMIDCCTLR0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 3:

TRCVMIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR3. Each bit in this field corresponds to a byte in TRCVMIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 2:

TRCVMIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR2. Each bit in this field corresponds to a byte in TRCVMIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 1:

TRCVMIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR1. Each bit in this field corresponds to a byte in TRCVMIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 0:

TRCVMIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR0. Each bit in this field corresponds to a byte in TRCVMIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR0

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=0-3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVMIDCCTLR0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x0 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0;
```

MSR TRCVMIDCCTLR0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x0 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64];
```

## D24.4.72 TRCVMIDCCTLR1, Trace Virtual Context Identifier Comparator Control Register 1

The TRCVMIDCCTLR1 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=4-7.

## Configuration

AArch64 System register TRCVMIDCCTLR1 bits [31:0] are architecturally mapped to External register TRCVMIDCCTLR1[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x4 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR1 are UNDEFINED.

## Attributes

TRCVMIDCCTLR1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP7[&lt;m&gt;] , bits [m+24], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 7:

TRCVMIDCVR7 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR7. Each bit in this field corresponds to a byte in TRCVMIDCVR7.

| COMP7[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP6[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 6:

TRCVMIDCVR6 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR6. Each bit in this field corresponds to a byte in TRCVMIDCVR6.

| COMP6[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP5[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 5:

TRCVMIDCVR5 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR5. Each bit in this field corresponds to a byte in TRCVMIDCVR5.

| COMP5[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP4[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 4:

TRCVMIDCVR4 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR4. Each bit in this field corresponds to a byte in TRCVMIDCVR4.

| COMP4[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR1

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=4-7, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVMIDCCTLR1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x4 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1;
```

MSR TRCVMIDCCTLR1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x4 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64];
```

## D24.4.73 TRCVMIDCVR&lt;n&gt;, Trace Virtual Context Identifier Comparator Value Register &lt;n&gt;, n = 0 - 7

The TRCVMIDCVR&lt;n&gt; characteristics are:

## Purpose

Contains the Virtual Context Identifier Comparator value.

## Configuration

AArch64 System register TRCVMIDCVR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCVMIDCVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMVMIDC) &gt; n. Otherwise, direct accesses to TRCVMIDCVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCVMIDCVR&lt;n&gt; is a 64-bit register.

## Field descriptions

VALUE

63

32

VALUE

31

0

<!-- image -->

## VALUE, bits [63:0]

Virtual context identifier value. The width of this field is indicated by TRCIDR2.VMIDSIZE. Unimplemented bits are RES0. After a PE Reset, the trace unit assumes that the Virtual context identifier is zero until the PE updates the Virtual context identifier .

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCVMIDCVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCRSCTLR&lt;a&gt;.GROUP == 0b0111 and TRCRSCTLR&lt;a&gt;.VMID[n] == 1. · TRCACATR&lt;a&gt;.CONTEXTTYPE == 0b10 or 0b11 and TRCACATR&lt;a&gt;.CONTEXT == n.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCVMIDCVR<m> ; Where m = 0-7
```

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b001 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_VIRTUAL_CONTEXT_IDENTIFIER_COMPARATORS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCVR[m];
```

MSR TRCVMIDCVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b001 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_VIRTUAL_CONTEXT_IDENTIFIER_COMPARATORS then
```

UNDEFINED;

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCVR[m] = X[t, 64];
```

## D24.4.74 TRFCR\_EL1, Trace Filter Control Register (EL1)

The TRFCR\_EL1 characteristics are:

## Purpose

Provides EL1 controls for Trace.

## Configuration

AArch64 System register TRFCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register TRFCR[31:0].

This register is present only when FEAT\_TRF is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRFCR\_EL1 are UNDEFINED.

## Attributes

TRFCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## DnVM, bit [11]

## When FEAT\_TRBEv1p1 is implemented and FEAT\_NV is implemented:

Reserved for software use in nested virtualization. See also TRFCR\_EL2.DnVM.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KE, bit [10]

## When FEAT\_TRBE\_EXC is implemented:

Kernel exception enable for TRBE Profiling exceptions taken to EL1.

| KE   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | TRBE Profiling exceptions taken to EL1 are always masked at EL1.                                                       |
| 0b1  | Enabled TRBE Profiling exceptions taken to EL1 are masked at EL1 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EE, bits [9:8]

## When FEAT\_TRBE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Applies when           |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| 0b00 | Disabled. TRBE Profiling exceptions for EL1 are disabled. All of the following apply: • Unless enabled by a higher Exception level, TRBE Profiling exceptions are not generated. • TRBSR_EL1.IRQ drives the interrupt request signal TRBIRQ . • Accesses to TRBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1.                                                                                                                                                                                   |                        |
| 0b01 | Reserved for software use in nested virtualization. Behaves as 0b00 for the purpose of controlling the TRBE Profiling exception and interrupt request signal TRBIRQ , and as 0b11 for the purpose of accesses to TRBSR_EL1.                                                                                                                                                                                                                                                                     | FEAT_NV is implemented |
| 0b10 | Reserved for software use in nested virtualization. Behaves as 0b11 for the purposes of controlling the TRBE Profiling exception and interrupt request signal TRBIRQ , and accesses to TRBSR_EL1.                                                                                                                                                                                                                                                                                               | FEAT_NV is implemented |
| 0b11 | Enabled. TRBE Profiling exceptions for EL1 are enabled, as follows: • All trace buffer management events are recorded in TRBSR_EL1, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE or TRBSR_EL2 by TRFCR_EL2.EE. • TRBE Profiling exceptions are generated and taken to EL1 when unmasked and TRBSR_EL1.IRQ is 1, unless the Effective value of HCR_EL2.TGE is 1, in which case the exception is taken to EL2. • The interrupt request signal TRBIRQ is not asserted. |                        |

For more information on the values reserved for software use in nested virtualization, see TRFCR\_EL2.EE.

If the Effective value of TRFCR\_EL2.EE is 0b00 , then the Effective value of TRFCR\_EL1.EE is 0b00 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '00' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                                                                                                                                                                                                                                                | Applies when              |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| 0b00 | Reserved for software use in nested virtualization. Behaves as 0b01 . See also TRFCR_EL2.TS,                                                                                                                                                                                                                           | FEAT_NV2p1 is implemented |
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF_EL2.                                                                                                                                                                                                                  |                           |
| 0b10 | Guest physical timestamp. The traced timestamp is the physical counter value minus a physical offset. If any of the following are true, then the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn == 0. • CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented   |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                                                                                                                                                                                                                                                |                           |

All other values are reserved.

If any of the following are true, then this field is ignored by the PE:

- EL2 is implemented and TRFCR\_EL2.TS is not 0b00 .
- SelfHostedTraceEnabled() == FALSE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [4]

Reserved, RES0.

## CX, bit [3]

## When FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization. See also TRFCR\_EL2.CX.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [2]

Reserved, RES0.

## E1TRE, bit [1]

EL1 Trace Enable.

| E1TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL1. |
| 0b1     | Trace is allowed at EL1.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0TRE, bit [0]

EL0 Trace Enable.

| E0TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL0. |
| 0b1     | Trace is allowed at EL0.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRFCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRFCR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x880]; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRFCR_EL2; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRFCR_EL1;
```

MSR TRFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x880] = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif ELIsInHost(EL2) then TRFCR_EL2 = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRFCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x880]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRFCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TRFCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TRFCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x880] = X[t, 64];
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRFCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TRFCR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.4.75 TRFCR\_EL2, Trace Filter Control Register (EL2)

The TRFCR\_EL2 characteristics are:

## Purpose

Provides EL2 controls for Trace.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register TRFCR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HTRFCR[31:0].

This register is present only when FEAT\_TRF is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRFCR\_EL2 are UNDEFINED.

## Attributes

TRFCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

DnVM, bit [11]

## When FEAT\_TRBEv1p1 is implemented:

Disable use of physical address trace buffer pointers.

| DnVM   | Meaning                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0    | Use of physical address trace buffer pointers is permitted.                                             |
| 0b1    | Use of physical address trace buffer pointers is disabled. The PE behaves as if TRBLIMITR_EL1.nVM is 0. |

If EL2 is disabled in the owning Security state, or the trace buffer owning Exception level is EL2, then the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KE, bit [10]

## When FEAT\_TRBE\_EXC is implemented:

Kernel exception enable for TRBE Profiling exceptions taken to EL2.

| KE   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | TRBE Profiling exceptions taken to EL2 are always masked at EL2.                                                       |
| 0b1  | Enabled TRBE Profiling exceptions taken to EL2 are masked at EL2 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EE, bits [9:8]

## When FEAT\_TRBE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00 | Disabled. TRBE Profiling exceptions for EL2 and EL1 are disabled. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL2. • Unless enabled by a higher Exception level, TRBE Profiling exceptions are not generated. • TRBSR_EL1.IRQ drives the interrupt request signal TRBIRQ . • Accesses to TRBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1 and accesses to TRBSR_EL1 at EL2 ignore the value of HCR_EL2.E2H. |
| 0b01 | Delegated. TRBE Profiling exceptions for EL2 are disabled, but might be enabled for EL1 by TRFCR_EL1.EE. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL2. • TRBSR_EL2.IRQ is ignored and TRBE Profiling exceptions are not taken to EL2, other than the case when the Effective value of HCR_EL2.TGE is 1.                                                                                                  |

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b10 | Enabled. TRBE Profiling exceptions for EL2 are enabled for trace buffer management events targeting EL2, as follows: • Trace buffer management events due to a fault on a write to the trace buffer that would generate a Data Abort exception taken to EL2 if generated by a store instruction executed at the owning Exception level are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. If the trace buffer owning Exception level is EL2, then this means any fault on a write to the trace buffer. If the trace buffer owning Exception level is EL1, then this means any of the following faults on a write to the trace buffer: • Stage 2 faults. • If HCR_EL2.TEA is 1, synchronous External aborts. • If HCR_EL2.GPF is 1, Granule Protection Faults (GPFs). • Trace buffer management events due to Granule Protection Check faults other than GPFs on a write to the trace buffer are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. • TRBE Profiling exceptions are generated and taken to EL2 when unmasked and TRBSR_EL2.IRQ is 1. |
| 0b11 | Trap all. TRBE Profiling exceptions for EL2 are enabled for all trace buffer management events, as follows: • All trace buffer management events are recorded in TRBSR_EL2, unless they are configured to be recorded in TRBSR_EL3 by MDCR_EL3.TRBEE. • TRBE Profiling exceptions are generated and taken to EL2 when unmasked and TRBSR_EL2.IRQ is 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

If the Effective value of MDCR\_EL3.TRBEE is 0b00 , then the Effective value of TRFCR\_EL2.EE is 0b00 . Otherwise, if EL2 is not implemented or the Effective value of SCR\_EL3.{NS, EEL2} is {0, 0}, then the Effective value of TRFCR\_EL2.EE is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                               | Applies when   |
|------|-------------------------------------------------------------------------------------------------------|----------------|
| 0b00 | Timestamp controlled by TRFCR_EL1.TS or TRFCR.TS.                                                     |                |
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF_EL2. |                |

| TS   | Meaning                                                                                                                                                                                                                                                                                                           | Applies when            |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b10 | Guest physical timestamp. The traced timestamp is the physical counter value minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn == 0. • CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                                                                                                                                                                                                                                           |                         |

If SelfHostedTraceEnabled() == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## Bit [4]

Reserved, RES0.

## CX, bit [3]

CONTEXTIDR\_EL2 and VMID trace enable.

| CX   | Meaning                                  |
|------|------------------------------------------|
| 0b0  | CONTEXTIDR_EL2 and VMIDtrace prohibited. |
| 0b1  | CONTEXTIDR_EL2 and VMIDtrace allowed.    |

If SelfHostedTraceEnabled () == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [2]

Reserved, RES0.

## E2TRE, bit [1]

EL2 Trace Enable.

| E2TRE   | Meaning                     |
|---------|-----------------------------|
| 0b0     | Trace is prohibited at EL2. |
| 0b1     | Trace is allowed at EL2.    |

If SelfHostedTraceEnabled () == FALSE, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0HTRE, bit [0]

EL0 Trace Enable.

| E0HTRE   | Meaning                     |
|----------|-----------------------------|
| 0b0      | Trace is prohibited at EL0. |
| 0b1      | Trace is allowed at EL0.    |

If any of the following are true, then this field is ignored by the PE:

- SelfHostedTraceEnabled () == FALSE.
- The Effective value of HCR\_EL2.TGE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRFCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRFCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRFCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TRFCR_EL2;
```

MSR TRFCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRFCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRFCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x880]; else X[t, 64] = TRFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRFCR_EL2;
```

<!-- formula-not-decoded -->

When FEAT\_VHE is implemented MSR TRFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_TRF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.TRFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TTRF == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x880] = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRFCR_EL2 = X[t, 64]; else TRFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRFCR_EL1 = X[t, 64];
```