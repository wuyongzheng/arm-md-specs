## D24.7 Statistical Profiling Extension registers

This section lists the Statistical Profiling Extension registers in AArch64.

## D24.7.1 PMBIDR\_EL1, Profiling Buffer ID Register

The PMBIDR\_EL1 characteristics are:

## Purpose

Provides information to software as to whether the buffer can be programmed at the current Exception level.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMBIDR\_EL1 are UNDEFINED.

## Attributes

PMBIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## MaxBuffSize, bits [47:32]

Maximum supported Profiling Buffer size. Reserved for software use.

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

## Bits [31:12]

Reserved, RES0.

## EA, bits [11:8]

External Abort handling. Describes how the PE manages External aborts on writes made by the Statistical Profiling Unit to the Profiling Buffer.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EA     | Meaning                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not described.                                                                                                            |
| 0b0001 | The PE ignores External aborts on writes made by the Statistical Profiling Unit.                                          |
| 0b0010 | An External abort on a write made by the Statistical Profiling Unit generates an asynchronous SError exception at the PE. |

## All other values are reserved.

From Armv8.8, the value 0b0000 is not permitted.

The behavior described by this field does not apply for External aborts on a translation table walk, translation table update, or GPT walk made by the Statistical Profiling Unit that are reported as MMU faults using PMBSR\_ELx. For more information, see 'External aborts'.

Access to this field is RO.

## AddrMode, bits [7:6]

## When FEAT\_SPE\_nVM is implemented:

Address Modes. Describes the addressing modes available for the Profiling Buffer.

| AddrMode   | Meaning                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------|
| 0b00       | Only virtual address mode is supported.                                                               |
| 0b01       | Virtual and physical address modes are supported.                                                     |
| 0b11       | Reserved for software use under virtualization, to show that only physical address mode is supported. |

Other values are reserved.

If the Effective value of PMSCR\_EL2.EnVM is 1 and the value returned for PMBIDR\_EL1.P is 0, then this field reads as 0b01 . Otherwise, this field reads as 0b00 .

Note

Ahypervisor might trap accesses to this register to describe limitations of its virtualization support to a guest operating system.

## Otherwise:

Reserved, RES0.

## F, bit [5]

Flag updates. Describes how address translations performed by the Statistical Profiling Unit manage the Access flag and dirty state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F   | Meaning                                                                                                                                                                                                                 |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Hardware management of the Access flag and dirty state for accesses made by the Statistical Profiling Unit is always disabled for all translation stages.                                                               |
| 0b1 | Hardware management of the Access flag and dirty state for accesses made by the Statistical Profiling Unit is controlled in the same way as explicit memory accesses in the Profiling Buffer owning translation regime. |

Note

If hardware management of the Access flag is disabled for a stage of translation, an access to a Page or Block with the Access flag bit not set in the descriptor will generate an Access Flag fault.

If hardware management of the dirty state is disabled for a stage of translation, an access to a Page or Block will ignore the Dirty Bit Modifier in the descriptor and might generate a Permission fault, depending on the values of the access permission bits in the descriptor.

From Armv8.8, the value 0 is not permitted.

Access to this field is RO.

## P, bit [4]

Programming not allowed. When read at EL3, this field reads as zero. Otherwise, indicates that the Profiling Buffer owning Exception level is a higher Exception level or the Profiling Buffer owning Security state is not the current Security state.

| P   | Meaning                  |
|-----|--------------------------|
| 0b0 | Programming is allowed.  |
| 0b1 | Programming not allowed. |

The value read from this field depends on the current Exception level and the Effective values of MDCR\_EL3.NSPB, MDCR\_EL3.NSPBE, and MDCR\_EL2.E2PB:

- If EL3 is implemented, MDCR\_EL3.NSPB is 0b0x , and either FEAT\_RME is not implemented, or Secure state is implemented and MDCR\_EL3.NSPBE is 0, then this field reads as one from:
- Non-secure EL1 and Non-secure EL2.
- If FEAT\_RME is implemented, Realm EL1 and Realm EL2.
- If Secure EL2 is implemented and enabled, and MDCR\_EL2.E2PB is 0b00 , Secure EL1.
- If EL3 is implemented, MDCR\_EL3.NSPB is 0b1x and either FEAT\_RME is not implemented or MDCR\_EL3.NSPBE is 0, then this field reads as one from:
- If Secure state is implemented, Secure EL1.
- If Secure EL2 is implemented, Secure EL2.
- If EL2 is implemented and MDCR\_EL2.E2PB is 0b00 , Non-secure EL1.
- If FEAT\_RME is implemented, Realm EL1 and Realm EL2.
- If FEAT\_RME is implemented, and MDCR\_EL3.{NSPB, NSPBE} is { 0b1x , 1}, then this field reads as one from:
- Non-secure EL1 and Non-secure EL2.
- If Secure state is implemented, Secure EL1 and Secure EL2.
- If MDCR\_EL2.E2PB is 0b00 , Realm EL1.
- If EL3 is not implemented, EL2 is implemented, and MDCR\_EL2.E2PB is 0b00 , then this field reads as one from EL1.

Otherwise, this field reads as zero.

## Align, bits [3:0]

Defines the minimum alignment constraint for writes to PMBPTR\_EL1.

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

All other values are reserved.

For more information, see Restrictions on the current write pointer.

If this field is nonzero, then every record is a multiple of this size.

Access to this field is RO.

## Accessing PMBIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b111 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMBIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = PMBIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = PMBIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBIDR_EL1;
```

## D24.7.2 PMBLIMITR\_EL1, Profiling Buffer Limit Address Register

The PMBLIMITR\_EL1 characteristics are:

## Purpose

Defines the upper limit for the profiling buffer, and enables the profiling buffer

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMBLIMITR\_EL1 are UNDEFINED.

## Attributes

PMBLIMITR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## LIMIT, bits [63:12]

Limit address. PMBLIMITR\_EL1.LIMIT:Zeros(12) is the address of the first byte in memory after the last byte in the profiling buffer. If the smallest implemented translation granule is not 4KB, then bits[N-1:12] are RES0, where Nis the IMPLEMENTATION DEFINED value, Log2(smallest implemented translation granule).

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:8]

Reserved, RES0.

## nVM, bit [7]

## When FEAT\_SPE\_nVM is implemented:

Address mode.

| nVM   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The Profiling Buffer pointers are virtual addresses. |
| 0b1   | The Profiling Buffer pointers are:                   |

If the Effective value of PMSCR\_EL2.EnVM is 0, then the PE ignores the value of this field, and the Profiling Buffer pointers are always virtual addresses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RW.

## Otherwise:

Reserved, RES0.

Bit [6]

Reserved, RES0.

## PMFZ, bit [5]

## When FEAT\_SPEv1p2 is implemented:

Freeze PMU on SPE event. Stop PMU event counters when PMBSR\_EL1.S == 1.

| PMFZ   | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0    | Do not freeze PMUevent counters on Statistical Profiling Buffer Management event. |
| 0b1    | Freeze PMUevent counters on Statistical Profiling Buffer Management event.        |

The PMU event counters affected by this control is controlled by PMCR\_EL0.FZS and, if EL2 is implemented, MDCR\_EL2.HPMFZS. See the descriptions of these control bits for more information.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [4:3]

Reserved, RES0.

## FM, bits [2:1]

Fill mode.

| FM   | Meaning                                                                    | Applies when                |
|------|----------------------------------------------------------------------------|-----------------------------|
| 0b00 | Fill mode. Stop collection and raise maintenance interrupt on buffer fill. |                             |
| 0b10 | Discard mode. All output is discarded.                                     | FEAT_SPEv1p2 is implemented |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

E, bit [0]

## Profiling Buffer enable

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing PMBLIMITR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMBLIMITR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMBLIMITR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x800]; else X[t, 64] = PMBLIMITR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBLIMITR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBLIMITR_EL1;
```

| E   | Meaning                   |
|-----|---------------------------|
| 0b0 | All output is discarded.  |
| 0b1 | Profiling buffer enabled. |

