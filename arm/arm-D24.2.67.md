## D24.2.67 HDFGRTR\_EL2, Hypervisor Debug Fine-Grained Read Trap Register

The HDFGRTR\_EL2 characteristics are:

## Purpose

Provides controls for traps of MRS and MRC reads of debug, trace, PMU, and Statistical Profiling System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HDFGRTR\_EL2 are UNDEFINED.

## Attributes

HDFGRTR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

PMBIDR\_EL1, bit [63]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMBIDR\_EL1 at EL1 using AArch64 to EL2.

| PMBIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMBIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMBIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMSNEVFR\_EL1, bit [62]

## When FEAT\_SPE\_FnE is implemented:

Trap MRS reads of PMSNEVFR\_EL1 at EL1 using AArch64 to EL2.

| nPMSNEVFR_EL1   | Meaning                                                                                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSNEVFR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1             | MRS reads of PMSNEVFR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nBRBDATA, bit [61]

## When FEAT\_BRBE is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- BRBINF&lt;n&gt;\_EL1.
- BRBINFINJ\_EL1.
- BRBSRC&lt;n&gt;\_EL1.
- BRBSRCINJ\_EL1.
- BRBTGT&lt;n&gt;\_EL1.

- BRBTGTINJ\_EL1.
- BRBTS\_EL1.

| nBRBDATA   | Meaning                                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1        | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nBRBCTL, bit [60]

## When FEAT\_BRBE is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- BRBCR\_EL1.
- BRBFCR\_EL1.

| nBRBCTL   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nBRBIDR, bit [59]

## When FEAT\_BRBE is implemented:

Trap MRS reads of BRBIDR0\_EL1 at EL1 using AArch64 to EL2.

| nBRBIDR   | Meaning                                                                                                                                                                                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of BRBIDR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1       | MRS reads of BRBIDR0_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMCEIDn\_EL0, bit [58]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMCEID&lt;n&gt;\_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMCEID&lt;n&gt; at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| PMCEIDn_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of PMCEID<n>_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMCEID<n> at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of PMCEID<n>_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of PMCEID<n> at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMUSERENR\_EL0, bit [57]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMUSERENR\_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMUSERENR at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| PMUSERENR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of PMUSERENR_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMUSERENRat EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1             | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of PMUSERENR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of PMUSERENRat EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBTRG\_EL1, bit [56]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBTRG\_EL1 at EL1 using AArch64 to EL2.

| TRBTRG_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRBTRG_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBTRG_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBSR\_EL1, bit [55]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBSR\_EL1 at EL1 using AArch64 to EL2.

| TRBSR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TRBSR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBSR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBPTR\_EL1, bit [54]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBPTR\_EL1 at EL1 using AArch64 to EL2.

| TRBPTR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRBPTR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBPTR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBMAR\_EL1, bit [53]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBMAR\_EL1 at EL1 using AArch64 to EL2.

| TRBMAR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRBMAR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBMAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBLIMITR\_EL1, bit [52]

When FEAT\_TRBE is implemented:

Trap MRS reads of TRBLIMITR\_EL1 at EL1 using AArch64 to EL2.

| TRBLIMITR_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of TRBLIMITR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBLIMITR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TRBIDR\_EL1, bit [51]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBIDR\_EL1 at EL1 using AArch64 to EL2.

| TRBIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRBIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBBASER\_EL1, bit [50]

## When FEAT\_TRBE is implemented:

Trap MRS reads of TRBBASER\_EL1 at EL1 using AArch64 to EL2.

| TRBBASER_EL1   | Meaning                                                                                                                                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | MRS reads of TRBBASER_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRBBASER_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [49]

Reserved, RES0.

## TRCVICTLR, bit [48]

When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCVICTLR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCVICTLR at EL1 using AArch64 to EL2.

| TRCVICTLR   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TRCVICTLR are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCVICTLR at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCSTATR, bit [47]

