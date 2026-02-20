## D24.2.93 ID\_AA64PFR0\_EL1, AArch64 Processor Feature Register 0

The ID\_AA64PFR0\_EL1 characteristics are:

## Purpose

Provides additional information about implemented PE features in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

The external register EDPFR gives information from this register.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64PFR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64PFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   | 32   |
|------|---------|---------|---------|---------|---------|---------|---------|------|
| CSV3 | CSV2    | RME     | DIT     | AMU     | MPAM    | SEL2    | SVE     |      |
| 31   | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4 3     | 0    |
| RAS  | GIC     | AdvSIMD | FP      | EL3     | EL2     | EL1     | EL0     |      |

## CSV3, bits [63:60]

Speculative use of faulting data.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSV3   | Meaning                                                                                                                                                                                                                                                                                                                                            |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | This PE does not disclose whether data loaded or read from a register under speculation where the data load or register read would not be permitted architecturally, can be used by instructions newer than the load or register read in a manner that allows the value of the inaccessible data to be recovered by code architecturally executed. |
| 0b0001 | Data loaded or read from a register under speculation where the data load or register read would not be permitted architecturally, cannot be used by instructions newer than the load or register read in a manner that allows the value of the inaccessible data to be recovered by code architecturally executed.                                |

All other values are reserved.

FEAT\_CSV3 implements the functionality identified by the value 0b0001 .

If FEAT\_E0PD is implemented, FEAT\_CSV3 must be implemented.

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## CSV2, bits [59:56]

Speculative use of out of context prediction resources.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSV2   | Meaning                                                                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The implementation does not disclose whether FEAT_CSV2 is implemented.                                                                                                                        |
| 0b0001 | FEAT_CSV2 is implemented, but FEAT_CSV2_2 and FEAT_CSV2_3 are not implemented. ID_AA64PFR1_EL1.CSV2_frac determines whether either or both of FEAT_CSV2_1p1 or FEAT_CSV2_1p2 are implemented. |
| 0b0010 | FEAT_CSV2_2 is implemented, but FEAT_CSV2_3 is not implemented.                                                                                                                               |
| 0b0011 | FEAT_CSV2_3 is implemented.                                                                                                                                                                   |

All other values are reserved.

FEAT\_CSV2 implements the functionality identified by the value 0b0001 .

FEAT\_CSV2\_2 implements the functionality identified by the value 0b0010 .

FEAT\_CSV2\_3 implements the functionality identified by the feature 0b0011 .

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## RME, bits [55:52]

Realm Management Extension (RME).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RME    | Meaning                                              |
|--------|------------------------------------------------------|
| 0b0000 | Realm Management Extension not implemented.          |
| 0b0001 | RMEv1 is implemented.                                |
| 0b0010 | As 0b0001 , and adds support for the GPC2 Extension. |
| 0b0011 | As 0b0010 , and adds support for the GPC3 Extension. |

All other values are reserved.

FEAT\_RME implements the functionality identified by the value 0b0001 .

FEAT\_RME\_GPC2 implements the functionality identified by the value 0b0010 .

FEAT\_RME\_GPC3 implements the functionality identified by the value 0b0011 .

Access to this field is RO.

## DIT, bits [51:48]

Data Independent Timing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DIT    | Meaning                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------|
| 0b0000 | AArch64 does not guarantee constant execution time of any instructions.                                 |
| 0b0001 | AArch64 provides the PSTATE.DIT mechanism to guarantee constant execution time of certain instructions. |

All other values are reserved.

FEAT\_DIT implements the functionality identified by the value 0b0001 .

From Armv8.4, the value 0b0000 is not permitted.

Access to this field is RO.

## AMU,bits [47:44]

Indicates support for Activity Monitors Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AMU    | Meaning                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Activity Monitors Extension is not implemented.                                                                    |
| 0b0001 | FEAT_AMUv1 is implemented.                                                                                         |
| 0b0010 | FEAT_AMUv1p1 is implemented. As 0b0001 and adds support for virtualization of the activity monitor event counters. |