MSR PMBLIMITR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMBLIMITR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x800] = X[t, 64]; else PMBLIMITR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMBLIMITR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBLIMITR_EL1 = X[t, 64];
```

## D24.7.3 PMBMAR\_EL1, Profiling Buffer Memory Attribute Register

The PMBMAR\_EL1 characteristics are:

## Purpose

Controls Statistical Profiling Unit accesses to memory.

If the Profiling Buffer pointers specify virtual addresses, the address properties are defined by the translation tables and this register is ignored.

## Configuration

This register is present only when FEAT\_SPE\_nVM is implemented. Otherwise, direct accesses to PMBMAR\_EL1are UNDEFINED.

## Attributes

PMBMAR\_EL1is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## SH, bits [9:8]

Profiling Buffer shareability domain. Defines the shareability domain for Normal memory used by the Profiling Buffer.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

All other values are reserved.

This field is ignored when PMBMAR\_EL1.Attr specifies any of the following memory types:

- Any Device memory type.
- Normal memory, Inner Non-cacheable, Outer Non-cacheable.

All Device and Normal Inner Non-cacheable Outer Non-cacheable memory regions are always treated as Outer Shareable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Attr, bits [7:0]

Profiling Buffer memory type and attributes. Defines the memory type and, for Normal memory, the cacheability attributes, for memory addressed by the Profiling Buffer.

The encoding of this field is the same as that of a MAIR\_ELx.Attr&lt;n&gt; field, as follows:

| Attr        |                                                                       | Meaning                                                                                                                                                                                                          |
|-------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 dd00 |                                                                       | Device memory. See encoding of 'dd' for the type of Device memory.                                                                                                                                               |
| 0b0000 dd01 |                                                                       | If FEAT_XS is implemented: Device memory with the XS attribute set to 0. See encoding of 'dd' for the type of Device memory. Otherwise, UNPREDICTABLE.                                                           |
| 0b0000 dd1x |                                                                       | UNPREDICTABLE.                                                                                                                                                                                                   |
| 0booooiiii  | where oooo != 0000 and iiii != 0000                                   | Normal memory. See encoding of 'oooo' and 'iiii' for the type of Normal memory.                                                                                                                                  |
| 0b01000000  |                                                                       | If FEAT_XS is implemented: Normal Inner Non-cacheable, Outer Non-cacheable memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE.                                                                      |
| 0b10100000  |                                                                       | If FEAT_XS is implemented: Normal Inner Write-through Cacheable, Outer Write-through Cacheable, Read-Allocate, No-Write Allocate, Non-transient memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE. |
| 0b11110000  |                                                                       | If FEAT_MTE2 is implemented: Tagged Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. Otherwise, UNPREDICTABLE.                                                     |
| 0bxxxx0000  | where xxxx != 0000 and xxxx != 0100 and xxxx != 1010 and xxxx != 1111 | UNPREDICTABLE.                                                                                                                                                                                                   |

## dd is encoded as follows:

oooo is encoded as follows:

| 'oooo'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Outer Write-Through Transient.     |
| 0b0100   |              | Normal memory, Outer Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Outer Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Outer Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Outer Write-Back Non-transient.    |

| 'dd'   | Meaning               |
|--------|-----------------------|
| 0b00   | Device-nGnRnE memory. |
| 0b01   | Device-nGnRE memory.  |
| 0b10   | Device-nGRE memory.   |
| 0b11   | Device-GRE memory.    |

R encodes the Outer Read-Allocate policy and W encodes the Outer Write-Allocate policy.

iiii is encoded as follows:

| 'iiii'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Inner Write-Through Transient.     |
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

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMBMAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b101 |

```
if !IsFeatureImplemented(FEAT_SPE_nVM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS4 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMBMAR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS4 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBMAR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS4 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS4 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBMAR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBMAR_EL1;
```

MSR PMBMAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b101 |

```
if !IsFeatureImplemented(FEAT_SPE_nVM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS4 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMBMAR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS4 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMBMAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS4 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS4 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMBMAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBMAR_EL1 = X[t, 64];
```

## D24.7.4 PMBPTR\_EL1, Profiling Buffer Write Pointer Register

The PMBPTR\_EL1 characteristics are:

## Purpose

Defines the current write pointer for the profiling buffer.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMBPTR\_EL1 are UNDEFINED.

## Attributes

PMBPTR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |     | 32   |
|------|-----|------|
|      | PTR |      |
| 31   |     | 0    |
|      | PTR |      |

## PTR, bits [63:0]

Current write address. Defines the virtual address of the next entry to be written to the buffer.

If PMBIDR\_EL1.Align is not zero, then it is IMPLEMENTATION DEFINED whether bits [M-1:0] are RES0 or read/write, where M is an integer between 1 and PMBIDR\_EL1.Align inclusive.

The architecture places restrictions on the values software can write to the pointer when the SPU is not in Discard mode. For more information see Restrictions on the current write pointer.

On a management interrupt, PMBPTR\_EL1 is frozen.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMBPTR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMBPTR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMBPTR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x810]; else X[t, 64] = PMBPTR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBPTR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBPTR_EL1;
```

MSR PMBPTR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMBPTR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x810] = X[t, 64]; else PMBPTR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED;
```

else

```
AArch64.SystemAccessTrap(EL3, 0x18); else PMBPTR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBPTR_EL1 = X[t, 64];
```

## D24.7.5 PMBSR\_EL1, Profiling Buffer Status/syndrome Register (EL1)

The PMBSR\_EL1 characteristics are:

## Purpose

Provides syndrome information to software for a Profiling Buffer management event.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMBSR\_EL1 are UNDEFINED.

## Attributes

PMBSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## MSS2, bits [55:32]

Management event Specific Syndrome 2. Contains syndrome specific to the management event.

The syndrome contents for each management event are described in the following sections.

MSS2 encoding for other Profiling Buffer management events

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

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

AssuredOnly, bit [7]

## When FEAT\_THE is implemented, PMBSR\_EL1.EC == '100101', and GetPMBSR\_EL1\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetPMBSR\_EL1\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetPMBSR\_EL1\_FSC() IN {'0011xx'}:

DirtyBit flag. If a write access to memory generates a Data Abort for a Permission fault using Indirect Permission, then this field holds information about the fault.

| DirtyBit   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0        | Permission Fault is not due to dirty state. |
| 0b1        | Permission Fault is due to dirty state.     |

## Otherwise:

Reserved, RES0.

## Bits [4:0]

Reserved, RES0.

MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED.

## EC, bits [31:26]

Event class. Top-level description of the cause of the Profiling Buffer management event.

| EC       | Meaning                                                                                                                                                                                                                                                                                                                                                                      | MSS                                                                                    | MSS2                                                                                     | Applies when            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------|
| 0b000000 | Other Profiling Buffer management event. All Profiling Buffer management events other than those described by the other defined Event class codes.                                                                                                                                                                                                                           | MSSencoding for other Profiling Buffer management events                               | MSS2 encoding for other Profiling Buffer management events                               |                         |
| 0b011110 | Granule Protection Check fault on write to Profiling Buffer, other than Granule Protection Fault (GPF). That is, any of the following: • Granule Protection Table (GPT) address size fault. • GPT walk fault. • Synchronous External abort on GPT fetch. AGPFontranslation table walk or update is reported as either a Stage 1 or Stage 2 Data Abort, as appropriate. Other | MSSencoding for Granule Protection Check faults on write to Profiling Buffer           | MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer           | FEAT_RME is implemented |
| 0b011111 | Profiling Buffer management event for an IMPLEMENTATION DEFINED reason.                                                                                                                                                                                                                                                                                                      | MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason | MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason |                         |
| 0b100100 | Stage 1 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |
| 0b100101 | Stage 2 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:20]

Reserved, RES0.

## DL, bit [19]

Partial record lost. Following a buffer management event other than an asynchronous External abort, indicates whether the last record written to the Profiling Buffer is complete.

| DL   | Meaning                                                                                                                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | PMBPTR_EL1 points to the first byte after the last complete record written to the Profiling Buffer.                                                                                                                                                                                            |
| 0b1  | Part of a record was lost because of a buffer management event or synchronous External abort. PMBPTR_EL1 might not point to the first byte after the last complete record written to the buffer, and so restarting collection might result in a data record stream that software cannot parse. |

When the buffer management event was because of an asynchronous External abort, this bit is set to 1 and software must not assume that any valid data has been written to the Profiling Buffer.

This bit is RES0 if the PE never sets this bit as a result of a buffer management event caused by an asynchronous External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [18]

External abort.

| EA   | Meaning                                                                             |
|------|-------------------------------------------------------------------------------------|
| 0b0  | An External abort has not been asserted.                                            |
| 0b1  | An External abort has been asserted and detected by the Statistical Profiling Unit. |

This bit is RES0 if the PE never sets this bit as the result of an External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S, bit [17]

Service. Indicates that a Profiling Buffer management event has been recorded.

| S   | Meaning                                                         |
|-----|-----------------------------------------------------------------|
| 0b0 | No Profiling Buffer management event for EL1 has been recorded. |
| 0b1 | AProfiling Buffer management event for EL1 has been recorded.   |

When FEAT\_SPE\_EXC is implemented, this field indicates a management event for EL1.

If FEAT\_SPE\_EXC is implemented and the SPE Profiling exception for EL1 is enabled, then when this field is 1, an SPE Profiling exception for EL1 is pending

If FEAT\_SPE\_EXC is not implemented or the SPE Profiling exception for EL1 is disabled, then this field drives the PMBIRQ Profiling Buffer interrupt request signal.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COLL, bit [16]

Collision detected.

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Profiling Buffer status code

| BSC      | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b000000 | Collection not stopped, or access not allowed.                  |
| 0b000001 | Profiling Buffer filled.                                        |
| 0b000100 | Buffer size. The requested Profiling Buffer size was too large. |

All other values are reserved.

## MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

<!-- image -->

## Bits [15:6]

Reserved, RES0.

| COLL   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | No collision events detected.              |
| 0b1    | At least one collision event was recorded. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MSS, bits [15:0]

Management Event Specific Syndrome. Contains syndrome specific to the Profiling Buffer management event.

The syndrome contents for each Profiling Buffer management event are described in the following sections.

## MSSencoding for other Profiling Buffer management events

<!-- image -->

## FSC, bits [5:0]

Fault status code

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
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

| FSC      | Meaning                                                                                               | Applies when                                         |
|----------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 0b100001 | Alignment fault.                                                                                      |                                                      |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2. | FEAT_D128 is implemented and FEAT_RME is implemented |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1. | FEAT_RME is implemented and FEAT_LPA2 is implemented |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.  | FEAT_RME is implemented                              |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.  | FEAT_RME is implemented                              |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.  | FEAT_RME is implemented                              |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.  | FEAT_RME is implemented                              |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.      | FEAT_RME is implemented                              |
| 0b101001 | Address size fault, level -1.                                                                         | FEAT_LPA2 is implemented                             |
| 0b101010 | Translation fault, level -2.                                                                          | FEAT_D128 is implemented                             |
| 0b101011 | Translation fault, level -1.                                                                          | FEAT_LPA2 is implemented                             |
| 0b101100 | Address Size fault, level -2.                                                                         | FEAT_D128 is implemented                             |
| 0b110000 | TLB conflict abort.                                                                                   |                                                      |
| 0b110001 | Unsupported atomic hardware update fault.                                                             | FEAT_HAFDBS is implemented                           |

## All other values are reserved.

It is IMPLEMENTATION DEFINED whether each of the Access Flag fault, asynchronous External abort and synchronous External abort, Alignment fault, and TLB Conflict abort values can be generated by the PE. For more information see 'Faults and Watchpoints'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MSSencoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

Bits [15:0]

Reserved, RES0.

MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing PMBSR\_EL1

When the Effective value of HCR\_EL2.E2H is 1 and FEAT\_SPE\_EXC is implemented, without explicit synchronization, accesses from EL3 using the accessor name PMBSR\_EL1 or PMBSR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMBSR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (EffectivePMSCR_EL2_EE() == '00' || PMSCR_EL1.EE == '00' ↪ → || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x820]; else X[t, 64] = PMBSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectivePMSCR_EL2_EE() != '00' && ELIsInHost(EL2) then X[t, 64] = PMBSR_EL2; else X[t, 64] = PMBSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBSR_EL1;
```

IMPLEMENTATION DEFINED

MSR PMBSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (EffectivePMSCR_EL2_EE() == '00' || PMSCR_EL1.EE == '00' ↪ → || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x820] = X[t, 64]; else PMBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectivePMSCR_EL2_EE() != '00' && ELIsInHost(EL2) then PMBSR_EL2 = X[t, 64]; else PMBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBSR_EL1 = X[t, 64];
```

When FEAT\_SPE\_EXC is implemented and FEAT\_VHE is implemented MRS &lt;Xt&gt;, PMBSR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x820]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBSR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = PMBSR_EL1; else UNDEFINED;
```

When FEAT\_SPE\_EXC is implemented and FEAT\_VHE is implemented MSR PMBSR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x820] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMBSR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then PMBSR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.7.6 PMBSR\_EL2, Profiling Buffer Syndrome Register (EL2)

The PMBSR\_EL2 characteristics are:

## Purpose

Provides syndrome information to software for a Profiling Buffer management event.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_SPE\_EXC is implemented. Otherwise, direct accesses to PMBSR\_EL2 are UNDEFINED.

## Attributes

PMBSR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## MSS2, bits [55:32]

Management event Specific Syndrome 2. Contains syndrome specific to the management event.

The syndrome contents for each management event are described in the following sections.

MSS2 encoding for other Profiling Buffer management events

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

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

AssuredOnly, bit [7]

## When FEAT\_THE is implemented, PMBSR\_EL2.EC == '100101', and GetPMBSR\_EL2\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetPMBSR\_EL2\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetPMBSR\_EL2\_FSC() IN {'0011xx'}:

DirtyBit flag. If a write access to memory generates a Data Abort for a Permission fault using Indirect Permission, then this field holds information about the fault.

| DirtyBit   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0        | Permission Fault is not due to dirty state. |
| 0b1        | Permission Fault is due to dirty state.     |

## Otherwise:

Reserved, RES0.

## Bits [4:0]

Reserved, RES0.

MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED.

## EC, bits [31:26]

Event class. Top-level description of the cause of the Profiling Buffer management event.

| EC       | Meaning                                                                                                                                                                                                                                                                                                                                                                      | MSS                                                                                    | MSS2                                                                                     | Applies when            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------|
| 0b000000 | Other Profiling Buffer management event. All Profiling Buffer management events other than those described by the other defined Event class codes.                                                                                                                                                                                                                           | MSSencoding for other Profiling Buffer management events                               | MSS2 encoding for other Profiling Buffer management events                               |                         |
| 0b011110 | Granule Protection Check fault on write to Profiling Buffer, other than Granule Protection Fault (GPF). That is, any of the following: • Granule Protection Table (GPT) address size fault. • GPT walk fault. • Synchronous External abort on GPT fetch. AGPFontranslation table walk or update is reported as either a Stage 1 or Stage 2 Data Abort, as appropriate. Other | MSSencoding for Granule Protection Check faults on write to Profiling Buffer           | MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer           | FEAT_RME is implemented |
| 0b011111 | Profiling Buffer management event for an IMPLEMENTATION DEFINED reason.                                                                                                                                                                                                                                                                                                      | MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason | MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason |                         |
| 0b100100 | Stage 1 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |
| 0b100101 | Stage 2 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:20]

Reserved, RES0.

## DL, bit [19]

Partial record lost. Following a buffer management event other than an asynchronous External abort, indicates whether the last record written to the Profiling Buffer is complete.

| DL   | Meaning                                                                                                                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | PMBPTR_EL1 points to the first byte after the last complete record written to the Profiling Buffer.                                                                                                                                                                                            |
| 0b1  | Part of a record was lost because of a buffer management event or synchronous External abort. PMBPTR_EL1 might not point to the first byte after the last complete record written to the buffer, and so restarting collection might result in a data record stream that software cannot parse. |

When the buffer management event was because of an asynchronous External abort, this bit is set to 1 and software must not assume that any valid data has been written to the Profiling Buffer.

This bit is RES0 if the PE never sets this bit as a result of a buffer management event caused by an asynchronous External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [18]

External abort.

| EA   | Meaning                                                                             |
|------|-------------------------------------------------------------------------------------|
| 0b0  | An External abort has not been asserted.                                            |
| 0b1  | An External abort has been asserted and detected by the Statistical Profiling Unit. |

This bit is RES0 if the PE never sets this bit as the result of an External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S, bit [17]

Service. Indicates that a Profiling Buffer management event has been recorded.

| S   | Meaning                                                         |
|-----|-----------------------------------------------------------------|
| 0b0 | No Profiling Buffer management event for EL2 has been recorded. |
| 0b1 | AProfiling Buffer management event for EL2 has been recorded.   |

When FEAT\_SPE\_EXC is implemented, this field indicates a management event for EL2.

If the SPE Profiling exception for EL2 is enabled, then when this field is 1, an SPE Profiling exception for EL2 is pending

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COLL, bit [16]

Collision detected.

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Profiling Buffer status code

| BSC      | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b000000 | Collection not stopped, or access not allowed.                  |
| 0b000001 | Profiling Buffer filled.                                        |
| 0b000100 | Buffer size. The requested Profiling Buffer size was too large. |

All other values are reserved.

## MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

<!-- image -->

## Bits [15:6]

Reserved, RES0.

## FSC, bits [5:0]

Fault status code

| COLL   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | No collision events detected.              |
| 0b1    | At least one collision event was recorded. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MSS, bits [15:0]

Management Event Specific Syndrome. Contains syndrome specific to the Profiling Buffer management event.

The syndrome contents for each Profiling Buffer management event are described in the following sections.

## MSSencoding for other Profiling Buffer management events

<!-- image -->

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
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