When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCSTATR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCSTATR at EL1 using AArch64 to EL2.

| TRCSTATR   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of TRCSTATR are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCSTATR at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCSSCSRn, bit [46]

## When IsFeatureImplemented(FEAT\_ETE) || ((IsFeatureImplemented(FEAT\_ETMv4) &amp;&amp; TRCSSCSR&lt;n&gt; are implemented) &amp;&amp; IsFeatureImplemented(FEAT\_TRC\_SR)):

In an Armv9 implementation, trap MRS reads of TRCSSCSR&lt;n&gt; at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCSSCSR&lt;n&gt; at EL1 using AArch64 to EL2.

| TRCSSCSRn   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TRCSSCSR<n> are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCSSCSR<n> at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If Single-shot Comparator n is not implementented, a read of TRCSSCSR&lt;n&gt; is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCSEQSTR, bit [45]

When IsFeatureImplemented(FEAT\_ETE) || ((IsFeatureImplemented(FEAT\_ETMv4) &amp;&amp; TRCSEQSTR is implemented) &amp;&amp; IsFeatureImplemented(FEAT\_TRC\_SR)):

In an Armv9 implementation, trap MRS reads of TRCSEQSTR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCSEQSTR at EL1 using AArch64 to EL2.

| TRCSEQSTR   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TRCSEQSTR are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCSEQSTR at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCPRGCTLR, bit [44]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCPRGCTLR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCPRGCTLR at EL1 using AArch64 to EL2.

| TRCPRGCTLR   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRCPRGCTLR are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCPRGCTLR at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCOSLSR, bit [43]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCOSLSR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCOSLSR at EL1 using AArch64 to EL2.

| TRCOSLSR   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of TRCOSLSR are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCOSLSR at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [42]

Reserved, RES0.

## TRCIMSPECn, bit [41]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCIMSPEC&lt;n&gt; at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCIMSPEC&lt;n&gt; at EL1 using AArch64 to EL2.

| TRCIMSPECn   | Meaning                                                                                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRCIMSPEC<n> are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCIMSPEC<n> at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

TRCIMSPEC&lt;1-7&gt; are optional. If TRCIMSPEC&lt;n&gt; is not implemented, a read of TRCIMSPEC&lt;n&gt; is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCID, bit [40]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- In an Armv9 implementation:

- TRCDEVARCH.
- TRCDEVID.
- All of the TRCIDR&lt;n&gt; registers.
- In an Armv8 implementation:
- ETMTRCDEVARCH.
- ETMTRCDEVID.
- All of the ETM TRCIDR&lt;n&gt; registers.

| TRCID   | Meaning                                                                                                                                                                                                                                                                                                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1     | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [39:38]

Reserved, RES0.

## TRCCNTVRn, bit [37]

When IsFeatureImplemented(FEAT\_ETE) || ((IsFeatureImplemented(FEAT\_ETMv4) &amp;&amp; TRCCNTVR&lt;n&gt; are implemented) &amp;&amp; IsFeatureImplemented(FEAT\_TRC\_SR)):

In an Armv9 implementation, trap MRS reads of TRCCNTVR&lt;n&gt; at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCCNTVR&lt;n&gt; at EL1 using AArch64 to EL2.

| TRCCNTVRn   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TRCCNTVR<n> are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCCNTVR<n> at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If Counter n is not implemented, a read of TRCCNTVR&lt;n&gt; is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCCLAIM, bit [36]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- In an Armv9 implementation: TRCCLAIMCLR and TRCCLAIMSET.
- In an Armv8 implementation: ETM TRCCLAIMCLR and ETM TRCCLAIMSET.

| TRCCLAIM   | Meaning                                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCAUXCTLR,bit [35]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCAUXCTLR at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCAUXCTLR at EL1 using AArch64 to EL2.

| TRCAUXCTLR   | Meaning                                                                                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of TRCAUXCTLRare not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCAUXCTLRat EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCAUTHSTATUS, bit [34]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

