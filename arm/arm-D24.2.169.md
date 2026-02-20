## D24.2.169 SCR\_EL3, Secure Configuration Register

The SCR\_EL3 characteristics are:

## Purpose

Defines the configuration of the current Security state. It specifies:

- The Security state of EL0, EL1, and EL2. The Security state is Secure, Non-secure, or Realm.
- The Execution state at lower Exception levels.
- Whether IRQ, FIQ, SError exceptions, and External abort exceptions are taken to EL3.
- Whether various operations are trapped to EL3.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCR\_EL3 are UNDEFINED.

## Attributes

SCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bit [63]

Reserved, RES0.

## NSE, bit [62]

## When FEAT\_RME is implemented:

This field, evaluated with SCR\_EL3.NS, selects the Security state of EL2 and lower Exception levels.

For a description of the values derived by evaluating NS and NSE together, see SCR\_EL3.NS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

The Effective value of this bit is 0b0 .

Access to this field is RES0.

## HACDBSEn, bit [61]

## When FEAT\_HACDBS is implemented:

Enables access to the HACDBSBR\_EL2 and HACDBSCONS\_EL2 registers at EL2.

| HACDBSEn   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | EL2 accesses to the specified registers are trapped to EL3. |
| 0b1        | This control does not cause any instructions to be trapped. |

Traps are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HDBSSEn, bit [60]

## When FEAT\_HDBSS is implemented:

Enables access to HDBSSBR\_EL2 and HDBSSPROD\_EL2 registers at EL2.

| HDBSSEn   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0       | EL2 accesses to the specified registers are trapped to EL3. |
| 0b1       | This control does not cause any instructions to be trapped. |

Traps are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FGTEn2, bit [59]

## When FEAT\_FGT2 is implemented:

Fine-Grained Traps Enable 2.

When EL2 is implemented, enables the traps to EL2 controlled by HDFGRTR2\_EL2, HDFGWTR2\_EL2, HFGITR2\_EL2, HFGRTR2\_EL2, and HFGWTR2\_EL2, and controls access to those registers.

| FGTEn2   | Meaning                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------|
| 0b0      | EL2 accesses to the specified registers are trapped to EL3. The values in these registers are treated as 0. |
| 0b1      | EL2 accesses to the specified registers are not trapped to EL3 by this mechanism.                           |

Traps caused by accesses to the fine-grained trap registers are reported using EC syndrome value 0x18 and its associated ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnDSE, bit [58]

## When FEAT\_E3DSE is implemented:

Enable for delegated SError exceptions pended by SCR\_EL3.DSE.

| EnDSE   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | Delegated SError exceptions pended by SCR_EL3.DSE are disabled. |
| 0b1     | Delegated SError exceptions pended by SCR_EL3.DSE are enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DSE, bit [57]

## When FEAT\_E3DSE is implemented:

Delegated SError exception for EL2, EL1, and EL0.

| DSE   | Meaning                                                                                 |
|-------|-----------------------------------------------------------------------------------------|
| 0b0   | This mechanism is not making a delegated SError exception pending.                      |
| 0b1   | Adelegated SError exception for EL2, EL1, and EL0 is pending because of this mechanism. |

When EL2 is implemented and enabled in the current Security state, delegated SError exceptions pended by this field are affected by HCR\_EL2.AMO and HCRX\_EL2.TMEA.

Virtual SError exceptions pended by HCR\_EL2.VSE have priority over delegated SError exceptions pended by this field.

This field is ignored by the PE and treated as zero when SCR\_EL3.EnDSE == 0

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [56]

Reserved, RES0.

## EnIDCP128, bit [55]

## When FEAT\_SYSREG128 is implemented:

Enables access to IMPLEMENTATION DEFINED 128-bit System registers.

| EnIDCP128   | Meaning                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Accesses at EL2, EL1, EL0 to IMPLEMENTATION DEFINED 128-bit System registers are trapped to EL3 using EC syndrome value 0x14 , unless the access generates a higher priority exception. Disables the functionality of the 128-bit IMPLEMENTATION DEFINED System registers that are accessible at EL3. |
| 0b1         | No accesses are trapped by this control.                                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SRMASKEn, bit [54]

## When FEAT\_SRMASK is implemented:

Enables access to the following MASK registers:

- CPACRMASK\_EL1, and CPACRMASK\_EL12.
- SCTLRMASK\_EL1, and SCTLRMASK\_EL12.
- SCTLR2MASK\_EL1, and SCTLR2MASK\_EL12.
- TCRMASK\_EL1, and TCRMASK\_EL12.
- TCR2MASK\_EL1, and TCR2MASK\_EL12.
- ACTLRMASK\_EL1 and ACTLRMASK\_EL12, if they are implemented.
- CPTRMASK\_EL2.
- SCTLRMASK\_EL2.
- SCTLR2MASK\_EL2.
- TCRMASK\_EL2.
- TCR2MASK\_EL2.
- ACTLRMASK\_EL2, if it is implemented.

| SRMASKEn   | Meaning                                                                                                                                                                   |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | EL2 accesses to the specified registers are trapped to EL3. EL1 accesses to the specified EL1 registers are trapped to EL3. The values in the registers are treated as 0. |
| 0b1        | No accesses are trapped by this control.                                                                                                                                  |

## SRMASKEn

## Meaning

Traps are reported using EC syndrome value 0x18 .