| FSC      | Meaning                                                                                               | Applies when                                         |
|----------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2. | FEAT_D128 is implemented and FEAT_RME is implemented |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1. | FEAT_RME is implemented and FEAT_LPA2 is implemented |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.  | FEAT_RME is implemented                              |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.  | FEAT_RME is implemented                              |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.  | FEAT_RME is implemented                              |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.  | FEAT_RME is implemented                              |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.      | FEAT_RME is implemented                              |
| 0b101001 | Address size fault, level -1.                                                                         | FEAT_LPA2 is implemented                             |
| 0b101010 | Translation fault, level -2.                                                                          | FEAT_D128 is implemented                             |
| 0b101011 | Translation fault, level -1.                                                                          | FEAT_LPA2 is implemented                             |
| 0b101100 | Address Size fault, level -2.                                                                         | FEAT_D128 is implemented                             |
| 0b110000 | TLB conflict abort.                                                                                   |                                                      |
| 0b110001 | Unsupported atomic hardware update fault.                                                             | FEAT_HAFDBS is implemented                           |

All other values are reserved.

It is IMPLEMENTATION DEFINED whether each of the Access Flag fault, asynchronous External abort and synchronous External abort, Alignment fault, and TLB Conflict abort values can be generated by the PE. For more information see 'Faults and Watchpoints'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MSSencoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

Bits [15:0]

Reserved, RES0.

MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing PMBSR\_EL2

When the Effective value of HCR\_EL2.E2H is 1 and FEAT\_SPE\_EXC is implemented, without explicit synchronization, accesses from EL2 using the accessor name PMBSR\_EL2 or PMBSR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMBSR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE_EXC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.PMSEE == '00' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.PMSEE == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMBSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = PMBSR_EL2;
```

MSR PMBSR\_EL2, &lt;Xt&gt;

IMPLEMENTATION DEFINED

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE_EXC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.PMSEE == '00' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.PMSEE == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMBSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBSR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, PMBSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (EffectivePMSCR_EL2_EE() == '00' || PMSCR_EL1.EE == '00' ↪ → || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x820]; else
```

```
X[t, 64] = PMBSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectivePMSCR_EL2_EE() != '00' && ELIsInHost(EL2) then X[t, 64] = PMBSR_EL2; else X[t, 64] = PMBSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMBSR_EL1;
```

MSR PMBSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMBSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2PB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (EffectivePMSCR_EL2_EE() == '00' || PMSCR_EL1.EE == '00' ↪ → || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x820] = X[t, 64]; else PMBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectivePMSCR_EL2_EE() != '00' && ELIsInHost(EL2) then PMBSR_EL2 = X[t, 64]; else PMBSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMBSR_EL1 = X[t, 64];
```

## D24.7.7 PMBSR\_EL3, Profiling Buffer Syndrome Register (EL3)

The PMBSR\_EL3 characteristics are:

## Purpose

Provides syndrome information to software for a Profiling Buffer management event.

## Configuration

This register is present only when FEAT\_SPE\_EXC is implemented and EL3 is implemented. Otherwise, direct accesses to PMBSR\_EL3 are UNDEFINED.

## Attributes

PMBSR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## MSS2, bits [55:32]

Management event Specific Syndrome 2. Contains syndrome specific to the management event.

The syndrome contents for each management event are described in the following sections.

MSS2 encoding for other Profiling Buffer management events

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

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

AssuredOnly, bit [7]

## When FEAT\_THE is implemented, PMBSR\_EL3.EC == '100101', and GetPMBSR\_EL3\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetPMBSR\_EL3\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetPMBSR\_EL3\_FSC() IN {'0011xx'}:

DirtyBit flag. If a write access to memory generates a Data Abort for a Permission fault using Indirect Permission, then this field holds information about the fault.

| DirtyBit   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0        | Permission Fault is not due to dirty state. |
| 0b1        | Permission Fault is due to dirty state.     |

## Otherwise:

Reserved, RES0.

## Bits [4:0]

Reserved, RES0.

MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED.

## EC, bits [31:26]

Event class. Top-level description of the cause of the Profiling Buffer management event.

| EC       | Meaning                                                                                                                                                                                                                                                                                                                                                                      | MSS                                                                                    | MSS2                                                                                     | Applies when            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------|
| 0b000000 | Other Profiling Buffer management event. All Profiling Buffer management events other than those described by the other defined Event class codes.                                                                                                                                                                                                                           | MSSencoding for other Profiling Buffer management events                               | MSS2 encoding for other Profiling Buffer management events                               |                         |
| 0b011110 | Granule Protection Check fault on write to Profiling Buffer, other than Granule Protection Fault (GPF). That is, any of the following: • Granule Protection Table (GPT) address size fault. • GPT walk fault. • Synchronous External abort on GPT fetch. AGPFontranslation table walk or update is reported as either a Stage 1 or Stage 2 Data Abort, as appropriate. Other | MSSencoding for Granule Protection Check faults on write to Profiling Buffer           | MSS2 encoding for Granule Protection Check faults on write to Profiling Buffer           | FEAT_RME is implemented |
| 0b011111 | Profiling Buffer management event for an IMPLEMENTATION DEFINED reason.                                                                                                                                                                                                                                                                                                      | MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason | MSS2 encoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason |                         |
| 0b100100 | Stage 1 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |
| 0b100101 | Stage 2 Data Abort on write to Profiling Buffer.                                                                                                                                                                                                                                                                                                                             | MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer            |                         |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:20]

Reserved, RES0.

## DL, bit [19]

Partial record lost. Following a buffer management event other than an asynchronous External abort, indicates whether the last record written to the Profiling Buffer is complete.

| DL   | Meaning                                                                                                                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | PMBPTR_EL1 points to the first byte after the last complete record written to the Profiling Buffer.                                                                                                                                                                                            |
| 0b1  | Part of a record was lost because of a buffer management event or synchronous External abort. PMBPTR_EL1 might not point to the first byte after the last complete record written to the buffer, and so restarting collection might result in a data record stream that software cannot parse. |

When the buffer management event was because of an asynchronous External abort, this bit is set to 1 and software must not assume that any valid data has been written to the Profiling Buffer.

This bit is RES0 if the PE never sets this bit as a result of a buffer management event caused by an asynchronous External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [18]

External abort.

| EA   | Meaning                                                                             |
|------|-------------------------------------------------------------------------------------|
| 0b0  | An External abort has not been asserted.                                            |
| 0b1  | An External abort has been asserted and detected by the Statistical Profiling Unit. |

This bit is RES0 if the PE never sets this bit as the result of an External abort.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S, bit [17]

Service. Indicates that a Profiling Buffer management event has been recorded.

| S   | Meaning                                                         |
|-----|-----------------------------------------------------------------|
| 0b0 | No Profiling Buffer management event for EL3 has been recorded. |
| 0b1 | AProfiling Buffer management event for EL3 has been recorded.   |

When FEAT\_SPE\_EXC is implemented, this field indicates a management event for EL3.

If the SPE Profiling exception for EL3 is enabled, then when this field is 1, an SPE Profiling exception for EL3 is pending

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COLL, bit [16]

Collision detected.

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Profiling Buffer status code

| BSC      | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b000000 | Collection not stopped, or access not allowed.                  |
| 0b000001 | Profiling Buffer filled.                                        |
| 0b000100 | Buffer size. The requested Profiling Buffer size was too large. |

All other values are reserved.

## MSSencoding for stage 1 or stage 2 Data Aborts on write to Profiling Buffer

<!-- image -->

## Bits [15:6]

Reserved, RES0.

## FSC, bits [5:0]

Fault status code

| COLL   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | No collision events detected.              |
| 0b1    | At least one collision event was recorded. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MSS, bits [15:0]

Management Event Specific Syndrome. Contains syndrome specific to the Profiling Buffer management event.

The syndrome contents for each Profiling Buffer management event are described in the following sections.

## MSSencoding for other Profiling Buffer management events

<!-- image -->

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
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

| FSC      | Meaning                                                                                               | Applies when                                         |
|----------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2. | FEAT_D128 is implemented and FEAT_RME is implemented |
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1. | FEAT_RME is implemented and FEAT_LPA2 is implemented |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.  | FEAT_RME is implemented                              |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.  | FEAT_RME is implemented                              |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.  | FEAT_RME is implemented                              |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.  | FEAT_RME is implemented                              |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.      | FEAT_RME is implemented                              |
| 0b101001 | Address size fault, level -1.                                                                         | FEAT_LPA2 is implemented                             |
| 0b101010 | Translation fault, level -2.                                                                          | FEAT_D128 is implemented                             |
| 0b101011 | Translation fault, level -1.                                                                          | FEAT_LPA2 is implemented                             |
| 0b101100 | Address Size fault, level -2.                                                                         | FEAT_D128 is implemented                             |
| 0b110000 | TLB conflict abort.                                                                                   |                                                      |
| 0b110001 | Unsupported atomic hardware update fault.                                                             | FEAT_HAFDBS is implemented                           |

All other values are reserved.

It is IMPLEMENTATION DEFINED whether each of the Access Flag fault, asynchronous External abort and synchronous External abort, Alignment fault, and TLB Conflict abort values can be generated by the PE. For more information see 'Faults and Watchpoints'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MSSencoding for Granule Protection Check faults on write to Profiling Buffer

<!-- image -->

Bits [15:0]

Reserved, RES0.

MSSencoding for Profiling Buffer management event for an IMPLEMENTATION DEFINED reason

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing PMBSR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMBSR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1001 | 0b1010 | 0b011 |

if !(IsFeatureImplemented(FEAT\_SPE\_EXC) &amp;&amp; HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = PMBSR\_EL3;

MSR PMBSR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1001 | 0b1010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPE_EXC) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then PMBSR_EL3 = X[t, 64];
```

IMPLEMENTATION DEFINED

## D24.7.8 PMSCR\_EL1, Statistical Profiling Control Register (EL1)

The PMSCR\_EL1 characteristics are:

## Purpose

Provides EL1 controls for Statistical Profiling.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSCR\_EL1 are UNDEFINED.

## Attributes

PMSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## EnVM, bit [11]

## When FEAT\_SPE\_nVM is implemented and FEAT\_NV is implemented:

Reserved for software use in nested virtualization. See also PMSCR\_EL2.EnVM.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KE, bit [10]

## When FEAT\_SPE\_EXC is implemented:

Kernel exception enable for SPE Profiling exceptions taken to EL1.

| KE   | Meaning                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0  | SPE Profiling exceptions taken to EL1 are always masked at EL1.                                                       |
| 0b1  | Enabled SPE Profiling exceptions taken to EL1 are masked at EL1 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EE, bits [9:8]

## When FEAT\_SPE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Applies when           |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| 0b00 | Disabled. SPE Profiling exceptions for EL1 are disabled. All of the following apply: • Unless enabled by a higher Exception level, SPE Profiling exceptions are not generated. • PMBSR_EL1.S drives the interrupt request signal PMBIRQ . • Accesses to PMBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1.                                                                                                                                                                                       |                        |
| 0b01 | Reserved for software use in nested virtualization. Behaves as 0b00 for the purpose of controlling the SPE Profiling exception and interrupt request signal PMBIRQ , and as 0b11 for the purpose of accesses to PMBSR_EL1.                                                                                                                                                                                                                                                                      | FEAT_NV is implemented |
| 0b10 | Reserved for software use in nested virtualization. Behaves as 0b11 for the purposes of controlling the SPE Profiling exception and interrupt request signal PMBIRQ , and accesses to PMBSR_EL1.                                                                                                                                                                                                                                                                                                | FEAT_NV is implemented |
| 0b11 | Enabled. SPE Profiling exceptions for EL1 are enabled, as follows: • All Profiling Buffer management events are recorded in PMBSR_EL1, unless they are configured to be recorded in PMBSR_EL3 by MDCR_EL3.PMSEE or PMBSR_EL2 by PMSCR_EL2.EE. • SPE Profiling exceptions are generated and taken to EL1 when unmasked and PMBSR_EL1.S is 1, unless the Effective value of HCR_EL2.TGE is 1, in which case the exception is taken to EL2. • The interrupt request signal PMBIRQ is not asserted. |                        |

For more information on the values reserved for software use in nested virtualization, see PMSCR\_EL2.EE.

If the Effective value of PMSCR\_EL2.EE is 0b00 , then the Effective value of PMSCR\_EL1.EE is 0b00 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PCT, bits [7:6]

## When EL2 is implemented:

Physical Timestamp. If timestamp sampling is enabled and the Profiling Buffer owning Exception level is EL1, requests which timestamp counter value is collected.

If FEAT\_ECV is implemented, this is a two-bit field as shown. Otherwise, bit[7] is RES0.

| PCT   | Meaning                                                                                                                                                                                                                                                                                                        | Applies when            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b00  | Virtual timestamp. The collected timestamp is the physical counter minus the value of CNTVOFF_EL2.                                                                                                                                                                                                             |                         |
| 0b01  | Physical timestamp. The collected timestamp is the physical counter.                                                                                                                                                                                                                                           |                         |
| 0b11  | Guest physical timestamp. The collected timestamp is the physical counter minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn == 0. • CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |

When EL2 is implemented, all of the following apply:

- If the Profiling Buffer owning Exception level is EL1 and EL2 is enabled in the owning Security state, then the value of PMSCR\_EL2.PCT might override or modify the meaning of this field.
- If the Profiling Buffer owning Exception level is EL2, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Physical Timestamp. Reserved. This field reads as 0b01 and ignores writes. Software should treat this field as UNK/SBZP.

When EL2 is not implemented, the Effective values of CNTVOFF\_EL2 and CNTPOFF\_EL2 are zero, meaning the virtual counter and physical counter have the same value.

