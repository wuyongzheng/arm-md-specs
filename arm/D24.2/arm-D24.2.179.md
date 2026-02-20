## D24.2.179 SCTLRMASK\_EL2, System Control Masking Register (EL2)

The SCTLRMASK\_EL2 characteristics are:

## Purpose

Mask register to prevent updates of fields in SCTLR\_EL2 on writes.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCTLRMASK\_EL2 are UNDEFINED.

## Attributes

SCTLRMASK\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## TIDCP, bit [63]

## When FEAT\_TIDCP1 is implemented:

Mask bit for TIDCP.

| TIDCP   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.TIDCP is writeable.     |
| 0b1     | SCTLR_EL2.TIDCP is not writeable. |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SPINTMASK, bit [62]

## When FEAT\_NMI is implemented:

Mask bit for SPINTMASK.

| SPINTMASK   | Meaning                               |
|-------------|---------------------------------------|
| 0b0         | SCTLR_EL2.SPINTMASK is writeable.     |
| 0b1         | SCTLR_EL2.SPINTMASK is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NMI, bit [61]

## When FEAT\_NMI is implemented:

Mask bit for NMI.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EnTP2, bit [60]

## When FEAT\_SME is implemented:

Mask bit for EnTP2.

| NMI   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.NMI is writeable.     |
| 0b1   | SCTLR_EL2.NMI is not writeable. |

| EnTP2   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.EnTP2 is writeable.     |
| 0b1     | SCTLR_EL2.EnTP2 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TCSO, bit [59]

## When FEAT\_MTE\_STORE\_ONLY is implemented:

Mask bit for TCSO.

| TCSO   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.TCSO is writeable.     |
| 0b1    | SCTLR_EL2.TCSO is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TCSO0, bit [58]

## When FEAT\_MTE\_STORE\_ONLY is implemented:

Mask bit for TCSO0.

| TCSO0   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.TCSO0 is writeable.     |
| 0b1     | SCTLR_EL2.TCSO0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EPAN, bit [57]

## When FEAT\_PAN3 is implemented:

Mask bit for EPAN.

| EPAN   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.EPAN is writeable.     |
| 0b1    | SCTLR_EL2.EPAN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnALS, bit [56]

## When FEAT\_LS64 is implemented:

Mask bit for EnALS.

| EnALS   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.EnALS is writeable.     |
| 0b1     | SCTLR_EL2.EnALS is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnAS0, bit [55]

## When FEAT\_LS64\_ACCDATA is implemented:

Mask bit for EnAS0.

| EnAS0   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.EnAS0 is writeable.     |
| 0b1     | SCTLR_EL2.EnAS0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnASR, bit [54]

## When FEAT\_LS64\_V is implemented:

Mask bit for EnASR.

| EnASR   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.EnASR is writeable.     |
| 0b1     | SCTLR_EL2.EnASR is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [53:47]

Reserved, RES0.

## TWEDEL,bit [46]

## When FEAT\_TWED is implemented:

Mask bit for TWEDEL.

| TWEDEL   | Meaning                            |
|----------|------------------------------------|
| 0b0      | SCTLR_EL2.TWEDEL is writeable.     |
| 0b1      | SCTLR_EL2.TWEDEL is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWEDEn, bit [45]

## When FEAT\_TWED is implemented:

Mask bit for TWEDEn.

| TWEDEn   | Meaning                            |
|----------|------------------------------------|
| 0b0      | SCTLR_EL2.TWEDEn is writeable.     |
| 0b1      | SCTLR_EL2.TWEDEn is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DSSBS, bit [44]

## When FEAT\_SSBS is implemented:

Mask bit for DSSBS.

| DSSBS   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.DSSBS is writeable.     |
| 0b1     | SCTLR_EL2.DSSBS is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATA, bit [43]

## When FEAT\_MTE2 is implemented:

Mask bit for ATA.

The reset behavior of this field is:

| ATA   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.ATA is writeable.     |
| 0b1   | SCTLR_EL2.ATA is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATA0, bit [42]

## When FEAT\_MTE2 is implemented:

Mask bit for ATA0.

| ATA0   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.ATA0 is writeable.     |
| 0b1    | SCTLR_EL2.ATA0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [41]

Reserved, RES0.

## TCF, bit [40]

## When FEAT\_MTE2 is implemented:

Mask bit for TCF.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [39]

Reserved, RES0.

| TCF   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.TCF is writeable.     |
| 0b1   | SCTLR_EL2.TCF is not writeable. |

## TCF0, bit [38]

## When FEAT\_MTE2 is implemented:

Mask bit for TCF0.

| TCF0   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.TCF0 is writeable.     |
| 0b1    | SCTLR_EL2.TCF0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ITFSB, bit [37]

