## D24.2.51 FGWTE3\_EL3, Fine-Grained Write Traps EL3

The FGWTE3\_EL3 characteristics are:

## Purpose

Provides controls for traps of MSR and MSRR writes to specified EL3 system registers.

## Configuration

This register is present only when EL3 is implemented, FEAT\_FGWTE3 is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to FGWTE3\_EL3 are UNDEFINED.

## Attributes

FGWTE3\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

MSR accesses are trapped to EL3 and reported with EC syndrome value 0x18 .

MSRR accesses are trapped to EL3 and reported with EC syndrome value 0x14 .

The bits in this register are sticky. Writes to these bits have the following properties:

- Awrite of 0b0 is ignored.
- Awrite of 0b1 updates the bit to 0b1 .

## Bits [63:23]

Reserved, RES0.

## GPCBW\_EL3, bit [22]

When FEAT\_RME\_GPC3 is implemented:

Traps accesses of GPCBW\_EL3 to EL3.

| GPCBW_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## VBAR\_EL3, bit [21]

Traps accesses of VBAR\_EL3 to EL3.

| VBAR_EL3   | Meaning                                                                                       |
|------------|-----------------------------------------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped.                                   |
| 0b1        | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## TTBR0\_EL3, bit [20]

Traps accesses of TTBR0\_EL3 to EL3.

| TTBR0_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## TPIDR\_EL3, bit [19]

Traps accesses of TPIDR\_EL3 to EL3.

| TPIDR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## TCR\_EL3, bit [18]

Traps accesses of TCR\_EL3 to EL3.

| TCR_EL3   | Meaning                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------|
| 0b0       | This control does not cause any instructions to be trapped.                                   |
| 0b1       | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## SPMROOTCR\_EL3, bit [17]

## When FEAT\_RME is implemented and FEAT\_SPMU is implemented:

Traps accesses of SPMROOTCR\_EL3 to EL3.

| SPMROOTCR_EL3   | Meaning                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------|
| 0b0             | This control does not cause any instructions to be trapped.                                   |
| 0b1             | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## SCTLR2\_EL3, bit [16]

## When FEAT\_SCTLR2 is implemented:

Traps accesses of SCTLR2\_EL3 to EL3.

| SCTLR2_EL3   | Meaning                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------|
| 0b0          | This control does not cause any instructions to be trapped.                                   |
| 0b1          | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## SCTLR\_EL3, bit [15]

Traps accesses of SCTLR\_EL3 to EL3.

| SCTLR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## PIR\_EL3, bit [14]

## When FEAT\_S1PIE is implemented:

Traps accesses of PIR\_EL3 to EL3.

| PIR_EL3   | Meaning                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------|
| 0b0       | This control does not cause any instructions to be trapped.                                   |
| 0b1       | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## MPAM3\_EL3, bit [13]

## When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented:

Traps accesses of MPAM3\_EL3 to EL3.

| MPAM3_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

MECID\_RL\_A\_EL3, bit [12]

## When FEAT\_MEC is implemented:

Traps accesses of MECID\_RL\_A\_EL3 to EL3.

| MECID_RL_A_EL3   | Meaning                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------|
| 0b0              | This control does not cause any instructions to be trapped.                                   |
| 0b1              | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## MDCR\_EL3, bit [11]

Traps accesses of MDCR\_EL3 to EL3.

| MDCR_EL3   | Meaning                                                                                       |
|------------|-----------------------------------------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped.                                   |
| 0b1        | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## MAIR2\_EL3, bit [10]

## When FEAT\_AIE is implemented:

Traps accesses of MAIR2\_EL3 to EL3.

| MAIR2_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## MAIR\_EL3, bit [9]

Traps accesses of MAIR\_EL3 to EL3.

| MAIR_EL3   | Meaning                                                                                       |
|------------|-----------------------------------------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped.                                   |
| 0b1        | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## GPTBR\_EL3, bit [8]

## When FEAT\_RME is implemented:

Traps accesses of GPTBR\_EL3 to EL3.

| GPTBR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## GPCCR\_EL3, bit [7]

## When FEAT\_RME is implemented:

Traps accesses of GPCCR\_EL3 to EL3.

| GPCCR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## GCSPR\_EL3, bit [6]

## When FEAT\_GCS is implemented:

Traps accesses of GCSPR\_EL3 to EL3.

| GCSPR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

GCSCR\_EL3, bit [5]

## When FEAT\_GCS is implemented:

Traps accesses of GCSCR\_EL3 to EL3.

| GCSCR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## AMAIR2\_EL3, bit [4]

## When FEAT\_AIE is implemented:

Traps accesses of AMAIR2\_EL3 to EL3.

| AMAIR2_EL3   | Meaning                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------|
| 0b0          | This control does not cause any instructions to be trapped.                                   |
| 0b1          | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Otherwise:

Reserved, RES0.

## AMAIR\_EL3, bit [3]

Traps accesses of AMAIR\_EL3 to EL3.

| AMAIR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## AFSR1\_EL3, bit [2]

Traps accesses of AFSR1\_EL3 to EL3.

| AFSR1_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## AFSR0\_EL3, bit [1]

Traps accesses of AFSR0\_EL3 to EL3.

| AFSR0_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## ACTLR\_EL3, bit [0]

Traps accesses of ACTLR\_EL3 to EL3.

| ACTLR_EL3   | Meaning                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------|
| 0b0         | This control does not cause any instructions to be trapped.                                   |
| 0b1         | MSR write accesses to the specified register are trapped to EL3 with EC syndrome value 0x18 . |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1S.

## Accessing FGWTE3\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, FGWTE3\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b101 |

if !(HaveEL(EL3) &amp;&amp;

IsFeatureImplemented(FEAT\_FGWTE3) &amp;&amp;

IsFeatureImplemented(FEAT\_AA64))

then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = FGWTE3\_EL3;

MSR FGWTE3\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b101 |

if !(HaveEL(EL3) &amp;&amp; IsFeatureImplemented(FEAT\_FGWTE3) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then UNDEFINED;

elsif PSTATE.EL == EL3 then FGWTE3\_EL3 = X[t, 64];