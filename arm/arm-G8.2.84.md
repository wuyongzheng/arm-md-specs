## G8.2.84 ID\_DFR0, Debug Feature Register 0

The ID\_DFR0 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch32 state.

Must be interpreted with the Main ID Register, MIDR.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_DFR0 bits [31:0] are architecturally mapped to AArch64 System register ID\_DFR0\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_DFR0 are UNDEFINED.

## Attributes

ID\_DFR0 is a 32-bit register.

## Field descriptions

| 31        | 28 27   | 24 23    | 20 19   | 16 15   | 12 11   | 8 7     | 4 3   | 0      |
|-----------|---------|----------|---------|---------|---------|---------|-------|--------|
| TraceFilt | PerfMon | MProfDbg | MMapTrc | CopTrc  | MMapDbg | CopSDbg |       | CopDbg |

## TraceFilt, bits [31:28]

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

## PerfMon, bits [27:24]

Performance Monitors Extension version.

This field does not follow the standard ID scheme, but uses the alternative ID scheme described in 'Alternative ID scheme used for the Performance Monitors Extension version'.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PerfMon   | Meaning                                                                                                                                                                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Performance Monitors Extension not implemented.                                                                                                                                                                                            |
| 0b0001    | Performance Monitors Extension, PMUv1 implemented.                                                                                                                                                                                         |
| 0b0010    | Performance Monitors Extension, PMUv2 implemented.                                                                                                                                                                                         |
| 0b0011    | Performance Monitors Extension, PMUv3 implemented.                                                                                                                                                                                         |
| 0b0100    | PMUv3 for Armv8.1. As 0b0011 , and adds support for: • Extended 16-bit PMEVTYPER<n>.evtCount field. • If EL2 is implemented, theHDCR.HPMD control.                                                                                         |
| 0b0101    | PMUv3 for Armv8.4. As 0b0100 , and adds support for the PMMIRregister.                                                                                                                                                                     |
| 0b0110    | PMUv3 for Armv8.5. As 0b0101 , and adds support for: • 64-bit event counters. • If EL2 is implemented, the HDCR.HCCD control. • If EL3 is implemented, the SDCR.SCCD control.                                                              |
| 0b0111    | PMUv3 for Armv8.7. As 0b0110 , and adds support for: • The PMCR.FZO and, if EL2 is implemented, HDCR.HPMFZO controls. • If EL3 is implemented and using AArch64, the MDCR_EL3.{MPMX,MCCD} controls.                                        |
| 0b1000    | PMUv3 for Armv8.8. As 0b0111 , and: • Extends the Common event number space to include 0x0040 to 0x00BF and 0x4040 to 0x40BF • Removes the CONSTRAINED UNPREDICTABLE behaviors if a reserved or unimplementedPMU event number is selected. |
| 0b1001    | PMUv3 for Armv8.9. As 0b1000 , and: • Updates the definitions of existing PMUevents. • Adds support for the EDECR.PME control.                                                                                                             |
| 0b1111    | IMPLEMENTATION DEFINED form of performance monitors supported, PMUv3 not supported. Arm does not recommend this value for new implementations.                                                                                             |

## All other values are reserved.

| FEAT_PMUv3 implements the functionality identified by the value 0b0011 .       |
|--------------------------------------------------------------------------------|
| FEAT_PMUv3p1 implements the functionality identified by the value 0b0100 .     |
| FEAT_PMUv3p4 implements the functionality identified by the value 0b0101 .     |
| FEAT_PMUv3p5 implements the functionality identified by the value 0b0110 .     |
| FEAT_PMUv3p7 implements the functionality identified by the value 0b0111 .     |
| FEAT_PMUv3p8 implements the functionality identified by the value 0b1000 .     |
| FEAT_PMUv3p9 implements the functionality identified by the value 0b1001 .     |
| In any Armv8 implementation, the values 0b0001 and 0b0010 are not permitted.   |
| From Armv8.1, if FEAT_PMUv3 is implemented, the value 0b0011 is not permitted. |
| From Armv8.4, if FEAT_PMUv3 is implemented, the value 0b0100 is not permitted. |
| From Armv8.5, if FEAT_PMUv3 is implemented, the value 0b0101 is not permitted. |
| From Armv8.7, if FEAT_PMUv3 is implemented, the value 0b0110 is not permitted. |
| From Armv8.8, if FEAT_PMUv3 is implemented, the value 0b0111 is not permitted. |
| From Armv8.9, if FEAT_PMUv3 is implemented, the value 0b1000 is not permitted. |

