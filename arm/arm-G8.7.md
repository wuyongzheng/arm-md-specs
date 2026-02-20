## G8.7 Generic Timer registers

This section lists the Generic Timer registers in AArch32.

## G8.7.1 CNTFRQ, Counter-timer Frequency register

The CNTFRQ characteristics are:

## Purpose

This register is provided so that software can discover the effective frequency of the system counter. It must be programmed with this value as part of system initialization. The value of the register is not interpreted by hardware.

## Configuration

AArch32 System register CNTFRQ bits [31:0] are architecturally mapped to AArch64 System register CNTFRQ\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTFRQ are UNDEFINED.

## Attributes

CNTFRQ is a 32-bit register.

## Field descriptions

```
Clock frequency 31 0
```

## ClockFreq, bits [31:0]

Clock frequency. Indicates the effective frequency of the system counter, in Hz.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTFRQ

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.<EL0PCTEN,EL0VCTEN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PCTEN == '0' && ↪ → CNTKCTL.PL0VCTEN == '0' then
```

```
if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.<EL0PCTEN,EL0VCTEN> == '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else R[t] = CNTFRQ; elsif PSTATE.EL == EL1 then R[t] = CNTFRQ; elsif PSTATE.EL == EL2 then R[t] = CNTFRQ; elsif PSTATE.EL == EL3 then R[t] = CNTFRQ;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then CNTFRQ = R[t]; else UNDEFINED;
```

## G8.7.2 CNTHCTL, Counter-timer Hyp Control register

The CNTHCTL characteristics are:

## Purpose

Controls the generation of an event stream from the physical counter, and access from Non-secure EL1 modes to the physical counter and the Non-secure EL1 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register CNTHCTL bits [31:0] are architecturally mapped to AArch64 System register CNTHCTL\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to CNTHCTL are UNDEFINED.

## Attributes

CNTHCTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

EVNTIS, bit [17]

## When FEAT\_ECV is implemented:

Controls the scale of the generation of the event stream.

| EVNTIS   | Meaning                                          |
|----------|--------------------------------------------------|
| 0b0      | The CNTHCTL.EVNTI field applies to CNTPCT[15:0]. |
| 0b1      | The CNTHCTL.EVNTI field applies to CNTPCT[23:8]. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:8]

Reserved, RES0.

## EVNTI, bits [7:4]

Selects which bit of CNTPCT, as seen from EL2, is the trigger for the event stream generated from that counter when that stream is enabled.

If FEAT\_ECV is implemented, and CNTHCTL.EVNTIS is 1, this field selects a trigger bit in the range 8 to 23 of CNTPCT.

Otherwise, this field selects a trigger bit in the range 0 to 15 of CNTPCT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTDIR, bit [3]

Controls which transition of the CNTPCT trigger bit, as seen from EL2 and defined by EVNTI, generates an event when the event stream is enabled.

| EVNTDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | A0to 1 transition of the trigger bit triggers an event. |
| 0b1       | A1to 0 transition of the trigger bit triggers an event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTEN, bit [2]

Enables the generation of an event stream from CNTPCT as seen from EL2.

| EVNTEN   | Meaning                    |
|----------|----------------------------|
| 0b0      | Disables the event stream. |
| 0b1      | Enables the event stream.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PL1PCEN, bit [1]

Traps Non-secure EL0 and EL1 MRC or MCR accesses, reported using EC syndrome value 0x03 , and MRRC or MCRRaccesses, reported using EC syndrome value 0x04 , to the physical timer registers to Hyp mode.

| PL1PCEN   | Meaning                                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Non-secure EL0 and EL1 accesses to the CNTP_CTL, CNTP_CVAL, and CNTP_TVAL are trapped to Hyp mode, unless trapped by CNTKCTL.PL0PTEN. |
| 0b1       | This control does not cause any instructions to be trapped.                                                                           |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PL1PCTEN, bit [0]

Traps Non-secure EL0 and EL1 MRRC or MCRR accesses, reported using EC syndrome value 0x04 , to the physical counter register to Hyp mode.

| PL1PCTEN   | Meaning                                                                                                          |
|------------|------------------------------------------------------------------------------------------------------------------|
| 0b0        | Non-secure EL0 and EL1 accesses to the CNTPCT are trapped to Hyp mode, unless it is trapped by CNTKCTL.PL0PCTEN. |
| 0b1        | This control does not cause any instructions to be trapped.                                                      |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHCTL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = CNTHCTL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = CNTHCTL;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then CNTHCTL = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else CNTHCTL = R[t];
```

## G8.7.3 CNTHP\_CTL, Counter-timer Hyp Physical Timer Control register

The CNTHP\_CTL characteristics are:

## Purpose

Control register for the Hyp mode physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register CNTHP\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTHP\_CTL\_EL2[31:0].

This register is banked between CNTHP\_CTL and CNTHP\_CTL\_S and CNTHP\_CTL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTHP\_CTL are UNDEFINED.

