## D24.4.54 TRCRSCTLR&lt;n&gt;, Trace Resource Selection Control Register &lt;n&gt;, n = 2 - 31

The TRCRSCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the selection of the resources in the trace unit.

## Configuration

Resource selector 0 always returns FALSE.

Resource selector 1 always returns TRUE.

Resource selectors are implemented in pairs. Each odd numbered resource selector is part of a pair with the even numbered resource selector that is numbered as one less than it. For example, resource selectors 2 and 3 form a pair.

AArch64 System register TRCRSCTLR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCRSCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and ((UInt(TRCIDR4.NUMRSPAIR) + 1) * 2) &gt; n. Otherwise, direct accesses to TRCRSCTLR&lt;n&gt; are UNDEFINED.

## Attributes

TRCRSCTLR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:22]

Reserved, RES0.

## PAIRINV, bit [21]

When (n MOD 2) == 0:

Controls whether the combined result from a resource selector pair is inverted.

| PAIRINV   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0       | Do not invert the combined output of the 2 resource selectors. |
| 0b1       | Invert the combined output of the 2 resource selectors.        |

If:

- Ais the register TRCRSCTLR&lt;n&gt;.
- Bis the register TRCRSCTLR&lt;n+1&gt;.

Then the combined output of the 2 resource selectors A and B depends on the value of (A.PAIRINV , A.INV , B.INV) as follows:

- 0b000 -&gt; A and B.
- 0b001 -&gt; Reserved.
- 0b010 -&gt; not(A) and B.
- 0b011 -&gt; not(A) and not(B).
- 0b100 -&gt; not(A) or not(B).
- 0b101 -&gt; not(A) or B.
- 0b110 -&gt; Reserved.
- 0b111 -&gt; A or B.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## INV, bit [20]

Controls whether the resource, that TRCRSCTLR&lt;n&gt;.GROUP and TRCRSCTLR&lt;n&gt;.SELECT selects, is inverted.

| INV   | Meaning                                    |
|-------|--------------------------------------------|
| 0b0   | Do not invert the output of this selector. |
| 0b1   | Invert the output of this selector.        |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## GROUP, bits [19:16]

Selects a group of resources.

| GROUP   | Meaning                                 | SELECT                                                     |
|---------|-----------------------------------------|------------------------------------------------------------|
| 0b0000  | External Input Selectors.               | SELECT encoding for External Input Selectors               |
| 0b0001  | PE Comparator Inputs.                   | SELECT encoding for PE Comparator Inputs                   |
| 0b0010  | Counters and Sequencer.                 | SELECT encoding for Counters and Sequencer                 |
| 0b0011  | Single-shot Comparator Controls.        | SELECT encoding for Single-shot Comparator Controls        |
| 0b0100  | Single Address Comparators.             | SELECT encoding for Single Address Comparators             |
| 0b0101  | Address Range Comparators.              | SELECT encoding for Address Range Comparators              |
| 0b0110  | Context Identifier Comparators.         | SELECT encoding for Context Identifier Comparators         |
| 0b0111  | Virtual Context Identifier Comparators. | SELECT encoding for Virtual Context Identifier Comparators |

All other values are reserved.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT, bits [15:0]

Resource Specific Controls. Contains the controls specific to the resource group selected by GROUP, described in the following sections.

## SELECT encoding for External Input Selectors

<!-- image -->

| EXTIN[<m>]   | Meaning           |
|--------------|-------------------|
| 0b0          | Ignore EXTIN <m>. |
| 0b1          | Select EXTIN <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMEXTINSEL.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for PE Comparator Inputs

<!-- image -->

## Bits [15:8]

Reserved, RES0.