Traps generated by this control have a lower priority than traps generated by the HCRX\_EL2.SRMASKEn, HFGRTR2\_EL2 and HFGWTR2\_EL2 controls.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PFAREn, bit [53]

## When FEAT\_PFAR is implemented:

Enable access to Physical Fault Address Registers. When disabled, accesses to Physical Fault Address Registers generate a trap to EL3.

| PFAREn   | Meaning                                                                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses of the specified Physical Fault Address Registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1      | This control does not cause any instructions to be trapped.                                                                                                 |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to PFAR\_EL1, PFAR\_EL2, and PFAR\_EL12.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWERR,bit [52]

## When FEAT\_RASv2 is implemented:

Trap writes of Error Record registers. Enables a trap to EL3 on writes of Error Record registers.

| TWERR   | Meaning                                                                                                                                         |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                     |
| 0b1     | Writes of the specified Error Record registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are: MSR accesses to ERRSELR\_EL1, ERXADDR\_EL1, ERXCTLR\_EL1, ERXMISC0\_EL1, ERXMISC1\_EL1, ERXMISC2\_EL1, ERXMISC3\_EL1, and ERXSTATUS\_EL1.

In AArch32 state, the instructions affected by this control are: MCR accesses to ERRSELR, ERXADDR, ERXADDR2, ERXCTLR, ERXCTLR2, ERXMISC0, ERXMISC1, ERXMISC2, ERXMISC3, ERXMISC4, ERXMISC5, ERXMISC6, ERXMISC7, and ERXSTATUS.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 .

Accessing this field has the following behavior:

- This field is permitted to be RES0 if all of the following are true:
- ERRSELR\_EL1 and all ERX* registers are implemented as UNDEFINED or RAZ/WI.
- ERRIDR\_EL1.NUM is zero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TMEA, bit [51]

## When FEAT\_DoubleFault2 is implemented:

Trap Masked External Aborts. Controls whether a masked error exception at a lower Exception level is taken to EL3.

| TMEA   | Meaning                                                                                                                                                                                                                                                                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Synchronous External abort exceptions and SError exceptions at EL2, EL1, and EL0 are unaffected by this mechanism. That is, these exceptions are not taken to EL3 unless routed to EL3 by another control.                                                                                                                                                            |
| 0b1    | When executing at Exception levels below EL3, all of the following apply: • When PSTATE.A is 1, synchronous External abort exceptions are taken to EL3, unless they are taken from EL1 or EL0 and routed to EL2 by another control. • Masked physical SError exceptions are taken to EL3, unless they are taken from EL1 or EL0 and routed to EL2 by another control. |

This field has no effect on the routing of virtual or delegated SError exceptions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnFPM, bit [50]

## When FEAT\_FPMR is implemented:

Enables direct and indirect accesses to FPMR from EL2, EL1, and EL0.

When accesses to FPMR are disabled by this control:

- Direct accesses to FPMR from EL2, EL1, and EL0 are trapped to EL3 and reported with EC syndrome value 0x18 .

- Execution of FP8 data-processing instructions that indirectly access FPMR is UNDEFINED at EL2, EL1 and EL0.

| EnFPM   | Meaning                                                               |
|---------|-----------------------------------------------------------------------|
| 0b0     | Direct and indirect accesses to FPMRare disabled at EL2, EL1 and EL0. |
| 0b1     | This control does not cause any instructions to be trapped.           |

Traps are not taken if there is a higher priority exception generated by the access.

If EL3 is not implemented, the Effective value of this field is 0b1 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MECEn, bit [49]

## When FEAT\_MEC is implemented:

Enables access to the following EL2 MECID registers, from EL2:

- MECID\_P0\_EL2.
- MECID\_A0\_EL2
- MECID\_P1\_EL2
- MECID\_A1\_EL2
- VMECID\_P\_EL2
- VMECID\_A\_EL2

Accesses to these registers are trapped and reported using EC syndrome value 0x18 .

| MECEn   | Meaning                                                                                                                                                                                                |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | EL2 accesses to any of the specified registers are trapped to EL3. The values of the specified registers are treated as 0 for all purposes other than direct reads or writes to the register from EL3. |
| 0b1     | This control does not cause any instructions to be trapped.                                                                                                                                            |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## GPF, bit [48]

## When FEAT\_RME is implemented:

Controls the reporting of Granule protection faults at EL0, EL1 and EL2.

| GPF   | Meaning                                                                                         |
|-------|-------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause exceptions to be routed from EL0, EL1 or EL2 to EL3.                |
| 0b1   | GPFs at EL0, EL1 and EL2 are routed to EL3 and reported as Granule Protection Check exceptions. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## D128En, bit [47]

## When FEAT\_D128 is implemented:

128-bit System Register trap control. Enables access to 128-bit System Registers via MRRS , MSRR instructions.

MRRSand MSRR accesses from EL1 and EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x14 :

- TTBR0\_EL1.
- TTBR1\_EL1.
- RCWMASK\_EL1, RCWSMASK\_EL1.
- PAR\_EL1.

MRRSand MSRR accesses from EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x14 :

- TTBR1\_EL2 and accesses using the register name TTBR1\_EL12.
- TTBR0\_EL2 and accesses using the register name TTBR0\_EL12.
- VTTBR\_EL2.

