## D24.2.140 MVFR1\_EL1, AArch32 Media and VFP Feature Register 1

The MVFR1\_EL1 characteristics are:

## Purpose

Describes the features provided by the AArch32 Advanced SIMD and floating-point implementation.

Must be interpreted with MVFR0\_EL1 and MVFR2\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

In an implementation where at least one Exception level supports execution in AArch32 state, but there is no support for Advanced SIMD and floating-point operation, this register is RAZ.

AArch64 System register MVFR1\_EL1 bits [31:0] are architecturally mapped to AArch32 System register MVFR1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MVFR1\_EL1 are UNDEFINED.

## Attributes

MVFR1\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

| 63       |       |        |         |       | 32   |
|----------|-------|--------|---------|-------|------|
|          |       |        | RES0    |       |      |
| 31       | 28 27 | 24 23  | 16 15   | 3     | 0    |
| SIMDFMAC | FPHP  | SIMDHP | SIMDInt | FPFtZ |      |

## Bits [63:32]

Reserved, RES0.

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

0b0010

As for 0b0001 , and adds support for half-precision floating-point arithmetic.

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

| SIMDLS   | Meaning          |
|----------|------------------|
| 0b0000   | Not implemented. |
| 0b0001   | Implemented.     |

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

| SIMDInt   | Meaning   |
|-----------|-----------|

| FPFtZ   | Meaning                                                                         |
|---------|---------------------------------------------------------------------------------|
| 0b0000  | Not implemented, or hardware supports only the Flush-to-Zero mode of operation. |
| 0b0001  | Hardware supports full denormalized number arithmetic.                          |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing MVFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MVFR1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = MVFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MVFR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MVFR1_EL1;
```