All other values are reserved.

FEAT\_AMUv1 implements the functionality identified by the value 0b0001 .

FEAT\_AMUv1p1 implements the functionality identified by the value 0b0010 .

In Armv8.0, the only permitted value is 0b0000 .

In Armv8.4, the permitted values are 0b0000 and 0b0001 .

From Armv8.6, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

Access to this field is RO.

## MPAM,bits [43:40]

Indicates the major version number of support for the MPAM Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MPAM   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b0000 | The major version number of the MPAMextension is 0. |
| 0b0001 | The major version number of the MPAMextension is 1. |

All other values are reserved.

When combined with the minor version number from ID\_AA64PFR1\_EL1.MPAM\_frac, the 'major.minor' version is:

| MPAM Extension version   | MPAM   | MPAM_frac   |
|--------------------------|--------|-------------|
| Not implemented.         | 0b0000 | 0b0000      |
| v0.1 is implemented.     | 0b0000 | 0b0001      |
| v1.0 is implemented.     | 0b0001 | 0b0000      |
| v1.1 is implemented.     | 0b0001 | 0b0001      |

For more information, see 'The Memory Partitioning and Monitoring (MPAM) Extension'.

Access to this field is RO.

## SEL2, bits [39:36]

Secure EL2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SEL2   | Meaning                        |
|--------|--------------------------------|
| 0b0000 | Secure EL2 is not implemented. |
| 0b0001 | Secure EL2 is implemented.     |

All other values are reserved.

FEAT\_SEL2 implements the functionality identified by the value 0b0001 .

From Armv8.4, if Secure state and EL2 are implemented, the value 0b0000 is not permitted.

From Armv8.4, if Secure state is not implemented, or if EL2 is not implemented, the only permitted value is 0b0000 .

Access to this field is RO.

## SVE, bits [35:32]

Scalable Vector Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SVE    | Meaning                                                             |
|--------|---------------------------------------------------------------------|
| 0b0000 | SVE architectural state and programmers' model are not implemented. |
| 0b0001 | SVE architectural state and programmers' model are implemented.     |

All other values are reserved.

FEAT\_SVE implements the functionality identified by the value 0b0001 .

If implemented, refer to ID\_AA64ZFR0\_EL1 for information about which SVE instructions are available.

Access to this field is RO.

## RAS, bits [31:28]

RAS Extension version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RAS    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | No RAS Extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 0b0001 | Support for the Reliability, Availability, and Serviceability Extension is implemented. The ESB instruction and the Error synchronization event are supported.                                                                                                                                                                                                                                                                                                                                                                                                       |
| 0b0010 | As 0b0001 , and adds support for: • If EL3 is implemented, FEAT_DoubleFault. • Additional ERXMISC<m>_EL1 System registers. • Additional System registers ERXPFGCDN_EL1, ERXPFGCTL_EL1, and ERXPFGF_EL1, and the SCR_EL3.FIEN and HCR_EL2.FIEN trap controls, to support the optional RAS Common Fault Injection Model Extension. Error records accessed through System registers conform to RAS System Architecture v1.1, which includes simplifications to ERR<n>STATUS and support for the optional RAS Timestamp and RAS Common Fault Injection Model Extensions. |
| 0b0011 | As 0b0010 and adds support for: • The error group status register, ERXGSR_EL1. • The SCR_EL3.TWERR write trap control for error record System registers. • Additional fields in ESR_ELx.ISS for error exceptions. Error records accessed through System registers conform to either RAS System Architecture v1.1 or RAS System Architecture v2.                                                                                                                                                                                                                      |

All other values are reserved.

FEAT\_RAS implements the functionality identified by the value 0b0001 .

FEAT\_RASv1p1 and FEAT\_DoubleFault implement the functionality identified by the value 0b0010 .

FEAT\_RASv2 implements the functionality identified by the value 0b0011 .

In Armv8.0 and Armv8.1, the permitted values are 0b0000 and 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