| D128En   | Meaning                                                                           |
|----------|-----------------------------------------------------------------------------------|
| 0b0      | EL1 and EL2 accesses to the specified registers are disabled, and trapped to EL3. |
| 0b1      | This control does not cause any instructions to be trapped.                       |

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AIEn, bit [46]

## When FEAT\_AIE is implemented:

MAIR2\_ELx, AMAIR2\_ELx Register access trap control.

Accesses from EL1 and EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x18 :

- AMAIR2\_EL1.
- MAIR2\_EL1.

Accesses from EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x18 :

- AMAIR2\_EL2 and accesses using the register name AMAIR2\_EL12.
- MAIR2\_EL2 and accesses using the register name MAIR2\_EL12.

| AIEn   | Meaning                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | EL1 and EL2 accesses to the specified registers are disabled, and trapped to EL3. The values in these registers are treated as 0. |
| 0b1    | This control does not cause any instructions to be trapped.                                                                       |

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PIEn, bit [45]

## When FEAT\_S1PIE is implemented, or FEAT\_S2PIE is implemented, or FEAT\_S1POE is implemented, or FEAT\_S2POE is implemented:

Permission Indirection, Overlay Register access trap control. Enables access to Permission Indirection and Overlay registers.

Accesses from EL0, EL1 and EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x18 :

- POR\_EL0.

Accesses from EL1 and EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x18 :

- PIRE0\_EL1.
- PIR\_EL1.
- POR\_EL1.
- S2POR\_EL1.

Accesses from EL2 using AArch64 to the following registers are trapped and reported using EC syndrome value 0x18 :

- PIRE0\_EL2 and accesses using the register name PIRE0\_EL12.
- PIR\_EL2 and accesses using the register name PIR\_EL12.
- POR\_EL2 and accesses using the register name POR\_EL12.
- S2PIR\_EL2.

| PIEn   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | EL0, EL1 and EL2 accesses to the specified registers are disabled, and trapped to EL3. |
| 0b1    | This control does not cause any instructions to be trapped.                            |

If this field is 0, it is IMPLEMENTA TION SPECIFIC whether the values of the named registers are treated as zero.

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCTLR2En, bit [44]

## When FEAT\_SCTLR2 is implemented:

SCTLR2\_ELx register trap control. Enables access to SCTLR2\_EL1 and SCTLR2\_EL2 registers.

| SCTLR2En   | Meaning                                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | EL1 and EL2 accesses to SCTLR2_EL1 and SCTLR2_EL2 registers are disabled, and trapped to EL3. The values in these registers are treated as 0. |
| 0b1        | This control does not cause any instructions to be trapped.                                                                                   |

Traps are reported using EC syndrome value 0x18 .

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TCR2En, bit [43]

## When FEAT\_TCR2 is implemented:

TCR2\_ELx register trap control. Enables access to TCR2\_EL1 and TCR2\_EL2 registers.

| TCR2En   | Meaning                                                                                                                                   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | EL1 and EL2 accesses to TCR2_EL1 and TCR2_EL2 registers are disabled, and trapped to EL3. The values in these registers are treated as 0. |
| 0b1      | This control does not cause any instructions to be trapped.                                                                               |

Traps are reported using EC syndrome value 0x18 .

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RCWMASKEn,bit [42]

## When FEAT\_THE is implemented:

RCWand RCWS Mask register trap control. Enables access to RCWMASK\_EL1, RCWSMASK\_EL1.

| RCWMASKEn   | Meaning                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------|
| 0b0         | EL1 and EL2 accesses to RCWMASK_EL1and RCWSMASK_EL1 registers are disabled, and trapped to EL3. |
| 0b1         | This control does not cause any instructions to be trapped.                                     |

Traps for MRS , MSR access are reported using EC syndrome value 0x18 .

Traps for MRRS , MSRR acceess are reported using EC syndrome value 0x14 .

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnTP2, bit [41]

## When FEAT\_SME is implemented:

Traps instructions executed at EL2, EL1, and EL0 that access TPIDR2\_EL0 to EL3. The exception is reported using EC syndrome value 0x18 .

| EnTP2   | Meaning                                                                                 |
|---------|-----------------------------------------------------------------------------------------|
| 0b0     | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped. |
| 0b1     | This control does not cause execution of any instructions to be trapped.                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRNDR, bit [40]

## When FEAT\_RNG\_TRAP is implemented:

Controls trapping of reads of RNDR and RNDRRS. The exception is reported using EC syndrome value 0x18 .

| TRNDR   | Meaning                                                                                                                                                                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause RNDRand RNDRRSto be trapped. When FEAT_RNG is implemented: • ID_AA64ISAR0_EL1.RNDR returns the value 0b0001 . When FEAT_RNG is not implemented: • ID_AA64ISAR0_EL1.RNDR returns the value 0b0000 . • MRSreads of RNDRand RNDRRSare UNDEFINED. |
| 0b1     | ID_AA64ISAR0_EL1.RNDR returns the value 0b0001 . Any attempt to read RNDRor RNDRRSis trapped to EL3.                                                                                                                                                                      |

When FEAT\_RNG is not implemented, Arm recommends that SCR\_EL3.TRNDR is initialized before entering Exception levels below EL3 and not subsequently changed.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## GCSEn, bit [39]

## When FEAT\_GCS is implemented:

Guarded Control Stack enable. Controls access to the Guarded Control Stack registers from EL2, EL1, and EL0, and controls whether the Guarded Control Stack is enabled.

