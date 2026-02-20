## D24.2.57 GPTBR\_EL3, Granule Protection Table Base Register

The GPTBR\_EL3 characteristics are:

## Purpose

The control register for Granule Protection Table base address.

## Configuration

This register is present only when FEAT\_RME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GPTBR\_EL3 are UNDEFINED.

## Attributes

GPTBR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:44]

Reserved, RES0.

## BADDR[43:40], bits [43:40]

## When FEAT\_RME\_GPC3 is implemented:

Extension to BADDR[39:0]. This field represents bit [55:52] of the level 0 GPT base address.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BADDR, bits [39:0]

Base address for the level 0 GPT.

This field represents bits [51:12] of the level 0 GPT base address.

The level 0 GPT is aligned in memory to the greater of:

- The size of the level 0 GPT in bytes.
- 4KB.

Bits [x:0] of the base address are treated as zero, where:

- x = Max(pps - l0gptsz + 2, 11)
- pps is derived from GPCCR\_EL3.PPS as follows:

| GPCCR_EL3.PPS   |   pps |
|-----------------|-------|
| 0b000           |    32 |
| 0b001           |    36 |
| 0b010           |    40 |
| 0b011           |    42 |
| 0b100           |    44 |
| 0b101           |    48 |
| 0b110           |    52 |

- l0gptsz is derived from GPCCR\_EL3.L0GPTSZ as follows:

| GPCCR_EL3.L0GPTSZ   |   l0gptsz |
|---------------------|-----------|
| 0b0000              |        30 |
| 0b0100              |        34 |
| 0b0110              |        36 |
| 0b1001              |        39 |

If x is greater than 11, then BADDR[x - 12:0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing GPTBR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GPTBR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_RME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = GPTBR_EL3;
```

MSR GPTBR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_RME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.GPTBR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else GPTBR_EL3 = X[t, 64];
```