PECOMP[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs.

## Bits [15:4]

Reserved, RES0.

## EXTIN[&lt;m&gt;] , bits [m], for m = 3 to 0

Selects one or more External Inputs.

## Bits [15:8]

Reserved, RES0.

## SEQUENCER[&lt;m&gt;] , bits [m+4], for m = 3 to 0

Sequencer states.

| PECOMP[<m>]   | Meaning                         |
|---------------|---------------------------------|
| 0b0           | Ignore PE Comparator Input <m>. |
| 0b1           | Select PE Comparator Input <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Counters and Sequencer

<!-- image -->

| SEQUENCER[<m>]   | Meaning                     |
|------------------|-----------------------------|
| 0b0              | Ignore Sequencer state <m>. |
| 0b1              | Select Sequencer state <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMSEQSTATE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

COUNTERS[&lt;m&gt;] , bits [m], for m = 3 to 0

Counters resources at zero.

## Bits [15:8]

Reserved, RES0.

## SINGLE\_SHOT[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Single-shot Comparator Controls.

| SINGLE_SHOT[<m>]   | Meaning                                    |
|--------------------|--------------------------------------------|
| 0b0                | Ignore Single-shot Comparator Control <m>. |
| 0b1                | Select Single-shot Comparator Control <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMSSCC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single Address Comparators

| COUNTERS[<m>]   | Meaning                     |
|-----------------|-----------------------------|
| 0b0             | Ignore Counter <m>.         |
| 0b1             | Select Counter <m> is zero. |

This bit is RES0 if m &gt;= TRCIDR5.NUMCNTR.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single-shot Comparator Controls

<!-- image -->

## Bits [15:8]

Reserved, RES0.

ARC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Address Range Comparators.

| ARC[<m>]   | Meaning                              |
|------------|--------------------------------------|
| 0b0        | Ignore Address Range Comparator <m>. |
| 0b1        | Select Address Range Comparator <m>. |

<!-- image -->

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators.

| SAC[<m>]   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | Ignore Single Address Comparator <m>. |
| 0b1        | Select Single Address Comparator <m>. |

This bit is RES0 if m &gt;= 2 × TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Address Range Comparators

<!-- image -->

This bit is RES0 if m &gt;= TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

## CID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Context Identifier Comparators.

| CID[<m>]   | Meaning                                   |
|------------|-------------------------------------------|
| 0b0        | Ignore Context Identifier Comparator <m>. |
| 0b1        | Select Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMCIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Virtual Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

VMID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Virtual Context Identifier Comparators.

| VMID[<m>]   | Meaning                                           |
|-------------|---------------------------------------------------|
| 0b0         | Ignore Virtual Context Identifier Comparator <m>. |
| 0b1         | Select Virtual Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMVMIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCRSCTLR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n/2.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n/2.
- TRCEVENTCTL0R.EVENT0.TYPE == 0 and TRCEVENTCTL0R.EVENT0.SEL == n.
- TRCEVENTCTL0R.EVENT0.TYPE == 1 and TRCEVENTCTL0R.EVENT0.SEL == n/2.
- TRCEVENTCTL0R.EVENT1.TYPE == 0 and TRCEVENTCTL0R.EVENT1.SEL == n.
- TRCEVENTCTL0R.EVENT1.TYPE == 1 and TRCEVENTCTL0R.EVENT1.SEL == n/2.
- TRCEVENTCTL0R.EVENT2.TYPE == 0 and TRCEVENTCTL0R.EVENT2.SEL == n.
- TRCEVENTCTL0R.EVENT2.TYPE == 1 and TRCEVENTCTL0R.EVENT2.SEL == n/2.
- TRCEVENTCTL0R.EVENT3.TYPE == 0 and TRCEVENTCTL0R.EVENT3.SEL == n.
- TRCEVENTCTL0R.EVENT3.TYPE == 1 and TRCEVENTCTL0R.EVENT3.SEL == n/2.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 0 and TRCSEQEVR&lt;a&gt;.B.SEL = n.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 1 and TRCSEQEVR&lt;a&gt;.B.SEL = n/2.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 0 and TRCSEQEVR&lt;a&gt;.F.SEL = n.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 1 and TRCSEQEVR&lt;a&gt;.F.SEL = n/2.
- TRCSEQRSTEVR.RST.TYPE == 0 and TRCSEQRSTEVR.RST.SEL == n.
- TRCSEQRSTEVR.RST.TYPE == 1 and TRCSEQRSTEVR.RST.SEL == n/2.
- TRCTSCTLR.EVENT.TYPE == 0 and TRCTSCTLR.EVENT.SEL == n.
- TRCTSCTLR.EVENT.TYPE == 1 and TRCTSCTLR.EVENT.SEL == n/2.
- TRCVICTLR.EVENT.TYPE == 0 and TRCVICTLR.EVENT.SEL == n.
- TRCVICTLR.EVENT.TYPE == 1 and TRCVICTLR.EVENT.SEL == n/2.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCRSCTLR<m> ; Where m = 2-31
```

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b0001 | m[3:0] | 0b00 :m[4] |

```
integer m = UInt(op2<0>:CRm<3:0>); if m >= NUM_TRACE_RESOURCE_SELECTOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED;
```

```
elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCRSCTLR[m];
```

MSR TRCRSCTLR&lt;m&gt;, &lt;Xt&gt; ; Where m = 2-31

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b0001 | m[3:0] | 0b00 :m[4] |

```
integer m = UInt(op2<0>:CRm<3:0>); if m >= NUM_TRACE_RESOURCE_SELECTOR_PAIRS * 2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCRSCTLR[m] = X[t, 64];
```
