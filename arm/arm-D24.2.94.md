## D24.2.94 ID\_AA64PFR1\_EL1, AArch64 Processor Feature Register 1

The ID\_AA64PFR1\_EL1 characteristics are:

## Purpose

Provides additional information about implemented PE features in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64PFR1\_EL1 are UNDEFINED.

## Attributes

ID\_AA64PFR1\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 60 59   | 56 55   | 52 51     | 48 47   | 44 43    | 40 39    | 36   | 35        | 32   |
|-----------|---------|---------|-----------|---------|----------|----------|------|-----------|------|
| PFAR      | DF2     | MTEX    | THE       | GCS     |          | MTE_frac | NMI  | CSV2_frac |      |
| 31        | 28 27   | 24 23   | 20 19     | 16 15   | 12 11    | 8 7      |      | 4 3       | 0    |
| RNDR_trap | SME     | RES0    | MPAM_frac |         | RAS_frac | MTE      | SSBS |           | BT   |

## PFAR, bits [63:60]

Support for physical fault address registers, FEAT\_PFAR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PFAR   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b0000 | FEAT_PFAR is not implemented.                                                                               |
| 0b0001 | FEAT_PFAR is implemented. Includes support for the PFAR_ELx and, if EL3 is implemented, MFAR_EL3 registers. |

All other values are reserved.

FEAT\_PFAR implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## DF2, bits [59:56]

Support for error exception routing extensions, FEAT\_DoubleFault2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DF2    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | FEAT_DoubleFault2 is not implemented. Note This does not mean that FEAT_DoubleFault, as identified by ID_AA64PFR0_EL1.RAS >= 0b0010 , not implemented.                                                                                                                                                                                                                                                             |
| 0b0001 | FEAT_DoubleFault2 is implemented. As ID_AA64PFR0_EL1.RAS == 0b0010 , and also includes support for routing error exceptions: • Traps for masked error exceptions, HCRX_EL2.TMEA and SCR_EL3.TMEA. • Additional controls for masking SError exceptions, SCTLR2_EL1.NMEA, and SCTLR2_EL2.NMEA. • Additional controls for taking external aborts to the SError exception vector, SCTLR2_EL1.EASE and SCTLR2_EL2.EASE. |

All other values are reserved.

FEAT\_DoubleFault2 implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## MTEX, bits [55:52]

Support for additional MTE tag checking modes.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTEX   | Meaning                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Canonical Tag checking and Memory tagging with Address tagging disabled are not supported.                                                  |
| 0b0001 | The following additional tag checking modes for MTEare supported: • Canonical Tag checking. • Memory tagging with Address tagging disabled. |

All other values are reserved.

This field is valid only if ID\_AA64PFR1\_EL1.MTE &gt;= 0b0010 .

FEAT\_MTE\_NO\_ADDRESS\_TAGS and FEAT\_MTE\_CANONICAL\_TAGS implement the functionality identified by the value 0b0001 .

If FEAT\_MTE2 is not implemented, the value 0b0001 is not permitted.

From Armv8.9, if FEAT\_MTE2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## THE, bits [51:48]

Support for Translation Hardening Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| THE    | Meaning                                                                                                                                                                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Translation Hardening Extension is not implemented.                                                                                                                                                                                                              |
| 0b0001 | The RCWand RCWSinstructions, their associated registers and traps are supported. If EL2 is implemented, the AssuredOnly check, TopLevel check, and their associated controls are implemented. If EL2 and FEAT_GCS are implemented, VTCR_EL2.GCSH is implemented. |

All other values are reserved.

FEAT\_THE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## GCS, bits [47:44]

Support for Guarded Control Stack.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GCS    | Meaning                                   |
|--------|-------------------------------------------|
| 0b0000 | Guarded Control Stack is not implemented. |
| 0b0001 | Guarded Control Stack is implemented.     |

All other values are reserved.

FEAT\_GCS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## MTE\_frac, bits [43:40]

Support for Asynchronous reporting of a Tag Check Fault.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTE_frac   | Meaning                                                       |
|------------|---------------------------------------------------------------|
| 0b0000     | Asynchronous reporting of a Tag Check Fault is supported.     |
| 0b1111     | Asynchronous reporting of a Tag Check Fault is not supported. |

