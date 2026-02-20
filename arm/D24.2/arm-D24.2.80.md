## D24.2.80 ID\_AA64DFR0\_EL1, AArch64 Debug Feature Register 0

The ID\_AA64DFR0\_EL1 characteristics are:

Purpose

Provides top-level information about the debug system in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

The external register EDDFR gives information from this register.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64DFR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64DFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 60 59      | 56 55   | 52 51   | 48 47   | 44 43       | 40 39     | 36         | 35       | 32   |
|----------|------------|---------|---------|---------|-------------|-----------|------------|----------|------|
| HPMN0    | ExtTrcBuff | BRBE    | MTPMU   |         | TraceBuffer | TraceFilt | DoubleLock | PMSVer   |      |
| 31       | 28 27      | 24 23   | 20 19   | 16 15   | 12          | 11 8      | 7 4        | 3        | 0    |
| CTX_CMPs | SEBEP      | WRPs    | PMSS    |         | BRPs        | PMUVer    | TraceVer   | DebugVer |      |

## HPMN0, bits [63:60]

Zero PMU event counters for a Guest operating system.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HPMN0   | Meaning                                                               |
|---------|-----------------------------------------------------------------------|
| 0b0000  | Setting MDCR_EL2.HPMN to zero has CONSTRAINED UNPREDICTABLE behavior. |
| 0b0001  | Setting MDCR_EL2.HPMN to zero has defined behavior.                   |

All other values are reserved.

FEAT\_HPMN0 implements the functionality identified by the value 0b0001 .

From Armv8.8, in an implementation that includes FEAT\_PMUv3, FEAT\_FGT, and EL2, the value 0b0000 is not permitted.

Access to this field is RO.

## ExtTrcBuff, bits [59:56]

Trace Buffer External Mode Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ExtTrcBuff   | Meaning                                     |
|--------------|---------------------------------------------|
| 0b0000       | Trace Buffer External Mode not implemented. |
| 0b0001       | Trace Buffer External Mode implemented.     |

All other values are reserved.

FEAT\_TRBE\_EXT implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## BRBE, bits [55:52]

Branch Record Buffer Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BRBE   | Meaning                                                   |
|--------|-----------------------------------------------------------|
| 0b0000 | Branch Record Buffer Extension not implemented.           |
| 0b0001 | Branch Record Buffer Extension implemented.               |
| 0b0010 | As 0b0001 , and adds support for branch recording at EL3. |

All other values are reserved.

FEAT\_BRBE implements the functionality identified by the value 0b0001 .

FEAT\_BRBEv1p1 implements the functionality identified by the value 0b0010 .

From Armv9.3, if FEAT\_BRBE is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## MTPMU,bits [51:48]

Multi-threaded PMU extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTPMU   | Meaning                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | FEAT_MTPMU not implemented. If FEAT_PMUv3 is implemented, it is IMPLEMENTATION DEFINED whether PMEVTYPER<n>_EL0.MT and PMEVTYPER<n>.MT are read/write or RES0.                                     |
| 0b0001  | FEAT_MTPMU and FEAT_PMUv3 implemented. PMEVTYPER<n>_EL0.MT and PMEVTYPER<n>.MT are read/write. When FEAT_MTPMU is disabled, the Effective values of PMEVTYPER<n>_EL0.MT and PMEVTYPER<n>.MT are 0. |
| 0b1111  | FEAT_MTPMU not implemented. If FEAT_PMUv3 is implemented, PMEVTYPER<n>_EL0.MT and PMEVTYPER<n>.MT are RES0.                                                                                        |

All other values are reserved.

FEAT\_MTPMU implements the functionality identified by the value 0b0001 .

From Armv8.6, in an implementation that includes FEAT\_PMUv3, the value 0b0000 is not permitted.

In an implementation that does not include FEAT\_PMUv3, the value 0b0001 is not permitted.

Access to this field is RO.

## TraceBuffer, bits [47:44]

Trace Buffer Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceBuffer   | Meaning                                                                                                                                                                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000        | Trace Buffer Extension not implemented.                                                                                                                                                                                                        |
| 0b0001        | Trace Buffer Extension implemented.                                                                                                                                                                                                            |
| 0b0010        | As 0b0001 , and adds: • If EL2 and FEAT_FGT are implemented, a fine-grained trap on the TSB CSYNC instruction. • If EL2 is implemented, an EL2 control to override TRBLIMITR_EL1.nVM. • The TRBE Profiling exception extension, FEAT_TRBE_EXC. |