The Guarded Control Stack registers trapped by this mechanism are:

- GCSCRE0\_EL1.
- GCSCR\_EL1.
- GCSCR\_EL2.
- GCSCR\_EL12.
- GCSPR\_EL0.
- GCSPR\_EL1.
- GCSPR\_EL2.
- GCSPR\_EL12.

| GCSEn   | Meaning                                                                                                                                          |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Trap read and write accesses to all Guarded Control Stack registers to EL3. All Guarded Control Stack behavior is disabled at EL2, EL1, and EL0. |
| 0b1     | This control does not cause any instructions to be trapped, and does not disable Guarded Control Stack behavior at EL2, EL1, or EL0.             |

Traps are reported using EC syndrome value 0x18 .

Traps are not taken if there is a higher priority exception generated by the access.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HXEn, bit [38]

## When FEAT\_HCX is implemented:

Enables access to the HCRX\_EL2 register at EL2 from EL3.

| HXEn   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0    | Accesses at EL2 to HCRX_EL2 are trapped to EL3.             |
| 0b1    | This control does not cause any instructions to be trapped. |

When EL3 is not implemented, the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

ADEn, bit [37]

## When FEAT\_LS64\_ACCDATA is implemented:

Enables access to the ACCDATA\_EL1 register at EL1 and EL2.

| ADEn   | Meaning                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses to ACCDATA_EL1 at EL1 and EL2 are trapped to EL3, unless the accesses are trapped to EL2 by the EL2 fine-grained trap. |
| 0b1    | This control does not cause accesses to ACCDATA_EL1 to be trapped.                                                              |

If the HFGWTR\_EL2.nACCDATA\_EL1 or HFGRTR\_EL2.nACCDATA\_EL1 traps are enabled, they take priority over this trap.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EnAS0, bit [36]

## When FEAT\_LS64\_ACCDATA is implemented:

Traps execution of an ST64BV0 instruction at EL0, EL1, or EL2 to EL3.

| EnAS0   | Meaning                                                                                                                                                                                                                                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | EL0 execution of an ST64BV0 instruction is trapped to EL3, unless it is trapped to EL1 by SCTLR_EL1.EnAS0, or to EL2 by either HCRX_EL2.EnAS0 or SCTLR_EL2.EnAS0. EL1 execution of an ST64BV0 instruction is trapped to EL3, unless it is trapped to EL2 by HCRX_EL2.EnAS0. EL2 execution of an ST64BV0 instruction is trapped to EL3. |
| 0b1     | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                            |

Atrap of an ST64BV0 instruction is reported using EC syndrome value 0x0A , with an ISS code of 0x0000001 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AMVOFFEN,bit [35]

## When FEAT\_AMUv1p1 is implemented:

Activity Monitors Virtual Offsets Enable.

| AMVOFFEN   | Meaning                                                                                                                                     |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Accesses to AMEVCNTVOFF0<n>_EL2 and AMEVCNTVOFF1<n>_EL2 at EL2 are trapped to EL3. Indirect reads of the virtual offset registers are zero. |
| 0b1        | Accesses to AMEVCNTVOFF0<n>_EL2 and AMEVCNTVOFF1<n>_EL2 are not affected by this field.                                                     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [34]

Reserved, RES0.

## TWEDEL,bits [33:30]

## When FEAT\_TWED is implemented:

TWEDelay. A 4-bit unsigned number that, when SCR\_EL3.TWEDEn is 1, encodes the minimum delay in taking a trap of WFE* caused by SCR\_EL3.TWE as 2 (TWEDEL + 8) cycles.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWEDEn, bit [29]

## When FEAT\_TWED is implemented:

TWEDelay Enable. Enables a configurable delayed trap of the WFE* instruction caused by SCR\_EL3.TWE.

Traps are reported using EC syndrome value 0x01 .

| TWEDEn   | Meaning                                                                                   |
|----------|-------------------------------------------------------------------------------------------|
| 0b0      | The delay for taking the trap is IMPLEMENTATION DEFINED.                                  |
| 0b1      | The delay for taking the trap is at least the number of cycles defined in SCR_EL3.TWEDEL. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ECVEn, bit [28]

## When FEAT\_ECV\_POFF is implemented:

ECVEnable. Enables access to the CNTPOFF\_EL2 register.

| ECVEn   | Meaning                                                                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | EL2 accesses to CNTPOFF_EL2 are trapped to EL3, and the value of CNTPOFF_EL2 is treated as 0 for all purposes other than direct reads or writes to the register from EL3. |
| 0b1     | EL2 accesses to CNTPOFF_EL2 are not trapped to EL3 by this mechanism.                                                                                                     |

When FEAT\_ECV\_POFF is not implemented, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FGTEn, bit [27]

## When FEAT\_FGT is implemented:

Fine-Grained Traps Enable. When EL2 is implemented, enables the traps to EL2 controlled by HAFGRTR\_EL2, HDFGRTR\_EL2, HDFGWTR\_EL2, HFGRTR\_EL2, HFGITR\_EL2, and HFGWTR\_EL2, and controls access to those registers.

Note

If EL2 is not implemented but EL3 is implemented, FEAT\_FGT implements the MDCR\_EL3.TDCC traps.