## Attributes

CNTHP\_CTL is a 32-bit register.

This register has the following instances:

- CNTHP\_CTL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHP\_CTL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHP\_CTL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHP\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_CTL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = CNTHP_CTL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = CNTHP_CTL;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then CNTHP_CTL = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else CNTHP_CTL = R[t];
```

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHPS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHP_CTL_EL2<31:0>; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = CNTP_CTL_S; else R[t] = CNTP_CTL_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = R[t]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CTL_S = R[t]; else CNTP_CTL_NS = R[t];
```

## G8.7.4 CNTHP\_CVAL, Counter-timer Hyp Physical CompareValue register

The CNTHP\_CVAL characteristics are:

## Purpose

Holds the compare value for the Hyp mode physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register CNTHP\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTHP\_CVAL\_EL2[63:0].

This register is banked between CNTHP\_CVAL and CNTHP\_CVAL\_S and CNTHP\_CVAL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTHP\_CVAL are UNDEFINED.

## Attributes

CNTHP\_CVAL is a 64-bit register.

This register has the following instances:

- CNTHP\_CVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHP\_CVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHP\_CVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL2 physical timer CompareValue.

When CNTHP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTHP\_CTL.ISTATUS is set to 1.
- If CNTHP\_CTL.IMASK is 0, an interrupt is generated.

When CNTHP\_CTL.ENABLE is 0, the timer condition is not met, but CNTPCT continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_CVAL

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0110 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then R[t, t2] = CNTHP_CVAL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t, t2] = CNTHP_CVAL;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0110 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then CNTHP_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else CNTHP_CVAL = R[t, t2];
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then
```

```
if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHP_CVAL_EL2; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t, t2] = CNTP_CVAL_S; else R[t, t2] = CNTP_CVAL_NS;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = R[t, t2]; else CNTP_CVAL_NS = R[t, t2];
```

## G8.7.5 CNTHP\_TVAL, Counter-timer Hyp Physical Timer TimerValue register

The CNTHP\_TVAL characteristics are:

## Purpose

Holds the timer value for the Hyp mode physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register CNTHP\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTHP\_TVAL\_EL2[31:0].

This register is banked between CNTHP\_TVAL and CNTHP\_TVAL\_S and CNTHP\_TVAL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTHP\_TVAL are UNDEFINED.

## Attributes

CNTHP\_TVAL is a 32-bit register.

This register has the following instances:

- CNTHP\_TVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHP\_TVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHP\_TVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

TimerValue

31

0

## TimerValue, bits [31:0]

The TimerValue view of the EL2 physical timer.

On a read of this register:

- If CNTHP\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHP\_CTL.ENABLE is 1, the value returned is (CNTHP\_CVAL - CNTPCT).

On a write of this register, CNTHP\_CV AL is set to (CNTPCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CNTHP\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHP\_CTL.ISTATUS is set to 1.
- If CNTHP\_CTL.IMASK is 0, an interrupt is generated.

When CNTHP\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_TVAL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then if CNTHP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHP_CVAL -PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else if CNTHP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHP_CVAL -PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then CNTHP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else CNTHP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt();
```

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHPS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>; elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS -PhysicalCountInt())<31:0>; else if CNTP_CTL_S.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then
```

```
if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then if CNTP_CTL_S.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.6 CNTHPS\_CTL, Counter-timer Secure Physical Timer Control Register (EL2)

The CNTHPS\_CTL characteristics are:

## Purpose

Provides AArch32 access from EL0 to the Secure EL2 physical timer.

## Configuration

AArch32 System register CNTHPS\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTHPS\_CTL\_EL2[31:0].

This register is banked between CNTHPS\_CTL and CNTHPS\_CTL\_S and CNTHPS\_CTL\_NS.

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHPS\_CTL are UNDEFINED.

## Attributes

CNTHPS\_CTL is a 32-bit register.

This register has the following instances:

- CNTHPS\_CTL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHPS\_CTL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHPS\_CTL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the CNTHPS\_CTL.ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the CNTHPS\_CTL.ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHPS\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_CTL

This register is accessed using the encoding for CNTP\_CTL.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHPS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHP_CTL_EL2<31:0>; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = CNTP_CTL_S; else R[t] = CNTP_CTL_NS;
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = R[t]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t];
```

```
elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CTL_S = R[t]; else CNTP_CTL_NS = R[t];
```

## G8.7.7 CNTHPS\_CVAL, Counter-timer Secure Physical Timer CompareValue Register (EL2)

The CNTHPS\_CVAL characteristics are:

## Purpose

Provides AArch32 access from EL0 to the compare value for the Secure EL2 physical timer.

## Configuration

AArch32 System register CNTHPS\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTHPS\_CVAL\_EL2[63:0].

This register is banked between CNTHPS\_CVAL and CNTHPS\_CVAL\_S and CNTHPS\_CVAL\_NS.

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHPS\_CVAL are UNDEFINED.

## Attributes

CNTHPS\_CVAL is a 64-bit register.

This register has the following instances:

- CNTHPS\_CVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHPS\_CVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHPS\_CVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

| 63           | 32           |              |
|--------------|--------------|--------------|
| CompareValue | CompareValue | CompareValue |
| 31           | 0            |              |
| CompareValue | CompareValue | CompareValue |

## CompareValue, bits [63:0]

Holds the EL2 physical timer CompareValue.

When CNTHPS\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTHPS\_CTL.ISTATUS is set to 1.
- If CNTHPS\_CTL.IMASK is 0, an interrupt is generated.

When CNTHPS\_CTL.ENABLE is 0, the timer condition is not met, but CNTPCT continues to count

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_CVAL

This register is accessed using the encoding for CNTP\_CV AL.

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHP_CVAL_EL2; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL;
```