## TS, bit [5]

Timestamp sample enable. Enables recording of a Timestamp packet when the owning Exception level is EL1.

| TS   | Meaning                              |
|------|--------------------------------------|
| 0b0  | Timestamp packet recording disabled. |
| 0b1  | Timestamp packet recording enabled.  |

If the Profiling Buffer owning Exception level is EL2, then this field is ignored by the PE. For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PA, bit [4]

Physical Address sample enable.

| PA   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Physical addresses are not collected. |
| 0b1  | Physical addresses are collected.     |

When EL2 is implemented, all of the following apply:

- If the Profiling Buffer owning Exception level is EL1, then this field is combined with the Effective value PMSCR\_EL2.PA to determine whether Physical addresses are collected.
- If the Profiling Buffer owning Exception level is EL2, then this field is ignored by the PE.

For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CX, bit [3]

CONTEXTIDR\_EL1 sample enable. Enables recording of a Context packet containing the value of CONTEXTIDR\_EL1.

| CX   | Meaning                            |
|------|------------------------------------|
| 0b0  | CONTEXTIDR_EL1 recording disabled. |
| 0b1  | CONTEXTIDR_EL1 recording enabled.  |

The PE ignores the value of this field and CONTEXTIDR\_EL1 is not recorded when any of the following apply:

- The sampled operation executes at EL2.
- The sampled operation executes at EL0 and the Effective value of HCR\_EL2.TGE is 1.

For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## E1SPE, bit [1]

EL1 Statistical Profiling Enable.

| E1SPE   | Meaning                   |
|---------|---------------------------|
| 0b0     | Sampling disabled at EL1. |
| 0b1     | Sampling enabled at EL1.  |

If the Effective value of HCR\_EL2.TGE is 1, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E0SPE, bit [0]

EL0 Statistical Profiling Enable. Controls sampling at EL0 when HCR\_EL2.TGE == 0 or if EL2 is disabled or not implemented.

| E0SPE   | Meaning                   |
|---------|---------------------------|
| 0b0     | Sampling disabled at EL0. |
| 0b1     | Sampling enabled at EL0.  |

If the Effective value of HCR\_EL2.TGE is 1, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x828]; else X[t, 64] = PMSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = PMSCR_EL2; else
```

```
X[t, 64] = PMSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSCR_EL1;
```

MSR PMSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x828] = X[t, 64]; else PMSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then PMSCR_EL2 = X[t, 64]; else PMSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, PMSCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x828]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = PMSCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR PMSCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x828] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then PMSCR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.7.9 PMSCR\_EL2, Statistical Profiling Control Register (EL2)

The PMSCR\_EL2 characteristics are:

## Purpose

Provides EL2 controls for Statistical Profiling.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSCR\_EL2 are UNDEFINED.

## Attributes

PMSCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

EnVM, bit [11]

## When FEAT\_SPE\_nVM is implemented:

Enable use of physical address Profiling Buffer pointers.

| EnVM   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b0    | Use of physical address Profiling Buffer pointers is disabled. The PE behaves as if PMBLIMITR_EL1.nVM is 0. |
| 0b1    | Use of physical address Profiling Buffer pointers is permitted.                                             |

If EL2 is disabled in the owning Security state, or the Profiling Buffer owning Exception level is EL2, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

KE, bit [10]

## When FEAT\_SPE\_EXC is implemented:

Kernel exception enable for SPE Profiling exceptions taken to EL2.

| KE   | Meaning                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0  | SPE Profiling exceptions taken to EL2 are always masked at EL2.                                                       |
| 0b1  | Enabled SPE Profiling exceptions taken to EL2 are masked at EL2 when PSTATE.PM is 1 and unmasked when PSTATE.PM is 0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EE, bits [9:8]

## When FEAT\_SPE\_EXC is implemented:

Exception Enable.

| EE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00 | Disabled. SPE Profiling exceptions for EL2 and EL1 are disabled. All of the following apply: • No Profiling Buffer management events are recorded in PMBSR_EL2. • Unless enabled by a higher Exception level, SPE Profiling exceptions are not generated. • PMBSR_EL1.S drives the interrupt request signal PMBIRQ . • Accesses to PMBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1 and accesses to PMBSR_EL1 at EL2 ignore the value of HCR_EL2.E2H. |
| 0b01 | Delegated. SPE Profiling exceptions for EL2 are disabled, but might be enabled for EL1 by PMSCR_EL1.EE. All of the following apply: • No Profiling Buffer management events are recorded in PMBSR_EL2. • PMBSR_EL2.S is ignored and SPE Profiling exceptions are not taken to EL2, other than for the case when the Effective value of HCR_EL2.TGE is 1.                                                                                              |
| 0b10 | Enabled. SPE Profiling exceptions for EL2 are enabled for Profiling Buffer management events targeting EL2, as follows:                                                                                                                                                                                                                                                                                                                               |

| EE   | Meaning                                                                                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b11 | Trap all. SPE Profiling exceptions for EL2 are enabled for all Profiling Buffer management events, as follows:                                                                                                                              |
|      | • All Profiling Buffer management events are recorded in PMBSR_EL2, unless they are configured to be recorded in PMBSR_EL3 by MDCR_EL3.PMSEE. • SPE Profiling exceptions are generated and taken to EL2 when unmasked and PMBSR_EL2.S is 1. |

If the Effective value of MDCR\_EL3.PMSEE is 0b00 , then the Effective value of PMSCR\_EL2.EE is 0b00 . Otherwise, if EL2 is not implemented or the Effective value of SCR\_EL3.{NS, EEL2} is {0, 0}, then the Effective value of PMSCR\_EL2.EE is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PCT, bits [7:6]

Physical Timestamp. If timestamp sampling is enabled, determines which counter is collected. The behavior depends on the Profiling Buffer owning Exception level.

If FEAT\_ECV is implemented, this is a two-bit field as shown. Otherwise, bit[7] is RES0.

| PCT   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Applies when            |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b00  | Virtual timestamp. The collected timestamp is the physical counter minus a virtual offset. If the Profiling Buffer owning Exception level is EL2 and any of the following are true, then the virtual offset is zero: • The sampled operation executed at EL2 and the Effective value of HCR_EL2.E2H is 1. • The sampled operation executed at EL0 and the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}. Otherwise, the virtual offset is the value of CNTVOFF_EL2.                                                          |                         |
| 0b01  | If the Profiling Buffer owning Exception level is EL1, then the timestamp value is selected by PMSCR_EL1.PCT. Otherwise, physical timestamp. The collected timestamp is the physical counter.                                                                                                                                                                                                                                                                                                                                  |                         |
| 0b11  | If the Profiling Buffer owning Exception level is EL1 and PMSCR_EL1.PCT is 0b00 , then guest virtual timestamp. The collected timestamp is the physical counter minus the value of CNTVOFF_EL2. Otherwise, guest physical timestamp. The collected timestamp is the physical counter minus a physical offset. If any of the following are true, then the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • SCR_EL3.ECVEn is 0. • CNTHCTL_EL2.ECV is 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |

All other values are reserved.

If EL2 is not implemented or EL2 is disabled in the current Security state, then the Effective value of this field is 0b01 , other than for a direct read of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TS, bit [5]

Timestamp sample enable. Enables recording of a Timestamp packet when the owning Exception level is EL2.

| TS   | Meaning                              |
|------|--------------------------------------|
| 0b0  | Timestamp packet recording disabled. |
| 0b1  | Timestamp packet recording enabled.  |

If the Profiling Buffer owning Exception level is EL1, then this field is ignored by the PE. For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PA, bit [4]

Physical Address Sample Enable.

| PA   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Physical addresses are not collected. |
| 0b1  | Physical addresses are collected.     |

If the Profiling Buffer owning Exception level is EL2, then this field determines whether physical addresses are collected.

If EL2 is not implemented or EL2 is disabled in the owning Security state, then the Effective value of this field is 1.

For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CX, bit [3]

CONTEXTIDR\_EL2 sample enable. Enables recording of a Context packet containing the value of CONTEXTIDR\_EL2.

| CX   | Meaning                            |
|------|------------------------------------|
| 0b0  | CONTEXTIDR_EL2 recording disabled. |

| CX   | Meaning                           |
|------|-----------------------------------|
| 0b1  | CONTEXTIDR_EL2 recording enabled. |

The PE ignores the value of this field and CONTEXTIDR\_EL2 is not recorded when EL2 is not implemented or EL2 is disabled in the current Security state.

For more information, see Controlling the data that is collected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## E2SPE, bit [1]

EL2 Statistical Profiling Enable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MDCR\_EL2.E2PB != '00', access to this field is RES0.
- Otherwise, access to this field is RW.

## E0HSPE, bit [0]

EL0 Statistical Profiling Enable.

| E2SPE   | Meaning                   |
|---------|---------------------------|
| 0b0     | Sampling disabled at EL2. |
| 0b1     | Sampling enabled at EL2.  |

| E0HSPE   | Meaning                   |
|----------|---------------------------|
| 0b0      | Sampling disabled at EL0. |
| 0b1      | Sampling enabled at EL0.  |

If the Effective value of HCR\_EL2.TGE is 0, then this field is ignored by the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MDCR\_EL2.E2PB != '00', access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing PMSCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = PMSCR_EL2;
```

MSR PMSCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSCR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, PMSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x828]; else X[t, 64] = PMSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = PMSCR_EL2; else X[t, 64] = PMSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSCR_EL1;
```

MSR PMSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSCR_EL1 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x828] = X[t, 64]; else PMSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then PMSCR_EL2 = X[t, 64]; else PMSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSCR_EL1 = X[t, 64];
```

## D24.7.10 PMSDSFR\_EL1, Sampling Data Source Filter Register

The PMSDSFR\_EL1 characteristics are:

## Purpose

Controls sample filtering by Data Source.

## Configuration

This register is present only when FEAT\_SPE\_FDS is implemented. Otherwise, direct accesses to PMSDSFR\_EL1 are UNDEFINED.

## Attributes

PMSDSFR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      | 32   |
|------|------|------|
|      | S<m> |      |
| 31   |      | 0    |
|      | S<m> |      |

S&lt;m&gt; , bits [m], for m = 63 to 0

When filtering on Data Source &lt;m&gt; is supported:

S[&lt;m&gt;] is the Data Source filter for IMPLEMENTATION DEFINED Data Source &lt;m&gt;.

| S<m>   | Meaning                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------|
| 0b0    | If PMSFCR_EL1.FDS is 1, do not record load operations that have bits [5:0] of the Data Source packet set to <m>. |
| 0b1    | Load operations with Data Source <m> are unaffected by PMSFCR_EL1.FDS.                                           |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Accessing PMSDSFR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSDSFR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b100 |

```
if !IsFeatureImplemented(FEAT_SPE_FDS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS3 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMSDSFR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS3 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x858]; else X[t, 64] = PMSDSFR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS3 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS3 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSDSFR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSDSFR_EL1;
```

MSR PMSDSFR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1010 | 0b100 |

```
if !IsFeatureImplemented(FEAT_SPE_FDS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS3 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMSDSFR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS3 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x858] = X[t, 64]; else PMSDSFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMS3 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMS3 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSDSFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSDSFR_EL1 = X[t, 64];
```

## D24.7.11 PMSEVFR\_EL1, Sampling Event Filter Register

The PMSEVFR\_EL1 characteristics are:

## Purpose

Controls sample filtering by events. The overall filter is the logical AND of these filters. For example, if PMSEVFR\_EL1.E[3] and PMSEVFR\_EL1.E[5] are both set to 1, only samples that have both event 3 (Level 1 unified or data cache refill) and event 5 (TLB walk) set to 1 are recorded.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSEVFR\_EL1 are UNDEFINED.

## Attributes

PMSEVFR\_EL1 is a 64-bit register.

## Field descriptions

E[63], bit [63]

<!-- image -->

When event 63 is implemented and filtering on event 63 is supported:

Filter on IMPLEMENTATION DEFINED event 63.

| E[63]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 63 is ignored.                           |
| 0b1     | Do not record samples that have event 63 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[62], bit [62]

## When event 62 is implemented and filtering on event 62 is supported:

Filter on IMPLEMENTATION DEFINED event 62.

| E[62]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 62 is ignored.                           |
| 0b1     | Do not record samples that have event 62 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[61], bit [61]

## When event 61 is implemented and filtering on event 61 is supported:

Filter on IMPLEMENTATION DEFINED event 61.

| E[61]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 61 is ignored.                           |
| 0b1     | Do not record samples that have event 61 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[60], bit [60]

## When event 60 is implemented and filtering on event 60 is supported:

Filter on IMPLEMENTATION DEFINED event 60.

| E[60]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 60 is ignored.                           |
| 0b1     | Do not record samples that have event 60 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[59], bit [59]

## When event 59 is implemented and filtering on event 59 is supported:

Filter on IMPLEMENTATION DEFINED event 59.

| E[59]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 59 is ignored.                           |
| 0b1     | Do not record samples that have event 59 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[58], bit [58]

## When event 58 is implemented and filtering on event 58 is supported:

Filter on IMPLEMENTATION DEFINED event 58.

