## D24.2.198 TCRMASK\_EL2, Translation Control Masking Register (EL2)

The TCRMASK\_EL2 characteristics are:

## Purpose

Mask register to prevent updates of fields in TCR\_EL2 on writes.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TCRMASK\_EL2 are UNDEFINED.

## Attributes

TCRMASK\_EL2 is a 64-bit register.

## Field descriptions

When !ELIsInHost(EL2):

<!-- image -->

## Bits [63:34]

Reserved, RES0.

## MTX, bit [33]

## When FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented or FEAT\_MTE\_CANONICAL\_TAGS is implemented:

Mask bit for MTX.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| MTX   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.MTX is writeable.     |
| 0b1   | TCR_EL2.MTX is not writeable. |

## Otherwise:

Reserved, RES0.

DS, bit [32]

## When FEAT\_LPA2 is implemented:

Mask bit for DS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [31]

Reserved, RES0.

## TCMA,bit [30]

## When FEAT\_MTE2 is implemented:

Mask bit for TCMA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBID, bit [29]

## When FEAT\_PAuth is implemented:

Mask bit for TBID.

| DS   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.DS is writeable.     |
| 0b1  | TCR_EL2.DS is not writeable. |

| TCMA   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.TCMA is writeable.     |
| 0b1    | TCR_EL2.TCMA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU62, bit [28]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU62.

| HWU62   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.HWU62 is writeable.     |
| 0b1     | TCR_EL2.HWU62 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU61, bit [27]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU61.

| HWU61   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.HWU61 is writeable.     |
| 0b1     | TCR_EL2.HWU61 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

| TBID   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.TBID is writeable.     |
| 0b1    | TCR_EL2.TBID is not writeable. |

## HWU60, bit [26]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU60.

| HWU60   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.HWU60 is writeable.     |
| 0b1     | TCR_EL2.HWU60 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU59, bit [25]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU59.

| HWU59   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.HWU59 is writeable.     |
| 0b1     | TCR_EL2.HWU59 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPD, bit [24]

## When FEAT\_HPDS is implemented:

Mask bit for HPD.

The reset behavior of this field is:

| HPD   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.HPD is writeable.     |
| 0b1   | TCR_EL2.HPD is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## HD, bit [22]

## When FEAT\_HAFDBS is implemented:

Mask bit for HD.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HA, bit [21]

## When FEAT\_HAFDBS is implemented:

Mask bit for HA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBI, bit [20]

Mask bit for TBI.

| HD   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.HD is writeable.     |
| 0b1  | TCR_EL2.HD is not writeable. |

| HA   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.HA is writeable.     |
| 0b1  | TCR_EL2.HA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [19:17]

Reserved, RES0.

## PS, bit [16]

Mask bit for PS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [15]

Reserved, RES0.

## TG0, bit [14]

Mask bit for TG0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

| TBI   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.TBI is writeable.     |
| 0b1   | TCR_EL2.TBI is not writeable. |

| PS   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.PS is writeable.     |
| 0b1  | TCR_EL2.PS is not writeable. |

| TG0   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.TG0 is writeable.     |
| 0b1   | TCR_EL2.TG0 is not writeable. |

## SH0, bit [12]

Mask bit for SH0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## ORGN0, bit [10]

Mask bit for ORGN0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## IRGN0, bit [8]

Mask bit for IRGN0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .

| SH0   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.SH0 is writeable.     |
| 0b1   | TCR_EL2.SH0 is not writeable. |

| ORGN0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.ORGN0 is writeable.     |
| 0b1     | TCR_EL2.ORGN0 is not writeable. |

| IRGN0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.IRGN0 is writeable.     |
| 0b1     | TCR_EL2.IRGN0 is not writeable. |

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [7:1]

Reserved, RES0.

## T0SZ, bit [0]

Mask bit for T0SZ.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## When ELIsInHost(EL2):

<!-- image -->

## Bits [63:62]

Reserved, RES0.

MTX1, bit [61]

When FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented or FEAT\_MTE\_CANONICAL\_TAGS is implemented:

Mask bit for MTX1.

| T0SZ   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.T0SZ is writeable.     |
| 0b1    | TCR_EL2.T0SZ is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MTX0, bit [60]

## When FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented or FEAT\_MTE\_CANONICAL\_TAGS is implemented:

Mask bit for MTX0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DS, bit [59]

## When FEAT\_LPA2 is implemented:

Mask bit for DS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| MTX1   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.MTX1 is writeable.     |
| 0b1    | TCR_EL2.MTX1 is not writeable. |

| MTX0   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.MTX0 is writeable.     |
| 0b1    | TCR_EL2.MTX0 is not writeable. |

| DS   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.DS is writeable.     |
| 0b1  | TCR_EL2.DS is not writeable. |

## Otherwise:

Reserved, RES0.

## TCMA1, bit [58]

## When FEAT\_MTE2 is implemented:

Mask bit for TCMA1.

| TCMA1   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.TCMA1 is writeable.     |
| 0b1     | TCR_EL2.TCMA1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TCMA0, bit [57]

## When FEAT\_MTE2 is implemented:

Mask bit for TCMA0.

| TCMA0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.TCMA0 is writeable.     |
| 0b1     | TCR_EL2.TCMA0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

E0PD1, bit [56]

## When FEAT\_E0PD is implemented:

Mask bit for E0PD1.

| E0PD1   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.E0PD1 is writeable.     |
| 0b1     | TCR_EL2.E0PD1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0PD0, bit [55]

## When FEAT\_E0PD is implemented:

Mask bit for E0PD0.

| E0PD0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.E0PD0 is writeable.     |
| 0b1     | TCR_EL2.E0PD0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NFD1, bit [54]

## When FEAT\_SVE is implemented:

Mask bit for NFD1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

| NFD1   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.NFD1 is writeable.     |
| 0b1    | TCR_EL2.NFD1 is not writeable. |

## NFD0, bit [53]

## When FEAT\_SVE is implemented:

Mask bit for NFD0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBID1, bit [52]

## When FEAT\_PAuth is implemented:

Mask bit for TBID1.

| TBID1   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.TBID1 is writeable.     |
| 0b1     | TCR_EL2.TBID1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBID0, bit [51]

## When FEAT\_PAuth is implemented:

Mask bit for TBID0.

| TBID0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.TBID0 is writeable.     |
| 0b1     | TCR_EL2.TBID0 is not writeable. |

The reset behavior of this field is:

| NFD0   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.NFD0 is writeable.     |
| 0b1    | TCR_EL2.NFD0 is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU162, bit [50]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU162.

| HWU162   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU162 is writeable.     |
| 0b1      | TCR_EL2.HWU162 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU161, bit [49]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU161.

| HWU161   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU161 is writeable.     |
| 0b1      | TCR_EL2.HWU161 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU160, bit [48]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU160.

| HWU160   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU160 is writeable.     |
| 0b1      | TCR_EL2.HWU160 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU159, bit [47]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU159.

| HWU159   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU159 is writeable.     |
| 0b1      | TCR_EL2.HWU159 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU062, bit [46]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU062.

| HWU062   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU062 is writeable.     |
| 0b1      | TCR_EL2.HWU062 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU061, bit [45]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU061.

| HWU061   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU061 is writeable.     |
| 0b1      | TCR_EL2.HWU061 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HWU060, bit [44]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU060.

| HWU060   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU060 is writeable.     |
| 0b1      | TCR_EL2.HWU060 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU059, bit [43]

## When FEAT\_HPDS2 is implemented:

Mask bit for HWU059.

| HWU059   | Meaning                          |
|----------|----------------------------------|
| 0b0      | TCR_EL2.HWU059 is writeable.     |
| 0b1      | TCR_EL2.HWU059 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPD1, bit [42]

## When FEAT\_HPDS is implemented:

Mask bit for HPD1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPD0, bit [41]

## When FEAT\_HPDS is implemented:

Mask bit for HPD0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HD, bit [40]

## When FEAT\_HAFDBS is implemented:

Mask bit for HD.

| HPD1   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.HPD1 is writeable.     |
| 0b1    | TCR_EL2.HPD1 is not writeable. |

| HPD0   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.HPD0 is writeable.     |
| 0b1    | TCR_EL2.HPD0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HA, bit [39]

## When FEAT\_HAFDBS is implemented:

Mask bit for HA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBI1, bit [38]

Mask bit for TBI1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TBI0, bit [37]

Mask bit for TBI0.

| HD   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.HD is writeable.     |
| 0b1  | TCR_EL2.HD is not writeable. |

| HA   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.HA is writeable.     |
| 0b1  | TCR_EL2.HA is not writeable. |