| FGTEn   | Meaning                                                                                                                                                                                     |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | EL2 accesses to HAFGRTR_EL2, HDFGRTR_EL2, HDFGWTR_EL2, HFGRTR_EL2, HFGITR_EL2 and HFGWTR_EL2 registers are trapped to EL3, and the traps to EL2 controlled by those registers are disabled. |
| 0b1     | EL2 accesses to HAFGRTR_EL2, HDFGRTR_EL2, HDFGWTR_EL2, HFGRTR_EL2, HFGITR_EL2 and HFGWTR_EL2 registers are not trapped to EL3 by this mechanism.                                            |

Traps caused by accesses to the fine-grained trap registers are reported using EC syndrome value 0x18 and its associated ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATA, bit [26]

## When FEAT\_MTE2 is implemented:

Memory tagging enable override:

- Overrides enabling of Memory tagging at EL2, EL1 and EL0.
- If not trapped to EL2, accesses to the following registers at EL1 and EL2 are trapped to EL3 and reported using EC syndrome value 0x18 :
- GCR\_EL1.
- RGSR\_EL1.
- TFSRE0\_EL1.
- TFSR\_EL1.
- TFSR\_EL2.
- Accesses with the register name TFSR\_EL12 that are not UNDEFINED.

| ATA   | Meaning                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Disables the use of Memory tagging at EL2, EL1 and EL0. The specified registers are trapped to EL3 unless trapped to a lower Exception level. |
| 0b1   | This field does not disable the use of Memory tagging at EL2, EL1 and EL0. The field does not trap the specified registers to EL3.            |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnSCXT, bit [25]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Enables access to the SCXTNUM\_EL2, SCXTNUM\_EL1, and SCXTNUM\_EL0 registers.

| EnSCXT   | Meaning                                                                                                                                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses at EL0, EL1 and EL2 to SCXTNUM_EL0, SCXTNUM_EL1, or SCXTNUM_EL2 registers are trapped to EL3 if they are not trapped by a higher priority exception, and the values of these registers are treated as 0. |
| 0b1      | This control does not cause any accesses to be trapped, or register values to be treated as 0.                                                                                                                    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [24]

Reserved, RES0.

## TID5, bit [23]

## When FEAT\_IDTE3 is implemented and FEAT\_MTE2 is implemented:

Trap ID group 5. EL2 and EL1 reads of the group 5 ID register GMID\_EL1 are trapped to EL3, reported using EC syndrome value 0x18 , unless the instruction generates a higher priority exception.

| TID5   | Meaning                                                                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                                                                                               |
| 0b1    | The specified EL2 accesses to ID group 5 registers are trapped to EL3. When EL2 is not enabled in the current Security state, or when HCR_EL2.TID5 is 0, EL1 read accesses to the specified registers are trapped to EL3. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TID3, bit [22]

## When FEAT\_IDTE3 is implemented:

Trap ID group 3. EL2 and EL1 reads of the following group 3 registers are trapped to EL3, reported using EC syndrome value 0x18 , unless the instruction generates a higher priority exception:

- ID\_PFR0\_EL1, ID\_PFR1\_EL1, ID\_DFR0\_EL1, ID\_AFR0\_EL1, ID\_MMFR0\_EL1, ID\_MMFR1\_EL1, ID\_MMFR2\_EL1, ID\_MMFR3\_EL1, ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, ID\_ISAR5\_EL1, MVFR0\_EL1, MVFR1\_EL1, and MVFR2\_EL1.
- ID\_AA64PFR0\_EL1, ID\_AA64PFR1\_EL1, ID\_AA64DFR0\_EL1, ID\_AA64DFR1\_EL1, ID\_AA64ISAR0\_EL1, ID\_AA64ISAR1\_EL1, ID\_AA64MMFR0\_EL1, ID\_AA64MMFR1\_EL1, ID\_AA64AFR0\_EL1, and ID\_AA64AFR1\_EL1.
- ID\_PFR2\_EL1, and ID\_MMFR4\_EL1.
- ID\_MMFR5\_EL1.
- ID\_AA64MMFR3\_EL1.
- ID\_AA64MMFR4\_EL1.
- ID\_AA64PFR2\_EL1.

- ID\_AA64MMFR2\_EL1 and ID\_ISAR6\_EL1.
- ID\_DFR1\_EL1.
- ID\_AA64DFR2\_EL1.
- ID\_AA64ZFR0\_EL1.
- ID\_AA64SMFR0\_EL1.
- ID\_AA64FPFR0\_EL1.
- ID\_AA64ISAR2\_EL1.
- ID\_AA64ISAR3\_EL1.
- This field traps all MRS accesses to registers in the following range that are not already mentioned in this field description: op0 == 3, op1 == 0, CRn == 0, CRm == {2-7}, op2 == {0-7}.

| TID3   | Meaning                                                                                                                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                                                                                                    |
| 0b1    | The specified EL2 read accesses to ID group 3 registers are trapped to EL3. When EL2 is not enabled in the current Security state, or when HCR_EL2.TID3 is 0, EL1 read accesses to the specified registers are trapped to EL3. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FIEN, bit [21]

## When FEAT\_RASv1p1 is implemented:

Fault Injection enable. Trap accesses to the registers ERXPFGCDN\_EL1, ERXPFGCTL\_EL1, and ERXPFGF\_EL1 from EL1 and EL2 to EL3, reported using EC syndrome value 0x18 .