All other values are reserved.

FEAT\_TRBE implements the functionality identified by the value 0b0001 .

FEAT\_TRBEv1p1 implements the functionality identified by the value 0b0010 .

In any Armv9 implementation, if FEAT\_ETE is implemented, the value 0b0000 is not permitted.

From Armv9.6, if FEAT\_TRBE is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## TraceFilt, bits [43:40]

Armv8.4 Self-hosted Trace Extension version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceFilt   | Meaning                                              |
|-------------|------------------------------------------------------|
| 0b0000      | Armv8.4 Self-hosted Trace Extension not implemented. |
| 0b0001      | Armv8.4 Self-hosted Trace Extension implemented.     |

All other values are reserved.

FEAT\_TRF implements the functionality identified by the value 0b0001 .

From Armv8.4, if FEAT\_ETMv4 is implemented, the value 0b0000 is not permitted.

If FEAT\_ETE is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## DoubleLock, bits [39:36]

OS Double Lock implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DoubleLock   | Meaning                                              |
|--------------|------------------------------------------------------|
| 0b0000       | OS Double Lock implemented. OSDLR_EL1 is RW.         |
| 0b1111       | OS Double Lock not implemented. OSDLR_EL1 is RAZ/WI. |

All other values are reserved.

FEAT\_DoubleLock implements the functionality identified by the value 0b0000 .

In Armv8.0, the only permitted value is 0b0000 .

If FEAT\_Debugv8p2 is implemented and FEAT\_DoPD is not implemented, the permitted values are 0b0000 and 0b1111 .

If FEAT\_DoPD is implemented, the only permitted value is 0b1111 .

Access to this field is RO.

## PMSVer, bits [35:32]

Statistical Profiling Extension version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMSVer   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | Statistical Profiling Extension not implemented.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 0b0001   | Statistical Profiling Extension implemented.                                                                                                                                                                                                                                                                                                                                                                                                                |
| 0b0010   | As 0b0001 , and adds: • Support for the Events packet Alignment flag. • If FEAT_SVE is implemented, support for the Scalable Vector extensions to Statistical Profiling.                                                                                                                                                                                                                                                                                    |
| 0b0011   | As 0b0010 , and adds: • Discard mode. • Extended event filtering, including the PMSNEVFR_EL1 System register. • Support for the OPTIONAL previous branch target Address packet. • If FEAT_PMUv3 is implemented, controls to freeze the PMUevent counters after an SPE buffer management event occurs. • If FEAT_PMUv3 is implemented, the SAMPLE_FEED_BR, SAMPLE_FEED_EVENT, SAMPLE_FEED_LAT, SAMPLE_FEED_LD, SAMPLE_FEED_OP, and SAMPLE_FEED_ST PMUevents. |
| 0b0100   | As 0b0011 , and adds: • If FEAT_MOPS is implemented, Operation Type packet encodings for Memory Copy and Set operations. • If FEAT_MTE is implemented, Operation Type packet encodings for loads and stores of Allocation Tags.                                                                                                                                                                                                                             |
| 0b0101   | As 0b0100 , and adds: • Support for the Events packet Level 2 Data cache access, Level 2 Data cache miss, Cached data modified, Recently fetched cache line, and Cache snoop flags. • Support for Data Source filtering.                                                                                                                                                                                                                                    |
| 0b0110   | As 0b0101 , and adds: • If EL2 and FEAT_FGT are implemented, a fine-grained trap on the PSB CSYNC instruction. • The SPE Profiling exception extension, FEAT_SPE_EXC. • The Statistical Profiling physical addressing mode extension, FEAT_SPE_nVM.                                                                                                                                                                                                         |

All other values are reserved.

FEAT\_SPE implements the functionality identified by the value 0b0001 .

FEAT\_SPEv1p1 implements the functionality identified by the value 0b0010 .

FEAT\_SPEv1p2 implements the functionality identified by the value 0b0011 .

FEAT\_SPEv1p3 implements the functionality identified by the value 0b0100 .

FEAT\_SPEv1p4 implements the functionality identified by the value 0b0101 .

FEAT\_SPEv1p5 implements the functionality identified by the value 0b0110 .