From Armv8.4, if FEAT\_DoubleFault is implemented or ERRIDR\_EL1.NUM is nonzero, the value 0b0001 is not permitted.

Note

When the value of this field is 0b0001 , ID\_AA64PFR1\_EL1.RAS\_frac indicates whether FEAT\_RASv1p1 is implemented.

From Armv8.9, if ERRIDR\_EL1.NUM is nonzero, the value 0b0010 is not permitted.

Access to this field is RO.

## GIC, bits [27:24]

System register GIC CPU interface.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GIC    | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b0000 | GIC CPU interface system registers not implemented.                                      |
| 0b0001 | System register interface to versions 3.0 and 4.0 of the GIC CPU interface is supported. |
| 0b0011 | System register interface to version 4.1 of the GIC CPU interface is supported.          |

All other values are reserved.

Access to this field is RO.

## AdvSIMD, bits [23:20]

Advanced SIMD.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AdvSIMD   | Meaning                                                                                                                                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Advanced SIMD is implemented, including support for the following SISD and SIMD operations: • Integer byte, halfword, word and doubleword element operations. • Single-precision and double-precision floating-point arithmetic. • Conversions between single-precision and half-precision data types, and double-precision and half-precision data types. |
| 0b0001    | As for 0b0000 , and also includes support for half-precision floating-point arithmetic.                                                                                                                                                                                                                                                                    |
| 0b1111    | Advanced SIMD is not implemented.                                                                                                                                                                                                                                                                                                                          |

All other values are reserved.

This field must have the same value as the FP field.

The permitted values are:

- 0b0000 in an implementation with Advanced SIMD support that does not include the FEAT\_FP16 extension.
- 0b0001 in an implementation with Advanced SIMD support that includes the FEAT\_FP16 extension.
- 0b1111 in an implementation without Advanced SIMD support.

Access to this field is RO.

## FP, bits [19:16]

Floating-point.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FP     | Meaning                                                                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Floating-point is implemented, and includes support for: • Single-precision and double-precision floating-point types. • Conversions between single-precision and half-precision data types, and double-precision and half-precision data types. |
| 0b0001 | As for 0b0000 , and also includes support for half-precision floating-point arithmetic.                                                                                                                                                          |
| 0b1111 | Floating-point is not implemented.                                                                                                                                                                                                               |

All other values are reserved.

This field must have the same value as the AdvSIMD field.

The permitted values are:

- 0b0000 in an implementation with floating-point support that does not include the FEAT\_FP16 extension.
- 0b0001 in an implementation with floating-point support that includes the FEAT\_FP16 extension.
- 0b1111 in an implementation without floating-point support.

Access to this field is RO.

## EL3, bits [15:12]

EL3 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL3    | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0000 | EL3 is not implemented.                                 |
| 0b0001 | EL3 can be executed in AArch64 state only.              |
| 0b0010 | EL3 can be executed in either AArch64 or AArch32 state. |

All other values are reserved.

The value 0b0010 is not permitted in Armv9-A implementations.

Access to this field is RO.

## EL2, bits [11:8]

EL2 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL2    | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0000 | EL2 is not implemented.                                 |
| 0b0001 | EL2 can be executed in AArch64 state only.              |
| 0b0010 | EL2 can be executed in either AArch64 or AArch32 state. |

All other values are reserved.

The value 0b0010 is not permitted in Armv9-A implementations.

Access to this field is RO.

## EL1, bits [7:4]

EL1 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL1    | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0001 | EL1 can be executed in AArch64 state only.              |
| 0b0010 | EL1 can be executed in either AArch64 or AArch32 state. |

All other values are reserved.

The value 0b0010 is not permitted in Armv9-A implementations.

Access to this field is RO.

## EL0, bits [3:0]

EL0 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL0    | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0001 | EL0 can be executed in AArch64 state only.              |
| 0b0010 | EL0 can be executed in either AArch64 or AArch32 state. |

All other values are reserved.

Access to this field is RO.

## Accessing ID\_AA64PFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64PFR0_EL1;
```