| FIEN   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | Accesses to the specified registers from EL1 and EL2 generate a Trap exception to EL3. |
| 0b1    | This control does not cause any instructions to be trapped.                            |

If EL3 is not implemented, the Effective value of SCR\_EL3.FIEN is 0b1 .

If ERRIDR\_EL1.NUM is zero, meaning no error records are implemented, or no error record accessible using System registers is owned by a node that implements the RAS Common Fault Injection Model Extension, then this bit might be RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NMEA,bit [20]

## When FEAT\_DoubleFault is implemented:

Non-maskable External Aborts. Controls whether PSTATE.A masks SError exceptions at EL3.

| NMEA   | Meaning                                                                 |
|--------|-------------------------------------------------------------------------|
| 0b0    | SError exceptions are not taken at EL3 if PSTATE.A == 1.                |
| 0b1    | SError exceptions are taken at EL3 regardless of the value of PSTATE.A. |

This field is ignored by the PE and treated as zero when all of the following are true:

- FEAT\_DoubleFault2 is not implemented.
- SCR\_EL3.EA is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EASE, bit [19]

## When FEAT\_DoubleFault is implemented:

External aborts to SError exception vector.

| EASE   | Meaning                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Synchronous External abort exceptions taken to EL3 are taken to the appropriate synchronous exception vector offset from VBAR_EL3. |
| 0b1    | Synchronous External abort exceptions taken to EL3 are taken to the appropriate SError exception vector offset from VBAR_EL3.      |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EEL2, bit [18]

## When FEAT\_SEL2 is implemented:

Secure EL2 Enable.

| EEL2   | Meaning                                                                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | All behaviors associated with Secure EL2 are disabled. All registers, including timer registers, defined by FEAT_SEL2 are UNDEFINED, and those timers are disabled. |
| 0b1    | All behaviors associated with Secure EL2 are enabled.                                                                                                               |

When the value of this bit is 1, then:

- When SCR\_EL3.NS == 0, the SCR\_EL3.RW bit is treated as 1 for all purposes other than reading or writing the register.
- If Secure EL1 is using AArch32, then any of the following operations, executed in Secure EL1, is trapped to Secure EL2, using EC syndrome value 0x03 :
- Aread or write of the SCR.
- Aread or write of the NSACR.
- Aread or write of the MVBAR.
- Aread or write of the SDCR.
- Execution of an ATS12NSO** instruction.
- If Secure EL1 is using AArch32, then any of the following operations, executed in Secure EL1, is trapped to Secure EL2 using EC syndrome value 0x00 :
- Execution of an SRS instruction that uses R13\_mon.
- Execution of an MRS (Banked register) or MSR (Banked register) instruction that would access SPSR\_mon, R13\_mon, or R14\_mon.

## Note

If the Effective value of SCR\_EL3.EEL2 is 0, then these operations executed in Secure EL1 using AArch32 are trapped to EL3.

ASecure only implementation that does not implement EL3 but implements EL2, behaves as if SCR\_EL3.EEL2 == 1.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## API, bit [17]

## When FEAT\_PAuth is implemented:

Controls the use of the following instructions related to Pointer Authentication.

- PACGA.
- AUTDA, AUTDB, AUTDZA, AUTDZB, AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZA, AUTIZB, PACDA, PACDB, PACDZA, PACDZB, PACIA, PACIA1716, PACIASP, PACIAZ, PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZA, PACIZB, RETAA, RETAB, BRAA, BRAB, BLRAA, BLRAB, BRAAZ, BRABZ, BLRAAZ, BLRABZ, ERETAA, ERETAB, LDRAA and LDRAB, when any of the following are true:
- In EL0, when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, and the associated SCTLR\_EL1.En&lt;N&gt;&lt;M&gt; == 1.
- In EL0, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, and the associated SCTLR\_EL2.En&lt;N&gt;&lt;M&gt; == 1.
- In EL1, when the associated SCTLR\_EL1.En&lt;N&gt;&lt;M&gt; == 1.
- In EL2, when the associated SCTLR\_EL2.En&lt;N&gt;&lt;M&gt; == 1.
- When FEAT\_PAuth\_LR is implemented, AUTIASPPC, AUTIASPPCR, AUTIA171615, AUTIBSPPC, AUTIBSPPCR, AUTIB171615, PACIASPPC, PACNBIASPPC, PACIA171615, PACIBSPPC, PACNBIBSPPC, PACIB171615, RETAASPPC, RETAASPPCR, RETABSPPC, RETABSPPCR, when any of the following are true:
- In EL0, when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, and the associated SCTLR\_EL1.En&lt;N&gt;&lt;M&gt; == 1.
- In EL0, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, and the associated SCTLR\_EL2.En&lt;N&gt;&lt;M&gt; == 1.
- In EL1, when the associated SCTLR\_EL1.En&lt;N&gt;&lt;M&gt; == 1.
- In EL2, when the associated SCTLR\_EL2.En&lt;N&gt;&lt;M&gt; == 1.

| API   | Meaning                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The specified instructions are trapped to EL3, when the instructions are enabled, unless they are trapped to EL2 as a result of the higher priority HCR_EL2.API trap. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                                           |

Traps are reported using EC syndrome value 0x09 .

An instruction is trapped only if Pointer Authentication is enabled for that instruction, for more information, see 'PAC generation and verification keys'.

Note

