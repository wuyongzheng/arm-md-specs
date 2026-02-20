## G8.2.97 ID\_MMFR4, Memory Model Feature Register 4

The ID\_MMFR4 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_MMFR4 bits [31:0] are architecturally mapped to AArch64 System register ID\_MMFR4\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_MMFR4 are UNDEFINED.

## Attributes

ID\_MMFR4 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7   | 4 3     |
|------|---------|---------|---------|---------|---------|-------|---------|
| EVT  | CCIDX   | LSM     | HPDS    | CnP     | XNX     | AC2   | SpecSEI |

## EVT, bits [31:28]

Enhanced Virtualization Traps. If EL2 is implemented, indicates support for the HCR2.{TTLBIS, TOCU, TICAB, TID4} traps.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EVT    | Meaning                                                                          |
|--------|----------------------------------------------------------------------------------|
| 0b0000 | HCR2.{TTLBIS, TOCU, TICAB, TID4} traps are not supported.                        |
| 0b0001 | HCR2.{TOCU, TICAB, TID4} traps are supported. HCR2.TTLBIS trap is not supported. |
| 0b0010 | HCR2.{TTLBIS, TOCU, TICAB, TID4} traps are supported.                            |

All other values are reserved.

FEAT\_EVT implements the functionality identified by the values 0b0001 and 0b0010 .

If EL2 is not implemented or does not support AArch32, the only permitted value is 0b0000 .

From Armv8.5, if EL2 is implemented and supports AArch32, the value 0b0001 is not permitted.

Access to this field is RO.

## CCIDX, bits [27:24]

Support for use of the revised CCSIDR format and the presence of the CCSIDR2 is indicated.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCIDX   | Meaning                                                                                              |
|---------|------------------------------------------------------------------------------------------------------|
| 0b0000  | 32-bit format implemented for all levels of the CCSIDR, and the CCSIDR2 register is not implemented. |
| 0b0001  | 64-bit format implemented for all levels of the CCSIDR, and the CCSIDR2 register is implemented.     |

All other values are reserved.

FEAT\_CCIDX implements the functionality identified by 0b0001 .

From Armv8.3, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## LSM, bits [23:20]

Indicates support for LSMAOE and nTLSMD bits in HSCTLR and SCTLR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LSM    | Meaning                              |
|--------|--------------------------------------|
| 0b0000 | LSMAOEand nTLSMD bits not supported. |
| 0b0001 | LSMAOEand nTLSMD bits supported.     |

All other values are reserved.

FEAT\_LSMAOC implements the functionality identified by the value 0b0001 .

From Armv8.2, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## HPDS, bits [19:16]

Hierarchical permission disables bits in translation tables.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HPDS   | Meaning                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Disabling of hierarchical controls not supported.                                                                                                                           |
| 0b0001 | Supports disabling of hierarchical controls using the TTBCR2.HPD0, TTBCR2.HPD1, and HTCR.HPD bits.                                                                          |
| 0b0010 | As for value 0b0001 , and adds possible hardware allocation of bits[62:59] of the Translation table descriptors from the final lookup level for IMPLEMENTATION DEFINED use. |

All other values are reserved.

FEAT\_AA32HPD implements the functionality identified by the value 0b0001 .

FEAT\_HPDS2 implements the functionality added by the value 0b0010 .

Note

The value 0b0000 implies that the encoding for TTBCR2 is UNDEFINED.

Access to this field is RO.

## CnP, bits [15:12]

Common not Private translations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CnP    | Meaning                                        |
|--------|------------------------------------------------|
| 0b0000 | Common not Private translations not supported. |
| 0b0001 | Common not Private translations supported.     |

All other values are reserved.

FEAT\_TTCNP implements the functionality identified by the value 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

Access to this field is RO.

## XNX, bits [11:8]

Support for execute-never control distinction by Exception level at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| XNX    | Meaning                                                                         |
|--------|---------------------------------------------------------------------------------|
| 0b0000 | Distinction between EL0 and EL1 execute-never control at stage 2 not supported. |
| 0b0001 | Distinction between EL0 and EL1 execute-never control at stage 2 supported.     |

All other values are reserved.

FEAT\_XNX implements the functionality identified by the value 0b0001 .

When FEAT\_XNX is implemented:

- If all of the following conditions are true, it is IMPLEMENTATION DEFINED whether the value of ID\_MMFR4.XNX is 0b0000 or 0b0001 :
- ID\_AA64MMFR1\_EL1.XNX ==1.
- EL2 cannot use AArch32.
- EL1 can use AArch32.
- If EL2 can use AArch32 then the value 0b0000 is not permitted.

Access to this field is RO.

## AC2, bits [7:4]

Indicates the extension of the ACTLR and HACTLR registers using ACTLR2 and HACTLR2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AC2    | Meaning                                 |
|--------|-----------------------------------------|
| 0b0000 | ACTLR2 and HACTLR2 are not implemented. |
| 0b0001 | ACTLR2 and HACTLR2 are implemented.     |

All other values are reserved.

In Armv8.0, the permitted values are 0b0000 and 0b0001 .

From Armv8.2, the only permitted value is 0b0001 .

Access to this field is RO.

## SpecSEI, bits [3:0]

## When FEAT\_RAS is implemented:

Describes whether the PE can generate SError exceptions from speculative reads of memory, including speculative instruction fetches.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SpecSEI   | Meaning                                                                                    |
|-----------|--------------------------------------------------------------------------------------------|
| 0b0000    | The PE never generates an SError exception due to an External abort on a speculative read. |
| 0b0001    | The PE might generate an SError exception due to an External abort on a speculative read.  |

All other values are reserved.

FEAT\_SpecSEI implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing ID\_MMFR4

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0010 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_MMFR4) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_MMFR4 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_MMFR4) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_MMFR4 trapped by HCR.TID3") && HCR.TID3 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = ID_MMFR4; elsif PSTATE.EL == EL2 then R[t] = ID_MMFR4; elsif PSTATE.EL == EL3 then R[t] = ID_MMFR4;
```