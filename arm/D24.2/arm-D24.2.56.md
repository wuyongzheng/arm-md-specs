## D24.2.56 GPCCR\_EL3, Granule Protection Check Control Register (EL3)

The GPCCR\_EL3 characteristics are:

## Purpose

The control register for Granule Protection Checks.

## Configuration

This register is present only when FEAT\_RME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GPCCR\_EL3 are UNDEFINED.

## Attributes

GPCCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:30]

Reserved, RES0.

## GPCBW, bit [29]

## When FEAT\_RME\_GPC3 is implemented:

GPC Bypass Window Enable.

This field governs the behavior of the GPC bypass windows.

| GPCBW   | Meaning                          |
|---------|----------------------------------|
| 0b0     | GPC bypass windows are disabled. |
| 0b1     | GPC bypass windows are enabled.  |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NA7, bit [28]

## When FEAT\_RME\_GDI is implemented:

No access 7.

This field governs the behavior of the GPI encoding for NA7.

| NA7   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b0   | GPI encoding value of 0b0111 is reserved.                         |
| 0b1   | GPI encoding value of 0b0111 is No access permitted from this PE. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NA6, bit [27]

## When FEAT\_RME\_GDI is implemented:

No access 6.

This field governs the behavior of the GPI encoding for NA6.

| NA6   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b0   | GPI encoding value of 0b0110 is reserved.                         |
| 0b1   | GPI encoding value of 0b0110 is No access permitted from this PE. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSP, bit [26]

## When FEAT\_RME\_GDI is implemented:

Non-secure Protected.

This field governs the behavior of the GPI encoding for NSP.

| NSP   | Meaning                                   |
|-------|-------------------------------------------|
| 0b0   | GPI encoding value of 0b0101 is reserved. |

| NSP   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b1   | GPI encoding value of 0b0101 is No access permitted from this PE. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SA, bit [25]

## When FEAT\_RME\_GDI is implemented:

System Agent.

This field governs the behavior of the GPI encoding for SA.

| SA   | Meaning                                                           |
|------|-------------------------------------------------------------------|
| 0b0  | GPI encoding value of 0b0100 is reserved.                         |
| 0b1  | GPI encoding value of 0b0100 is No access permitted from this PE. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APPSAA, bit [24]

## When FEAT\_RME\_GPC2 is implemented:

Above PPS All Access. This field governs the behavior of memory accesses to Secure, Realm and Root PA space, for physical addresses above the range configured by GPCCR\_EL3.PPS.

| APPSAA   | Meaning                                                                                                                  |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses to addresses above the configured PPS must be to Non-secure PA space, otherwise they generate a GPF at level 0. |
| 0b1      | Accesses to addresses above the configured PPS, to any PA space, do not generate a GPF because of this control.          |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## L0GPTSZ, bits [23:20]

Level 0 GPT entry size.

This field advertises the number of least-significant address bits protected by each entry in the level 0 GPT.

| L0GPTSZ   | Meaning                                            |
|-----------|----------------------------------------------------|
| 0b0000    | 30-bits. Each entry covers 1GB of address space.   |
| 0b0100    | 34-bits. Each entry covers 16GB of address space.  |
| 0b0110    | 36-bits. Each entry covers 64GB of address space.  |
| 0b1001    | 39-bits. Each entry covers 512GB of address space. |

All other values are reserved.

Access to this field is RO.

## NSO, bit [19]

## When FEAT\_RME\_GPC2 is implemented:

Non-secure Only. This field governs the behavior of the GPI encoding for NSO.

| NSO   | Meaning                                   |
|-------|-------------------------------------------|
| 0b0   | GPI encoding value of 0b1101 is reserved. |
| 0b1   | GPI encoding value of 0b1101 is NSO.      |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TBGPCD, bit [18]

## When FEAT\_TRBE\_EXT is implemented:

Trace Buffer Granule Protection Check Disabled. Controls whether the Trace Buffer Unit accepts or rejects trace when Granule Protection Checks are disabled.

| TBGPCD   | Meaning                                                      |
|----------|--------------------------------------------------------------|
| 0b0      | The Trace Buffer Unit rejects trace when GPCCR_EL3.GPC is 0. |
| 0b1      | The Trace Buffer Unit accepts trace when GPCCR_EL3.GPC is 0. |

When the Trace Buffer Unit rejects trace, the trace might remain buffered by the trace unit until the Trace Buffer Unit is able to accept trace. When the Trace Buffer Unit accepts trace, the Trace Buffer Unit writes the trace to memory.

## Note

Setting GPCCR\_EL3.{TBGPCD, GPC} to {1, 0} means that the Trace Buffer Unit might write to memory without any Granule Protection Checks. The addresses that the Trace Buffer Unit writes to can be programmed by an external agent. The physical address spaces the Trace Buffer Unit can address are restricted by an IMPLEMENTATION DEFINED debug authentication interface.

Setting GPCCR\_EL3.{TBGPCD, GPC} to {1, 1} means that GPCCR\_EL3.{TBGPCD, GPC} will become {1, 0} on a Warm reset.

This field is ignored by the PE and treated as one when any of the following are true:

- GPCCR\_EL3.GPC == 1.
- ExternalRootInvasiveDebugEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## GPCP, bit [17]

Granule Protection Check Priority.

This control governs behavior of granule protection checks on fetches of stage 2 Table descriptors.

| GPCP   | Meaning                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | GPC faults are all reported with a priority that is consistent with the GPC being performed on any access to physical address space.                                                                                                                         |
| 0b1    | AGPCfault for the fetch of a Table descriptor for a stage 2 translation table walk might not be generated or reported. All other GPC faults are reported with a priority consistent with the GPC being performed on all accesses to physical address spaces. |