| E[58]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 58 is ignored.                           |
| 0b1     | Do not record samples that have event 58 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[57], bit [57]

## When event 57 is implemented and filtering on event 57 is supported:

Filter on IMPLEMENTATION DEFINED event 57.

| E[57]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 57 is ignored.                           |
| 0b1     | Do not record samples that have event 57 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[56], bit [56]

## When event 56 is implemented and filtering on event 56 is supported:

Filter on IMPLEMENTATION DEFINED event 56.

| E[56]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 56 is ignored.                           |
| 0b1     | Do not record samples that have event 56 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[55], bit [55]

## When event 55 is implemented and filtering on event 55 is supported:

Filter on IMPLEMENTATION DEFINED event 55.

| E[55]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 55 is ignored.                           |
| 0b1     | Do not record samples that have event 55 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[54], bit [54]

## When event 54 is implemented and filtering on event 54 is supported:

Filter on IMPLEMENTATION DEFINED event 54.

| E[54]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 54 is ignored.                           |
| 0b1     | Do not record samples that have event 54 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[53], bit [53]

## When event 53 is implemented and filtering on event 53 is supported:

Filter on IMPLEMENTATION DEFINED event 53.

| E[53]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 53 is ignored.                           |
| 0b1     | Do not record samples that have event 53 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[52], bit [52]

## When event 52 is implemented and filtering on event 52 is supported:

Filter on IMPLEMENTATION DEFINED event 52.

| E[52]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 52 is ignored.                           |
| 0b1     | Do not record samples that have event 52 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[51], bit [51]

## When event 51 is implemented and filtering on event 51 is supported:

Filter on IMPLEMENTATION DEFINED event 51.

| E[51]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 51 is ignored.                           |
| 0b1     | Do not record samples that have event 51 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[50], bit [50]

## When event 50 is implemented and filtering on event 50 is supported:

Filter on IMPLEMENTATION DEFINED event 50.

| E[50]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 50 is ignored.                           |
| 0b1     | Do not record samples that have event 50 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[49], bit [49]

## When event 49 is implemented and filtering on event 49 is supported:

Filter on IMPLEMENTATION DEFINED event 49.

| E[49]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 49 is ignored.                           |
| 0b1     | Do not record samples that have event 49 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[48], bit [48]

## When event 48 is implemented and filtering on event 48 is supported:

Filter on IMPLEMENTATION DEFINED event 48.

| E[48]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 48 is ignored.                           |
| 0b1     | Do not record samples that have event 48 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Bits [47:32]

Reserved, RAZ/WI.

## E[31], bit [31]

## When FEAT\_SPEv1p4 is not implemented, event 31 is implemented, and filtering on event 31 is supported:

Filter on IMPLEMENTATION DEFINED event 31.

| E[31]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 31 is ignored.                           |
| 0b1     | Do not record samples that have event 31 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[30], bit [30]

## When FEAT\_SPEv1p4 is not implemented, event 30 is implemented, and filtering on event 30 is supported:

Filter on IMPLEMENTATION DEFINED event 30.

| E[30]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 30 is ignored.                           |
| 0b1     | Do not record samples that have event 30 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[29], bit [29]

## When FEAT\_SPEv1p4 is not implemented, event 29 is implemented, and filtering on event 29 is supported:

Filter on IMPLEMENTATION DEFINED event 29.

| E[29]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 29 is ignored.                           |
| 0b1     | Do not record samples that have event 29 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[28], bit [28]

When FEAT\_SPEv1p4 is not implemented, event 28 is implemented, and filtering on event 28 is supported:

Filter on IMPLEMENTATION DEFINED event 28.

| E[28]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 28 is ignored.                           |
| 0b1     | Do not record samples that have event 28 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[27], bit [27]

## When FEAT\_SPEv1p4 is not implemented, event 27 is implemented, and filtering on event 27 is supported:

Filter on IMPLEMENTATION DEFINED event 27.

| E[27]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 27 is ignored.                           |
| 0b1     | Do not record samples that have event 27 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[26], bit [26]

## When FEAT\_SPEv1p4 is not implemented, event 26 is implemented, and filtering on event 26 is supported:

Filter on IMPLEMENTATION DEFINED event 26.

| E[26]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 26 is ignored.                           |
| 0b1     | Do not record samples that have event 26 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[25], bit [25]

## When (FEAT\_SPE\_SME is implemented or FEAT\_SPEv1p5 is implemented) and event 25 is implemented:

Filter on SMCU or other shared resource operation event.

| E[25]   | Meaning                                                                                |
|---------|----------------------------------------------------------------------------------------|
| 0b0     | SMCUor other shared resource operation event is ignored.                               |
| 0b1     | Do not record samples that have theSMCU or other shared resource operation event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPEv1p4 is not implemented, event 25 is implemented, and filtering on event 25 is supported:

Filter on IMPLEMENTATION DEFINED event 25.

| E[25]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 25 is ignored.                           |
| 0b1     | Do not record samples that have event 25 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[24], bit [24]

When FEAT\_SPE\_SME is implemented:

Filter on Streaming SVE mode event.

| E[24]   | Meaning                                                            |
|---------|--------------------------------------------------------------------|
| 0b0     | Streaming SVE mode event is ignored.                               |
| 0b1     | Do not record samples that have the Streaming SVE mode event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPEv1p4 is not implemented, event 24 is implemented, and filtering on event 24 is supported:

Filter on IMPLEMENTATION DEFINED event 24.

| E[24]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 24 is ignored.                           |
| 0b1     | Do not record samples that have event 24 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[23], bit [23]

## When FEAT\_SPEv1p4 is implemented and event 23 is implemented:

Filter on Data snooped event.

| E[23]   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0     | Data snooped event is ignored.                               |
| 0b1     | Do not record samples that have the Data snooped event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[22], bit [22]

## When FEAT\_SPEv1p4 is implemented and event 22 is implemented:

Filter on Recently fetched event.

| E[22]   | Meaning                                                          |
|---------|------------------------------------------------------------------|
| 0b0     | Recently fetched event is ignored.                               |
| 0b1     | Do not record samples that have the Recently fetched event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[21], bit [21]

## When FEAT\_SPEv1p4 is implemented and event 21 is implemented:

Filter on Cache data modified event.

| E[21]   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b0     | Cache data modified event is ignored.                               |
| 0b1     | Do not record samples that have the Cache data modified event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[20], bit [20]

## When FEAT\_SPEv1p4 is implemented and event 20 is implemented:

Filter on Level 2 data cache miss event.

| E[20]   | Meaning                                                                 |
|---------|-------------------------------------------------------------------------|
| 0b0     | Level 2 data cache miss event is ignored.                               |
| 0b1     | Do not record samples that have the Level 2 data cache miss event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[19], bit [19]

## When FEAT\_SPEv1p4 is implemented and event 19 is implemented:

Filter on Level 2 data cache access event.

| E[19]   | Meaning                                                                   |
|---------|---------------------------------------------------------------------------|
| 0b0     | Level 2 data cache access event is ignored.                               |
| 0b1     | Do not record samples that have the Level 2 data cache access event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[18], bit [18]

## When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented):

Filter on Empty predicate event.

| E[18]   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | Empty predicate event is ignored.                               |
| 0b1     | Do not record samples that have the Empty predicate event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[17], bit [17]

## When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented):

Filter on Partial or empty predicate event.

| E[17]   | Meaning                                                                    |
|---------|----------------------------------------------------------------------------|
| 0b0     | Partial or empty predicate event is ignored.                               |
| 0b1     | Do not record samples that have the Partial or empty predicate event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Bit [16]

Reserved, RAZ/WI.

E[15], bit [15]

## When event 15 is implemented and filtering on event 15 is supported:

Filter on IMPLEMENTATION DEFINED event 15.

| E[15]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 15 is ignored.                           |
| 0b1     | Do not record samples that have event 15 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[14], bit [14]

## When event 14 is implemented and filtering on event 14 is supported:

Filter on IMPLEMENTATION DEFINED event 14.

| E[14]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 14 is ignored.                           |
| 0b1     | Do not record samples that have event 14 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[13], bit [13]

## When event 13 is implemented and filtering on event 13 is supported:

Filter on IMPLEMENTATION DEFINED event 13.

| E[13]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 13 is ignored.                           |
| 0b1     | Do not record samples that have event 13 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[12], bit [12]

## When event 12 is implemented and filtering on event 12 is supported:

Filter on IMPLEMENTATION DEFINED event 12.

| E[12]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 12 is ignored.                           |
| 0b1     | Do not record samples that have event 12 == 0. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[11], bit [11]

## When FEAT\_SPEv1p1 is implemented:

Filter on Misalignment event.

| E[11]   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0     | Misalignment event is ignored.                               |
| 0b1     | Do not record samples that have the Misalignment event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[10], bit [10]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 10 is optionally supported) and event 10 is implemented:

Filter on Remote access event.

| E[10]   | Meaning                                                       |
|---------|---------------------------------------------------------------|
| 0b0     | Remote access event is ignored.                               |
| 0b1     | Do not record samples that have the Remote access event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[9], bit [9]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 9 is optionally supported) and event 9 is implemented:

Filter on Last Level cache miss event.

| E[9]   | Meaning                                                               |
|--------|-----------------------------------------------------------------------|
| 0b0    | Last Level cache miss event is ignored.                               |
| 0b1    | Do not record samples that have the Last Level cache miss event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[8], bit [8]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 8 is optionally supported) and event 8 is implemented:

Filter on Last Level cache access event.

| E[8]   | Meaning                                                                 |
|--------|-------------------------------------------------------------------------|
| 0b0    | Last Level cache access event is ignored.                               |
| 0b1    | Do not record samples that have the Last Level cache access event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[7], bit [7]

Filter on Mispredicted event.

| E[7]   | Meaning                                                      |
|--------|--------------------------------------------------------------|
| 0b0    | Mispredicted event is ignored.                               |
| 0b1    | Do not record samples that have the Mispredicted event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

E[6], bit [6]

## When FEAT\_SPE\_FnE is implemented:

Filter on Not taken event.

| E[6]   | Meaning                                                   |
|--------|-----------------------------------------------------------|
| 0b0    | Not taken event is ignored.                               |
| 0b1    | Do not record samples that have the Not taken event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[5], bit [5]

Filter on TLB walk event.

| E[5]   | Meaning                                                  |
|--------|----------------------------------------------------------|
| 0b0    | TLB walk event is ignored.                               |
| 0b1    | Do not record samples that have the TLB walk event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E[4], bit [4]

## When FEAT\_SPEv1p4 is implemented or filtering on event 4 is optionally supported:

Filter on TLB access event.

| E[4]   | Meaning                                                    |
|--------|------------------------------------------------------------|
| 0b0    | TLB access event is ignored.                               |
| 0b1    | Do not record samples that have the TLB access event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[3], bit [3]

Filter on Level 1 data cache refill or miss event.

| E[3]   | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0    | Level 1 data cache refill or miss event is ignored.                               |
| 0b1    | Do not record samples that have the Level 1 data cache refill or miss event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E[2], bit [2]

## When FEAT\_SPEv1p4 is implemented or filtering on event 2 is optionally supported:

Filter on Level 1 data cache access event.

| E[2]   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0    | Level 1 data cache access event is ignored.                               |
| 0b1    | Do not record samples that have the Level 1 data cache access event == 0. |

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[1], bit [1]

## When the PE supports sampling of speculative instructions:

Filter on Architecturally retired event.

| E[1]   | Meaning                                   |
|--------|-------------------------------------------|
| 0b0    | Architecturally retired event is ignored. |

0b1

Do not record samples that have the Architecturally retired event == 0.

This field is ignored by the PE when PMSFCR\_EL1.FE is 0.

If the PE does not support the sampling of speculative instructions, or always discards the sample record for speculative instructions, this bit reads as an UNKNOWN value and the PE ignores its value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, UNKNOWN.

## Bit [0]

Reserved, RAZ/WI.

## Accessing PMSEVFR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSEVFR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b101 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSEVFR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x830]; else X[t, 64] = PMSEVFR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = PMSEVFR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSEVFR_EL1;
```

MSR PMSEVFR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b101 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSEVFR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x830] = X[t, 64]; else PMSEVFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSEVFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSEVFR_EL1 = X[t, 64];
```

## D24.7.12 PMSFCR\_EL1, Sampling Filter Control Register

The PMSFCR\_EL1 characteristics are:

## Purpose

Controls sample filtering. The filter is the logical AND of the filters controlled by FDS, FnE, FL, FT, and FE bits. For example, if PMSFCR\_EL1.FE is 1 and PMSFCR\_EL1.FT is 1, then only samples including the selected types and the selected events will be recorded.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSFCR\_EL1 are UNDEFINED.

## Attributes

PMSFCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 53 52   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   | 48 47 32   |
|------|---------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|      | RES0    | TYPEm      |            |            | RES0       |            |            |            |            |            |            |            |
| 31   |         |            | 16 15      | 5 4        | 5 4        | 3          | 2          | 1          | 0          |            |            |            |
|      | RES0    | TYPE       |            | RES0       | FDS FnE    |            | FL         | FT         | FE         |            |            |            |

## Bits [63:53]

Reserved, RES0.

## TYPEm, bits [52:48]

