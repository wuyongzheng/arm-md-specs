## D24.2.90 ID\_AA64MMFR2\_EL1, AArch64 Memory Model Feature Register 2

The ID\_AA64MMFR2\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64MMFR2\_EL1 are UNDEFINED.

## Attributes

ID\_AA64MMFR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   | 32   |
|------|---------|---------|---------|---------|---------|---------|---------|------|
| E0PD | EVT     | BBM     | TTL     | RES0    | FWB     | IDS     | AT      |      |
| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4 3     | 0    |
| ST   | NV      | CCIDX   | VARange | IESB    | LSM     | UAO     | CnP     |      |

## E0PD, bits [63:60]

Indicates support for the E0PD mechanism.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| E0PD   | Meaning                             |
|--------|-------------------------------------|
| 0b0000 | E0PDx mechanism is not implemented. |
| 0b0001 | E0PDx mechanism is implemented.     |

All other values are reserved.

FEAT\_E0PD implements the functionality identified by the value 0b0001 .

In Armv8.4, the permitted values are 0b0000 and 0b0001 .

From Armv8.5, the only permitted value is 0b0001 .

If FEAT\_E0PD is implemented, FEAT\_CSV3 must be implemented.

Access to this field is RO.

## EVT, bits [59:56]

Enhanced Virtualization Traps. If EL2 is implemented, indicates support for the HCR\_EL2.{TTLBOS, TTLBIS, TOCU, TICAB, TID4} traps.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EVT    | Meaning                                                                                            |
|--------|----------------------------------------------------------------------------------------------------|
| 0b0000 | HCR_EL2.{TTLBOS, TTLBIS, TOCU, TICAB, TID4} traps are not supported.                               |
| 0b0001 | HCR_EL2.{TOCU, TICAB, TID4} traps are supported. HCR_EL2.{TTLBOS, TTLBIS} traps are not supported. |
| 0b0010 | HCR_EL2.{TTLBOS, TTLBIS, TOCU, TICAB, TID4} traps are supported.                                   |

All other values are reserved.

FEAT\_EVT implements the functionality identified by the values 0b0001 and 0b0010 .

If EL2 is not implemented, the only permitted value is 0b0000 .

From Armv8.5, if EL2 is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## BBM, bits [55:52]

Allows identification of the requirements of the hardware to have break-before-make sequences when changing block or table size for a translation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BBM    | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0000 | Break-before-make sequence must be used.              |
| 0b0001 | Level 1 support for changing block size is supported. |
| 0b0010 | Level 2 support for changing block size is supported. |

All other values are reserved.

FEAT\_BBML1 implements the functionality identified by the value 0b0001 .

FEAT\_BBML2 implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## TTL, bits [51:48]

Indicates support for TTL field in address operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TTL    | Meaning                                                           |
|--------|-------------------------------------------------------------------|
| 0b0000 | TLB maintenance instructions by address have bits[47:44] as RES0. |

| TTL    | Meaning                                                                         |
|--------|---------------------------------------------------------------------------------|
| 0b0001 | TLB maintenance instructions by address have bits[47:44] holding the TTL field. |

All other values are reserved.

FEAT\_TTL implements the functionality identified by the value 0b0001 .

This field affects TLBI IPAS2E1, TLBI IPAS2E1IS, TLBI IPAS2E1OS, TLBI IPAS2LE1, TLBI IPAS2LE1IS, TLBI IPAS2LE1OS, TLBI VAAE1, TLBI VAAE1IS, TLBI VAAE1OS, TLBI VAALE1, TLBI VAALE1IS, TLBI VAALE1OS, TLBI VAE1, TLBI VAE1IS, TLBI VAE1OS, TLBI VAE2, TLBI VAE2IS, TLBI VAE2OS, TLBI VAE3, TLBI VAE3IS, TLBI VAE3OS,TLBI VALE1, TLBI VALE1IS, TLBI VALE1OS, TLBI VALE2, TLBI VALE2IS, TLBI VALE2OS, TLBI VALE3, TLBI VALE3IS, TLBI VALE3OS.

From Armv8.4, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [47:44]

Reserved, RES0.

## FWB, bits [43:40]

Indicates support for HCR\_EL2.FWB.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FWB    | Meaning                           |
|--------|-----------------------------------|
| 0b0000 | HCR_EL2.FWB bit is not supported. |
| 0b0001 | HCR_EL2.FWB is supported.         |

All other values reserved.

FEAT\_S2FWB implements the functionality identified by the value 0b0001 .

From Armv8.4, the value 0b0000 is not permitted.

Access to this field is RO.

## IDS, bits [39:36]

Indicates the EC syndrome value in ESR\_ELx.EC that is reported if an exception is generated by a read access to the feature ID space.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IDS    | Meaning                                                                                                                                                                                |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | An exception which is generated by a read access to the feature ID space, other than a trap caused by HCR_EL2.TIDx, SCTLR_EL1.UCT, or SCTLR_EL2.UCT is reported by ESR_ELx.EC == 0x0 . |
| 0b0001 | All exceptions generated by an AArch64 read access to the feature ID space are reported by ESR_ELx.EC == 0x18 .                                                                        |
| 0b0010 | As 0b0001 and introduces support for trapping ID register accesses to EL3.                                                                                                             |