## When FEAT\_MTE\_ASYNC is implemented:

Mask bit for ITFSB.

| ITFSB   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.ITFSB is writeable.     |
| 0b1     | SCTLR_EL2.ITFSB is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BT, bit [36]

## When FEAT\_BTI is implemented:

Mask bit for BT.

The reset behavior of this field is:

| BT   | Meaning                        |
|------|--------------------------------|
| 0b0  | SCTLR_EL2.BT is writeable.     |
| 0b1  | SCTLR_EL2.BT is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BT0, bit [35]

## When FEAT\_BTI is implemented:

Mask bit for BT0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnFPM, bit [34]

## When FEAT\_FPMR is implemented:

Mask bit for EnFPM.

| EnFPM   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.EnFPM is writeable.     |
| 0b1     | SCTLR_EL2.EnFPM is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

MSCEn, bit [33]

## When FEAT\_MOPS is implemented:

Mask bit for MSCEn.

| BT0   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.BT0 is writeable.     |
| 0b1   | SCTLR_EL2.BT0 is not writeable. |

| MSCEn   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.MSCEn is writeable.     |
| 0b1     | SCTLR_EL2.MSCEn is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CMOW,bit [32]

## When FEAT\_CMOWis implemented:

Mask bit for CMOW.

| CMOW   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.CMOW is writeable.     |
| 0b1    | SCTLR_EL2.CMOW is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EnIA, bit [31]

## When FEAT\_PAuth is implemented:

Mask bit for EnIA.

| EnIA   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.EnIA is writeable.     |
| 0b1    | SCTLR_EL2.EnIA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnIB, bit [30]

## When FEAT\_PAuth is implemented:

Mask bit for EnIB.

| EnIB   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.EnIB is writeable.     |
| 0b1    | SCTLR_EL2.EnIB is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LSMAOE, bit [29]

## When FEAT\_LSMAOC is implemented:

Mask bit for LSMAOE.

| LSMAOE   | Meaning                            |
|----------|------------------------------------|
| 0b0      | SCTLR_EL2.LSMAOE is writeable.     |
| 0b1      | SCTLR_EL2.LSMAOE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTLSMD, bit [28]

## When FEAT\_LSMAOC is implemented:

Mask bit for nTLSMD.

| nTLSMD   | Meaning                            |
|----------|------------------------------------|
| 0b0      | SCTLR_EL2.nTLSMD is writeable.     |
| 0b1      | SCTLR_EL2.nTLSMD is not writeable. |

The reset behavior of this field is:

## EE, bit [25]

## When FEAT\_MixedEnd is implemented:

Mask bit for EE.

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnDA, bit [27]

## When FEAT\_PAuth is implemented:

Mask bit for EnDA.

| EnDA   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.EnDA is writeable.     |
| 0b1    | SCTLR_EL2.EnDA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UCI, bit [26]

Mask bit for UCI.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| UCI   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.UCI is writeable.     |
| 0b1   | SCTLR_EL2.UCI is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0E, bit [24]

## When FEAT\_MixedEndEL0 is implemented:

Mask bit for E0E.

| E0E   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.E0E is writeable.     |
| 0b1   | SCTLR_EL2.E0E is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SPAN, bit [23]

Mask bit for SPAN.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EIS, bit [22]

| EE   | Meaning                        |
|------|--------------------------------|
| 0b0  | SCTLR_EL2.EE is writeable.     |
| 0b1  | SCTLR_EL2.EE is not writeable. |

| SPAN   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.SPAN is writeable.     |
| 0b1    | SCTLR_EL2.SPAN is not writeable. |

## When FEAT\_ExS is implemented:

Mask bit for EIS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IESB, bit [21]

## When FEAT\_IESB is implemented:

Mask bit for IESB.

| IESB   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.IESB is writeable.     |
| 0b1    | SCTLR_EL2.IESB is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TSCXT, bit [20]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Mask bit for TSCXT.

| EIS   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.EIS is writeable.     |
| 0b1   | SCTLR_EL2.EIS is not writeable. |

| TSCXT   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | SCTLR_EL2.TSCXT is writeable.     |
| 0b1     | SCTLR_EL2.TSCXT is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## WXN,bit [19]

Mask bit for WXN.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## nTWE, bit [18]

Mask bit for nTWE.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

Bit [17]

Reserved, RES0.

## nTWI, bit [16]

Mask bit for nTWI.

The reset behavior of this field is:

| WXN   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.WXN is writeable.     |
| 0b1   | SCTLR_EL2.WXN is not writeable. |

| nTWE   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.nTWE is writeable.     |
| 0b1    | SCTLR_EL2.nTWE is not writeable. |