All other values are reserved.

This field is valid only if ID\_AA64PFR1\_EL1.MTE &gt;= 0b0010 .

FEAT\_MTE\_ASYNC implements the functionality identified by the value 0b0000 .

If FEAT\_MTE\_ASYM\_FAULT is implemented this field must be 0b0000 .

Access to this field is RO.

## NMI, bits [39:36]

Non-maskable Interrupt. Indicates support for Non-maskable interrupts.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NMI    | Meaning                                                                                          |
|--------|--------------------------------------------------------------------------------------------------|
| 0b0000 | SCTLR_ELx.{SPINTMASK, NMI} and PSTATE.ALLINT with its associated instructions are not supported. |
| 0b0001 | SCTLR_ELx.{SPINTMASK, NMI} and PSTATE.ALLINT with its associated instructions are supported.     |

All other values are reserved.

FEAT\_NMI implements the functionality identified by the value 0b0001 .

From Armv8.8, the value 0b0000 is not permitted.

Access to this field is RO.

## CSV2\_frac, bits [35:32]

CSV2 fractional field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CSV2_frac   | Meaning                                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | Either ID_AA64PFR0_EL1.CSV2 is not 0b0001 , or the implementation does not disclose whether FEAT_CSV2_1p1 is implemented. FEAT_CSV2_1p2 is not implemented. |
| 0b0001      | FEAT_CSV2_1p1 is implemented, but FEAT_CSV2_1p2 is not implemented.                                                                                         |
| 0b0010      | FEAT_CSV2_1p2 is implemented.                                                                                                                               |

All other values are reserved.

FEAT\_CSV2\_1p1 implements the functionality identified by the value 0b0001 .

FEAT\_CSV2\_1p2 implements the functionality identified by the value 0b0010 .

From Armv8.0, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

The values 0b0001 and 0b0010 are permitted only when ID\_AA64PFR0\_EL1.CSV2 is 0b0001 .

Access to this field is RO.

## RNDR\_trap, bits [31:28]

Random Number trap to EL3 field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RNDR_trap   | Meaning                                                                  |
|-------------|--------------------------------------------------------------------------|
| 0b0000      | Trapping of RNDRand RNDRRSto EL3 is not supported.                       |
| 0b0001      | Trapping of RNDRand RNDRRSto EL3 is supported. SCR_EL3.TRNDR is present. |

All other values are reserved.

FEAT\_RNG\_TRAP implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SME, bits [27:24]

Scalable Matrix Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SME    | Meaning                                                            |
|--------|--------------------------------------------------------------------|
| 0b0000 | SMEarchitectural state and programmers' model are not implemented. |
| 0b0001 | SMEarchitectural state and programmers' model are implemented.     |
| 0b0010 | As 0b0001 , plus the SME2 ZT0 register.                            |

All other values are reserved.

FEAT\_SME implements the functionality identified by the value 0b0001 .

FEAT\_SME2 implements the functionality identified by the value 0b0010 .

From Armv9.2, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

If implemented, refer to ID\_AA64SMFR0\_EL1 and ID\_AA64ZFR0\_EL1 for information about which SME and SVE instructions are available.

Access to this field is RO.

## Bits [23:20]

Reserved, RES0.

## MPAM\_frac, bits [19:16]

Indicates the minor version number of support for the MPAM Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MPAM_frac   | Meaning                                             |
|-------------|-----------------------------------------------------|
| 0b0000      | The minor version number of theMPAM extension is 0. |
| 0b0001      | The minor version number of theMPAM extension is 1. |

All other values are reserved.

When combined with the major version number from ID\_AA64PFR0\_EL1.MPAM, The combined 'major.minor' version is:

| MPAM Extension version   | MPAM   | MPAM_frac   |
|--------------------------|--------|-------------|
| Not implemented.         | 0b0000 | 0b0000      |

| MPAM Extension version   | MPAM   | MPAM_frac   |
|--------------------------|--------|-------------|
| v0.1 is implemented.     | 0b0000 | 0b0001      |
| v1.0 is implemented.     | 0b0001 | 0b0000      |
| v1.1 is implemented.     | 0b0001 | 0b0001      |

