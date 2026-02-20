## G8.2.116 MVFR0, Media and VFP Feature Register 0

The MVFR0 characteristics are:

## Purpose

Describes the features provided by the AArch32 Advanced SIMD and floating-point implementation.

Must be interpreted with MVFR1 and MVFR2.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Implemented only if the implementation includes Advanced SIMD and floating-point instructions.

AArch32 System register MVFR0 bits [31:0] are architecturally mapped to AArch64 System register MVFR0\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to MVFR0 are UNDEFINED.

## Attributes

MVFR0is a 32-bit register.

## Field descriptions

| 31      | 28 27   | 24 23   | 20 19    | 16 15   | 12 11   | 8 7   | 4 3   | 0       |
|---------|---------|---------|----------|---------|---------|-------|-------|---------|
| FPRound | FPShVec | FPSqrt  | FPDivide | FPTrap  | FPDP    | FPSP  |       | SIMDReg |

## FPRound, bits [31:28]

Floating-Point Rounding modes. Indicates whether the floating-point implementation provides support for rounding modes.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPRound   | Meaning                                                                                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Not implemented, or only Round to Nearest mode supported, except that Round towards Zero mode is supported for VCVTinstructions that always use that rounding mode regardless of the FPSCR setting. |
| 0b0001    | All rounding modes supported.                                                                                                                                                                       |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

Access to this field is RO.

## FPShVec, bits [27:24]

Short Vectors. Indicates whether the floating-point implementation provides support for the use of short vectors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

The VSQRT.F32 instruction also requires the single-precision floating-point attribute, bits [7:4], and the VSQRT.F64 instruction also requires the double-precision floating-point attribute, bits [11:8].

Access to this field is RO.

## FPDivide, bits [19:16]

Indicates whether the floating-point implementation provides support for VFP divide operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPDivide   | Meaning                    |
|------------|----------------------------|
| 0b0000     | Not supported in hardware. |
| 0b0001     | Supported.                 |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

The VDIV.F32 instruction also requires the single-precision floating-point attribute, bits [7:4], and the VDIV .F64 instruction also requires the double-precision floating-point attribute, bits [11:8].

Access to this field is RO.

## FPTrap, bits [15:12]

| FPShVec   | Meaning                           |
|-----------|-----------------------------------|
| 0b0000    | Short vectors not supported.      |
| 0b0001    | Short vector operation supported. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## FPSqrt, bits [23:20]

Square Root. Indicates whether the floating-point implementation provides support for the ARMv6 VFP square root operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPSqrt   | Meaning                    |
|----------|----------------------------|
| 0b0000   | Not supported in hardware. |
| 0b0001   | Supported.                 |

Floating-Point Exception Trapping. Indicates whether the floating-point implementation provides support for exception trapping.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPTrap   | Meaning        |
|----------|----------------|
| 0b0000   | Not supported. |
| 0b0001   | Supported.     |

All other values are reserved.

Avalue of 0b0001 indicates that, when the corresponding trap is enabled, a floating-point exception generates an exception.

Access to this field is RO.

## FPDP, bits [11:8]

Floating-Point Double-Precision. Indicates whether the floating-point implementation provides support for double-precision operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPDP   | Meaning                                                                                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not supported in hardware.                                                                                                                                                                 |
| 0b0001 | Supported, VFPv2.                                                                                                                                                                          |
| 0b0010 | Supported, VFPv3, VFPv4, or Armv8. VFPv3 and Armv8 add an instruction to load a double-precision floating-point constant, and conversions between double-precision and fixed-point values. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0010 .

Avalue of 0b0001 or 0b0010 indicates support for all VFP double-precision instructions in the supported version of VFP, except that, in addition to this field being nonzero:

- VSQRT.F64 is only available if the Square root field is 0b0001 .
- VDIV.F64 is only available if the Divide field is 0b0001 .
- Conversion between double-precision and single-precision is only available if the single-precision field is nonzero.

Access to this field is RO.

## FPSP, bits [7:4]

Floating-Point Single-Precision. Indicates whether the floating-point implementation provides support for single-precision operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPSP   | Meaning                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not supported in hardware.                                                                                                                                                |
| 0b0001 | Supported, VFPv2.                                                                                                                                                         |
| 0b0010 | Supported, VFPv3 or VFPv4. VFPv3 adds an instruction to load a single-precision floating-point constant, and conversions between single-precision and fixed-point values. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0010 .

Avalue of 0b0001 or 0b0010 indicates support for all VFP single-precision instructions in the supported version of VFP, except that, in addition to this field being nonzero:

- VSQRT.F32 is only available if the Square root field is 0b0001 .
- VDIV.F32 is only available if the Divide field is 0b0001 .
- Conversion between double-precision and single-precision is only available if the double-precision field is nonzero.

Access to this field is RO.

## SIMDReg, bits [3:0]

Advanced SIMD registers. Indicates whether the Advanced SIMD and floating-point implementation provides support for the Advanced SIMD and floating-point register bank.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDReg   | Meaning                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------|
| 0b0000    | The implementation has no Advanced SIMD and floating-point support.                              |
| 0b0001    | The implementation includes floating-point support with 16 x 64-bit registers.                   |
| 0b0010    | The implementation includes Advanced SIMD and floating-point support with 32 x 64-bit registers. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0010 .

Access to this field is RO.

## Accessing MVFR0

Accesses to this register use the following encodings in the System register encoding space:

VMRS{&lt;c&gt;}{&lt;q&gt;} &lt;Rt&gt;, &lt;spec\_reg&gt;

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;

| reg    |
|--------|
| 0b0111 |

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || CPACR.cp10 == '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) ↪ → && CPTR_EL2.TFP == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.FPEN ↪ → IN {'x0'} then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x08); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' ↪ → && NSACR.cp10 == '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x00); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR0; elsif PSTATE.EL == EL3 then if CPACR.cp10 == '00' then UNDEFINED; else R[t] = MVFR0;
```