```
elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t, t2] = CNTP_CVAL_S; else R[t, t2] = CNTP_CVAL_NS;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2];
```

```
else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = R[t, t2]; else CNTP_CVAL_NS = R[t, t2];
```

## G8.7.8 CNTHPS\_TVAL, Counter-timer Secure Physical Timer TimerValue Register (EL2)

The CNTHPS\_TVAL characteristics are:

## Purpose

Provides AArch32 access from EL0 to the timer value for the Secure EL2 physical timer.

## Configuration

AArch32 System register CNTHPS\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTHPS\_TVAL\_EL2[31:0].

This register is banked between CNTHPS\_TVAL and CNTHPS\_TVAL\_S and CNTHPS\_TVAL\_NS.

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHPS\_TVAL are UNDEFINED.

## Attributes

CNTHPS\_TVAL is a 32-bit register.

This register has the following instances:

- CNTHPS\_TVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTHPS\_TVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTHPS\_TVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

TimerValue

31

0

## TimerValue, bits [31:0]

The TimerValue view of the EL2 physical timer.

On a read of this register:

- If CNTHPS\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHPS\_CTL.ENABLE is 1, the value returned is (CNTHPS\_CVAL - CNTPCT).

On a write of this register, CNTHPS\_CVAL is set to (CNTPCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHPS\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CNTHPS\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHPS\_CTL.ISTATUS is set to 1.
- If CNTHPS\_CTL.IMASK is 0, an interrupt is generated.

When CNTHPS\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_TVAL

This register is accessed using the encoding for CNTP\_TV AL.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHPS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>; elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS -PhysicalCountInt())<31:0>; else if CNTP_CTL_S.ENABLE == '0' then
```

```
R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then if CNTP_CTL_S.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt();
```

```
else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.9 CNTHV\_CTL, Counter-timer Virtual Timer Control register (EL2)

The CNTHV\_CTL characteristics are:

## Purpose

Provides AArch32 access to the control register for the EL2 virtual timer.

## Configuration

AArch32 System register CNTHV\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTHV\_CTL\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_VHE is implemented. Otherwise, direct accesses to CNTHV\_CTL are UNDEFINED.

## Attributes

CNTHV\_CTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHV\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHV\_CTL

This register is accessed using the encoding for CNTV\_CTL.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHVS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHV_CTL_EL2<31:0>; else R[t] = CNTV_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else R[t] = CNTV_CTL; elsif PSTATE.EL == EL2 then R[t] = CNTV_CTL; elsif PSTATE.EL == EL3 then R[t] = CNTV_CTL;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
CNTHVS_CTL_EL2 = R[t]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = R[t]; else CNTV_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else CNTV_CTL = R[t]; elsif PSTATE.EL == EL2 then CNTV_CTL = R[t]; elsif PSTATE.EL == EL3 then CNTV_CTL = R[t];
```

## G8.7.10 CNTHV\_CVAL, Counter-timer Virtual Timer CompareValue register (EL2)

The CNTHV\_CVAL characteristics are:

## Purpose

Provides AArch32 access to the compare value for the EL2 virtual timer.

## Configuration

AArch32 System register CNTHV\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTHV\_CVAL\_EL2[63:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_VHE is implemented. Otherwise, direct accesses to CNTHV\_CVAL are UNDEFINED.

## Attributes

CNTHV\_CVAL is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
|      | 0    |
| 31   |      |

## CompareValue, bits [63:0]

Holds the EL2 virtual timer CompareValue.

When CNTHV\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTHV\_CTL.ISTATUS is set to 1.
- If CNTHV\_CTL.IMASK is 0, an interrupt is generated.

When CNTHV\_CTL.ENABLE is 0, the timer condition is not met, but CNTVCT continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

## Accessing CNTHV\_CVAL

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHV_CVAL_EL2; else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL2 then R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL3 then R[t, t2] = CNTV_CVAL;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = R[t, t2]; else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then CNTV_CVAL = R[t, t2];
```

## G8.7.11 CNTHV\_TVAL, Counter-timer Virtual Timer TimerValue register (EL2)

The CNTHV\_TVAL characteristics are:

## Purpose

