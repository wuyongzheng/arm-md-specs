## D24.2.113 ID\_MMFR5\_EL1, AArch32 Memory Model Feature Register 5

The ID\_MMFR5\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch64 System register ID\_MMFR5\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_MMFR5[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_MMFR5\_EL1 are UNDEFINED.

## Attributes

ID\_MMFR5\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:8]

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

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_MMFR5\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_MMFR5\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0011 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_MMFR5_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_MMFR5_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR5_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR5_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_MMFR5_EL1;
```