## G8.2.98 ID\_MMFR5, Memory Model Feature Register 5

The ID\_MMFR5 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_MMFR5 bits [31:0] are architecturally mapped to AArch64 System register ID\_MMFR5\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_MMFR5 are UNDEFINED.

## Attributes

ID\_MMFR5 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 3   |
|------|--------|-----|
|      | nTLBPA | ETS |

## Bits [31:8]

Reserved, RES0.

## nTLBPA, bits [7:4]

Indicates support for intermediate caching of translation table walks.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| nTLBPA   | Meaning                                                                                                        |
|----------|----------------------------------------------------------------------------------------------------------------|
| 0b0000   | The intermediate caching of translation table walks might include non-coherent physical translation caches.    |
| 0b0001   | The intermediate caching of translation table walks does not include non-coherent physical translation caches. |

Non-coherent physical translation caches are non-coherent caches of previous valid translation table entries since the last completed relevant TLBI applicable to the PE, where either:

- The caching is indexed by the physical address of the location holding the translation table entry.
- The caching is used for stage 1 translations and is indexed by the intermediate physical address of the location holding the translation table entry.

All other values are reserved.

FEAT\_nTLBPA implements the functionality identified by the value 0b0001 .

From Armv8.0, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## ETS, bits [3:0]

Indicates support for Enhanced Translation Synchronization.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ETS    | Meaning                                                |
|--------|--------------------------------------------------------|
| 0b0000 | Enhanced Translation Synchronization is not supported. |
| 0b0001 | Enhanced Translation Synchronization is not supported. |
| 0b0010 | FEAT_ETS2 is implemented.                              |
| 0b0011 | FEAT_ETS3 is implemented.                              |

All other values are reserved.

FEAT\_ETS2 implements the functionality identified by the value 0b0010 .

FEAT\_ETS3 implements the functionality identified by the value 0b0011 .

From Armv8.8, the values 0b0000 and 0b0001 are not permitted.

From Armv9.5, the value 0b0010 is not permitted.

Access to this field is RO.

## Accessing ID\_MMFR5

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0011 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_MMFR5) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_MMFR5 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_MMFR5) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_MMFR5 trapped by HCR.TID3") && HCR.TID3 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = ID_MMFR5; elsif PSTATE.EL == EL2 then R[t] = ID_MMFR5;
```

```
elsif PSTATE.EL == EL3 then R[t] = ID_MMFR5;
```