Provides AArch32 access to the timer value for the EL2 virtual timer.

## Configuration

AArch32 System register CNTHV\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTHV\_TVAL\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_VHE is implemented. Otherwise, direct accesses to CNTHV\_TVAL are UNDEFINED.

## Attributes

CNTHV\_TVAL is a 32-bit register.

## Field descriptions

## TimerValue, bits [31:0]

The TimerValue view of the EL2 virtual timer.

On a read of this register:

- If CNTHV\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHV\_CTL.ENABLE is 1, the value returned is (CNTHV\_CVAL - CNTVCT).

On a write of this register, CNTHV\_CVAL is set to (CNTVCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHV\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CNTHV\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHV\_CTL.ISTATUS is set to 1.
- If CNTHV\_CTL.IMASK is 0, an interrupt is generated.

When CNTHV\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

## Accessing CNTHV\_TVAL

This register is accessed using the encoding for CNTV\_TV AL.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

31

TimerValue

0

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHVS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>; else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; elsif PSTATE.EL == EL3 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN;
```

```
elsif HaveEL(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; elsif PSTATE.EL == EL3 then
```

```
if HaveEL(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.12 CNTHVS\_CTL, Counter-timer Secure Virtual Timer Control Register (EL2)

The CNTHVS\_CTL characteristics are:

## Purpose

Provides AArch32 access from EL0 to the Secure EL2 virtual timer.

## Configuration

AArch32 System register CNTHVS\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTHVS\_CTL\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHVS\_CTL are UNDEFINED.

## Attributes

CNTHVS\_CTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHVS\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHVS\_CTL

This register is accessed using the encoding for CNTV\_CTL.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHVS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHV_CTL_EL2<31:0>; else R[t] = CNTV_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else R[t] = CNTV_CTL; elsif PSTATE.EL == EL2 then R[t] = CNTV_CTL; elsif PSTATE.EL == EL3 then R[t] = CNTV_CTL;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
CNTHVS_CTL_EL2 = R[t]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = R[t]; else CNTV_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else CNTV_CTL = R[t]; elsif PSTATE.EL == EL2 then CNTV_CTL = R[t]; elsif PSTATE.EL == EL3 then CNTV_CTL = R[t];
```

## G8.7.13 CNTHVS\_CVAL, Counter-timer Secure Virtual Timer CompareValue Register (EL2)

The CNTHVS\_CVAL characteristics are:

## Purpose

Provides AArch32 access to the compare value for the Secure EL2 virtual timer.

## Configuration

AArch32 System register CNTHVS\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTHVS\_CVAL\_EL2[63:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHVS\_CVAL are UNDEFINED.

## Attributes

CNTHVS\_CVAL is a 64-bit register.

## Field descriptions

<!-- image -->

| 63           | 32           |              |
|--------------|--------------|--------------|
| CompareValue | CompareValue | CompareValue |
| 31           | 0            |              |
| CompareValue | CompareValue | CompareValue |

## CompareValue, bits [63:0]

Holds the EL2 virtual timer CompareValue.

When CNTHVS\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTHVS\_CTL.ISTATUS is set to 1.
- If CNTHVS\_CTL.IMASK is 0, an interrupt is generated.

When CNTHVS\_CTL.ENABLE is 0, the timer condition is not met, but CNTVCT continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

## Accessing CNTHVS\_CVAL

This register is accessed using the encoding for CNTV\_CV AL.

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHV_CVAL_EL2; else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL2 then R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL3 then R[t, t2] = CNTV_CVAL;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = R[t, t2]; else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then CNTV_CVAL = R[t, t2];
```

## G8.7.14 CNTHVS\_TVAL, Counter-timer Secure Virtual Timer TimerValue Register (EL2)

The CNTHVS\_TVAL characteristics are:

## Purpose

Provides AArch32 access to the timer value for the Secure EL2 virtual timer.

## Configuration

AArch32 System register CNTHVS\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTHVS\_TVAL\_EL2[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_SEL2 is implemented. Otherwise, direct accesses to CNTHVS\_TVAL are UNDEFINED.

## Attributes

CNTHVS\_TVAL is a 32-bit register.

## Field descriptions

TimerValue

31

## TimerValue, bits [31:0]

The TimerValue view of the EL2 virtual timer.

On a read of this register:

- If CNTHVS\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHVS\_CTL.ENABLE is 1, the value returned is (CNTHVS\_CVAL - CNTVCT).

On a write of this register, CNTHVS\_CVAL is set to (CNTVCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHVS\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CNTHVS\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHVS\_CTL.ISTATUS is set to 1.
- If CNTHVS\_CTL.IMASK is 0, an interrupt is generated.

When CNTHVS\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

## Accessing CNTHVS\_TVAL

This register is accessed using the encoding for CNTV\_TV AL.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

0

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHVS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>; else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; elsif PSTATE.EL == EL3 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN;
```

```
elsif HaveEL(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; elsif PSTATE.EL == EL3 then
```

```
if HaveEL(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.15 CNTKCTL, Counter-timer Kernel Control register

The CNTKCTL characteristics are:

## Purpose

Controls the generation of an event stream from the virtual counter, and access from EL0 modes to the physical counter, virtual counter, EL1 physical timers, and the virtual timer.

## Configuration

AArch32 System register CNTKCTL bits [31:0] are architecturally mapped to AArch64 System register CNTKCTL\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CNTKCTL are UNDEFINED.

## Attributes

CNTKCTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## EVNTIS, bit [17]

## When FEAT\_ECV is implemented:

Controls the scale of the generation of the event stream.

| EVNTIS   | Meaning                                          |
|----------|--------------------------------------------------|
| 0b0      | The CNTKCTL.EVNTI field applies to CNTVCT[15:0]. |
| 0b1      | The CNTKCTL.EVNTI field applies to CNTVCT[23:8]. |

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:10]

Reserved, RES0.

## PL0PTEN, bit [9]

Traps PL0 accesses to the physical timer registers to Undefined mode.

| PL0PTEN   | Meaning                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------|
| 0b0       | PL0 accesses to the CNTP_CTL, CNTP_CVAL, and CNTP_TVAL registers are trapped to Undefined mode. |
| 0b1       | This control does not cause any instructions to be trapped.                                     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PL0VTEN, bit [8]

Traps PL0 accesses to the virtual timer registers to Undefined mode.

| PL0VTEN   | Meaning                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------|
| 0b0       | PL0 accesses to the CNTV_CTL, CNTV_CVAL, and CNTV_TVAL registers are trapped to Undefined mode. |
| 0b1       | This control does not cause any instructions to be trapped.                                     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTI, bits [7:4]

Selects which bit of CNTVCT, as seen from EL1, is the trigger for the event stream generated from that counter when that stream is enabled.

If FEAT\_ECV is implemented, and CNTKCTL.EVNTIS is 1, this field selects a trigger bit in the range 8 to 23 of CNTVCT.

Otherwise, this field selects a trigger bit in the range 0 to 15 of CNTVCT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTDIR, bit [3]

Controls which transition of the CNTVCT trigger bit, as seen from EL1 and defined by EVNTI, generates an event when the event stream is enabled.

| EVNTDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | A0to 1 transition of the trigger bit triggers an event. |
| 0b1       | A1to 0 transition of the trigger bit triggers an event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTEN, bit [2]

Enables the generation of an event stream from CNTVCT as seen from EL1.

| EVNTEN   | Meaning                    |
|----------|----------------------------|
| 0b0      | Disables the event stream. |
| 0b1      | Enables the event stream.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PL0VCTEN, bit [1]

Traps PL0 accesses to the frequency register and virtual counter register to Undefined mode.

| PL0VCTEN   | Meaning                                                                                                                                                   |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | PL0 accesses to the CNTVCTare trapped to Undefined mode. PL0 accesses to the CNTFRQregister are trapped to Undefined mode, if CNTKCTL.PL0PCTEN is also 0. |
| 0b1        | This control does not cause any instructions to be trapped.                                                                                               |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PL0PCTEN, bit [0]

Traps PL0 accesses to the frequency register and physical counter register to Undefined mode.

| PL0PCTEN   | Meaning                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | PL0 accesses to the CNTPCT are trapped to Undefined mode. PL0 accesses to the CNTFRQ register are trapped to Undefined mode, if CNTKCTL.PL0VCTEN is also 0. |
| 0b1        | This control does not cause any instructions to be trapped.                                                                                                 |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTKCTL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0001 | 0b000  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

R[t] = CNTKCTL;

elsif PSTATE.EL == EL2 then

R[t] = CNTKCTL;

elsif PSTATE.EL == EL3 then

R[t] = CNTKCTL;

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0001 | 0b000  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

CNTKCTL = R[t];

elsif PSTATE.EL == EL2 then

CNTKCTL

= R[t];

elsif PSTATE.EL == EL3 then CNTKCTL = R[t];

## G8.7.16 CNTP\_CTL, Counter-timer Physical Timer Control register

The CNTP\_CTL characteristics are:

## Purpose

Control register for the EL1 physical timer.

## Configuration

AArch32 System register CNTP\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTP\_CTL\_EL0[31:0].

This register is banked between CNTP\_CTL and CNTP\_CTL\_S and CNTP\_CTL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTP\_CTL are UNDEFINED.

## Attributes

CNTP\_CTL is a 32-bit register.

This register has the following instances:

- CNTP\_CTL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTP\_CTL\_S, when FEAT\_AA32EL3 is implemented.
- CNTP\_CTL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTP\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing CNTP\_CTL

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then
```

```
if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHPS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHP_CTL_EL2<31:0>; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CNTP_CTL_NS; else R[t] = CNTP_CTL; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = CNTP_CTL_S; else R[t] = CNTP_CTL_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = R[t]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CTL_NS = R[t]; else CNTP_CTL = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CTL_S = R[t]; else CNTP_CTL_NS = R[t];
```

## G8.7.17 CNTP\_CVAL, Counter-timer Physical Timer CompareValue register

The CNTP\_CVAL characteristics are:

## Purpose

Holds the compare value for the EL1 physical timer.

## Configuration

AArch32 System register CNTP\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTP\_CVAL\_EL0[63:0].

This register is banked between CNTP\_CVAL and CNTP\_CVAL\_S and CNTP\_CVAL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTP\_CVAL are UNDEFINED.

## Attributes

CNTP\_CVAL is a 64-bit register.

This register has the following instances:

- CNTP\_CVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTP\_CVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTP\_CVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL1 physical timer CompareValue.

When CNTP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTP\_CTL.ISTATUS is set to 1.
- If CNTP\_CTL.IMASK is 0, an interrupt is generated.

When CNTP\_CTL.ENABLE is 0, the timer condition is not met, but CNTPCT continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_CVAL

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHP_CVAL_EL2; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = CNTP_CVAL_NS; else R[t, t2] = CNTP_CVAL;
```

```
elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t, t2] = CNTP_CVAL_S; else R[t, t2] = CNTP_CVAL_NS;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0010 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2];
```

```
else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = R[t, t2]; else CNTP_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = R[t, t2]; else CNTP_CVAL_NS = R[t, t2];
```

## G8.7.18 CNTP\_TVAL, Counter-timer Physical Timer TimerValue register

The CNTP\_TVAL characteristics are:

## Purpose

Holds the timer value for the EL1 physical timer.

## Configuration

AArch32 System register CNTP\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTP\_TVAL\_EL0[31:0].

This register is banked between CNTP\_TVAL and CNTP\_TVAL\_S and CNTP\_TVAL\_NS.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTP\_TVAL are UNDEFINED.

## Attributes

CNTP\_TVAL is a 32-bit register.

This register has the following instances:

- CNTP\_TVAL, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CNTP\_TVAL\_S, when FEAT\_AA32EL3 is implemented.
- CNTP\_TVAL\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

TimerValue

31

0

<!-- image -->

## TimerValue, bits [31:0]

The TimerValue view of the EL1 physical timer.

On a read of this register:

- If CNTP\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTP\_CTL.ENABLE is 1, the value returned is (CNTP\_CVAL - CNTPCT).

On a write of this register, CNTP\_CV AL is set to (CNTPCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CNTP\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTP\_CTL.ISTATUS is set to 1.
- If CNTP\_CTL.IMASK is 0, an interrupt is generated.

When CNTP\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_TVAL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHPS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>; elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS -PhysicalCountInt())<31:0>; else if CNTP_CTL_S.ENABLE == '0' then
```

```
R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>; else if CNTP_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then if CNTP_CTL_S.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_S -PhysicalCountInt())<31:0>; else if CNTP_CTL_NS.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTP_CVAL_NS - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2)) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' && ↪ → !ELIsInHost(EL0) then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if SCR.NS == '1' then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) && ↪ → CNTHCTL_EL2.EL1PCEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCEN ↪ → == '0' then AArch32.TakeHypTrapException(0x03); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' then CNTP_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTPOFF_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt();
```

```
else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CNTP_CVAL_S = SignExtend(R[t], 64) + PhysicalCountInt(); else CNTP_CVAL_NS = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.19 CNTPCT, Counter-timer Physical Count register

The CNTPCT characteristics are:

## Purpose

Holds the 64-bit physical count value.

## Configuration

All reads to the CNTPCT occur in program order relative to reads to CNTPCTSS or CNTPCT.

AArch32 System register CNTPCT bits [63:0] are architecturally mapped to AArch64 System register CNTPCT\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTPCT are UNDEFINED.

## Attributes

CNTPCT is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |                      | 32   |
|------|----------------------|------|
|      | Physical count value |      |
| 31   |                      | 0    |
|      | Physical count value |      |

## PhysicalCount, bits [63:0]

Physical count value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPCT

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else
```

```
AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → CNTHCTL.PL1PCTEN == '0' then AArch32.TakeHypTrapException(0x04); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' ↪ → && !ELIsInHost(EL0) then R[t, t2] = PhysicalCountInt() -CNTPOFF_EL2; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCTEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' ↪ → then R[t, t2] = PhysicalCountInt() -CNTPOFF_EL2; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then R[t, t2] = PhysicalCountInt();
```

## G8.7.20 CNTPCTSS, Counter-timer Self-Synchronized Physical Count register

The CNTPCTSS characteristics are:

## Purpose

Holds the 64-bit physical count value.

## Configuration

All reads to the CNTPCTSS occur in program order relative to reads to CNTPCT or CNTPCTSS.

This register is a view of the CNTPCT register for which reads appear to occur in program order relative to other instructions, without the need for any explicit synchronization. Reads of this register return a value consistent with the counter not being read until the read instruction is known to be non-speculative.

AArch32 System register CNTPCTSS bits [63:0] are architecturally mapped to AArch64 System register CNTPCTSS\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_ECV is implemented. Otherwise, direct accesses to CNTPCTSS are UNDEFINED.

## Attributes

CNTPCTSS is a 64-bit register.

## Field descriptions

| 63                                     | 32   |
|----------------------------------------|------|
| Self-Synchronized Physical count value |      |
| 31                                     | 0    |
| Self-Synchronized Physical count value |      |

## SSPhysicalCount, bits [63:0]

Self-Synchronized Physical count value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPCTSS

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b1000 |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_ECV)) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0PCTEN == '0' then
```

```
if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0PCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL2) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '0' && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → CNTHCTL.PL1PCTEN == '0' then AArch32.TakeHypTrapException(0x04); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' ↪ → && !ELIsInHost(EL0) then R[t, t2] = PhysicalCountInt() -CNTPOFF_EL2; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && CNTHCTL.PL1PCTEN ↪ → == '0' then AArch32.TakeHypTrapException(0x04); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && ↪ → !ELUsingAArch32(EL2) && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') && CNTHCTL_EL2.ECV == '1' ↪ → then R[t, t2] = PhysicalCountInt() -CNTPOFF_EL2; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then R[t, t2] = PhysicalCountInt();
```

## G8.7.21 CNTV\_CTL, Counter-timer Virtual Timer Control register

The CNTV\_CTL characteristics are:

## Purpose

Control register for the virtual timer.

## Configuration

AArch32 System register CNTV\_CTL bits [31:0] are architecturally mapped to AArch64 System register CNTV\_CTL\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTV\_CTL are UNDEFINED.

## Attributes

CNTV\_CTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTV\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing CNTV\_CTL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t] = CNTHVS_CTL_EL2<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t] = CNTHV_CTL_EL2<31:0>; else R[t] = CNTV_CTL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else R[t] = CNTV_CTL; elsif PSTATE.EL == EL2 then R[t] = CNTV_CTL; elsif PSTATE.EL == EL3 then R[t] = CNTV_CTL;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = R[t];
```

```
elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = R[t]; else CNTV_CTL = R[t]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else CNTV_CTL = R[t]; elsif PSTATE.EL == EL2 then CNTV_CTL = R[t]; elsif PSTATE.EL == EL3 then CNTV_CTL = R[t];
```

## G8.7.22 CNTV\_CVAL, Counter-timer Virtual Timer CompareValue register

The CNTV\_CVAL characteristics are:

## Purpose

Holds the compare value for the virtual timer.

## Configuration

AArch32 System register CNTV\_CVAL bits [63:0] are architecturally mapped to AArch64 System register CNTV\_CVAL\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTV\_CVAL are UNDEFINED.

## Attributes

CNTV\_CVAL is a 64-bit register.

## Field descriptions

<!-- image -->

|   63 |   32 |
|------|------|
|   31 |    0 |

## CompareValue, bits [63:0]

Holds the EL1 virtual timer CompareValue.

When CNTV\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTV\_CTL.ISTATUS is set to 1.
- If CNTV\_CTL.IMASK is 0, an interrupt is generated.

When CNTV\_CTL.ENABLE is 0, the timer condition is not met, but CNTVCT continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_CVAL

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then R[t, t2] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then R[t, t2] = CNTHV_CVAL_EL2; else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL2 then R[t, t2] = CNTV_CVAL; elsif PSTATE.EL == EL3 then R[t, t2] = CNTV_CVAL;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0011 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = R[t, t2]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = R[t, t2]; else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL2 then CNTV_CVAL = R[t, t2]; elsif PSTATE.EL == EL3 then CNTV_CVAL = R[t, t2];
```

## G8.7.23 CNTV\_TVAL, Counter-timer Virtual Timer TimerValue register

The CNTV\_TVAL characteristics are:

## Purpose

Holds the timer value for the virtual timer.

## Configuration

AArch32 System register CNTV\_TVAL bits [31:0] are architecturally mapped to AArch64 System register CNTV\_TVAL\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTV\_TVAL are UNDEFINED.

## Attributes

CNTV\_TVAL is a 32-bit register.

## Field descriptions

TimerValue

31

0

## TimerValue, bits [31:0]

The TimerValue view of the virtual timer.

On a read of this register:

- If CNTV\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTV\_CTL.ENABLE is 1, the value returned is (CNTV\_CVAL - CNTVCT).

On a write of this register, CNTV\_CV AL is set to (CNTVCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTP\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CNTP\_CVAL) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTV\_CTL.ISTATUS is set to 1.
- If CNTV\_CTL.IMASK is 0, an interrupt is generated.

When CNTV\_CTL.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_TVAL

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHVS_CVAL_EL2 -PhysicalCountInt())<31:0>; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else R[t] = (CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>; else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>; elsif PSTATE.EL == EL2 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; else
```

```
R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; elsif PSTATE.EL == EL3 then if CNTV_CTL.ENABLE == '0' then R[t] = bits(32) UNKNOWN; elsif HaveEL(EL2) then R[t] = (CNTV_CVAL - (PhysicalCountInt() CNTVOFF))<31:0>; else R[t] = (CNTV_CVAL - PhysicalCountInt())<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b0011 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(R[t], 64) + PhysicalCountInt(); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else
```

```
CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; elsif PSTATE.EL == EL3 then if HaveEL(EL2) then CNTV_CVAL = (SignExtend(R[t], 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL = SignExtend(R[t], 64) + PhysicalCountInt();
```

## G8.7.24 CNTVCT, Counter-timer Virtual Count register

The CNTVCT characteristics are:

## Purpose

Holds the 64-bit virtual count value. The virtual count value is equal to the physical count value minus the virtual offset visible in CNTVOFF.

## Configuration

The value of this register is the same as the value of CNTPCT in the following conditions:

- When EL2 is not implemented.
- When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, and this register is read from Non-secure EL0.

All reads to the CNTVCT occur in program order relative to reads to CNTVCTSS or CNTVCT.

AArch32 System register CNTVCT bits [63:0] are architecturally mapped to AArch64 System register CNTVCT\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to CNTVCT are UNDEFINED.

## Attributes

CNTVCTis a 64-bit register.

## Field descriptions

<!-- image -->

| 63                  | 32   |
|---------------------|------|
| Virtual count value |      |
| 31                  | 0    |
| Virtual count value |      |

## VirtualCount, bits [63:0]

Virtual count value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVCT

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0001 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (!EL2Enabled() ↪ → || !ELIsInHost(EL0)) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && !ELUsingAArch32(EL2) && ↪ → (!EL2Enabled() || !ELIsInHost(EL0)) then R[t, t2] = PhysicalCountInt() CNTVOFF; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CNTHCTL_EL2.EL1TVCT ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt();
```

## G8.7.25 CNTVCTSS, Counter-timer Self-Synchronized Virtual Count register

The CNTVCTSS characteristics are:

## Purpose

Holds the 64-bit virtual count value. The virtual count value is equal to the physical count value visible in CNTPCT minus the virtual offset visible in CNTVOFF.

## Configuration

All reads to the CNTVCTSS occur in program order relative to reads to CNTVCT or CNTVCTSS.

This register is a view of the CNTVCT register for which reads appear to occur in program order relative to other instructions, without the need for any explicit synchronization. Reads of this register return a value consistent with the counter not being read until the read instruction is known to be non-speculative.

AArch32 System register CNTVCTSS bits [63:0] are architecturally mapped to AArch64 System register CNTVCTSS\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_ECV is implemented. Otherwise, direct accesses to CNTVCTSS are UNDEFINED.

## Attributes

CNTVCTSS is a 64-bit register.

## Field descriptions

| 63                                    | 32   |
|---------------------------------------|------|
| Self-Synchronized Virtual count value |      |
| 31                                    | 0    |
| Self-Synchronized Virtual count value |      |

## SSVirtualCount, bits [63:0]

Self-Synchronized Virtual count value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVCTSS

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b1001 |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_ECV)) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → CNTKCTL_EL1.EL0VCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && CNTKCTL.PL0VCTEN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif ELIsInHost(EL0) && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → CNTHCTL_EL2.EL0VCTEN == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (!EL2Enabled() ↪ → || !ELIsInHost(EL0)) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && !ELUsingAArch32(EL2) && ↪ → (!EL2Enabled() || !ELIsInHost(EL0)) then R[t, t2] = PhysicalCountInt() CNTVOFF; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CNTHCTL_EL2.EL1TVCT ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t, t2] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then R[t, t2] = PhysicalCountInt() CNTVOFF; else R[t, t2] = PhysicalCountInt();
```

## G8.7.26 CNTVOFF, Counter-timer Virtual Offset register

The CNTVOFF characteristics are:

## Purpose

Holds the 64-bit virtual offset. This is the offset between the physical count value visible in CNTPCT and the virtual count value visible in CNTVCT.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3 and the virtual counter uses a fixed virtual offset of zero.

Note

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the virtual counter uses a fixed virtual offset of zero when CNTVCT is read from Non-secure EL0.

AArch32 System register CNTVOFF bits [63:0] are architecturally mapped to AArch64 System register CNTVOFF\_EL2[63:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to CNTVOFF are UNDEFINED.

## Attributes

CNTVOFF is a 64-bit register.

## Field descriptions

Virtual offset

63

32

Virtual offset

31

0

<!-- image -->

## VOffset, bits [63:0]

Virtual offset.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVOFF

Accesses to this register use the following encodings in the System register encoding space:

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0100 |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then R[t, t2] = CNTVOFF; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t, t2] = CNTVOFF;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1110 | 0b0100 |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then CNTVOFF = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else CNTVOFF = R[t, t2];
```