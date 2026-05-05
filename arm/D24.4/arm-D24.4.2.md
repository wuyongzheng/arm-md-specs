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
