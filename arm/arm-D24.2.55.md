## D24.2.55 GPCBW\_EL3, Granule Protection Check Bypass Window Register (EL3)

The GPCBW\_EL3 characteristics are:

## Purpose

The control register for Granule Protection Check bypass window.

## Configuration

This register is present only when FEAT\_RME\_GPC3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GPCBW\_EL3 are UNDEFINED.

## Attributes

GPCBW\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:40]

Reserved, RES0.

## BWSIZE, bits [39:37]

GPC Bypass Window Size.

BWSIZE defines the size of the GPC bypass memory region.

| BWSIZE   | Meaning                          |
|----------|----------------------------------|
| 0b000    | 30 bits, 1GB GPC bypass window.  |
| 0b001    | 31 bits, 2GB GPC bypass window.  |
| 0b010    | 32 bits, 4GB GPC bypass window.  |
| 0b100    | 34 bits, 16GB GPC bypass window. |
| 0b110    | 36 bits, 64GB GPC bypass window. |

All other values are reserved.

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

· On a Warm reset, this field resets to an architecturally UNKNOWN value.

## BWSTRIDE, bits [36:32]

GPC Bypass Window Stride.

BWSTRIDE allows creating multiple GPC bypass memory regions in the memory map across a specific stride.

| BWSTRIDE   | Meaning           |
|------------|-------------------|
| 0b00000    | 1TB stride.       |
| 0b00010    | 4TB stride.       |
| 0b00100    | 16TB stride.      |
| 0b00110    | 64TB stride.      |
| 0b00111    | 128TB stride.     |
| 0b01000    | 256TB stride.     |
| 0b01001    | 512TB stride.     |
| 0b01010    | 1PB stride.       |
| 0b10000    | 64PB (No stride). |

All other values are reserved.

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [31:26]

Reserved, RES0.

## BWADDR,bits [25:0]

GPC Bypass window address.

This field represents bits [55:30] of the GPC bypass window base address.

The GPC bypass window is:

- Aligned in memory to the size of the window as specified by GPCBW\_EL3.BWSIZE.
- Duplicated in PA space across a stride specified using GPCBW\_EL3.BWSTRIDE.

This means that only bits [gpcbwu:gpcbwl] of a PA are compared against bits [gpcbwu:gpcbwl] of the window base address derived from BWADDR when checking if a PA falls within the range of a window, where:

- gpcbwl is derived from GPCBW\_EL3.BWSIZE as follows:

| BWSIZE   |   gpcbwl |
|----------|----------|
| 0b000    |       30 |
| 0b001    |       31 |
| 0b010    |       32 |
| 0b100    |       34 |
| 0b110    |       36 |

- gpcbwu is derived from GPCBW\_EL3.BWSTRIDE as follows:

| BWSTRIDE   |   gpcbwu |
|------------|----------|
| 0b00000    |       39 |
| 0b00010    |       41 |
| 0b00100    |       43 |
| 0b00110    |       45 |
| 0b00111    |       46 |
| 0b01000    |       47 |
| 0b01001    |       48 |
| 0b01010    |       49 |
| 0b10000    |       55 |

If the base address derived from BWADDR is not aligned to the size programmed in BWSIZE the configuration is invalid.

If this field is configured to a value that produces a GPC bypass window base address that is greater than or equal to the stride value configured by BWSTRIDE, the configuration is invalid.

An access to a PA falls within a GPC bypass window if the pseudocode function PAWithinGPCBypassWindow() returns TRUE.

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing GPCBW\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GPCBW\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_RME_GPC3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = GPCBW_EL3;
```

MSR GPCBW\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_RME_GPC3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.GPCBW_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else GPCBW_EL3 = X[t, 64];
```