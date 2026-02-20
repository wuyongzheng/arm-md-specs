## D24.2.81 ID\_AA64DFR1\_EL1, AArch64 Debug Feature Register 1

The ID\_AA64DFR1\_EL1 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch64.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64DFR1\_EL1 are UNDEFINED.

## Attributes

ID\_AA64DFR1\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 56 55    | 52 51 48   | 47   | 44 43   | 40 39   | 36 35    | 32   |
|----------|----------|------------|------|---------|---------|----------|------|
| ABL_CMPs | DPFZS    | EBEP       | ITE  | ABLE    | PMICNTR | SPMU     |      |
| 31       | 24 23    | 16         | 15   |         | 8 7     |          | 0    |
|          | CTX_CMPs | WRPs       |      | BRPs    |         | SYSPMUID |      |

## ABL\_CMPs, bits [63:56]

## When FEAT\_ABLE is implemented:

Number of breakpoints that support address linking, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ABL_CMPs     | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| 0x00 .. 0x3F | Number of breakpoints that support address linking minus 1. |

All other values are reserved.

The number of breakpoints that support address linking is never more than either the number of breakpoints or the number of watchpoints.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DPFZS, bits [55:52]

Behavior of the cycle counter when event counting is frozen by a Statistical Profiling management event.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DPFZS   | Meaning                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | The cycle counter PMCCNTR_EL0 is never affected by PMCR_EL0.FZS.                                                                                             |
| 0b0001  | The cycle counter PMCCNTR_EL0 does not count when PMCR_EL0.DP is 1 and counting by event counters accessible to EL1 is frozen by the PMCR_EL0.FZS mechanism. |

FEAT\_SPE\_DPFZS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## EBEP, bits [51:48]

Exception-based event profiling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EBEP   | Meaning                                          |
|--------|--------------------------------------------------|
| 0b0000 | Exception-based event profiling not implemented. |
| 0b0001 | Exception-based event profiling implemented.     |

All other values are reserved.

FEAT\_EBEP implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## ITE, bits [47:44]

Instrumentation Trace Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ITE    | Meaning                                          |
|--------|--------------------------------------------------|
| 0b0000 | Instrumentation Trace Extension not implemented. |
| 0b0001 | Instrumentation Trace Extension implemented.     |

All other values are reserved.

FEAT\_ITE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## ABLE, bits [43:40]

Address Breakpoint Linking Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ABLE   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0000 | Address Breakpoint Linking Extension not implemented. |
| 0b0001 | Address Breakpoint Linking Extension implemented.     |

All other values are reserved.

FEAT\_BWE implements the address range breakpoints and mismatch breakpoints part of the functionality identified by the value 0b0001 .

FEAT\_ABLE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## PMICNTR, bits [39:36]

PMUfixed-function instruction counter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMICNTR   | Meaning                                                |
|-----------|--------------------------------------------------------|
| 0b0000    | PMUfixed-function instruction counter not implemented. |
| 0b0001    | PMUfixed-function instruction counter implemented.     |

All other values are reserved.

FEAT\_PMUv3\_ICNTR implements the functionality identified by the value 0b0001 .

If FEAT\_PMUv3 is not implemented, then the only permitted value is 0b0000 .

Access to this field is RO.

## SPMU, bits [35:32]

System PMU extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SPMU   | Meaning                                     |
|--------|---------------------------------------------|
| 0b0000 | System PMUextension not implemented.        |
| 0b0001 | System PMUextension implemented.            |
| 0b0010 | As 0b0001 , and adds support for SPMZR_EL0. |

All other values are reserved.

FEAT\_SPMU implements the functionality identified by the value 0b0001 .

FEAT\_SPMU2 implements the functionality identified by the value 0b0010 .

From Armv9.5, the value 0b0001 is not permitted.

Access to this field is RO.

## CTX\_CMPs, bits [31:24]

Context-aware breakpoints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CTX_CMPs     | Meaning                                                                       |
|--------------|-------------------------------------------------------------------------------|
| 0x00         | ID_AA64DFR0_EL1.CTX_CMPs is the number of context-aware breakpoints, minus 1. |
| 0x01 .. 0x3F | Number of context-aware breakpoints minus 1.                                  |

## All other values are reserved.

If 16 or fewer context-aware breakpoints are implemented, then the value of this field is either 0x00 or the same as ID\_AA64DFR0\_EL1.CTX\_CMPs. If more than 16 context-aware breakpoints are implemented, then the value 0x00 is not permitted.

Values greater than ID\_AA64DFR1\_EL1.BRPs are not permitted.

Access to this field is RO.

## WRPs, bits [23:16]

Watchpoints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WRPs         | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| 0x00         | ID_AA64DFR0_EL1.WRPs is the number of watchpoints, minus 1. |
| 0x01 .. 0x3F | Number of watchpoints minus 1.                              |

All other values are reserved.

Access to this field is RO.

## BRPs, bits [15:8]

Breakpoints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BRPs         | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| 0x00         | ID_AA64DFR0_EL1.BRPs is the number of breakpoints, minus 1. |
| 0x01 .. 0x3F | Number of breakpoints minus 1.                              |

All other values are reserved.

If more than 16 breakpoints are implemented, or the index of the highest numbered context-aware breakpoint is not the number of breakpoints minus 1, then the value 0x00 is not permitted.

Nonzero values less than ID\_AA64DFR0\_EL1.BRPs are not permitted.

Access to this field is RO.

## SYSPMUID, bits [7:0]

## When FEAT\_SPMU is implemented:

System PMU ID. Indicates the largest value that can be written to SPMSELR\_EL0.SYSPMUSEL.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYSPMUID     | Meaning                                                                   |
|--------------|---------------------------------------------------------------------------|
| 0x00 .. 0x1F | The largest supported value that can be written to SPMSELR_EL0.SYSPMUSEL. |

All other values are reserved.

Since System PMUs might not be contiguously accessible, this field does not necessarily indicate the total number of accessible System PMUs.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing ID\_AA64DFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64DFR1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then
```

```
UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64DFR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64DFR1_EL1;
```