## G8.2.172 VTCR, Virtualization Translation Control Register

The VTCR characteristics are:

## Purpose

The control register for stage 2 of the Non-secure PL1&amp;0 translation regime.

Note

This stage of translation always uses the Long-descriptor translation table format.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register VTCR bits [31:0] are architecturally mapped to AArch64 System register VTCR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to VTCR are UNDEFINED.

## Attributes

VTCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES1.

## Bits [30:29]

Reserved, RES0.

## HWU62, bit [28]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[62] of the stage 2 translation table Block or Page entry.

| HWU62   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[62] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[62] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU61, bit [27]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[61] of the stage 2 translation table Block or Page entry.

| HWU61   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[61] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[61] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU60, bit [26]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[60] of the stage 2 translation table Block or Page entry.

| HWU60   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[60] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[60] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HWU59, bit [25]

## When FEAT\_HPDS2 is implemented:

Hardware Use. Indicates IMPLEMENTATION DEFINED hardware use of bit[59] of the stage 2 translation table Block or Page entry.

| HWU59   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Bit[59] of each stage 2 translation table Block or Page entry cannot be used by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1     | Bit[59] of each stage 2 translation table Block or Page entry can be used by hardware for an IMPLEMENTATION DEFINED purpose.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [24:14]

Reserved, RES0.

## SH0, bits [13:12]

Shareability attribute for memory associated with translation table walks using VTTBR.

| SH0   | Meaning          |
|-------|------------------|
| 0b00  | Non-shareable.   |
| 0b10  | Outer Shareable. |
| 0b11  | Inner Shareable. |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ORGN0, bits [11:10]

Outer cacheability attribute for memory associated with translation table walks using VTTBR.

| ORGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN0, bits [9:8]

Inner cacheability attribute for memory associated with translation table walks using VTTBR.

| IRGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SL0, bits [7:6]

Starting level for translation table walks using VTTBR.

| SL0   | Meaning          |
|-------|------------------|
| 0b00  | Start at level 2 |
| 0b01  | Start at level 1 |

All other values are reserved. If this field is programmed to a reserved value, or to a value that is not consistent with the programming of T0SZ, then a stage 2 level 1 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## S, bit [4]

Sign extension bit. This bit must be programmed to the value of T0SZ[3]. If it is not, then the stage 2 T0SZ value is treated as an UNKNOWN value

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T0SZ, bits [3:0]

The size offset of the memory region addressed by VTTBR. The region size is 2 (32-T0SZ) bytes.

This field holds a four-bit signed integer value, meaning it supports values from -8 to 7.

Note

This is different from the other translation control registers, where TnSZ holds a three-bit unsigned integer, supporting values from 0 to 7.

If this field is programmed to a value that is not consistent with the programming of SL0 then a stage 2 level 1 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VTCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0010 | 0b0001 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = VTCR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = VTCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0010 | 0b0001 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then VTCR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else VTCR = R[t];
```