If FEAT\_PAuth is implemented but EL3 is not implemented, the system behaves as if this bit is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APK, bit [16]

## When FEAT\_PAuth is implemented:

Trap registers holding 'key' values for Pointer Authentication. Traps accesses to the following registers, using EC syndrome value 0x18 , from EL1 or EL2 to EL3 unless they are trapped to EL2 as a result of the HCR\_EL2.APK bit or other traps:

- APIAKeyLo\_EL1, APIAKeyHi\_EL1, APIBKeyLo\_EL1, APIBKeyHi\_EL1.
- APDAKeyLo\_EL1, APDAKeyHi\_EL1, APDBKeyLo\_EL1, APDBKeyHi\_EL1.
- APGAKeyLo\_EL1, and APGAKeyHi\_EL1.

| APK   | Meaning                                                                                                                                                                                      |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Access to the registers holding 'key' values for pointer authentication from EL1 or EL2 are trapped to EL3 unless they are trapped to EL2 as a result of the HCR_EL2.APK bit or other traps. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                                                                  |

For more information, see 'PAC generation and verification keys'.

Note

If FEAT\_PAuth is implemented but EL3 is not implemented, the system behaves as if this bit is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TERR, bit [15]

## When FEAT\_RAS is implemented:

Trap accesses of Error Record registers. Enables a trap to EL3 on accesses of Error Record registers.

| TERR   | Meaning                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                       |
| 0b1    | Accesses of the specified Error Record registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to ERRSELR\_EL1, ERXADDR\_EL1, ERXCTLR\_EL1, ERXMISC0\_EL1, ERXMISC1\_EL1, and ERXSTATUS\_EL1.
- MRS accesses to ERRIDR\_EL1 and ERXFR\_EL1.
- If FEAT\_RASv1p1 is implemented, MRS and MSR accesses to ERXMISC2\_EL1 and ERXMISC3\_EL1.
- If FEAT\_RASv2 is implemented, MRS accesses to ERXGSR\_EL1.

In AArch32 state, the instructions affected by this control are:

- MRC and MCR accesses to ERRSELR, ERXADDR, ERXADDR2, ERXCTLR, ERXCTLR2, ERXMISC0, ERXMISC1, ERXMISC2, ERXMISC3, and ERXSTATUS.
- MRC accesses to ERRIDR, ERXFR, and ERXFR2.
- If FEAT\_RASv1p1 is implemented, MRC and MCR accesses to ERXMISC4, ERXMISC5, ERXMISC6, and ERXMISC7.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 .

Accessing this field has the following behavior:

- This field is permitted to be RES0 if all of the following are true:
- ERRSELR\_EL1 and all ERX* registers are implemented as UNDEFINED or RAZ/WI.
- ERRIDR\_EL1.NUM is zero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLOR, bit [14]

## When FEAT\_LOR is implemented:

Trap LOR registers. Traps Non-secure and Realm accesses to the LORSA\_EL1, LOREA\_EL1, LORN\_EL1, LORC\_EL1, and LORID\_EL1 registers from EL1 and EL2 to EL3, unless the access has been trapped to EL2.

| TLOR   | Meaning                                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                    |
| 0b1    | Non-secure and Realm EL1 and EL2 accesses to the LORregisters that are not UNDEFINED are trapped to EL3, unless it is trapped by HCR_EL2.TLOR. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWE, bit [13]

Traps EL2, EL1, and EL0 execution of WFE instructions to EL3, from any Security state and both Execution states, reported using EC syndrome value 0x01 .

When FEAT\_WFxT is implemented, this trap also applies to the WFET instruction.

| TWE   | Meaning                                                                                                                                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                     |
| 0b1   | Any attempt to execute a WFEinstruction at any Exception level lower than EL3 is trapped to EL3, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWE, HCR.TWE, SCTLR_EL1.nTWE, SCTLR_EL2.nTWE, or HCR_EL2.TWE. |

In AArch32 state, the attempted execution of a conditional WFE instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

For more information about when WFE instructions can cause the PE to enter a low-power state, see 'Wait for Event mechanism and Send event'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TWI, bit [12]

Traps EL2, EL1, and EL0 execution of WFI instructions to EL3, from any Security state and both Execution states, reported using EC syndrome value 0x01 .

When FEAT\_WFxT is implemented, this trap also applies to the WFIT instruction.

| TWI   | Meaning                                                                                                                                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                      |
| 0b1   | Any attempt to execute a WFI instruction at any Exception level lower than EL3 is trapped to EL3, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWI, HCR.TWI, SCTLR_EL1.nTWI, SCTLR_EL2.nTWI, or HCR_EL2.TWI. |

In AArch32 state, the attempted execution of a conditional WFI instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

For more information about when WFI instructions can cause the PE to enter a low-power state, see 'Wait for Interrupt'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ST, bit [11]

Traps Secure EL1 accesses to the Counter-timer Physical Secure timer registers to EL3, from AArch64 state only, reported using EC syndrome value 0x18 .

| ST   | Meaning                                                                                                                                                                                                                      |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Secure EL1 using AArch64 accesses to the CNTPS_TVAL_EL1, CNTPS_CTL_EL1, and CNTPS_CVAL_EL1 are trapped to EL3 when Secure EL2 is disabled. If Secure EL2 is enabled, the behavior is as if the value of this field was 0b1 . |
| 0b1  | This control does not cause any instructions to be trapped.                                                                                                                                                                  |