Note

In Armv7, the value 0b0000 can mean that PMUv1 is implemented. PMUv1 and PMUv2 are not permitted in an Armv8 implementation.

Access to this field is RO.

## MProfDbg, bits [23:20]

M-profile Debug. Support for memory-mapped debug model for M-profile processors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MProfDbg   | Meaning                                                              |
|------------|----------------------------------------------------------------------|
| 0b0000     | Not supported.                                                       |
| 0b0001     | Support for M-profile Debug architecture, with memory-mapped access. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## MMapTrc, bits [19:16]

Memory-mapped Trace. Support for memory-mapped trace model.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MMapTrc   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0000    | Not supported.                                                 |
| 0b0001    | Support for Arm trace architecture, with memory-mapped access. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

For more information, see the Arm® Embedded Trace Macrocell Architecture Specification, ETMv4 (ARM IHI 0064).

Access to this field is RO.

## CopTrc, bits [15:12]

Support for System registers-based trace model, using registers in the coproc == 0b1110 encoding space.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CopTrc   | Meaning        |
|----------|----------------|
| 0b0000   | Not supported. |

| 0b0001   | Support for Arm trace architecture, with System registers access.   |
|----------|---------------------------------------------------------------------|

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0001 .

For more information, see the Arm® Embedded Trace Macrocell Architecture Specification, ETMv4 (ARM IHI 0064).

Access to this field is RO.

## MMapDbg, bits [11:8]

Memory-mapped Debug. Support for Armv7 memory-mapped debug model for A and R-profile processors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MMapDbg   | Meaning                                                                |
|-----------|------------------------------------------------------------------------|
| 0b0000    | Not supported.                                                         |
| 0b0100    | Support for Armv7, v7 Debug architecture, with memory-mapped access.   |
| 0b0101    | Support for Armv7, v7.1 Debug architecture, with memory-mapped access. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

The optional memory map defined by Armv8 is not compatible with Armv7.

Access to this field is RO.

## CopSDbg, bits [7:4]

Support for a System registers-based Secure debug model, using registers in the coproc = 0b1110 encoding space, for an A-profile processor that includes EL3.

If EL3 is not implemented and the implemented Security state is Non-secure state, this field is RES0. Otherwise, this field reads the same as bits [3:0].

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CopDbg, bits [3:0]

Debug architecture version. Indicates presence of Armv8 debug architecture.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CopDbg   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0000   | Not supported.                                                |
| 0b0010   | Armv6, v6 Debug architecture, with System registers access.   |
| 0b0011   | Armv6, v6.1 Debug architecture, with System registers access. |
| 0b0100   | Armv7, v7 Debug architecture, with System registers access.   |

| CopDbg   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0101   | Armv7, v7.1 Debug architecture, with System registers access. |
| 0b0110   | Armv8 debug architecture.                                     |
| 0b0111   | Armv8.1 debug architecture, FEAT_Debugv8p1.                   |
| 0b1000   | Armv8.2 debug architecture, FEAT_Debugv8p2.                   |
| 0b1001   | Armv8.4 debug architecture, FEAT_Debugv8p4.                   |
| 0b1010   | Armv8.8 debug architecture, FEAT_Debugv8p8.                   |
| 0b1011   | Armv8.9 debug architecture, FEAT_Debugv8p9.                   |

## All other values are reserved.

The values 0b0000 , 0b0010 , 0b0011 , 0b0100 , and 0b0101 are not permitted in Armv8.

FEAT\_Debugv8p1 implements the functionality identified by the value 0b0111 .

FEAT\_Debugv8p2 implements the functionality identified by the value 0b1000 .

FEAT\_Debugv8p4 implements the functionality identified by the value 0b1001 .

FEAT\_Debugv8p8 implements the functionality identified by the value 0b1010 .

FEAT\_Debugv8p9 implements the functionality identified by the value 0b1011 .

From Armv8.1, when FEAT\_Debugv8p1 is implemented the value 0b0110 is not permitted.

From Armv8.2, the values 0b0110 and 0b0111 are not permitted.

From Armv8.4, the value 0b1000 is not permitted.

From Armv8.8, the value 0b1001 is not permitted.

From Armv8.9, the value 0b1010 is not permitted.

Access to this field is RO.

## Accessing ID\_DFR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0001 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_DFR0; elsif PSTATE.EL == EL2 then R[t] = ID_DFR0; elsif PSTATE.EL == EL3 then R[t] = ID_DFR0;
```