From Armv8.5, if FEAT\_SPE is implemented, the value 0b0001 is not permitted.

From Armv8.7, if FEAT\_SPE is implemented, the value 0b0010 is not permitted.

From Armv8.8, if FEAT\_SPE is implemented, the value 0b0011 is not permitted.

From Armv8.9, if FEAT\_SPE is implemented, the value 0b0100 is not permitted.

From Armv9.6, if FEAT\_SPE is implemented, the value 0b0101 is not permitted.

Access to this field is RO.

## CTX\_CMPs, bits [31:28]

Number of context-aware breakpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CTX_CMPs         | Meaning                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 .. 0b1110 | The number of context-aware breakpoints, minus 1.                                                                                                                                                        |
| 0b1111           | If ID_AA64DFR1_EL1.CTX_CMPs is zero, then 16 context-aware breakpoints are implemented. Otherwise, 16 or more context-aware breakpoints are implemented and ID_AA64DFR1_EL1.CTX_CMPs indicates how many. |

Values greater than ID\_AA64DFR0\_EL1.BRPs are not permitted.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

Access to this field is RO.

## SEBEP, bits [27:24]

Synchronous-exception-based event profiling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SEBEP   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0000  | Synchronous-exception-based event profiling not implemented. |
| 0b0001  | Synchronous-exception-based event profiling implemented.     |

All other values are reserved.

FEAT\_SEBEP implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## WRPs, bits [23:20]

Number of watchpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WRPs             | Meaning                             |
|------------------|-------------------------------------|
| 0b0001 .. 0b1111 | The number of watchpoints, minus 1. |

If FEAT\_Debugv8p9 is implemented and 16 or more watchpoints are implemented, then this field reads as 0b1111 and ID\_AA64DFR1\_EL1.WRPs indicates the number of watchpoints.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 watchpoints.

The value

0b0000 is reserved.

Access to this field is RO.

## PMSS, bits [19:16]

PMUSnapshot extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMSS   | Meaning                                |
|--------|----------------------------------------|
| 0b0000 | PMUsnapshot extension not implemented. |
| 0b0001 | PMUsnapshot extension implemented.     |

All other values are reserved.

FEAT\_PMUv3\_SS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## BRPs, bits [15:12]

Index of the highest numbered context-aware breakpoint. Identifies which of the implemented breakpoints are context-aware breakpoints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BRPs             | Meaning                                                 |
|------------------|---------------------------------------------------------|
| 0b0001 .. 0b1110 | Index of the highest numbered context-aware breakpoint. |

| BRPs   | Meaning                                                                                                                                                                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1111 | If ID_AA64DFR0_EL1.CTX_CMPs and ID_AA64DFR1_EL1.CTX_CMPs indicate that 16 or fewer breakpoints are context-aware, then the index of the highest context-aware breakpoint is 15. Otherwise, the context-aware breakpoints are the lowest numbered breakpoints. |

If ID\_AA64DFR1\_EL1.BRPs is zero, then this is also the number of implemented breakpoints, minus 1, meaning the context-aware breakpoints are the highest numbered breakpoints.

The value of this field is always less than the number of implemented breakpoints.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

The value

0b0000 is reserved.

Access to this field is RO.

## PMUVer, bits [11:8]

Performance Monitors Extension version.