Note

Accesses to the Counter-timer Physical Secure timer registers are always enabled at EL3. These registers are not accessible at EL0.

When FEAT\_RME is implemented and Secure state is not implemented, this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## RW, bit [10]

## When FEAT\_AA32EL1 is implemented:

Execution state control for lower Exception levels.

| RW   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | All lower Exception levels are using AArch32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 0b1  | The next lower Exception level is using AArch64: • If EL2 is implemented and enabled in the Security state determined by SCR_EL3.{NSE,NS}, then EL2 is using AArch64 and EL2 controls the Execution state for EL1. • If EL2 is not implemented or EL2 is disabled in the Security state determined by SCR_EL3.{NSE,NS}, then EL1 is using AArch64. When executing at EL0, if the next higher Exception level is using AArch64, then the Execution state is determined by PSTATE.nRW. Otherwise, EL0 uses AArch32. |

If any of the following apply, then the Effective value of this bit is 1:

- EL2 is implemented and does not support AArch32, and SCR\_EL3.NS is 1.
- The Effective value of SCR\_EL3.{EEL2,NS} is {1,0}.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAO/WI.

## SIF, bit [9]

Secure instruction fetch. When the PE is in Secure state, this bit disables instruction execution from memory marked in the first stage of translation as being Non-secure.

| SIF   | Meaning                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Secure state instruction execution from memory marked in the first stage of translation as being Non-secure is permitted.     |
| 0b1   | Secure state instruction execution from memory marked in the first stage of translation as being Non-secure is not permitted. |

When FEAT\_RME is implemented and Secure state is not implemented, this bit is RES0.

When FEAT\_PAN3 is implemented, it is IMPLEMENTATION DEFINED whether SCR\_EL3.SIF is also used to determine instruction access permission for the purpose of PAN.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## HCE, bit [8]

Hypervisor Call instruction enable. Enables HVC instructions at EL3 and, if EL2 is enabled in the current Security state, at EL2 and EL1, in both Execution states, reported using EC syndrome value 0x00 .

| HCE   | Meaning                                           |
|-------|---------------------------------------------------|
| 0b0   | HVCinstructions are UNDEFINED.                    |
| 0b1   | HVCinstructions are enabled at EL3, EL2, and EL1. |

Note

HVC instructions are always UNDEFINED at EL0 and, if Secure EL2 is disabled, at Secure EL1. Any resulting exception is taken from the current Exception level to the current Exception level.

If EL2 is not implemented, this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SMD, bit [7]

Secure Monitor Call disable. Disables SMC instructions at EL1 and above, from any Security state and both Execution states, reported using EC syndrome value 0x00 .

Note

SMC instructions are always UNDEFINED at EL0. Any resulting exception is taken from the current Exception level to the current Exception level.

If HCR\_EL2.TSC or HCR.TSC traps attempted EL1 execution of SMC instructions to EL2, that trap has priority over this disable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [6]

Reserved, RES0.

## Bits [5:4]

Reserved, RES1.

## EA, bit [3]

External Abort and SError exception routing.

| EA   | Meaning                                                                                                                                                                                                              |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When executing at Exception levels below EL3, External aborts and SError exceptions are not taken to EL3. In addition, when executing at EL3: • SError exceptions are not taken. • External aborts are taken to EL3. |
| 0b1  | When executing at any Exception level, External aborts and SError exceptions are taken to EL3.                                                                                                                       |

This field has no effect on the routing of virtual or delegated SError exceptions.

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FIQ, bit [2]

Physical FIQ Routing.

| FIQ   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When executing at Exception levels below EL3, physical FIQ interrupts are not taken to EL3. When executing at EL3, physical FIQ interrupts are not taken. |

| SMD   | Meaning                                           |
|-------|---------------------------------------------------|
| 0b0   | SMC instructions are enabled at EL3, EL2 and EL1. |
| 0b1   | SMC instructions are UNDEFINED.                   |

0b1

When executing at any Exception level, physical FIQ interrupts are taken to EL3.

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRQ, bit [1]

Physical IRQ Routing.

| IRQ   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When executing at Exception levels below EL3, physical IRQ interrupts are not taken to EL3. When executing at EL3, physical IRQ interrupts are not taken. |
| 0b1   | When executing at any Exception level, physical IRQ interrupts are taken to EL3.                                                                          |

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS, bit [0]

## When FEAT\_RME is implemented:

Non-secure bit. This field is used in combination with SCR\_EL3.NSE to select the Security state of EL2 and lower Exception levels.

| NSE   | NS   | Meaning     |
|-------|------|-------------|
| 0b0   | 0b0  | Secure.     |
| 0b0   | 0b1  | Non-secure. |
| 0b1   | 0b0  | Reserved.   |
| 0b1   | 0b1  | Realm.      |

When Secure state is not implemented, SCR\_EL3.NS is RES1 and its Effective value is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Non-secure bit.

| NS   | Meaning                                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Indicates that EL0 and EL1 are in Secure state. When FEAT_SEL2 is implemented and SCR_EL3.EEL2 == 1, then EL2 is using AArch64 and in Secure state. |
| 0b1  | Indicates that Exception levels lower than EL3 are in Non-secure state, so memory accesses from those Exception levels cannot access Secure memory. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SCR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SCR_EL3;
```

MSR SCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then SCR_EL3 = X[t, 64];
```