| TBI1   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.TBI1 is writeable.     |
| 0b1    | TCR_EL2.TBI1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AS, bit [36]

Mask bit for AS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [35:33]

Reserved, RES0.

## IPS, bit [32]

Mask bit for IPS.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [31]

Reserved, RES0.

| TBI0   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.TBI0 is writeable.     |
| 0b1    | TCR_EL2.TBI0 is not writeable. |

| AS   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.AS is writeable.     |
| 0b1  | TCR_EL2.AS is not writeable. |

| IPS   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.IPS is writeable.     |
| 0b1   | TCR_EL2.IPS is not writeable. |

## TG1, bit [30]

Mask bit for TG1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [29]

Reserved, RES0.

## SH1, bit [28]

Mask bit for SH1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

Bit [27]

Reserved, RES0.

## ORGN1, bit [26]

Mask bit for ORGN1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .

| TG1   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.TG1 is writeable.     |
| 0b1   | TCR_EL2.TG1 is not writeable. |

| SH1   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.SH1 is writeable.     |
| 0b1   | TCR_EL2.SH1 is not writeable. |

| ORGN1   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.ORGN1 is writeable.     |
| 0b1     | TCR_EL2.ORGN1 is not writeable. |

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [25]

Reserved, RES0.

## IRGN1, bit [24]

Mask bit for IRGN1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EPD1, bit [23]

Mask bit for EPD1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## A1, bit [22]

Mask bit for A1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| IRGN1   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.IRGN1 is writeable.     |
| 0b1     | TCR_EL2.IRGN1 is not writeable. |

| EPD1   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.EPD1 is writeable.     |
| 0b1    | TCR_EL2.EPD1 is not writeable. |

| A1   | Meaning                      |
|------|------------------------------|
| 0b0  | TCR_EL2.A1 is writeable.     |
| 0b1  | TCR_EL2.A1 is not writeable. |

## Bits [21:17]

Reserved, RES0.

## T1SZ, bit [16]

Mask bit for T1SZ.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [15]

Reserved, RES0.

## TG0, bit [14]

Mask bit for TG0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## SH0, bit [12]

Mask bit for SH0.

The reset behavior of this field is:

| T1SZ   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.T1SZ is writeable.     |
| 0b1    | TCR_EL2.T1SZ is not writeable. |

| TG0   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.TG0 is writeable.     |
| 0b1   | TCR_EL2.TG0 is not writeable. |

| SH0   | Meaning                       |
|-------|-------------------------------|
| 0b0   | TCR_EL2.SH0 is writeable.     |
| 0b1   | TCR_EL2.SH0 is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## ORGN0, bit [10]

Mask bit for ORGN0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## IRGN0, bit [8]

Mask bit for IRGN0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EPD0, bit [7]

Mask bit for EPD0.

The reset behavior of this field is:

| ORGN0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.ORGN0 is writeable.     |
| 0b1     | TCR_EL2.ORGN0 is not writeable. |

| IRGN0   | Meaning                         |
|---------|---------------------------------|
| 0b0     | TCR_EL2.IRGN0 is writeable.     |
| 0b1     | TCR_EL2.IRGN0 is not writeable. |

| EPD0   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.EPD0 is writeable.     |
| 0b1    | TCR_EL2.EPD0 is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [6:1]

Reserved, RES0.

## T0SZ, bit [0]

Mask bit for T0SZ.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing TCRMASK\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name TCRMASK\_EL2 or TCRMASK\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TCRMASK\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0111 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TCRMASK_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TCRMASK_EL2;
```

| T0SZ   | Meaning                        |
|--------|--------------------------------|
| 0b0    | TCR_EL2.T0SZ is writeable.     |
| 0b1    | TCR_EL2.T0SZ is not writeable. |

MSR TCRMASK\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0111 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsZero(EffectiveTCRMASK_EL2()) then UNDEFINED; else TCRMASK_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TCRMASK_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, TCRMASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nTCRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x330]; else X[t, 64] = TCRMASK_EL1;
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TCRMASK_EL2; else X[t, 64] = TCRMASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCRMASK_EL1;
```

MSR TCRMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nTCRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x330] = X[t, 64]; elsif !IsZero(EffectiveTCRMASK_EL1()) then UNDEFINED; else TCRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveTCRMASK_EL2()) then UNDEFINED; else TCRMASK_EL2 = X[t, 64]; else TCRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCRMASK_EL1 = X[t, 64];
```