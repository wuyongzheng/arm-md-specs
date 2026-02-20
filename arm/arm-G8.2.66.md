## G8.2.66 HCR2, Hyp Configuration Register 2

The HCR2 characteristics are:

## Purpose

Provides additional configuration controls for virtualization.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HCR2 bits [31:0] are architecturally mapped to AArch64 System register HCR\_EL2[63:32].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HCR2 are UNDEFINED.

## Attributes

HCR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:23]

Reserved, RES0.

## TTLBIS, bit [22]

## When FEAT\_EVT is implemented:

Trap TLB maintenance instructions that operate on the Inner Shareable domain. Traps execution of the following TLB maintenance instructions at EL1 to EL2:

TLBIALLIS, TLBIASIDIS, TLBIMVAAIS, TLBIMVAALIS, TLBIMVAIS, and TLBIMVALIS

| TTLBIS   | Meaning                                                                                   |
|----------|-------------------------------------------------------------------------------------------|
| 0b0      | This control does not cause any instructions to be trapped.                               |
| 0b1      | Non-secure EL1 execution of the specified TLB maintenance instructions is trapped to EL2. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [21]

Reserved, RES0.

## TOCU, bit [20]

## When FEAT\_EVT is implemented:

Trap cache maintenance instructions that operate to the Point of Unification. Traps execution of DCCMV AU, ICIALLU, and ICIMVAU at EL1 to EL2.

| TOCU   | Meaning                                                                                 |
|--------|-----------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                             |
| 0b1    | Non-secure execution of the specified cache maintenance instructions is trapped to EL2. |

If the Point of Unification is before any level of data cache, it is IMPLEMENTATION DEFINED whether the execution of any data or unified cache clean by V A to the Point of Unification instruction can be trapped when the value of this control is 1.

If the Point of Unification is before any level of instruction cache, it is IMPLEMENTATION DEFINED whether the execution of any instruction cache invalidate to the Point of Unification instruction can be trapped when the value of this control is 1.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [19]

Reserved, RES0.

## TICAB, bit [18]

## When FEAT\_EVT is implemented:

Trap ICIALLUIS cache maintenance instructions. Traps execution of those cache maintenance instructions at EL1 to EL2.

This applies to the following instructions:

ICIALLUIS.

| TICAB   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped. |

| TICAB   | Meaning                                                                                     |
|---------|---------------------------------------------------------------------------------------------|
| 0b1     | Non-secure EL1 execution of the specified cache maintenance instructions is trapped to EL2. |

If the Point of Unification is before any level of instruction cache, it is IMPLEMENTATION DEFINED whether the execution of any instruction cache invalidate to the Point of Unification instruction can be trapped when the value of this control is 1.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TID4, bit [17]

## When FEAT\_EVT is implemented:

Trap ID group 4. Traps the following register accesses to EL2:

- EL1 reads of CCSIDR, CCSIDR2, CLIDR, and CSSELR.
- EL1 writes to CSSELR.

| TID4   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                               |
| 0b1    | The specified Non-secure EL1 and EL0 accesses to ID group 4 registers are trapped to EL2. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:6]

Reserved, RES0.

## TEA, bit [5]

## When FEAT\_RAS is implemented:

Route synchronous External abort exceptions from EL0 and EL1 to EL2.

| TEA   | Meaning                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------|
| 0b0   | Does not route synchronous External abort exceptions from Non-secure EL0 and EL1 to EL2.              |
| 0b1   | Route synchronous External abort exceptions from Non-secure EL0 and EL1 to EL2, if not routed to EL3. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TERR, bit [4]

## When FEAT\_RAS is implemented:

Trap Error record accesses from EL1 to EL2. Traps MRC or MCR accesses, reported using EC syndrome value 0x03 , and MRRC or MCRR accesses, reported using EC syndrome value 0x04 , to the following registers from EL1 to EL2:

ERRIDR, ERRSELR, ERXADDR, ERXADDR2, ERXCTLR, ERXCTLR2, ERXFR, ERXFR2, ERXMISC0, ERXMISC1, ERXMISC2, ERXMISC3, and ERXSTATUS.

When FEAT\_RASv1p1 is implemented, ERXMISC4, ERXMISC5, ERXMISC6, and ERXMISC7.

| TERR   | Meaning                                                                        |
|--------|--------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                    |
| 0b1    | Accesses to the specified registers from EL1 generate a Trap exception to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [3:2]

Reserved, RES0.

## ID, bit [1]

Stage 2 Instruction access cacheability disable. For the Non-secure PL1&amp;0 translation regime, when HCR.VM==1, this control forces all stage 2 translations for instruction accesses to Normal memory to be Non-cacheable.

| ID   | Meaning                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This control has no effect on stage 2 of the Non-secure PL1&0 translation regime.                                                           |
| 0b1  | For the Non-secure PL1&0 translation regime, forces all stage 2 translations for instruction accesses to Normal memory to be Non-cacheable. |

This bit has no effect on the EL2 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CD, bit [0]

Stage 2 Data access cacheability disable. When HCR.VM==1, this forces all stage 2 translations for data accesses and translation table walks to Normal memory to be Non-cacheable for the Non-secure PL1&amp;0 translation regime.

| CD   | Meaning                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This control has no effect on stage 2 of the Non-secure PL1&0 translation regime for data accesses and translation table walks.                                  |
| 0b1  | For the Non-secure PL1&0 translation regime, forces all stage 2 translations for data accesses and translation table walks to Normal memory to be Non-cacheable. |

This bit has no effect on the EL2 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HCR2

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HCR2; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HCR2;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HCR2 = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HCR2 = R[t];
```