In an Armv9 implementation, trap MRS reads of TRCAUTHSTATUS at EL1 using AArch64 to EL2.

In an Armv8 implementation, trap MRS reads of ETM TRCAUTHSTATUS at EL1 using AArch64 to EL2.

| TRCAUTHSTATUS   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of TRCAUTHSTATUS are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TRCAUTHSTATUS at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRC, bit [33]

## When FEAT\_ETE is implemented or (FEAT\_ETMv4 is implemented and System register access to the trace unit registers is implemented):

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- In an Armv9 implementation:
- TRCACATR&lt;n&gt;.
- TRCACVR&lt;n&gt;.
- TRCBBCTLR.
- TRCCCCTLR.
- TRCCIDCCTLR0.
- TRCCIDCCTLR1.
- TRCCIDCVR&lt;n&gt;.
- TRCCNTCTLR&lt;n&gt;.
- TRCCNTRLDVR&lt;n&gt;.
- TRCCONFIGR.
- TRCEVENTCTL0R.
- TRCEVENTCTL1R.
- TRCEXTINSELR&lt;n&gt;.
- TRCQCTLR.
- TRCRSCTLR&lt;n&gt;.
- TRCRSR.
- TRCSEQEVR&lt;n&gt;.
- TRCSEQRSTEVR.
- TRCSSCCR&lt;n&gt;.
- TRCSSPCICR&lt;n&gt;.
- TRCSTALLCTLR.
- TRCSYNCPR.
- TRCTRACEIDR.
- TRCTSCTLR.
- TRCVIIECTLR.
- TRCVIPCSSCTLR.

- TRCVISSCTLR.
- TRCVMIDCCTLR0.
- TRCVMIDCCTLR1.
- TRCVMIDCVR&lt;n&gt;.
- In an Armv8 implementation:
- ETMTRCACATR&lt;n&gt;.
- ETMTRCACVR&lt;n&gt;.
- ETMTRCBBCTLR.
- ETMTRCCCCTLR.
- ETMTRCCIDCCTLR0.
- ETMTRCCIDCCTLR1.
- ETMTRCCIDCVR&lt;n&gt;.
- ETMTRCCNTCTLR&lt;n&gt;.
- ETMTRCCNTRLDVR&lt;n&gt;.
- ETMTRCCONFIGR.
- ETMTRCEVENTCTL0R.
- ETMTRCEVENTCTL1R.
- ETMTRCEXTINSELR.
- ETMTRCQCTLR.
- ETMTRCRSCTLR&lt;n&gt;.
- ETMTRCSEQEVR&lt;n&gt;.
- ETMTRCSEQRSTEVR.
- ETMTRCSSCCR&lt;n&gt;.
- ETMTRCSSPCICR&lt;n&gt;.
- ETMTRCSTALLCTLR.
- ETMTRCSYNCPR.
- ETMTRCTRACEIDR.
- ETMTRCTSCTLR.
- ETMTRCVIIECTLR.
- ETMTRCVIPCSSCTLR.
- ETMTRCVISSCTLR.
- ETMTRCVMIDCCTLR0.
- ETMTRCVMIDCCTLR1.
- ETMTRCVMIDCVR&lt;n&gt;.

| TRC   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1   | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

Aread of an unimplemented register is UNDEFINED.

TRCEXTINSELR&lt;n&gt; and TRCRSR are implemented only if FEAT\_ETE is implemented.

TRCEXTINSELR is implemented only if FEAT\_ETE is not implemented and FEAT\_ETMv4 is implemented.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMSLATFR\_EL1, bit [32]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMSLATFR\_EL1 at EL1 using AArch64 to EL2.

| PMSLATFR_EL1   | Meaning                                                                                                                                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | MRS reads of PMSLATFR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSLATFR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PMSIRR\_EL1, bit [31]

When FEAT\_SPE is implemented:

Trap MRS reads of PMSIRR\_EL1 at EL1 using AArch64 to EL2.

| PMSIRR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMSIRR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSIRR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PMSIDR\_EL1, bit [30]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMSIDR\_EL1 at EL1 using AArch64 to EL2.

| PMSIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMSIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMSICR\_EL1, bit [29]

## When FEAT\_SPE is implemented:

Trap

MRS reads of PMSICR\_EL1 at EL1 using AArch64 to EL2.

| PMSICR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMSICR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSICR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMSFCR\_EL1, bit [28]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMSFCR\_EL1 at EL1 using AArch64 to EL2.

| PMSFCR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMSFCR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSFCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMSEVFR\_EL1, bit [27]

## When FEAT\_SPE is implemented:

Trap

MRS reads of PMSEVFR\_EL1 at EL1 using AArch64 to EL2.

| PMSEVFR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of PMSEVFR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSEVFR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PMSCR\_EL1, bit [26]

When FEAT\_SPE is implemented:

Trap MRS reads of PMSCR\_EL1 at EL1 using AArch64 to EL2.

| PMSCR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of PMSCR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMSCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMBSR\_EL1, bit [25]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMBSR\_EL1 at EL1 using AArch64 to EL2.

| PMBSR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of PMBSR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMBSR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMBPTR\_EL1, bit [24]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMBPTR\_EL1 at EL1 using AArch64 to EL2.

| PMBPTR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMBPTR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMBPTR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMBLIMITR\_EL1, bit [23]

## When FEAT\_SPE is implemented:

Trap MRS reads of PMBLIMITR\_EL1 at EL1 using AArch64 to EL2.

| PMBLIMITR_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of PMBLIMITR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMBLIMITR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMMIR\_EL1, bit [22]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMMIR\_EL1 at EL1 using AArch64 to EL2.

| PMMIR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of PMMIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PMMIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [21:20]

Reserved, RES0.

## PMSELR\_EL0, bit [19]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMSELR\_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMSELR at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| PMSELR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of PMSELR_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMSELR at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1          | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of PMSELR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of PMSELR at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

## The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMOVS, bit [18]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads and MRC reads of any of the following System registers to EL2:

- At EL1 and EL0 using AArch64: PMOVSCLR\_EL0 and PMOVSSET\_EL0.
- At EL0 using AArch32 when EL1 is using AArch64: PMOVSR and PMOVSSET.

| PMOVS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | MRS reads at EL1 and EL0 using AArch64 and MRC reads at EL0 using AArch32 of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1     | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads at EL1 and EL0 using AArch64 of any of the specified AArch64 System registers are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads at EL0 using AArch32 when EL1 is using AArch64 of any of the specified AArch32 System registers are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMINTEN, bit [17]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- PMINTENCLR\_EL1.
- PMINTENSET\_EL1.

| PMINTEN   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMCNTEN,bit [16]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads and MRC reads of any of the following System registers to EL2:

- At EL1 and EL0 using AArch64: PMCNTENCLR\_EL0 and PMCNTENSET\_EL0.
- At EL0 using AArch32 when EL1 is using AArch64: PMCNTENCLR and PMCNTENSET.

| PMCNTEN   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads at EL1 and EL0 using AArch64 and MRC reads at EL0 using AArch32 of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads at EL1 and EL0 using AArch64 of any of the specified AArch64 System registers are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads at EL0 using AArch32 when EL1 is using AArch64 of any of the specified AArch32 System registers are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMCCNTR\_EL0, bit [15]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMCCNTR\_EL0 at EL1 and EL0 using AArch64 and MRC and MRRC reads of PMCCNTR at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| PMCCNTR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of PMCCNTR_EL0 at EL1 and EL0 using AArch64 and MRC and MRRC reads of PMCCNTRat EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of PMCCNTR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of PMCCNTRat EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . • MRRC reads of PMCCNTRat EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x04 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMCCFILTR\_EL0, bit [14]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads of PMCCFILTR\_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMCCFILTR at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| PMCCFILTR_EL0   | Meaning                                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of PMCCFILTR_EL0 at EL1 and EL0 using AArch64 and MRC reads of PMCCFILTR at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                    |
| 0b1             | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception:                |
|                 | • MRS reads of PMCCFILTR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of PMCCFILTR at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