This bit is permitted to be cached in a TLB.

An implementation is permitted to treat this field as RES0, with an Effective value of 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GPC, bit [16]

Granule Protection Check Enable.

| GPC   | Meaning                                                                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Granule protection checks are disabled. Accesses are not prevented by this mechanism.                                                                                        |
| 0b1   | All accesses to physical address spaces are subject to granule protection checks, except for fetches of GPT information and accesses governed by the GPCCR_EL3.GPCP control. |

If any stage of translation is enabled, this bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PGS, bits [15:14]

Physical Granule size.

All other values are reserved.

The value of this field is permitted to be cached in a TLB.

Granule sizes not supported for stage 1 and not supported for stage 2, as defined in ID\_AA64MMFR0\_EL1, are reserved. For example, if ID\_AA64MMFR0\_EL1.TGran16 == 0b0000 and ID\_AA64MMFR0\_EL1.TGran16\_2 == 0b0001 , then the PGS encoding 0b10 is reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [13:12]

GPT fetch Shareability attribute

All other values are reserved.

Fetches of GPT information are made with the Shareability attribute that is configured in this field.

If both ORGN and IRGN are configured with Non-cacheable attributes, it is invalid to configure this field to any value other than 0b10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

| PGS   | Meaning   |
|-------|-----------|
| 0b00  | 4KB.      |
| 0b01  | 64KB.     |
| 0b10  | 16KB.     |

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

## ORGN, bits [11:10]

GPT fetch Outer cacheability attribute.

| ORGN   | Meaning                                                                       |
|--------|-------------------------------------------------------------------------------|
| 0b00   | Normal memory, Outer Non-cacheable.                                           |
| 0b01   | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10   | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11   | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

Fetches of GPT information are made with the Outer cacheability attributes configured in this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN, bits [9:8]

GPT fetch Inner cacheability attribute.

| IRGN   | Meaning                                                                       |
|--------|-------------------------------------------------------------------------------|
| 0b00   | Normal memory, Inner Non-cacheable.                                           |
| 0b01   | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10   | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11   | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

Fetches of GPT information are made with the Inner cacheability attributes configured in this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SPAD, bit [7]

## When FEAT\_RME\_GPC2 is implemented:

Secure PA space Disable. This field controls access to the Secure PA space.

| SPAD   | Meaning                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on accesses.                                                                                       |
| 0b1    | When granule protection checks are enabled, access to the Secure Physical Address space generates a Granule Protection fault. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSPAD, bit [6]

## When FEAT\_RME\_GPC2 is implemented:

Non-secure PA space Disable. This field controls access to the Non-secure PA space.

| NSPAD   | Meaning                                                                                                                           |
|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control has no effect on accesses.                                                                                           |
| 0b1     | When granule protection checks are enabled, access to the Non-secure Physical Address space generates a Granule Protection fault. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLPAD, bit [5]

## When FEAT\_RME\_GPC2 is implemented:

Realm PA space Disable. This field controls access to the Realm PA space.

| RLPAD   | Meaning                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control has no effect on accesses.                                                                                      |
| 0b1     | When granule protection checks are enabled, access to the Realm Physical Address space generates a Granule Protection fault. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [4]

Reserved, RES0.

## PPS3, bit [3]

## When FEAT\_RME\_GPC3 is implemented:

This field extends GPCCR\_EL3.PPS[2:0], creating a GPCCR\_EL3.PPS[3:0] field.

For a description of the values derived by evaluating PPS, see GPCCR\_EL3.PPS[2:0].

The value of this field is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PPS, bits [2:0]

## When FEAT\_RME\_GPC3 is implemented:

Protected Physical Address Size.

The size of the memory region protected by GPTBR\_EL3, in terms of the number of least-significant address bits.

This field is evaluated with PPS3, as {PPS3, PPS} to give PPS[3:0], interpreted as:

| PPS[3:0]   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0000     | 32 bits, 4GB protected address space.   |
| 0b0001     | 36 bits, 64GB protected address space.  |
| 0b0010     | 40 bits, 1TB protected address space.   |
| 0b0011     | 42 bits, 4TB protected address space.   |
| 0b0100     | 44 bits, 16TB protected address space.  |
| 0b1000     | 46 bits, 64TB protected address space.  |
| 0b1001     | 47 bits, 128TB protected address space. |
| 0b0101     | 48 bits, 256TB protected address space. |
| 0b0110     | 52 bits, 4PB protected address space.   |
| 0b0111     | 56 bits, 64PB protected address space.  |

All other values are reserved.

Configuration of this field to a value exceeding the implemented physical address size is invalid.

The value of this field is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Protected Physical Address Size.

The size of the memory region protected by GPTBR\_EL3, in terms of the number of least-significant address bits.

| PPS   | Meaning                                |
|-------|----------------------------------------|
| 0b000 | 32 bits, 4GB protected address space.  |
| 0b001 | 36 bits, 64GB protected address space. |

All other values are reserved.

Configuration of this field to a value exceeding the implemented physical address size is invalid.

The value of this field is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing GPCCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b110 |

if !(IsFeatureImplemented(FEAT\_RME) &amp;&amp;

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = GPCCR\_EL3;

MSR GPCCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_RME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then
```

IsFeatureImplemented(FEAT\_AA64)) then

| PPS   | Meaning                                 |
|-------|-----------------------------------------|
| 0b010 | 40 bits, 1TB protected address space.   |
| 0b011 | 42 bits, 4TB protected address space.   |
| 0b100 | 44 bits, 16TB protected address space.  |
| 0b101 | 48 bits, 256TB protected address space. |
| 0b110 | 52 bits, 4PB protected address space.   |

```
if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.GPCCR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else GPCCR_EL3 = X[t, 64];
```