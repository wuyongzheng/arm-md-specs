## D24.4.11 TRCACATR&lt;n&gt;, Trace Address Comparator Access Type Register &lt;n&gt;, n = 0 - 15

The TRCACATR&lt;n&gt; characteristics are:

## Purpose

Defines the type of access for the corresponding TRCACVR&lt;n&gt; Register. This register configures the context type, Exception levels, alignment, masking that is applied by the Address Comparator, and how the Address Comparator behaves when it is one half of an Address Range Comparator.

## Configuration

AArch64 System register TRCACATR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCACATR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and (UInt(TRCIDR4.NUMACPAIRS) * 2) &gt; n. Otherwise, direct accesses to TRCACATR&lt;n&gt; are UNDEFINED.

## Attributes

TRCACATR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:19]

Reserved, RES0.

EXLEVEL\_RL\_EL2, bit [18]

## When FEAT\_RME is implemented:

Realm EL2 address comparison control. Controls whether a comparison can occur at EL2 in Realm state.

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator performs comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator does not perform comparisons in Realm EL2. |

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator does not perform comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator performs comparisons in Realm EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL1, bit [17]

## When FEAT\_RME is implemented:

Realm EL1 address comparison control. Controls whether a comparison can occur at EL1 in Realm state.

| EXLEVEL_RL_EL1   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator performs comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator does not perform comparisons in Realm EL1. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator does not perform comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator performs comparisons in Realm EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL0, bit [16]

## When FEAT\_RME is implemented:

Realm EL0 address comparison control. Controls whether a comparison can occur at EL0 in Realm state.

| EXLEVEL_RL_EL0   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator performs comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator does not perform comparisons in Realm EL0. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator does not perform comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator performs comparisons in Realm EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [15]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [14]

## When Non-secure EL2 is implemented:

Non-secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Non-secure state.

| EXLEVEL_NS_EL2   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL2.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL1, bit [13]

## When Non-secure EL1 is implemented:

Non-secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Non-secure state.

| EXLEVEL_NS_EL1   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL1.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL0, bit [12]

## When Non-secure EL0 is implemented:

Non-secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Non-secure state.

| EXLEVEL_NS_EL0   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL0.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL3, bit [11]

## When EL3 is implemented:

EL3 address comparison control. Controls whether a comparison can occur at EL3.

| EXLEVEL_S_EL3   | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons at EL3.         |
| 0b1             | The Address Comparator does not perform comparisons at EL3. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL2, bit [10]

## When Secure EL2 is implemented:

Secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Secure state.

| EXLEVEL_S_EL2   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL2.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL1, bit [9]

## When Secure EL1 is implemented:

Secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Secure state.

| EXLEVEL_S_EL1   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL1.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL0, bit [8]

## When Secure EL0 is implemented:

Secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Secure state.

| EXLEVEL_S_EL0   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL0.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [7]

Reserved, RES0.

CONTEXT, bits [6:4]

When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Selects a Context Identifier Comparator or Virtual Context Identifier Comparator:

| CONTEXT   | Meaning       | Applies when                                            |
|-----------|---------------|---------------------------------------------------------|
| 0b000     | Comparator 0. |                                                         |
| 0b001     | Comparator 1. | UInt(TRCIDR4.NUMCIDC) > 1 or UInt(TRCIDR4.NUMVMIDC) > 1 |
| 0b010     | Comparator 2. | UInt(TRCIDR4.NUMCIDC) > 2 or UInt(TRCIDR4.NUMVMIDC) > 2 |
| 0b011     | Comparator 3. | UInt(TRCIDR4.NUMCIDC) > 3 or UInt(TRCIDR4.NUMVMIDC) > 3 |
| 0b100     | Comparator 4. | UInt(TRCIDR4.NUMCIDC) > 4 or UInt(TRCIDR4.NUMVMIDC) > 4 |
| 0b101     | Comparator 5. | UInt(TRCIDR4.NUMCIDC) > 5 or UInt(TRCIDR4.NUMVMIDC) > 5 |
| 0b110     | Comparator 6. | UInt(TRCIDR4.NUMCIDC) > 6 or UInt(TRCIDR4.NUMVMIDC) > 6 |
| 0b111     | Comparator 7. | UInt(TRCIDR4.NUMCIDC) > 7 or UInt(TRCIDR4.NUMVMIDC) > 7 |

The width of this field is dependent on the maximum number of Context Identifier Comparators or Virtual Context Identifier Comparators implemented. Unimplemented bits are RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CONTEXTTYPE, bits [3:2]

## When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Controls whether the Address Comparator is dependent on a Context Identifier Comparator, a Virtual Context Identifier Comparator, or both comparisons.

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                              | Applies when               |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 0b00          | The Address Comparator is not dependent on the Context Identifier Comparators or Virtual Context Identifier Comparators.                                                                                                                             |                            |
| 0b01          | The Address Comparator is dependent on the Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Context Identifier Comparator and the address comparison match.                 | TRCIDR4.NUMCIDC != '0000'  |
| 0b10          | The Address Comparator is dependent on the Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Virtual Context Identifier Comparator and the address comparison match. | TRCIDR4.NUMVMIDC != '0000' |

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                                                                                               | Applies when                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b11          | The Address Comparator is dependent on the Context Identifier Comparator and Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if the Context Identifier Comparator, the Virtual Context Identifier Comparator, and address comparison all match. | TRCIDR4.NUMCIDC != '0000' and TRCIDR4.NUMVMIDC != '0000' |

If TRCIDR4.NUMCIDC == 0b0000 , then bit [2] is RES0.

If TRCIDR4.NUMVMIDC == 0b0000 , then bit [3] is RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [1:0]

Reserved, RES0.

## Accessing TRCACATR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCBBCTLR.RANGE[n/2] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0100 and TRCRSCTLR&lt;a&gt;.SAC[n] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0101 and TRCRSCTLR&lt;a&gt;.ARC[n/2] == 1.
- TRCVIIECTLR.EXCLUDE[n/2] == 1.
- TRCVIIECTLR.INCLUDE[n/2] == 1.
- TRCVISSCTLR.START[n] == 1.
- TRCVISSCTLR.STOP[n] == 1.
- TRCSSCCR&lt;&gt;.ARC[n/2] == 1.
- TRCSSCCR&lt;&gt;.SAC[n] == 1.
- TRCQCTLR.RANGE[n/2] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCACATR<m> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b01 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then
```

```
AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCACATR[m];
```

MSR TRCACATR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2        |
|-------|-------|--------|-------------|------------|
| 0b10  | 0b001 | 0b0010 | m[2:0]: 0b0 | 0b01 :m[3] |

```
integer m = UInt(op2<0>:CRm<3:1>); if m >= NUM_TRACE_ADDRESS_COMPARATOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCACATR[m] = X[t, 64];
```