When FEAT\_SPE\_EFT is implemented:

## SIMDm, bit [4]

SIMD filter mask.

| SIMDm   | Meaning                                                                                                                                           |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | PMSFCR_EL1.SIMD controls whether SIMD operations are recorded as part of a Boolean-OR filter with other masked operation type filter controls.    |
| 0b1     | PMSFCR_EL1.SIMD controls whether SIMD operations are recorded as part of a Boolean-AND filter with other unmasked operation type filter controls. |

This field is ignored by the PE when PMSFCR\_EL1.FT is 0.

The reset behavior of this field is:

<!-- image -->

SIMDm

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FPm, bit [3]

Floating-point filter mask.

| FPm   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | PMSFCR_EL1.FP controls whether floating-point operations are recorded as part of a Boolean-OR filter with other masked operation type filter controls.    |
| 0b1   | PMSFCR_EL1.FP controls whether floating-point operations are recorded as part of a Boolean-AND filter with other unmasked operation type filter controls. |

This field is ignored by the PE when PMSFCR\_EL1.FT is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## STm, bit [2]

Store filter mask.

| STm   | Meaning                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | PMSFCR_EL1.ST controls whether store operations are recorded as part of a Boolean-OR filter with other masked operation type filter controls.    |
| 0b1   | PMSFCR_EL1.ST controls whether store operations are recorded as part of a Boolean-AND filter with other unmasked operation type filter controls. |

This field is ignored by the PE when PMSFCR\_EL1.FT is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LDm, bit [1]

Load filter mask.

| LDm   | Meaning                                                                                                                                         |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | PMSFCR_EL1.LD controls whether load operations are recorded as part of a Boolean-OR filter with other masked operation type filter controls.    |
| 0b1   | PMSFCR_EL1.LD controls whether load operations are recorded as part of a Boolean-AND filter with other unmasked operation type filter controls. |

This field is ignored by the PE when PMSFCR\_EL1.FT is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bm, bit [0]

Branch filter mask.

| Bm   | Meaning                                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | PMSFCR_EL1.B controls whether branch operations are recorded as part of a Boolean-OR filter with other masked operation type filter controls.    |
| 0b1  | PMSFCR_EL1.B controls whether branch operations are recorded as part of a Boolean-AND filter with other unmasked operation type filter controls. |

This field is ignored by the PE when PMSFCR\_EL1.FT is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPE\_EFT is not implemented:

## Bits [4:0]

Reserved, RES0.

Bits [47:21]

Reserved, RES0.

TYPE, bits [20:16]

SIMD, bit [4]

## When FEAT\_SPE\_EFT is implemented:

SIMD filter enable.

| SIMD   | Meaning                                                                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If PMSFCR_EL1.SIMDm is 1, then record only operations that are not SIMD operations. Otherwise, do not record SIMD operations, unless allowed by another operation type filter. |
| 0b1    | If PMSFCR_EL1.SIMDm is 1, then record only operations that are SIMD operations. Otherwise, record all SIMD operations.                                                         |

<!-- image -->

<!-- image -->

This field is ignored by the PE and no records are removed by this filter when any of the following apply:

- PMSFCR\_EL1.FT is 0.
- PMSFCR\_EL1.SIMDm is 0 and the values of the PMSFCR\_EL1.{SIMD, FP, ST, LD, B} bits for which the corresponding PMSFCR\_EL1.{SIMDm, FPm, STm, LDm, Bm} bit is zero are all zero.

For filtering purposes, SIMD operations means all Advanced SIMD, SVE, and SME SIMD operations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

FP, bit [3]

## When FEAT\_SPE\_EFT is implemented:

Floating-point filter enable.

| FP   | Meaning                                                                                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | If PMSFCR_EL1.FPm is 1, then record only operations that are not floating-point operations. Otherwise, do not record floating-point operations, unless allowed by another operation type filter. |
| 0b1  | If PMSFCR_EL1.FPm is 1, then record only operations that are floating-point operations. Otherwise, record all floating-point operations.                                                         |

This field is ignored by the PE and no records are removed by this filter when any of the following apply:

- PMSFCR\_EL1.FT is 0.
- PMSFCR\_EL1.FPm is 0 and the values of the PMSFCR\_EL1.{SIMD, FP, ST, LD, B} bits for which the corresponding PMSFCR\_EL1.{SIMDm, FPm, STm, LDm, Bm} bit is zero are all zero.

For filtering purposes, floating-point operations means all scalar, Advanced SIMD, SVE, and SME floating-point operations, as defined by the FP\_SPEC event.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ST, bit [2]

Store filter enable.

| ST   | Meaning                                                                                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.STm is 1, then record only operations that are not store operations. Otherwise, do not record store operations, unless allowed by another operation type filter. |

| ST   | Meaning                                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1  | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.STm is 1, then record only operations that are store operations. Otherwise, record all store operations. |

This field is ignored by the PE and no records are removed by this filter when any of the following apply:

- PMSFCR\_EL1.FT is 0.
- FEAT\_SPE\_EFT is implemented, PMSFCR\_EL1.STm is 0, and the values of the PMSFCR\_EL1.{SIMD, FP, ST, LD, B} bits for which the corresponding PMSFCR\_EL1.{SIMDm, FPm, STm, LDm, Bm} bit is zero are all zero.

For filtering purposes, store operations includes vector stores and all atomic operations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LD, bit [1]

Load filter enable.

| LD   | Meaning                                                                                                                                                                                                      |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.LDm is 1, then record only operations that are not load operations. Otherwise, do not record load operations, unless allowed by another operation type filter. |
| 0b1  | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.LDm is 1, then record only operations that are load operations. Otherwise, record all load operations.                                                         |

This field is ignored by the PE and no records are removed by this filter when any of the following apply:

- PMSFCR\_EL1.FT is 0.
- FEAT\_SPE\_EFT is implemented, PMSFCR\_EL1.LDm is 0, and the values of the PMSFCR\_EL1.{SIMD, FP, ST, LD, B} bits for which the corresponding PMSFCR\_EL1.{SIMDm, FPm, STm, LDm, Bm} bit is zero are all zero.

For filtering purposes, load operations includes vector loads and atomic operations that return a value to the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## B, bit [0]

Branch filter enable.

| B   | Meaning                                                                                                                                                        |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.Bm is 1, then record only operations that are not branch operations. Otherwise, do not record branch operations. |

| B   | Meaning                                                                                                                                                 |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1 | If FEAT_SPE_EFT is implemented and PMSFCR_EL1.Bm is 1, then record only operations that are branch operations. Otherwise, record all branch operations. |

This field is ignored by the PE and no records are removed by this filter when any of the following apply:

- PMSFCR\_EL1.FT is 0.
- FEAT\_SPE\_EFT is implemented, PMSFCR\_EL1.Bm is 0, and the values of the PMSFCR\_EL1.{SIMD, FP, ST, LD, B} bits for which the corresponding PMSFCR\_EL1.{SIMDm, FPm, STm, LDm, Bm} bit is zero are all zero.

For filtering purposes, branch operations includes exception returns.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:5]

Reserved, RES0.

## FDS, bit [4]

## When FEAT\_SPE\_FDS is implemented:

Filter by Data Source.

| FDS   | Meaning                                                                                                                               |
|-------|---------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Data Source filtering disabled.                                                                                                       |
| 0b1   | Data Source filtering enabled. Samples of load instructions reporting a Data Source not selected by PMSDSFR_EL1 will not be recorded. |

If PMSFCR\_EL1.FDS is 1 and PMSDSFR\_EL1 is zero, then no load operations with a Data Source will be recorded.

Load operations without a Data Source and other sampled operations are unaffected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

FnE, bit [3]

## When FEAT\_SPE\_FnE is implemented:

Filter by event, inverted.

| FnE   | Meaning                            |
|-------|------------------------------------|
| 0b0   | Inverted event filtering disabled. |

| FnE   | Meaning                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0b1   | Inverted event filtering enabled. Samples including the events selected by PMSNEVFR_EL1 will not be recorded. |

If any of the following are true, then it is CONSTRAINED UNPREDICTABLE whether no samples are recorded or the PE behaves as if PMSFCR\_EL1.FnE is 0:

- PMSFCR\_EL1.FnE is 1 and PMSNEVFR\_EL1 is zero.
- PMSFCR\_EL1.FnE is 1, PMSFCR\_EL1.FE is 1, and there exists a value x such that PMSEVFR\_EL1.E[x] is 1 and PMSNEVFR\_EL1.E[x] is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FL, bit [2]

Filter by latency.

| FL   | Meaning                                                                                                     |
|------|-------------------------------------------------------------------------------------------------------------|
| 0b0  | Latency filtering disabled.                                                                                 |
| 0b1  | Latency filtering enabled. Samples with a total latency less than PMSLATFR_EL1.MINLAT will not be recorded. |

If this field is 1 and PMSLATFR\_EL1.MINLAT is zero, then it is CONSTRAINED UNPREDICTABLE whether no samples are recorded or the PE behaves as if PMSFCR\_EL1.FL is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FT, bit [1]

Filter by type. The filter is controlled by the TYPE and, if FEAT\_SPE\_EFT is implemented, TYPEm fields.

| FT   | Meaning                                                                             |
|------|-------------------------------------------------------------------------------------|
| 0b0  | Type filtering disabled.                                                            |
| 0b1  | Type filtering enabled. Samples not one of the selected types will not be recorded. |

Type filtering filters according to the type of the sampled operation.

If FEAT\_SPE\_EFT is not implemented, this field is 1, and the PMSFCR\_EL1.{ST, LD, B} bits are all zero, then it is CONSTRAINED UNPREDICTABLE whether no samples are recorded or the PE behaves as if PMSFCR\_EL1.FT is 0.

For more information, see Filtering by operation type.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FE, bit [0]

Filter by event.

| FE   | Meaning                                                                                                 |
|------|---------------------------------------------------------------------------------------------------------|
| 0b0  | Event filtering disabled.                                                                               |
| 0b1  | Event filtering enabled. Samples not including the events selected by PMSEVFR_EL1 will not be recorded. |

If any of the following are true, then it is CONSTRAINED UNPREDICTABLE whether no samples are recorded or the PE behaves as if PMSFCR\_EL1.FE is 0:

- PMSFCR\_EL1.FE is 1 and PMSEVFR\_EL1 is zero.
- FEAT\_SPE\_FnE is implemented, PMSFCR\_EL1.FnE is 1, PMSFCR\_EL1.FE is 1, and there exists a value x such that PMSEVFR\_EL1.E[x] is 1 and PMSNEVFR\_EL1.E[x] is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSFCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSFCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b100 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else
```

AArch64.SystemAccessTrap(EL3, 0x18);

<!-- formula-not-decoded -->

MSR PMSFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b100 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSFCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSFCR_EL1 = X[t, 64];
```

## D24.7.13 PMSICR\_EL1, Sampling Interval Counter Register

The PMSICR\_EL1 characteristics are:

## Purpose

Software must write zero to PMSICR\_EL1 before enabling sample profiling for a sampling session. Software must then treat PMSICR\_EL1 as an opaque, 64-bit, read/write register used for context switches only.

## Configuration

The value of PMSICR\_EL1 does not change whilst profiling is disabled.

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSICR\_EL1 are UNDEFINED.

## Attributes

PMSICR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ECOUNT, bits [63:56]

## When FEAT\_SPE\_ERnd is implemented:

Secondary sample interval counter. Provides the secondary counter used after the primary counter reaches zero.

While the secondary counter is nonzero and profiling is enabled, the secondary counter decrements by 1 for each member of the sample population. The primary counter also continues to decrement since it is also nonzero. When the secondary counter reaches zero, a member of the sampling population is selected for sampling.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [55:32]

Reserved, RES0.

## COUNT, bits [31:0]

Primary sample interval counter. Provides the primary counter used for sampling.

When the PE moves from a state or Exception level where profiling is disabled to a state or Exception level where profiling is enabled, if the value of this register is zero, then the primary counter is loaded from PMSIRR\_EL1.

While the primary counter is nonzero and sampling is enabled, the primary counter decrements by 1 for each member of the sample population.

The sample interval counter counts either a number of operations or a number of instructions, depending on the IMPLEMENTATION DEFINED value of PMSIDR\_EL1.ArchInst.

When the counter reaches zero, the behavior depends on the value of PMSIRR\_EL1.RND and whether FEAT\_SPE\_ERnd is implemented:

- If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is implemented, then the secondary counter is set to a random or pseudorandom value in the range 0x00 to 0xFF .
- Otherwise, a member of the sampling population is selected for sampling.
- The primary counter is loaded from PMSIRR\_EL1.

The primary counter is loaded from PMSIRR\_EL1 means:

- PMSICR\_EL1.COUNT[31:8] is set to the value of PMSIRR\_EL1.INTERVAL.
- If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is not implemented, then PMSICR\_EL1.COUNT[7:0] is set to a random or pseudorandom value in the range 0x00 to 0xFF .
- Otherwise, PMSICR\_EL1.COUNT[7:0] is set to 0x00 .