PMCCFILTR\_EL0 can also be accessed in AArch64 state using PMXEVTYPER\_EL0 when PMSELR\_EL0.SEL == 31, and PMCCFILTR can also be accessed in AArch32 state using PMXEVTYPER when PMSELR.SEL == 31.

Setting this field to 1 has no effect on accesses to PMXEVTYPER\_EL0 and PMXEVTYPER, regardless of the value of PMSELR\_EL0.SEL or PMSELR.SEL.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMEVTYPERn\_EL0, bit [13]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads and MRC reads of any of the following System registers to EL2:

- At EL1 and EL0 using AArch64: PMEVTYPER&lt;n&gt;\_EL0 and PMXEVTYPER\_EL0.
- At EL0 using AArch32 when EL1 is using AArch64: PMEVTYPER&lt;n&gt; and PMXEVTYPER.

| PMEVTYPERn_EL0   | Meaning                                                                                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | MRS reads at EL1 and EL0 using AArch64 and MRC reads at EL0 using AArch32 of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                    |
| 0b1              | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception:                                                                                    |
|                  | • MRS reads at EL1 and EL0 using AArch64 of any of the specified AArch64 System registers are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads at EL0 using AArch32 when EL1 is using AArch64 of any of the specified AArch32 System registers are trapped to EL2 and reported with EC syndrome value 0x03 . |

Regardless of the value of this field, for each value n:

- If event counter n is not implemented, the following accesses are UNDEFINED:
- In AArch64 state, a read of PMEVTYPER&lt;n&gt;\_EL0, or, if n is not 31, a read of PMXEVTYPER\_EL0 when PMSELR\_EL0.SEL == n.
- In AArch32 state, a read of PMEVTYPER&lt;n&gt;, or, if n is not 31, a read of PMXEVTYPER when PMSELR.SEL == n.
- If event counter n is implemented, n is greater-than-or-equal-to MDCR\_EL2.HPMN, and EL2 is implemented and enabled in the current Security state, the following generate a Trap exception to EL2 from EL0 or EL1:
- In AArch64 state, a read of PMEVTYPER&lt;n&gt;\_EL0, or a read of PMXEVTYPER\_EL0 when PMSELR\_EL0.SEL == n, reported with EC syndrome value 0x18 .
- In AArch32 state, a read of PMEVTYPER&lt;n&gt;, or a read of PMXEVTYPER when PMSELR.SEL == n, reported with EC syndrome value 0x03 .

## See also HDFGRTR\_EL2.PMCCFILTR\_EL0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMEVCNTRn\_EL0, bit [12]

## When FEAT\_PMUv3 is implemented:

Trap MRS reads and MRC reads of any of the following System registers to EL2:

- At EL1 and EL0 using AArch64: PMEVCNTR&lt;n&gt;\_EL0 and PMXEVCNTR\_EL0.
- At EL0 using AArch32 when EL1 is using AArch64: PMEVCNTR&lt;n&gt; and PMXEVCNTR.

| PMEVCNTRn_EL0   | Meaning                                                                                                                                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads at EL1 and EL0 using AArch64 and MRC reads at EL0 using AArch32 of the specified System registers are not trapped by this mechanism.                                                                                                 |
| 0b1             | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: |

Regardless of the value of this field, for each value n:

- If event counter n is not implemented, the following accesses are UNDEFINED:
- In AArch64 state, a read of PMEVCNTR&lt;n&gt;\_EL0, or a read of PMXEVCNTR\_EL0 when PMSELR\_EL0.SEL is n.
- In AArch32 state, a read of PMEVCNTR&lt;n&gt;, or a read of PMXEVCNTR when PMSELR.SEL is n.
- If event counter n is implemented, n is greater than or equal to MDCR\_EL2.HPMN, and EL2 is implemented and enabled in the current Security state, the following generate a Trap exception to EL2 from EL0 or EL1:
- In AArch64 state, a read of PMEVCNTR&lt;n&gt;\_EL0, or a read of PMXEVCNTR\_EL0 when PMSELR\_EL0.SEL is n, reported with EC syndrome value 0x18 .
- In AArch32 state, a read of PMEVCNTR&lt;n&gt;, or a read of PMXEVCNTR when PMSELR.SEL is n, reported with EC syndrome value 0x03 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## OSDLR\_EL1, bit [11]

## When FEAT\_DoubleLock is implemented:

Trap MRS reads of OSDLR\_EL1 at EL1 using AArch64 to EL2.

| OSDLR_EL1   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| 0b0         | MRS reads of OSDLR_EL1 are not trapped by this mechanism. |

| OSDLR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of OSDLR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## OSECCR\_EL1, bit [10]

Trap MRS reads of OSECCR\_EL1 at EL1 using AArch64 to EL2.

| OSECCR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of OSECCR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of OSECCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## OSLSR\_EL1, bit [9]

Trap MRS reads of OSLSR\_EL1 at EL1 using AArch64 to EL2.

| OSLSR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of OSLSR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of OSLSR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [8]

Reserved, RES0.

## DBGPRCR\_EL1, bit [7]

Trap MRS reads of DBGPRCR\_EL1 at EL1 using AArch64 to EL2.

| DBGPRCR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of DBGPRCR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGPRCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGAUTHSTATUS\_EL1, bit [6]

Trap MRS reads of DBGAUTHSTATUS\_EL1 at EL1 using AArch64 to EL2.

| DBGAUTHSTATUS_EL1   | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                 | MRS reads of DBGAUTHSTATUS_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1                 | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGAUTHSTATUS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGCLAIM, bit [5]

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- DBGCLAIMCLR\_EL1.
- DBGCLAIMSET\_EL1.

| DBGCLAIM   | Meaning                                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## MDSCR\_EL1, bit [4]

Trap MRS reads of MDSCR\_EL1 at EL1 using AArch64 to EL2.

| MDSCR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of MDSCR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of MDSCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGWVRn\_EL1, bit [3]

Trap MRS reads of DBGWVR&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| DBGWVRn_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of DBGWVR<n>_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGWVR<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If watchpoint n is not implemented, a read of DBGWVR&lt;n&gt;\_EL1 is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGWCRn\_EL1, bit [2]

Trap MRS reads of DBGWCR&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| DBGWCRn_EL1   | Meaning                                                       |
|---------------|---------------------------------------------------------------|
| 0b0           | MRS reads of DBGWCR<n>_EL1 are not trapped by this mechanism. |

| DBGWCRn_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGWCR<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If watchpoint n is not implemented, a read of DBGWCR&lt;n&gt;\_EL1 is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGBVRn\_EL1, bit [1]

Trap MRS reads of DBGBVR&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| DBGBVRn_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of DBGBVR<n>_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGBVR<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If breakpoint n is not implemented, a read of DBGBVR&lt;n&gt;\_EL1 is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DBGBCRn\_EL1, bit [0]

Trap MRS reads of DBGBCR&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| DBGBCRn_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of DBGBCR<n>_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DBGBCR<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

If breakpoint n is not implemented, a read of DBGBCR&lt;n&gt;\_EL1 is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HDFGRTR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HDFGRTR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1D0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HDFGRTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HDFGRTR_EL2;
```

MSR HDFGRTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1D0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else HDFGRTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HDFGRTR_EL2 = X[t, 64];
```