All other values are reserved.

The Feature ID space is defined as the System register space in AArch64 with op0==3, op1=={0, 1, 3}, CRn==0, CRm=={0-7}, op2=={0-7}.

FEAT\_IDST implements the functionality identified by the value 0b0001 .

FEAT\_IDTE3 implements the functionality identified by 0b0010 .

From Armv8.4, the value 0b0000 is not permitted.

From Armv9.6, if EL3 is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## AT, bits [35:32]

Identifies support for unaligned single-copy atomicity and atomic functions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AT     | Meaning                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Unaligned single-copy atomicity and atomic functions are not supported.                                              |
| 0b0001 | Unaligned single-copy atomicity and atomic functions with a 16-byte address range aligned to 16-bytes are supported. |

All other values are reserved.

FEAT\_LSE2 implements the functionality identified by the value 0b0001 .

From Armv8.4, the value 0b0000 is not permitted.

Access to this field is RO.

## ST, bits [31:28]

Identifies support for small translation tables.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ST     | Meaning                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The maximum value of the TCR_ELx.{T0SZ,T1SZ} and VTCR_EL2.T0SZ fields is 39.                                                     |
| 0b0001 | The maximum value of the TCR_ELx.{T0SZ,T1SZ} and VTCR_EL2.T0SZ fields is 48 for 4KB and 16KB granules, and 47 for 64KB granules. |

All other values are reserved.

FEAT\_TTST implements the functionality identified by the value 0b0001 .

When FEAT\_SEL2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## NV, bits [27:24]

Nested Virtualization. If EL2 is implemented, indicates support for the use of nested virtualization.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NV     | Meaning                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | If ID_AA64MMFR4_EL1.NV_frac != 0b0000 , support for nested virtualization is described in ID_AA64MMFR4_EL1.NV_frac. Otherwise, nested virtualization is not supported. |
| 0b0001 | The HCR_EL2.{AT, NV1, NV} bits are implemented.                                                                                                                        |
| 0b0010 | The VNCR_EL2 register and the HCR_EL2.{NV2, AT, NV1, NV} bits are implemented.                                                                                         |

All other values are reserved.

If EL2 is not implemented, the only permitted value is 0b0000 .

FEAT\_NV implements the functionality identified by the value 0b0001 .

FEAT\_NV2 implements the functionality identified by the value 0b0010 .

In Armv8.3, if EL2 is implemented, the permitted values are 0b0000 and 0b0001 .

From Armv8.4, if EL2 is implemented, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

Access to this field is RO.

## CCIDX, bits [23:20]

Support for the use of revised CCSIDR\_EL1 register format.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCIDX   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0000  | 32-bit format implemented for all levels of the CCSIDR_EL1. |
| 0b0001  | 64-bit format implemented for all levels of the CCSIDR_EL1. |

All other values are reserved.

FEAT\_CCIDX implements the functionality identified by the value 0b0001 .

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## VARange, bits [19:16]

Indicates support for a larger virtual address.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VARange   | Meaning                                                                                                                                      | Applies when             |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| 0b0000    | VMSAv8-64 supports 48-bit VAs.                                                                                                               |                          |
| 0b0001    | VMSAv8-64 supports 52-bit VAs when using the 64KB translation granule. The size for other translation granules is not defined by this field. |                          |
| 0b0010    | VMSAv9-128 supports 56-bit VAs.                                                                                                              | FEAT_D128 is implemented |

All other values are reserved.

FEAT\_LVA implements the functionality identified by the value 0b0001 .

FEAT\_LVA3 implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## IESB, bits [15:12]

Indicates support for the IESB bit in the SCTLR\_ELx registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IESB   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0000 | IESB bit in the SCTLR_ELx registers is not supported. |
| 0b0001 | IESB bit in the SCTLR_ELx registers is supported.     |

All other values are reserved.

FEAT\_IESB implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## LSM, bits [11:8]

Indicates support for LSMAOE and nTLSMD bits in SCTLR\_EL1 and SCTLR\_EL2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LSM    | Meaning                              |
|--------|--------------------------------------|
| 0b0000 | LSMAOEand nTLSMD bits not supported. |
| 0b0001 | LSMAOEand nTLSMD bits supported.     |

All other values are reserved.

FEAT\_LSMAOC implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## UAO, bits [7:4]

User Access Override.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| UAO    | Meaning           |
|--------|-------------------|
| 0b0000 | UAOnot supported. |
| 0b0001 | UAOsupported.     |

All other values are reserved.

FEAT\_UAO implements the functionality identified by the value 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

Access to this field is RO.

## CnP, bits [3:0]

Indicates support for Common not Private translations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CnP    | Meaning                                        |
|--------|------------------------------------------------|
| 0b0000 | Common not Private translations not supported. |
| 0b0001 | Common not Private translations supported.     |

All other values are reserved.

FEAT\_TTCNP implements the functionality identified by the value 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64MMFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64MMFR2_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0111 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64MMFR2_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64MMFR2_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = ID_AA64MMFR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64MMFR2_EL1;
```