For more information, see Initializing the sample interval counters and Behavior of the sample interval counter while profiling is enabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSICR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMSICR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSICR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x838]; else X[t, 64] = PMSICR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else
```

AArch64.SystemAccessTrap(EL3, 0x18);

<!-- formula-not-decoded -->

MSR PMSICR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSICR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x838] = X[t, 64]; else PMSICR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSICR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSICR_EL1 = X[t, 64];
```

## D24.7.14 PMSIDR\_EL1, Sampling Profiling ID Register

The PMSIDR\_EL1 characteristics are:

## Purpose

Describes the Statistical Profiling implementation to software.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSIDR\_EL1 are UNDEFINED.

## Attributes

PMSIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## SME, bit [32]

SPE for SME. Describes support for the Scalable Matrix Extensions to Statistical Profiling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SME   | Meaning                                                                       |
|-------|-------------------------------------------------------------------------------|
| 0b0   | The SMEextensions to the Statistical Profiling Extension are not implemented. |
| 0b1   | Adds support for Statistical Profiling of the Scalable Matrix Extensions.     |

FEAT\_SPE\_SME implements the functionality identified by the value 1.

Access to this field is RO.

## ALTCLK, bits [31:28]

Alternate clock domain.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ALTCLK   | Meaning                                                                       |
|----------|-------------------------------------------------------------------------------|
| 0b0000   | Alternate clock domain not implemented, or CPU clock domain.                  |
| 0b0001   | The external Streaming Mode Compute Unit provides the alternate clock domain. |
| 0b1111   | IMPLEMENTATION DEFINED clock domain.                                          |

All other values are reserved.

FEAT\_SPE\_ALTCLK implements the functionality identified by a nonzero value.

Access to this field is RO.

## FPF, bit [27]

Floating-point flag. Describes whether Operation Type packets for sampled scalar and SIMD operations contain floating-point and Advanced SIMD indications.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPF   | Meaning                                                                                                                    |
|-------|----------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Operation Type packets for scalar and Advanced SIMD operations do not contain floating-point or Advanced SIMD information. |
| 0b1   | Operation Type packets for scalar and Advanced SIMD operations contain floating-point or Advanced SIMD information.        |

FEAT\_SPE\_FPF implements the functionality identified by the value 1.

Access to this field is RO.

## EFT, bit [26]

Extended filtering by type. Describes whether Extended filtering by operation type is supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EFT   | Meaning                                                          |
|-------|------------------------------------------------------------------|
| 0b0   | PMSFCR_EL1.{SIMDm, FPm, STm, Bm, LDm, SIMD, FP} are RES0.        |
| 0b1   | PMSFCR_EL1.{SIMDm, FPm, STm, Bm, LDm, SIMD, FP} are implemented. |

FEAT\_SPE\_EFT implements the functionality identified by the value 1.

Access to this field is RO.

## CRR, bit [25]

Call Return branch records. Describes whether the Operation Type packets for sampled branch operations contain Call Return information.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CRR   | Meaning                                                                              |
|-------|--------------------------------------------------------------------------------------|
| 0b0   | Operation Type packets for branch operations do not contain Call Return information. |
| 0b1   | Operation Type packets for branch operations contain Call Return information.        |

FEAT\_SPE\_CRR implements the functionality identified by the value 1.

Access to this field is RO.

## PBT, bit [24]

Previous branch target Address packet. Describes whether the Previous branch target Address packet is supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PBT   | Meaning                                                |
|-------|--------------------------------------------------------|
| 0b0   | Previous branch target Address packet not implemented. |
| 0b1   | Previous branch target Address packet implemented.     |

FEAT\_SPE\_PBT implements the OPTIONAL functionality identified by the value 1.

Access to this field is RO.

## Format, bits [23:20]

Defines the format of the sample records.

All other values are reserved.

Access to this field is RO.

## CountSize, bits [19:16]

Defines the size of the counters.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CountSize   | Meaning                     |
|-------------|-----------------------------|
| 0b0010      | 12-bit saturating counters. |
| 0b0011      | 16-bit saturating counters. |

All other values are reserved.

Access to this field is RO.

| Format   | Meaning   |
|----------|-----------|
| 0b0000   | Format 0. |

## MaxSize, bits [15:12]

Defines the largest size for a single record, rounded up to a power-of-two. If this is the same as the minimum alignment (PMBIDR\_EL1.Align), then each record is exactly this size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MaxSize   | Meaning    |
|-----------|------------|
| 0b0100    | 16 bytes.  |
| 0b0101    | 32 bytes.  |
| 0b0110    | 64 bytes.  |
| 0b0111    | 128 bytes. |
| 0b1000    | 256 bytes. |
| 0b1001    | 512 bytes. |
| 0b1010    | 1KB.       |
| 0b1011    | 2KB.       |

All other values are reserved.

The values 0b0100 and 0b0101 are not permitted for an implementation.

Access to this field is RO.

## Interval, bits [11:8]

Minimum sampling interval. This provides guidance from the implementer to the smallest sampling interval.

The interval is defined as a number of either operations or instructions, depending on the IMPLEMENTATION DEFINED value of PMSIDR\_EL1.ArchInst.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Interval   | Meaning                                                  |
|------------|----------------------------------------------------------|
| 0b0000     | 256 operations or instructions, or no minimum specified. |
| 0b0010     | 512 operations or instructions.                          |
| 0b0011     | 768 operations or instructions.                          |
| 0b0100     | 1,024 operations or instructions.                        |
| 0b0101     | 1,536 operations or instructions.                        |
| 0b0110     | 2,048 operations or instructions.                        |
| 0b0111     | 3,072 operations or instructions.                        |
| 0b1000     | 4,096 operations or instructions.                        |

## All other values are reserved.

If this field reads as a nonzero value, then setting the sample interval to a value less than the indicated value is likely to cause a statistically significant number of sample collisions. For example, the smallest interval might indicate the typical size of the speculation window for the implementation. That is, the number of operations or instructions that will be executing in parallel, when the processor implementation is not heavily loaded.

Setting the sample interval to a value greater than or equal to the indicated value does not guarantee a statistically insignificant number of sample collisions, as this is typically dependent on the program being profiled. For example, if the program has a large number of long latency loads due to cache misses, then this might cause more collisions when these operations or instructions are sampled.

For more information, see 'Sample collisions'.

Access to this field is RO.

## FDS, bit [7]

## When FEAT\_SPEv1p4 is implemented:

Filtering by data source.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FDS   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | PMSDSFR_EL1 is not implemented and PMSFCR_EL1.FDS is RES0. |
| 0b1   | PMSDSFR_EL1 and PMSFCR_EL1.FDS are implemented.            |

FEAT\_SPE\_FDS implements the functionality identified by the value 1.

From Armv8.9, if FEAT\_SPE\_LDS is implemented, the value 0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

FnE, bit [6]

## When FEAT\_SPE\_FnE is implemented:

Filtering by events, inverted.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FnE   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | PMSNEVFR_EL1 is not implemented and PMSFCR_EL1.FnE is RES0. |
| 0b1   | PMSNEVFR_EL1 and PMSFCR_EL1.FnE are implemented.            |

FEAT\_SPE\_FnE implements the functionality identified by the value 1.

From Armv8.7, if FEAT\_SPE is implemented, the value 0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## ERnd, bit [5]

Defines how the random number generator is used in determining the interval between samples, when enabled by PMSIRR\_EL1.RND.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ERnd   | Meaning                                                                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | The random number is added at the start of the interval, and the sample is taken and a new interval started when the combined interval expires.                                 |
| 0b1    | The random number is added and the new interval started after the interval programmed in PMSIRR_EL1.INTERVAL expires, and the sample is taken when the random interval expires. |

FEAT\_SPE\_ERnd implements the functionality identified by the value 1.

Access to this field is RO.

## LDS, bit [4]

Data source indicator for sampled load instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LDS   | Meaning                             |
|-------|-------------------------------------|
| 0b0   | Loaded data source not implemented. |
| 0b1   | Loaded data source implemented.     |

FEAT\_SPE\_LDS implements the functionality identified by the value 1.

Access to this field is RO.

## ArchInst, bit [3]

Architectural instruction profiling. Defines the subject of the profiling population.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ArchInst   | Meaning                                        |
|------------|------------------------------------------------|
| 0b0        | Micro-op sampling implemented.                 |
| 0b1        | Architecture instruction sampling implemented. |

FEAT\_SPE\_ArchInst implements the functionality identified by the value 1.

Access to this field is RO.

## FL, bit [2]

Filtering by latency.

Reads as 0b1

Access to this field is RO.

## FT, bit [1]

Filtering by operation type.

Reads as 0b1

Access to this field is RO.

## FE, bit [0]

Filtering by events.

Reads as 0b1

Access to this field is RO.

## Accessing PMSIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMSIDR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b111 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSIDR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSIDR_EL1;
```

## D24.7.15 PMSIRR\_EL1, Sampling Interval Reload Register

The PMSIRR\_EL1 characteristics are:

## Purpose

Defines the interval between samples.

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSIRR\_EL1 are UNDEFINED.

## Attributes

PMSIRR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## INTERVAL, bits [31:8]

Bits [31:8] of the PMSICR\_EL1 interval counter reload value. Software must set this to a nonzero value.

If this field is zero, then an UNKNOWN sampling interval is used.

If PMSIDR\_EL1.Interval is nonzero, then it provides guidance from the implementer to the smallest sampling interval that should be used.

Setting this field to a nonzero value smaller than the indicated value is likely to cause a statistically significant number of sample collisions. See Sample collisions. Setting the sample interval to a value greater than or equal to the indicated value does not guarantee a statistically insignificant number of sample collisions, as this is typically dependent on the program being profiled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [7:1]

Reserved, RES0.

## RND, bit [0]

Controls randomization of the sampling interval.

| RND   | Meaning                                          |
|-------|--------------------------------------------------|
| 0b0   | Disable randomization of sampling interval.      |
| 0b1   | Add (pseudo-)random jitter to sampling interval. |

The random number generator is not architected.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSIRR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSIRR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSIRR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x840]; else X[t, 64] = PMSIRR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSIRR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSIRR_EL1;
```

MSR PMSIRR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b011 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSIRR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x840] = X[t, 64]; else PMSIRR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSIRR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSIRR_EL1 = X[t, 64];
```

## D24.7.16 PMSLATFR\_EL1, Sampling Latency Filter Register

The PMSLATFR\_EL1 characteristics are:

## Purpose

Controls sample filtering by latency

## Configuration

This register is present only when FEAT\_SPE is implemented. Otherwise, direct accesses to PMSLATFR\_EL1 are UNDEFINED.

## Attributes

PMSLATFR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32     |
|----------|--------|
| RES0     | 0      |
| 31 16 15 |        |
| RES0     | MINLAT |

## Bits [63:16]

Reserved, RES0.

## MINLAT, bits [15:0]

Minimum latency.

When PMSFCR\_EL1.FL is 1, defines the value used for filtering by latency. Samples with a Total latency less than PMSLATFR\_EL1.MINLAT are not recorded.

If PMSIDR\_EL1.CountSize is 0b0010 , PMSLATFR\_EL1.MINLAT[15:12] is RES0.

This field is ignored by the PE when PMSFCR\_EL1.FL is 0.

For more information, see Filtering by latency.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSLATFR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSLATFR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSLATFR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x848]; else X[t, 64] = PMSLATFR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSLATFR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSLATFR_EL1;
```

MSR PMSLATFR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b110 |

```
if !IsFeatureImplemented(FEAT_SPE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSLATFR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x848] = X[t, 64]; else
```

```
PMSLATFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSLATFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSLATFR_EL1 = X[t, 64];
```

## D24.7.17 PMSNEVFR\_EL1, Sampling Inverted Event Filter Register

The PMSNEVFR\_EL1 characteristics are:

## Purpose

Controls sample filtering by events. The overall inverted filter is the logical OR of these filters. For example, if PMSNEVFR\_EL1.E[3] and PMSNEVFR\_EL1.E[5] are both set to 1, samples that have either event 3 (Level 1 unified or data cache refill) or event 5 (TLB walk) set to 1 are not recorded.

## Configuration

This register is present only when FEAT\_SPE\_FnE is implemented. Otherwise, direct accesses to PMSNEVFR\_EL1 are UNDEFINED.

## Attributes

PMSNEVFR\_EL1 is a 64-bit register.

## Field descriptions

E[63], bit [63]

<!-- image -->

When event 63 is implemented and filtering on event 63 is supported:

Filter on IMPLEMENTATION DEFINED event 63.

| E[63]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 63 is ignored.                           |
| 0b1     | Do not record samples that have event 63 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[62], bit [62]

## When event 62 is implemented and filtering on event 62 is supported:

Filter on IMPLEMENTATION DEFINED event 62.

| E[62]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 62 is ignored.                           |
| 0b1     | Do not record samples that have event 62 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[61], bit [61]

## When event 61 is implemented and filtering on event 61 is supported:

Filter on IMPLEMENTATION DEFINED event 61.

| E[61]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 61 is ignored.                           |
| 0b1     | Do not record samples that have event 61 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[60], bit [60]

## When event 60 is implemented and filtering on event 60 is supported:

Filter on IMPLEMENTATION DEFINED event 60.

| E[60]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 60 is ignored.                           |
| 0b1     | Do not record samples that have event 60 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[59], bit [59]