| nTWI   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.nTWI is writeable.     |
| 0b1    | SCTLR_EL2.nTWI is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## UCT, bit [15]

Mask bit for UCT.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DZE, bit [14]

Mask bit for DZE.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EnDB, bit [13]

## When FEAT\_PAuth is implemented:

Mask bit for EnDB.

| EnDB   | Meaning                          |
|--------|----------------------------------|
| 0b0    | SCTLR_EL2.EnDB is writeable.     |
| 0b1    | SCTLR_EL2.EnDB is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| UCT   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.UCT is writeable.     |
| 0b1   | SCTLR_EL2.UCT is not writeable. |

| DZE   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.DZE is writeable.     |
| 0b1   | SCTLR_EL2.DZE is not writeable. |

## Otherwise:

Reserved, RES0.

## I, bit [12]

Mask bit for I.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EOS, bit [11]

## When FEAT\_ExS is implemented:

Mask bit for EOS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnRCTX, bit [10]

## When FEAT\_SPECRES is implemented:

Mask bit for EnRCTX.

| EnRCTX   | Meaning                            |
|----------|------------------------------------|
| 0b0      | SCTLR_EL2.EnRCTX is writeable.     |
| 0b1      | SCTLR_EL2.EnRCTX is not writeable. |

The reset behavior of this field is:

| I   | Meaning                       |
|-----|-------------------------------|
| 0b0 | SCTLR_EL2.I is writeable.     |
| 0b1 | SCTLR_EL2.I is not writeable. |

| EOS   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.EOS is writeable.     |
| 0b1   | SCTLR_EL2.EOS is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [9]

Reserved, RES0.

## SED, bit [8]

## When FEAT\_AA32EL0 is implemented:

Mask bit for SED.

| SED   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.SED is writeable.     |
| 0b1   | SCTLR_EL2.SED is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ITD, bit [7]

## When FEAT\_AA32EL0 is implemented:

Mask bit for ITD.

| ITD   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.ITD is writeable.     |
| 0b1   | SCTLR_EL2.ITD is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nAA, bit [6]

Mask bit for nAA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CP15BEN, bit [5]

## When FEAT\_AA32EL0 is implemented:

Mask bit for CP15BEN.

| CP15BEN   | Meaning                             |
|-----------|-------------------------------------|
| 0b0       | SCTLR_EL2.CP15BEN is writeable.     |
| 0b1       | SCTLR_EL2.CP15BEN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SA0, bit [4]

Mask bit for SA0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SA, bit [3]

Mask bit for SA.

| nAA   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.nAA is writeable.     |
| 0b1   | SCTLR_EL2.nAA is not writeable. |

| SA0   | Meaning                         |
|-------|---------------------------------|
| 0b0   | SCTLR_EL2.SA0 is writeable.     |
| 0b1   | SCTLR_EL2.SA0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## C, bit [2]

Mask bit for C.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## A, bit [1]

Mask bit for A.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## M, bit [0]

Mask bit for M.

| SA   | Meaning                        |
|------|--------------------------------|
| 0b0  | SCTLR_EL2.SA is writeable.     |
| 0b1  | SCTLR_EL2.SA is not writeable. |

| C   | Meaning                       |
|-----|-------------------------------|
| 0b0 | SCTLR_EL2.C is writeable.     |
| 0b1 | SCTLR_EL2.C is not writeable. |

| A   | Meaning                       |
|-----|-------------------------------|
| 0b0 | SCTLR_EL2.A is writeable.     |
| 0b1 | SCTLR_EL2.A is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing SCTLRMASK\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name SCTLRMASK\_EL2 or SCTLRMASK\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SCTLRMASK_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCTLRMASK_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLRMASK_EL2;
```

MSR SCTLRMASK\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b000 |

| M   | Meaning                       |
|-----|-------------------------------|
| 0b0 | SCTLR_EL2.M is writeable.     |
| 0b1 | SCTLR_EL2.M is not writeable. |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsZero(EffectiveSCTLRMASK_EL2()) then UNDEFINED; else SCTLRMASK_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLRMASK_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, SCTLRMASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nSCTLRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x318]; else X[t, 64] = SCTLRMASK_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then
```

```
X[t, 64] = SCTLRMASK_EL2; else X[t, 64] = SCTLRMASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLRMASK_EL1;
```

MSR SCTLRMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nSCTLRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x318] = X[t, 64]; elsif !IsZero(EffectiveSCTLRMASK_EL1()) then UNDEFINED; else SCTLRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveSCTLRMASK_EL2()) then UNDEFINED; else SCTLRMASK_EL2 = X[t, 64]; else SCTLRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLRMASK_EL1 = X[t, 64];
```