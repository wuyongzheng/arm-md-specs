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