## When event 59 is implemented and filtering on event 59 is supported:

Filter on IMPLEMENTATION DEFINED event 59.

| E[59]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 59 is ignored.                           |
| 0b1     | Do not record samples that have event 59 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[58], bit [58]

## When event 58 is implemented and filtering on event 58 is supported:

Filter on IMPLEMENTATION DEFINED event 58.

| E[58]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 58 is ignored.                           |
| 0b1     | Do not record samples that have event 58 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[57], bit [57]

## When event 57 is implemented and filtering on event 57 is supported:

Filter on IMPLEMENTATION DEFINED event 57.

| E[57]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 57 is ignored.                           |
| 0b1     | Do not record samples that have event 57 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[56], bit [56]

## When event 56 is implemented and filtering on event 56 is supported:

Filter on IMPLEMENTATION DEFINED event 56.

| E[56]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 56 is ignored.                           |
| 0b1     | Do not record samples that have event 56 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[55], bit [55]

## When event 55 is implemented and filtering on event 55 is supported:

Filter on IMPLEMENTATION DEFINED event 55.

| E[55]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 55 is ignored.                           |
| 0b1     | Do not record samples that have event 55 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[54], bit [54]

## When event 54 is implemented and filtering on event 54 is supported:

Filter on IMPLEMENTATION DEFINED event 54.

| E[54]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 54 is ignored.                           |
| 0b1     | Do not record samples that have event 54 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[53], bit [53]

## When event 53 is implemented and filtering on event 53 is supported:

Filter on IMPLEMENTATION DEFINED event 53.

| E[53]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 53 is ignored.                           |
| 0b1     | Do not record samples that have event 53 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[52], bit [52]

## When event 52 is implemented and filtering on event 52 is supported:

Filter on IMPLEMENTATION DEFINED event 52.

| E[52]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 52 is ignored.                           |
| 0b1     | Do not record samples that have event 52 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[51], bit [51]

## When event 51 is implemented and filtering on event 51 is supported:

Filter on IMPLEMENTATION DEFINED event 51.

| E[51]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 51 is ignored.                           |
| 0b1     | Do not record samples that have event 51 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[50], bit [50]

## When event 50 is implemented and filtering on event 50 is supported:

Filter on IMPLEMENTATION DEFINED event 50.

| E[50]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 50 is ignored.                           |
| 0b1     | Do not record samples that have event 50 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[49], bit [49]

## When event 49 is implemented and filtering on event 49 is supported:

Filter on IMPLEMENTATION DEFINED event 49.

| E[49]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 49 is ignored.                           |
| 0b1     | Do not record samples that have event 49 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[48], bit [48]

## When event 48 is implemented and filtering on event 48 is supported:

Filter on IMPLEMENTATION DEFINED event 48.

| E[48]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 48 is ignored.                           |
| 0b1     | Do not record samples that have event 48 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Bits [47:32]

Reserved, RAZ/WI.

## E[31], bit [31]

## When FEAT\_SPEv1p4 is not implemented, event 31 is implemented, and filtering on event 31 is supported:

Filter on IMPLEMENTATION DEFINED event 31.

| E[31]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 31 is ignored.                           |
| 0b1     | Do not record samples that have event 31 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[30], bit [30]

## When FEAT\_SPEv1p4 is not implemented, event 30 is implemented, and filtering on event 30 is supported:

Filter on IMPLEMENTATION DEFINED event 30.

| E[30]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 30 is ignored.                           |
| 0b1     | Do not record samples that have event 30 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[29], bit [29]

## When FEAT\_SPEv1p4 is not implemented, event 29 is implemented, and filtering on event 29 is supported:

Filter on IMPLEMENTATION DEFINED event 29.

| E[29]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 29 is ignored.                           |
| 0b1     | Do not record samples that have event 29 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[28], bit [28]

When FEAT\_SPEv1p4 is not implemented, event 28 is implemented, and filtering on event 28 is supported:

Filter on IMPLEMENTATION DEFINED event 28.

| E[28]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 28 is ignored.                           |
| 0b1     | Do not record samples that have event 28 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[27], bit [27]

## When FEAT\_SPEv1p4 is not implemented, event 27 is implemented, and filtering on event 27 is supported:

Filter on IMPLEMENTATION DEFINED event 27.

| E[27]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 27 is ignored.                           |
| 0b1     | Do not record samples that have event 27 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[26], bit [26]

## When FEAT\_SPEv1p4 is not implemented, event 26 is implemented, and filtering on event 26 is supported:

Filter on IMPLEMENTATION DEFINED event 26.

| E[26]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 26 is ignored.                           |
| 0b1     | Do not record samples that have event 26 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[25], bit [25]

## When (FEAT\_SPE\_SME is implemented or FEAT\_SPEv1p5 is implemented) and event 25 is implemented:

Filter on Not SMCU or other shared resource operation event.

| E[25]   | Meaning                                                                                |
|---------|----------------------------------------------------------------------------------------|
| 0b0     | SMCUor other shared resource operation event is ignored.                               |
| 0b1     | Do not record samples that have theSMCU or other shared resource operation event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPEv1p4 is not implemented, event 25 is implemented, and filtering on event 25 is supported:

Filter on IMPLEMENTATION DEFINED event 25.

| E[25]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 25 is ignored.                           |
| 0b1     | Do not record samples that have event 25 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[24], bit [24]

When FEAT\_SPE\_SME is implemented:

Filter on Non-streaming SVE mode event.

| E[24]   | Meaning                                                            |
|---------|--------------------------------------------------------------------|
| 0b0     | Streaming SVE mode event is ignored.                               |
| 0b1     | Do not record samples that have the Streaming SVE mode event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPEv1p4 is not implemented, event 24 is implemented, and filtering on event 24 is supported:

Filter on IMPLEMENTATION DEFINED event 24.

| E[24]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 24 is ignored.                           |
| 0b1     | Do not record samples that have event 24 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[23], bit [23]

## When FEAT\_SPEv1p4 is implemented and event 23 is implemented:

Filter on Data not snooped event.

| E[23]   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0     | Data snooped event is ignored.                               |
| 0b1     | Do not record samples that have the Data snooped event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[22], bit [22]

## When FEAT\_SPEv1p4 is implemented and event 22 is implemented:

Filter on Not recently fetched event.

| E[22]   | Meaning                                                          |
|---------|------------------------------------------------------------------|
| 0b0     | Recently fetched event is ignored.                               |
| 0b1     | Do not record samples that have the Recently fetched event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[21], bit [21]

## When FEAT\_SPEv1p4 is implemented and event 21 is implemented:

Filter on Cache data not modified event.

| E[21]   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b0     | Cache data modified event is ignored.                               |
| 0b1     | Do not record samples that have the Cache data modified event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[20], bit [20]

## When FEAT\_SPEv1p4 is implemented and event 20 is implemented:

Filter on Level 2 data cache hit event.

| E[20]   | Meaning                                                                 |
|---------|-------------------------------------------------------------------------|
| 0b0     | Level 2 data cache miss event is ignored.                               |
| 0b1     | Do not record samples that have the Level 2 data cache miss event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[19], bit [19]

## When FEAT\_SPEv1p4 is implemented and event 19 is implemented:

Filter on No level 2 data cache access event.

| E[19]   | Meaning                                                                   |
|---------|---------------------------------------------------------------------------|
| 0b0     | Level 2 data cache access event is ignored.                               |
| 0b1     | Do not record samples that have the Level 2 data cache access event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[18], bit [18]

## When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented):

Filter on Not empty predicate event.

| E[18]   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | Empty predicate event is ignored.                               |
| 0b1     | Do not record samples that have the Empty predicate event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[17], bit [17]

## When FEAT\_SPEv1p1 is implemented and (FEAT\_SVE is implemented or FEAT\_SME is implemented):

Filter on Not partial predicate event.

| E[17]   | Meaning                                                                    |
|---------|----------------------------------------------------------------------------|
| 0b0     | Partial or empty predicate event is ignored.                               |
| 0b1     | Do not record samples that have the Partial or empty predicate event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Bit [16]

Reserved, RAZ/WI.

E[15], bit [15]

## When event 15 is implemented and filtering on event 15 is supported:

Filter on IMPLEMENTATION DEFINED event 15.

| E[15]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 15 is ignored.                           |
| 0b1     | Do not record samples that have event 15 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[14], bit [14]

## When event 14 is implemented and filtering on event 14 is supported:

Filter on IMPLEMENTATION DEFINED event 14.

| E[14]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 14 is ignored.                           |
| 0b1     | Do not record samples that have event 14 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[13], bit [13]

## When event 13 is implemented and filtering on event 13 is supported:

Filter on IMPLEMENTATION DEFINED event 13.

| E[13]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 13 is ignored.                           |
| 0b1     | Do not record samples that have event 13 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[12], bit [12]

## When event 12 is implemented and filtering on event 12 is supported:

Filter on IMPLEMENTATION DEFINED event 12.

| E[12]   | Meaning                                        |
|---------|------------------------------------------------|
| 0b0     | Event 12 is ignored.                           |
| 0b1     | Do not record samples that have event 12 == 1. |

An IMPLEMENTATION DEFINED event might be recorded as a multi-bit field. In this case, the corresponding bits of PMSNEVFR\_EL1 define an IMPLEMENTATION DEFINED filter for the event.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[11], bit [11]

## When FEAT\_SPEv1p1 is implemented:

Filter on Aligned event.

| E[11]   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0     | Misalignment event is ignored.                               |
| 0b1     | Do not record samples that have the Misalignment event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[10], bit [10]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 10 is optionally supported) and event 10 is implemented:

Filter on No remote access event.

| E[10]   | Meaning                                                       |
|---------|---------------------------------------------------------------|
| 0b0     | Remote access event is ignored.                               |
| 0b1     | Do not record samples that have the Remote access event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

E[9], bit [9]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 9 is optionally supported) and event 9 is implemented:

Filter on Last Level cache hit event.

| E[9]   | Meaning                                                               |
|--------|-----------------------------------------------------------------------|
| 0b0    | Last Level cache miss event is ignored.                               |
| 0b1    | Do not record samples that have the Last Level cache miss event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[8], bit [8]

## When (FEAT\_SPEv1p4 is implemented or filtering on event 8 is optionally supported) and event 8 is implemented:

Filter on No Last Level cache access event.

| E[8]   | Meaning                                                                 |
|--------|-------------------------------------------------------------------------|
| 0b0    | Last Level cache access event is ignored.                               |
| 0b1    | Do not record samples that have the Last Level cache access event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[7], bit [7]

Filter on Correctly predicted event.

| E[7]   | Meaning                                                      |
|--------|--------------------------------------------------------------|
| 0b0    | Mispredicted event is ignored.                               |
| 0b1    | Do not record samples that have the Mispredicted event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

E[6], bit [6]

## When FEAT\_SPE\_FnE is implemented:

Filter on Taken event.

| E[6]   | Meaning                                                   |
|--------|-----------------------------------------------------------|
| 0b0    | Not taken event is ignored.                               |
| 0b1    | Do not record samples that have the Not taken event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[5], bit [5]

Filter on TLB hit event.

| E[5]   | Meaning                                                  |
|--------|----------------------------------------------------------|
| 0b0    | TLB walk event is ignored.                               |
| 0b1    | Do not record samples that have the TLB walk event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E[4], bit [4]

## When FEAT\_SPEv1p4 is implemented or filtering on event 4 is optionally supported:

Filter on No TLB access event.

| E[4]   | Meaning                                                    |
|--------|------------------------------------------------------------|
| 0b0    | TLB access event is ignored.                               |
| 0b1    | Do not record samples that have the TLB access event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[3], bit [3]

Filter on Level 1 data cache hit event.

| E[3]   | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0    | Level 1 data cache refill or miss event is ignored.                               |
| 0b1    | Do not record samples that have the Level 1 data cache refill or miss event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E[2], bit [2]

## When FEAT\_SPEv1p4 is implemented or filtering on event 2 is optionally supported:

Filter on No Level 1 data cache access event.

| E[2]   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0    | Level 1 data cache access event is ignored.                               |
| 0b1    | Do not record samples that have the Level 1 data cache access event == 1. |

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## E[1], bit [1]

## When the PE supports sampling of speculative instructions:

Filter on Speculative event.

| E[1]   | Meaning                                   |
|--------|-------------------------------------------|
| 0b0    | Architecturally retired event is ignored. |

0b1

Do not record samples that have the Architecturally retired event == 1.

This field is ignored by the PE when PMSFCR\_EL1.FnE is 0.

If the PE does not support the sampling of speculative instructions, or always discards the sample record for speculative instructions, this bit reads as an UNKNOWN value and the PE ignores its value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## Bit [0]

Reserved, RAZ/WI.

## Accessing PMSNEVFR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSNEVFR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_SPE_FnE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSN == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nPMSNEVFR_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x850]; else X[t, 64] = PMSNEVFR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSN == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSNEVFR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSNEVFR_EL1;
```

MSR PMSNEVFR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_SPE_FnE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSN == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nPMSNEVFR_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x850] = X[t, 64]; else PMSNEVFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSPBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSN == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSPBTrap() then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSNEVFR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSNEVFR_EL1 = X[t, 64];
```