This field does not follow the standard ID scheme, but uses the alternative ID scheme described in 'Alternative ID scheme used for the Performance Monitors Extension version'.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMUVer   | Meaning                                                                                                                                                                                                                                      |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | Performance Monitors Extension not implemented.                                                                                                                                                                                              |
| 0b0001   | Performance Monitors Extension, PMUv3 implemented.                                                                                                                                                                                           |
| 0b0100   | PMUv3 for Armv8.1. As 0b0001 , and adds support for: • Extended 16-bit PMEVTYPER<n>_EL0.evtCount field. • If EL2 is implemented, the MDCR_EL2.HPMD control.                                                                                  |
| 0b0101   | PMUv3 for Armv8.4. As 0b0100 , and adds support for the PMMIR_EL1 register.                                                                                                                                                                  |
| 0b0110   | PMUv3 for Armv8.5. As 0b0101 , and adds support for: • 64-bit event counters. • If EL2 is implemented, the MDCR_EL2.HCCD control. • If EL3 is implemented, the MDCR_EL3.SCCD control.                                                        |
| 0b0111   | PMUv3 for Armv8.7. As 0b0110 , and adds support for: • The PMCR_EL0.FZO and, if EL2 is implemented, MDCR_EL2.HPMFZO controls. • If EL3 is implemented, the MDCR_EL3.{MPMX,MCCD} controls.                                                    |
| 0b1000   | PMUv3 for Armv8.8. As 0b0111 , and: • Extends the Common event number space to include 0x0040 to 0x00BF and 0x4040 to 0x40BF . • Removes the CONSTRAINED UNPREDICTABLE behaviors if a reserved or unimplemented PMUevent number is selected. |
| 0b1001   | PMUv3 for Armv8.9. As 0b1000 , and: • Updates the definitions of existing PMUevents. • Adds support for the PMUSERENR_EL0.UEN control and the PMUACR_EL1 register. • Adds support for the EDECR.PME control.                                 |
| 0b1111   | IMPLEMENTATION DEFINED form of performance monitors supported, PMUv3 not supported. Arm does not recommend this value for new implementations.                                                                                               |

All other values are reserved.

FEAT\_PMUv3 implements the functionality identified by the value 0b0001 .

FEAT\_PMUv3p1 implements the functionality identified by the value 0b0100 .

FEAT\_PMUv3p4 implements the functionality identified by the value 0b0101 .

FEAT\_PMUv3p5 implements the functionality identified by the value 0b0110 .

FEAT\_PMUv3p7 implements the functionality identified by the value 0b0111 .

FEAT\_PMUv3p8 implements the functionality identified by the value 0b1000 .

FEAT\_PMUv3p9 implements the functionality identified by the value 0b1001 .

From Armv8.1, if FEAT\_PMUv3 is implemented, the value 0b0001 is not permitted.

From Armv8.4, if FEAT\_PMUv3 is implemented, the value 0b0100 is not permitted.

From Armv8.5, if FEAT\_PMUv3 is implemented, the value 0b0101 is not permitted.

From Armv8.7, if FEAT\_PMUv3 is implemented, the value 0b0110 is not permitted.

From Armv8.8, if FEAT\_PMUv3 is implemented, the value 0b0111 is not permitted.

From Armv8.9, if FEAT\_PMUv3 is implemented, the value 0b1000 is not permitted.

Access to this field is RO.

## TraceVer, bits [7:4]

Trace support. Indicates whether System register interface to a trace unit is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceVer   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Trace unit System registers not implemented. |
| 0b0001     | Trace unit System registers implemented.     |

All other values are reserved.

When trace unit System registers are implemented, see TRCIDR1 for tracing capabilities of the trace unit. Access to this field is RO.

## DebugVer, bits [3:0]

Debug architecture version. Indicates presence of Armv8 debug architecture.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DebugVer   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0110     | Armv8.0 debug architecture.                 |
| 0b0111     | Armv8.1 debug architecture, FEAT_Debugv8p1. |
| 0b1000     | Armv8.2 debug architecture, FEAT_Debugv8p2. |
| 0b1001     | Armv8.4 debug architecture, FEAT_Debugv8p4. |
| 0b1010     | Armv8.8 debug architecture, FEAT_Debugv8p8. |

| DebugVer   | Meaning                                     |
|------------|---------------------------------------------|
| 0b1011     | Armv8.9 debug architecture, FEAT_Debugv8p9. |

All other values are reserved.

FEAT\_Debugv8p1 implements the functionality identified by the value 0b0111 . FEAT\_Debugv8p2 implements the functionality identified by the value 0b1000 . FEAT\_Debugv8p4 implements the functionality identified by the value 0b1001 . FEAT\_Debugv8p8 implements the functionality identified by the value 0b1010 . FEAT\_Debugv8p9 implements the functionality identified by the value 0b1011 . From Armv8.1, when FEAT\_Debugv8p1 is implemented the value 0b0110 is not permitted. From Armv8.2, the values 0b0110 and 0b0111 are not permitted. From Armv8.4, the value 0b1000 is not permitted. From Armv8.8, the value 0b1001 is not permitted. From Armv8.9, the value 0b1010 is not permitted. Access to this field is RO.

## Accessing ID\_AA64DFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64DFR0_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR0_EL1; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64DFR0_EL1;
```