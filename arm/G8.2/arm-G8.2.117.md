## G8.2.117 MVFR1, Media and VFP Feature Register 1

The MVFR1 characteristics are:

## Purpose

Describes the features provided by the AArch32 Advanced SIMD and floating-point implementation.

Must be interpreted with MVFR0 and MVFR2.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Implemented only if the implementation includes Advanced SIMD and floating-point instructions.

AArch32 System register MVFR1 bits [31:0] are architecturally mapped to AArch64 System register MVFR1\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to MVFR1 are UNDEFINED.

## Attributes

MVFR1is a 32-bit register.

## Field descriptions

| 31       | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7    | 4 3   | 0     |
|----------|---------|---------|---------|---------|---------|--------|-------|-------|
| SIMDFMAC | FPHP    | SIMDHP  | SIMDSP  | SIMDInt | SIMDLS  | FPDNaN |       | FPFtZ |

## SIMDFMAC, bits [31:28]

Advanced SIMD Fused Multiply-Accumulate. Indicates whether the Advanced SIMD implementation provides fused multiply accumulate instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDFMAC   | Meaning          |
|------------|------------------|
| 0b0000     | Not implemented. |
| 0b0001     | Implemented.     |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

The Advanced SIMD and floating-point implementations must provide the same level of support for these instructions.

Access to this field is RO.

## FPHP, bits [27:24]

Floating-Point Half-Precision. Indicates the level of half-precision floating-point support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPHP   | Meaning                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not supported.                                                                                                                  |
| 0b0001 | Floating-point half-precision conversion instructions are supported for conversion between single-precision and half-precision. |
| 0b0010 | As for 0b0001 , and adds instructions for conversion between double-precision and half-precision.                               |
| 0b0011 | As for 0b0010 , and adds support for half-precision floating-point arithmetic.                                                  |

All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 in an implementation without floating-point support.
- 0b0010 in an implementation with floating-point support that does not include the FEAT\_FP16 extension.
- 0b0011 in an implementation with floating-point support that includes the FEAT\_FP16 extension.

The level of support indicated by this field must be equivalent to the level of support indicated by the SIMDHP field, meaning the permitted values are:

| Half-Precision instructions supported   | FPHP   | SIMDHP   |
|-----------------------------------------|--------|----------|
| No support                              | 0b0000 | 0b0000   |
| Conversions only                        | 0b0010 | 0b0001   |
| Conversions and arithmetic              | 0b0011 | 0b0010   |

Access to this field is RO.

## SIMDHP, bits [23:20]

Advanced SIMD Half-Precision. Indicates the level of half-precision floating-point support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDHP   | Meaning                                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0000   | Not supported.                                                                                                        |
| 0b0001   | SIMD half-precision conversion instructions are supported for conversion between single-precision and half-precision. |
| 0b0010   | As for 0b0001 , and adds support for half-precision floating-point arithmetic.                                        |

All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 in an implementation without SIMD floating-point support.
- 0b0001 in an implementation with SIMD floating-point support that does not include the FEAT\_FP16 extension.
- 0b0010 in an implementation with SIMD floating-point support that includes the FEAT\_FP16 extension.

The level of support indicated by this field must be equivalent to the level of support indicated by the FPHP field, meaning the permitted values are:

| Half-Precision instructions supported   | FPHP   | SIMDHP   |
|-----------------------------------------|--------|----------|
| No support                              | 0b0000 | 0b0000   |
| Conversions only                        | 0b0010 | 0b0001   |
| Conversions and arithmetic              | 0b0011 | 0b0010   |

Access to this field is RO.

## SIMDSP, bits [19:16]

Advanced SIMD Single-Precision. Indicates whether the Advanced SIMD and floating-point implementation provides single-precision floating-point instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDSP   | Meaning                                                                    |
|----------|----------------------------------------------------------------------------|
| 0b0000   | Not implemented.                                                           |
| 0b0001   | Implemented. This value is permitted only if the SIMDInt field is 0b0001 . |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## SIMDInt, bits [15:12]

Advanced SIMD Integer. Indicates whether the Advanced SIMD and floating-point implementation provides integer instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDInt   | Meaning          |
|-----------|------------------|
| 0b0000    | Not implemented. |
| 0b0001    | Implemented.     |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## SIMDLS, bits [11:8]

Advanced SIMD Load/Store. Indicates whether the Advanced SIMD and floating-point implementation provides load/store instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## FPDNaN, bits [7:4]

Default NaN mode. Indicates whether the floating-point implementation provides support only for the Default NaN mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPDNaN   | Meaning                                                          |
|----------|------------------------------------------------------------------|
| 0b0000   | Not implemented, or hardware supports only the Default NaN mode. |
| 0b0001   | Hardware supports propagation of NaN values.                     |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## FPFtZ, bits [3:0]

Flush to Zero mode. Indicates whether the floating-point implementation provides support only for the Flush-to-Zero mode of operation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPFtZ   | Meaning                                                                         |
|---------|---------------------------------------------------------------------------------|
| 0b0000  | Not implemented, or hardware supports only the Flush-to-Zero mode of operation. |
| 0b0001  | Hardware supports full denormalized number arithmetic.                          |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## Accessing MVFR1

Accesses to this register use the following encodings in the System register encoding space:

| SIMDLS   | Meaning          |
|----------|------------------|
| 0b0000   | Not implemented. |
| 0b0001   | Implemented.     |

```
VMRS{<c>}{<q>} <Rt>, <spec_reg>
```

reg

0b0110

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || CPACR.cp10 == '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) ↪ → && CPTR_EL2.TFP == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.FPEN ↪ → IN {'x0'} then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x08); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' ↪ → && NSACR.cp10 == '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x00); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR1; elsif PSTATE.EL == EL3 then if CPACR.cp10 == '00' then UNDEFINED; else R[t] = MVFR1;
```