For more information, see 'The Memory Partitioning and Monitoring (MPAM) Extension'.

Access to this field is RO.

## RAS\_frac, bits [15:12]

RAS Extension fractional field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RAS_frac   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | If ID_AA64PFR0_EL1.RAS == 0b0001 , support for the Reliability, Availability, and Serviceability Extension is implemented.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0b0001     | If ID_AA64PFR0_EL1.RAS == 0b0001 , as 0b0000 and adds support for: • Additional ERXMISC<m>_EL1 System registers. • Additional System registers ERXPFGCDN_EL1, ERXPFGCTL_EL1, and ERXPFGF_EL1, and the SCR_EL3.FIEN and HCR_EL2.FIEN trap controls, to support the optional RAS Common Fault Injection Model Extension. Error records accessed through System registers conform to RAS System Architecture v1.1, which includes simplifications to ERR<n>STATUS, and support for the optional RAS Timestamp and RAS Common Fault Injection Model Extensions. |

All other values are reserved.

FEAT\_RAS implements the functionality identified by the value 0b0000 .

FEAT\_RASv1p1 implements the functionality identified by the value 0b0001 .

This field is valid only if ID\_AA64PFR0\_EL1.RAS == 0b0001 .

Access to this field is RO.

## MTE, bits [11:8]

Support for the Memory Tagging Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTE    | Meaning                                                   |
|--------|-----------------------------------------------------------|
| 0b0000 | Memory Tagging Extension is not implemented.              |
| 0b0001 | Instruction-only Memory Tagging Extension is implemented. |

| MTE    | Meaning                                                                                                                                                                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0010 | As 0b0001 , and adds: • Support for in-memory Allocation tags. • Support for synchronous tag checking. • Optional support for Asynchronous reporting of a Tag Check Fault, identified as FEAT_MTE_ASYNC. Support for FEAT_MTE_ASYNC is indicated by ID_AA64PFR1_EL1.MTE_frac. |
| 0b0011 | As 0b0010 , except that support for FEAT_MTE_ASYNC is mandatory, and adds support for Asymmetric Tag Check Fault handling, identified as FEAT_MTE_ASYM_FAULT.                                                                                                                 |

All other values are reserved.

FEAT\_MTE implements the functionality identified by the value 0b0001 .

FEAT\_MTE2 implements the functionality identified by the value 0b0010 .

FEAT\_MTE3 implements the functionality identified by the value 0b0011 .

From Armv8.7, when the value of this field is &gt;= 0b0010 , ID\_AA64PFR2\_EL1.MTEPERM indicates support for FEAT\_MTE\_PERM.

From Armv8.7, when the value of this field is &gt;= 0b0010 , the following fields indicate support for FEAT\_MTE4:

- ID\_AA64PFR1\_EL1.MTEX
- ID\_AA64PFR2\_EL1.MTEFAR
- ID\_AA64PFR2\_EL1.MTESTOREONLY

Access to this field is RO.

## SSBS, bits [7:4]

Speculative Store Bypassing controls in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SSBS   | Meaning                                                                                            |
|--------|----------------------------------------------------------------------------------------------------|
| 0b0000 | AArch64 provides no mechanism to control the use of Speculative Store Bypassing.                   |
| 0b0001 | AArch64 provides the PSTATE.SSBS mechanism to mark regions that are Speculative Store Bypass Safe. |
| 0b0010 | As 0b0001 , and adds the MSRand MRSinstructions to directly read and write the PSTATE.SSBS field.  |

All other values are reserved.

FEAT\_SSBS implements the functionality identified by the value 0b0001 .

FEAT\_SSBS2 implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## BT, bits [3:0]

Branch Target Identification mechanism support in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BT     | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0000 | The Branch Target Identification mechanism is not implemented. |
| 0b0001 | The Branch Target Identification mechanism is implemented.     |

All other values are reserved.

FEAT\_BTI implements the functionality identified by the value 0b0001 .

From Armv8.5, the value 0b0000 is not permitted.

Access to this field is RO.

## Accessing ID\_AA64PFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64PFR1_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64PFR1_EL1;
```

elsif PSTATE.EL == EL3 then X[t, 64] =

ID\_AA64PFR1\_EL1;