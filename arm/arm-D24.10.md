## D24.10 Generic Timer registers

This section lists the Generic Timer registers in AArch64.

## D24.10.1 CNTFRQ\_EL0, Counter-timer Frequency Register

The CNTFRQ\_EL0 characteristics are:

## Purpose

This register is provided so that software can discover the effective frequency of the system counter. It must be programmed with this value as part of system initialization. The value of the register is not interpreted by hardware.

## Configuration

AArch64 System register CNTFRQ\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CNTFRQ[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTFRQ\_EL0 are UNDEFINED.

## Attributes

CNTFRQ\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ClockFreq, bits [31:0]

Clock frequency. Indicates the effective frequency of the system counter, in Hz.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTFRQ\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTFRQ_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.<EL0PCTEN,EL0VCTEN> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then
```

elsif ELIsInHost(EL0) &amp;&amp; CNTHCTL\_EL2.&lt;EL0PCTEN,EL0VCTEN&gt; == '00' then

AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CNTFRQ\_EL0; elsif PSTATE.EL == EL1 then X[t, 64] = CNTFRQ\_EL0; elsif PSTATE.EL == EL2 then X[t, 64] = CNTFRQ\_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTFRQ\_EL0;

MSR CNTFRQ\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b000 |

elsif IsHighestEL(PSTATE.EL) then

CNTFRQ\_EL0 = X[t, 64];

else

UNDEFINED;

## D24.10.2 CNTHCTL\_EL2, Counter-timer Hypervisor Control Register

The CNTHCTL\_EL2 characteristics are:

## Purpose

Controls the generation of an event stream from the physical counter, and access from EL1 to the physical counter and the EL1 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register CNTHCTL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHCTL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHCTL\_EL2 are UNDEFINED.

## Attributes

CNTHCTL\_EL2 is a 64-bit register.

## Field descriptions

When ELIsInHost(EL2):

<!-- image -->

## Bits [63:20]

Reserved, RES0.

CNTPMASK,bit [19]

When FEAT\_RME is implemented:

| CNTPMASK   | Meaning                                                                                           |
|------------|---------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on CNTP_CTL_EL0.IMASK.                                                 |
| 0b1        | CNTP_CTL_EL0.IMASK behaves as if set to 1 for all purposes other than a direct read of the field. |

This bit is RES0 in Non-secure and Secure state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CNTVMASK,bit [18]

## When FEAT\_RME is implemented:

| CNTVMASK   | Meaning                                                                                           |
|------------|---------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on CNTV_CTL_EL0.IMASK.                                                 |
| 0b1        | CNTV_CTL_EL0.IMASK behaves as if set to 1 for all purposes other than a direct read of the field. |

This bit is RES0 in Non-secure and Secure state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVNTIS, bit [17]

## When FEAT\_ECV is implemented:

Controls the scale of the generation of the event stream.

| EVNTIS   | Meaning                                                  |
|----------|----------------------------------------------------------|
| 0b0      | The CNTHCTL_EL2.EVNTI field applies to CNTPCT_EL0[15:0]. |
| 0b1      | The CNTHCTL_EL2.EVNTI field applies to CNTPCT_EL0[23:8]. |

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVVCT, bit [16]

## When FEAT\_ECV is implemented:

When HCR\_EL2.TGE is 0 and the Effective value of HCR\_EL2.{NV2, NV1, NV} is {1, 0, 1}, traps EL1 accesses to the specified EL1 virtual timer registers using the EL02 descriptors to EL2 as follows:

Accesses to CNTV\_CTL\_EL02 and CNTV\_CVAL\_EL02 are trapped to EL2 and reported with EC syndrome value 0x18 .

| EL1NVVCT   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped. |
| 0b1        | EL1 accesses to the specified registers are trapped to EL2. |

If HCR\_EL2.TGE is 1 or the Effective value of HCR\_EL2.{NV2, NV1, NV} is not {1, 0, 1}, this control does not cause any instructions to be trapped.

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVPCT, bit [15]

## When FEAT\_ECV is implemented:

When HCR\_EL2.TGE is 0 and the Effective value of HCR\_EL2.{NV2, NV1, NV} is {1, 0, 1}, traps EL1 accesses to the specified EL1 physical timer registers using the EL02 descriptors to EL2 as follows:

Accesses to CNTP\_CTL\_EL02 and CNTP\_CVAL\_EL02 are trapped to EL2 and reported with EC syndrome value 0x18 .

| EL1NVPCT   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped. |
| 0b1        | EL1 accesses to the specified registers are trapped to EL2. |

If HCR\_EL2.TGE is 1 or the Effective value of HCR\_EL2.{NV2, NV1, NV} is not {1, 0, 1}, this control does not cause any instructions to be trapped.

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVCT, bit [14]

## When FEAT\_ECV is implemented:

Traps EL0 and EL1 accesses to the EL1 virtual counter registers to EL2 when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to CNTVCT\_EL0 and CNTVCTSS\_EL0 are trapped to EL2 and reported using EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0VCTEN.

- In AArch32 state, accesses to CNTVCT are trapped to EL2 and reported with EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0VCTEN or CNTKCTL.PL0VCTEN.

| EL1TVCT   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | This control does not cause any instructions to be trapped.         |
| 0b1       | EL0 and EL1 accesses to the specified registers are trapped to EL2. |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

If HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVT, bit [13]

## When FEAT\_ECV is implemented:

When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, traps EL0 and EL1 accesses to the EL1 virtual timer registers to EL2, when EL2 is enabled for the current Security state, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0VTEN:
- CNTV\_CTL\_EL0.
- CNTV\_CVAL\_EL0.
- CNTV\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 , and MCRR and MRRC accesses are trapped to EL2 and reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0VTEN or CNTKCTL.PL0VTEN:
- CNTV\_CTL.
- CNTV\_CVAL.
- CNTV\_TVAL.

| EL1TVT   | Meaning                                                             |
|----------|---------------------------------------------------------------------|
| 0b0      | This control does not cause any instructions to be trapped.         |
| 0b1      | EL0 and EL1 accesses to the specified registers are trapped to EL2. |

If HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ECV, bit [12]

## When FEAT\_ECV\_POFF is implemented:

Enables the Enhanced Counter Virtualization functionality registers.

When the Enhanced Counter Virtualization is enabled, the behavior is as follows:

- An MRS to CNTPCT\_EL0 from either EL0 or EL1 that is not trapped will return the value ( PCount &lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;).
- The EL1 physical timer interrupt is triggered when (( PCount &lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;) PCVal &lt;63:0&gt;) is greater than or equal to 0.

PCount &lt;63:0&gt; is the physical count returned when CNTPCT\_EL0 is read from EL2 or EL3.

PCVal &lt;63:0&gt; is the EL1 physical timer compare value for this timer.

| ECV   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | Enhanced Counter Virtualization functionality is disabled. |
| 0b1   | Enhanced Counter Virtualization functionality is enabled.  |

When HCR\_EL2.TGE is 1 or SCR\_EL3.{NS, EEL2} is {0, 0}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1PTEN, bit [11]

When HCR\_EL2.TGE is 0, traps EL0 and EL1 accesses to the EL1 physical timer registers to EL2 when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0PTEN:
- CNTP\_CTL\_EL0.
- CNTP\_CVAL\_EL0.
- CNTP\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0PTEN or CNTKCTL.PL0PTEN:
- CNTP\_CTL.
- CNTP\_CVAL.
- CNTP\_TVAL.

| EL1PTEN   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | EL0 and EL1 accesses to the specified registers are trapped to EL2. |
| 0b1       | This control does not cause any instructions to be trapped.         |

When HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL1PCTEN, bit [10]

When HCR\_EL2.TGE is 0, traps EL0 and EL1 accesses to the EL1 physical counter registers to EL2 when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to CNTPCT\_EL0 and CNTPCTSS\_EL0 are trapped to EL2 and reported with EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0PCTEN.
- In AArch32 state, MRRC or MCRR accesses to CNTPCT are trapped to EL2 and reported with EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0PCTEN or CNTKCTL.PL0PCTEN.

| EL1PCTEN   | Meaning                                                             |
|------------|---------------------------------------------------------------------|
| 0b0        | EL0 and EL1 accesses to the specified registers are trapped to EL2. |
| 0b1        | This control does not cause any instructions to be trapped.         |

When HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0PTEN, bit [9]

When HCR\_EL2.TGE is 1, traps EL0 accesses to the physical timer registers to EL2, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 :
- CNTP\_CTL\_EL0.
- CNTP\_CVAL\_EL0.
- CNTP\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTP\_CTL.
- CNTP\_CVAL.
- CNTP\_TVAL.

| EL0PTEN   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0       | EL0 accesses to the specified registers are trapped to EL2. |
| 0b1       | This control does not cause any instructions to be trapped. |

When HCR\_EL2.TGE is 0, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0VTEN, bit [8]

When HCR\_EL2.TGE is 1, traps EL0 accesses to the virtual timer registers to EL2 as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 :
- CNTV\_CTL\_EL0.
- CNTV\_CVAL\_EL0.
- CNTV\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTV\_CTL.
- CNTV\_CVAL.
- CNTV\_TVAL.

| EL0VTEN   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0       | EL0 accesses to the specified registers are trapped to EL2. |
| 0b1       | This control does not cause any instructions to be trapped. |

When HCR\_EL2.TGE is 0, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTI, bits [7:4]

Selects which bit of CNTPCT\_EL0, as seen from EL2, is the trigger for the event stream generated from that counter when that stream is enabled.

If FEAT\_ECV is implemented, and CNTHCTL\_EL2.EVNTIS is 1, this field selects a trigger bit in the range 8 to 23 of CNTPCT\_EL0.

Otherwise, this field selects a trigger bit in the range 0 to 15 of CNTPCT\_EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTDIR, bit [3]

Controls which transition of the CNTPCT\_EL0 trigger bit, as seen from EL2 and defined by EVNTI, generates an event when the event stream is enabled.

| EVNTDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | A0to 1 transition of the trigger bit triggers an event. |
| 0b1       | A1to 0 transition of the trigger bit triggers an event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTEN, bit [2]

Enables the generation of an event stream from CNTPCT\_EL0 as seen from EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0VCTEN, bit [1]

When HCR\_EL2.TGE is 1, traps EL0 accesses to the frequency register and virtual counter registers to EL2, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 :
- CNTVCT\_EL0.
- CNTVCTSS\_EL0.
- CNTFRQ\_EL0 if CNTHCTL\_EL2.EL0PCTEN is 0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTVCTand if CNTHCTL.EL0PCTEN is 0, CNTFRQ.

| EL0VCTEN   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | EL0 accesses to the specified registers are trapped to EL2. |
| 0b1        | This control does not cause any instructions to be trapped. |

If HCR\_EL2.TGE is 0, the field is ignored for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0PCTEN, bit [0]

Traps EL0 accesses to the frequency register and physical counter registers to EL2, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 :
- CNTPCT\_EL0.
- CNTPCTSS\_EL0.
- CNTFRQ\_EL0 if CNTHCTL\_EL2.EL0VCTEN is 0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTPCT and if CNTHCTL\_EL2.EL0VCTEN is 0, CNTFRQ.

| EL0PCTEN   | Meaning                                                                         |
|------------|---------------------------------------------------------------------------------|
| 0b0        | From AArch64 state: EL0 accesses to the specified registers are trapped to EL2. |
| 0b1        | This control does not cause any instructions to be trapped.                     |

| EVNTEN   | Meaning                    |
|----------|----------------------------|
| 0b0      | Disables the event stream. |
| 0b1      | Enables the event stream.  |

## EL0PCTEN

## Meaning

If HCR\_EL2.TGE is 0, the control does not cause any instructions to be trapped for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

The following field descriptions apply in all Armv8.0 implementations.

The descriptions also explain the behavior when EL3 is implemented and EL2 is not implemented.

## Bits [63:20]

Reserved, RES0.

## CNTPMASK,bit [19]

When FEAT\_RME is implemented:

| CNTPMASK   | Meaning                                                                                           |
|------------|---------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on CNTP_CTL_EL0.IMASK.                                                 |
| 0b1        | CNTP_CTL_EL0.IMASK behaves as if set to 1 for all purposes other than a direct read of the field. |

This bit is RES0 in Non-secure and Secure state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CNTVMASK,bit [18]

When FEAT\_RME is implemented:

| CNTVMASK   | Meaning                                                                                           |
|------------|---------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on CNTV_CTL_EL0.IMASK.                                                 |
| 0b1        | CNTV_CTL_EL0.IMASK behaves as if set to 1 for all purposes other than a direct read of the field. |

This bit is RES0 in Non-secure and Secure state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVNTIS, bit [17]

## When FEAT\_ECV is implemented:

Controls the scale of the generation of the event stream.

| EVNTIS   | Meaning                                                  |
|----------|----------------------------------------------------------|
| 0b0      | The CNTHCTL_EL2.EVNTI field applies to CNTPCT_EL0[15:0]. |
| 0b1      | The CNTHCTL_EL2.EVNTI field applies to CNTPCT_EL0[23:8]. |

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVVCT, bit [16]

## When FEAT\_ECV is implemented:

When the Effective value of HCR\_EL2.{NV2, NV1, NV} is {1, 0, 1}, traps EL1 accesses to the specified EL1 virtual timer registers using the EL02 descriptors to EL2 as follows:

Accesses to CNTV\_CTL\_EL02 and CNTV\_CVAL\_EL02 are trapped to EL2 and reported with EC syndrome value 0x18 .

| EL1NVVCT   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped. |
| 0b1        | EL1 accesses to the specified registers are trapped to EL2. |

If the Effective value of HCR\_EL2.{NV2, NV1, NV} is not {1, 0, 1}, this control does not cause any instructions to be trapped.

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVPCT, bit [15]

## When FEAT\_ECV is implemented:

When the Effective value of HCR\_EL2.{NV2, NV1, NV} is {1, 0, 1}, traps EL1 accesses to the specified EL1 physical timer registers using the EL02 descriptors to EL2 as follows:

Accesses to CNTP\_CTL\_EL02 and CNTP\_CVAL\_EL02 are trapped to EL2 and reported with EC syndrome value 0x18 .

| EL1NVPCT   | Meaning                                                     |
|------------|-------------------------------------------------------------|
| 0b0        | This control does not cause any instructions to be trapped. |
| 0b1        | EL1 accesses to the specified registers are trapped to EL2. |

If the Effective value of HCR\_EL2.{NV2, NV1, NV} is not {1, 0, 1}, this control does not cause any instructions to be trapped.

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVCT, bit [14]

## When FEAT\_ECV is implemented:

Traps EL0 and EL1 accesses to the EL1 virtual counter registers to EL2, when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to CNTVCT\_EL0 and CNTVCTSS\_EL0 are trapped to EL2 and reported using EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0VCTEN.
- In AArch32 state, accesses to CNTVCT are trapped to EL2 and reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0VCTEN or CNTKCTL.PL0VCTEN.

| EL1TVCT   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | This control does not cause any instructions to be trapped.         |
| 0b1       | EL0 and EL1 accesses to the specified registers are trapped to EL2. |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVT, bit [13]

## When FEAT\_ECV is implemented:

If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then traps EL0 and EL1 accesses to the EL1 virtual timer registers to EL2, when EL2 is enabled for the current Security state, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0VTEN:
- CNTV\_CTL\_EL0.
- CNTV\_CVAL\_EL0.
- CNTV\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 and MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0VTEN or CNTKCTL.PL0VTEN:
- CNTV\_CTL.
- CNTV\_CVAL.
- CNTV\_TVAL.

| EL1TVT   | Meaning                                                             |
|----------|---------------------------------------------------------------------|
| 0b0      | This control does not cause any instructions to be trapped.         |
| 0b1      | EL0 and EL1 accesses to the specified registers are trapped to EL2. |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 0 other than for the purpose of a direct read.

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ECV, bit [12]

## When FEAT\_ECV\_POFF is implemented:

Enables the Enhanced Counter Virtualization functionality registers.

When the Enhanced Counter Virtualization is enabled, the behavior is as follows:

- An MRS to CNTPCT\_EL0 from either EL0 or EL1 that is not trapped will return the value ( PCount &lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;).
- The EL1 physical timer interrupt is triggered when (( PCount &lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;) PCVal &lt;63:0&gt;) is greater than or equal to 0.

PCount is the physical count returned when CNTPCT\_EL0 is read from EL2 or EL3.

PCVal &lt;63:0&gt; is the EL1 physical timer compare value for this timer.

| ECV   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | Enhanced Counter Virtualization functionality is disabled. |
| 0b1   | Enhanced Counter Virtualization functionality is enabled.  |

When SCR\_EL3.{NS, EEL2} is {0, 0} or if FEAT\_ECV\_POFF is not implemented, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [11:8]

Reserved, RES0.

## EVNTI, bits [7:4]

Selects which bit of CNTPCT\_EL0, as seen from EL2,is the trigger for the event stream generated from that counter when that stream is enabled.

If FEAT\_ECV is implemented, and CNTHCTL\_EL2.EVNTIS is 1, this field selects a trigger bit in the range 8 to 23 of CNTPCT\_EL0.

Otherwise, this field selects a trigger bit in the range 0 to 15 of CNTPCT\_EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTDIR, bit [3]

Controls which transition of the CNTPCT\_EL0 trigger bit, as seen from EL2 and defined by EVNTI, generates an event when the event stream is enabled.

| EVNTDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | A0to 1 transition of the trigger bit triggers an event. |
| 0b1       | A1to 0 transition of the trigger bit triggers an event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTEN, bit [2]

Enables the generation of an event stream from CNTPCT\_EL0 as seen from EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL1PCEN, bit [1]

Traps EL0 and EL1 accesses to the EL1 physical timer registers to EL2 when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to CNTP\_CTL\_EL0, CNTP\_CVAL\_EL0, CNTP\_TVAL\_EL0 are trapped to EL2, reported using EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0PTEN.
- In AArch32 state, MRC or MCR accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 , and MRRC and MCRR accesses are trapped to EL2, reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0PTEN or CNTKCTL.PL0PTEN:
- CNTP\_CTL, CNTP\_CVAL, CNTP\_TVAL.

| EL1PCEN   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | EL0 and EL1 accesses to the specified registers are trapped to EL2. |
| 0b1       | This control does not cause any instructions to be trapped.         |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL1PCTEN, bit [0]

Traps EL0 and EL1 accesses to the EL1 physical counter registers to EL2 when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to CNTPCT\_EL0 and CNTPCTSS\_EL0 are trapped to EL2 and reported using EC syndrome value 0x18 , unless they are trapped by CNTKCTL\_EL1.EL0PCTEN.
- In AArch32 state, MRRC or MCRR accesses to CNTPCT are trapped to EL2 and reported using EC syndrome value 0x04 , unless they are trapped by CNTKCTL\_EL1.EL0PCTEN or CNTKCTL.PL0PCTEN.

| EL1PCTEN   | Meaning                                                             |
|------------|---------------------------------------------------------------------|
| 0b0        | EL0 and EL1 accesses to the specified registers are trapped to EL2. |
| 0b1        | This control does not cause any instructions to be trapped.         |

If EL3 is implemented and EL2 is not implemented, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

| EVNTEN   | Meaning                    |
|----------|----------------------------|
| 0b0      | Disables the event stream. |
| 0b1      | Enables the event stream.  |

## Accessing CNTHCTL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHCTL\_EL2 or CNTKCTL\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHCTL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = CNTHCTL_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CNTHCTL_EL2;
```

MSR CNTHCTL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTHCTL_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTHCTL_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTKCTL\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then X[t, 64] = CNTKCTL_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTHCTL_EL2_VHE(CNTHCTL_EL2); else X[t, 64] = CNTKCTL_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CNTKCTL_EL1;
```

When FEAT\_VHE is implemented MSR CNTKCTL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then CNTKCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTHCTL_EL2 = CNTHCTL_EL2_VHE(X[t, 64]); else CNTKCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTKCTL_EL1 = X[t, 64];
```

## D24.10.3 CNTHP\_CTL\_EL2, Counter-timer Hypervisor Physical Timer Control Register

The CNTHP\_CTL\_EL2 characteristics are:

## Purpose

Control register for the EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHP\_CTL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHP\_CTL[31:0].

This register is present only when (HaveEL(EL3) || (((!HaveEL(EL3)) &amp;&amp; HaveEL(EL2)) &amp;&amp; (!IsFeatureImplemented(FEAT\_SEL2)))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHP\_CTL\_EL2 are UNDEFINED.

## Attributes

CNTHP\_CTL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHP\_TV AL\_EL2 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_CTL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHP\_CTL\_EL2 or CNTP\_CTL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b001 |

```
if !((HaveEL(EL3) || (!HaveEL(EL3) && HaveEL(EL2) && !IsFeatureImplemented(FEAT_SEL2))) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = CNTHP_CTL_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CNTHP_CTL_EL2;
```

MSR CNTHP\_CTL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b001 |

```
if !((HaveEL(EL3) || (!HaveEL(EL3) && HaveEL(EL2) && !IsFeatureImplemented(FEAT_SEL2))) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTHP_CTL_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTHP_CTL_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, CNTP\_CTL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x180]; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CTL_EL0;
```

MSR CNTP\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x180] = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64];
```

```
elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CTL_EL0 = X[t, 64];
```

## D24.10.4 CNTHP\_CVAL\_EL2, Counter-timer Physical Timer CompareValue Register (EL2)

The CNTHP\_CVAL\_EL2 characteristics are:

## Purpose

Holds the compare value for the EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHP\_CVAL\_EL2 bits [63:0] are architecturally mapped to AArch32 System register CNTHP\_CVAL[63:0].

This register is present only when (HaveEL(EL3) || (((!HaveEL(EL3)) &amp;&amp; HaveEL(EL2)) &amp;&amp; (!IsFeatureImplemented(FEAT\_SEL2)))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHP\_CVAL\_EL2 are UNDEFINED.

## Attributes

CNTHP\_CVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL2 physical timer CompareValue.

When CNTHP\_CTL\_EL2.ENABLE is 1, and TimerConditionMet is TRUE for the EL2 physical timer, the timer condition is met and all of the following are true:

- CNTHP\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHP\_CTL\_EL2.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTHP\_CTL\_EL2.ENABLE is 0, the timer condition is not met, but CNTPCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_CVAL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHP\_CVAL\_EL2 or CNTP\_CVAL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHP\_CVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b010 |

if !((HaveEL(EL3) || (!HaveEL(EL3) &amp;&amp; HaveEL(EL2) &amp;&amp; !IsFeatureImplemented(FEAT\_SEL2))) &amp;&amp; ↪ → IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

X[t, 64] = CNTHP\_CVAL\_EL2;

elsif PSTATE.EL == EL3 then

X[t, 64] = CNTHP\_CVAL\_EL2;

MSR CNTHP\_CVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b010 |

if !((HaveEL(EL3) || (!HaveEL(EL3) &amp;&amp; HaveEL(EL2) &amp;&amp; !IsFeatureImplemented(FEAT\_SEL2))) &amp;&amp; ↪ → IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

CNTHP\_CVAL\_EL2 = X[t, 64];

elsif PSTATE.EL == EL3 then

CNTHP\_CVAL\_EL2 = X[t, 64];

MRS &lt;Xt&gt;, CNTP\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x178]; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CVAL_EL0;
```

MSR CNTP\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x178] = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = X[t, 64];
```

## D24.10.5 CNTHP\_TVAL\_EL2, Counter-timer Physical Timer TimerValue Register (EL2)

The CNTHP\_TVAL\_EL2 characteristics are:

## Purpose

Holds the timer value for the EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHP\_TVAL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHP\_TVAL[31:0].

This register is present only when (HaveEL(EL3) || (((!HaveEL(EL3)) &amp;&amp; HaveEL(EL2)) &amp;&amp; (!IsFeatureImplemented(FEAT\_SEL2)))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHP\_TVAL\_EL2 are UNDEFINED.

## Attributes

CNTHP\_TVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL2 physical timer.

On a read of this register:

- If CNTHP\_CTL\_EL2.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHP\_CTL\_EL2.ENABLE is 1, the value returned is (CNTHP\_CVAL\_EL2 - CNTPCT\_EL0).

On a write of this register, CNTHP\_CV AL\_EL2 is set to (CNTPCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHP\_CTL\_EL2.ENABLE is 1, the timer condition is met when (CNTPCT\_EL0 -

CNTHP\_CVAL\_EL2) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHP\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHP\_CTL\_EL2.IMASK is 0, an interrupt is generated.

When CNTHP\_CTL\_EL2.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHP\_TVAL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHP\_TVAL\_EL2 or CNTP\_TVAL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHP\_TVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b000 |

```
HaveEL(EL2) && !IsFeatureImplemented(FEAT_SEL2))) &&
```

```
if !((HaveEL(EL3) || (!HaveEL(EL3) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTHP\_TVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0010 | 0b000 |

```
HaveEL(EL2) && !IsFeatureImplemented(FEAT_SEL2))) &&
```

```
if !((HaveEL(EL3) || (!HaveEL(EL3) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

MRS &lt;Xt&gt;, CNTP\_TVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else
```

```
X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTP\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

```
else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

## D24.10.6 CNTHPS\_CTL\_EL2, Counter-timer Secure Physical Timer Control Register (EL2)

The CNTHPS\_CTL\_EL2 characteristics are:

## Purpose

Control register for the Secure EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHPS\_CTL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHPS\_CTL[31:0].

This register is present only when FEAT\_SEL2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHPS\_CTL\_EL2 are UNDEFINED.

## Attributes

CNTHPS\_CTL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the CNTHPS\_CTL\_EL2.ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

When the value of the CNTHPS\_CTL\_EL2.ENABLE bit is 0, the ISTATUS field is UNKNOWN.

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHPS\_TV AL\_EL2 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_CTL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTHPS_CTL_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else X[t, 64] = CNTHPS_CTL_EL2; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = CNTHPS_CTL_EL2;
```

MSR CNTHPS\_CTL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else CNTHPS_CTL_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else CNTHPS_CTL_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_CTL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18);
```

```
elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x180]; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CTL_EL0;
```

When FEAT\_VHE is implemented MSR CNTP\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x180] = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CTL_EL0 = X[t, 64];
```

## D24.10.7 CNTHPS\_CVAL\_EL2, Counter-timer Secure Physical Timer CompareValue Register (EL2)

The CNTHPS\_CVAL\_EL2 characteristics are:

## Purpose

Holds the compare value for the Secure EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHPS\_CVAL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHPS\_CVAL[31:0].

This register is present only when EL2 is implemented, FEAT\_SEL2 is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHPS\_CVAL\_EL2 are UNDEFINED.

## Attributes

CNTHPS\_CVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL2 physical timer CompareValue.

When CNTHPS\_CTL\_EL2.ENABLE is 1, and TimerConditionMet is TRUE for the Secure EL2 physical timer, the timer condition is met and all of the following are true:

- CNTHPS\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHPS\_CTL\_EL2.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTHPS\_CTL\_EL2.ENABLE is 0, the timer condition is not met, but CNTPCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_CVAL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

## MRS &lt;Xt&gt;, CNTHPS\_CVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b010 |

if !(HaveEL(EL2) &amp;&amp; UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; else X[t, 64] = CNTHPS\_CVAL\_EL2; elsif PSTATE.EL == EL3 then if SCR\_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = CNTHPS\_CVAL\_EL2;

IsFeatureImplemented(FEAT\_SEL2) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

MSR CNTHPS\_CVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b010 |

IsFeatureImplemented(FEAT\_SEL2) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then if !(HaveEL(EL2) &amp;&amp; UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; else CNTHPS\_CVAL\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR\_EL3.EEL2 == '0' then UNDEFINED; else CNTHPS\_CVAL\_EL2 = X[t, 64];

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x178]; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CVAL_EL0;
```

When FEAT\_VHE is implemented MSR CNTP\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x178] = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = X[t, 64];
```

## D24.10.8 CNTHPS\_TVAL\_EL2, Counter-timer Secure Physical Timer TimerValue Register (EL2)

The CNTHPS\_TVAL\_EL2 characteristics are:

## Purpose

Holds the timer value for the Secure EL2 physical timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHPS\_TVAL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHPS\_TVAL[31:0].

This register is present only when EL2 is implemented, FEAT\_SEL2 is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHPS\_TVAL\_EL2 are UNDEFINED.

## Attributes

CNTHPS\_TVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL2 physical timer.

On a read of this register:

- If CNTHPS\_CTL\_EL2.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHPS\_CTL\_EL2.ENABLE is 1, the value returned is (CNTHPS\_CVAL\_EL2 - CNTPCT\_EL0).

On a write of this register, CNTHPS\_CVAL\_EL2 is set to (CNTPCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHPS\_CTL\_EL2.ENABLE is 1, the timer condition is met when (CNTPCT\_EL0 -CNTHPS\_CVAL\_EL2) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHPS\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHPS\_CTL\_EL2.IMASK is 0, an interrupt is generated.

When CNTHPS\_CTL\_EL2.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHPS\_TVAL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHPS\_TVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b000 |

```
if !(HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTHPS\_TVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0101 | 0b000 |

```
if !(HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then
```

```
if SCR_EL3.EEL2 == '0' then UNDEFINED; else CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_TVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == ↪ → '1') && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == ↪ → '1') && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN;
```

else

```
X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

When FEAT\_VHE is implemented MSR CNTP\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) ↪ → then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == ↪ → '1') && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == ↪ → '1') && CNTHCTL_EL2.ECV == '1' then
```

```
CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

## D24.10.9 CNTHV\_CTL\_EL2, Counter-timer Virtual Timer Control Register (EL2)

The CNTHV\_CTL\_EL2 characteristics are:

## Purpose

Control register for the EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHV\_CTL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHV\_CTL[31:0].

This register is present only when (IsFeatureImplemented(FEAT\_VHE) &amp;&amp; (HaveEL(EL3) || ((!HaveEL(EL3)) &amp;&amp;(!IsFeatureImplemented(FEAT\_SEL2))))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHV\_CTL\_EL2 are UNDEFINED.

## Attributes

CNTHV\_CTL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHV\_TV AL\_EL2 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHV\_CTL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHV\_CTL\_EL2 or CNTV\_CTL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHV\_CTL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_VHE) && (HaveEL(EL3) || (!HaveEL(EL3) && ↪ → !IsFeatureImplemented(FEAT_SEL2))) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = CNTHV_CTL_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CNTHV_CTL_EL2;
```

MSR CNTHV\_CTL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_VHE) && (HaveEL(EL3) || (!HaveEL(EL3) && ↪ → !IsFeatureImplemented(FEAT_SEL2))) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTHV_CTL_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTHV_CTL_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, CNTV\_CTL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x170]; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CTL_EL0;
```

MSR CNTV\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x170] = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else
```

```
CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CTL_EL0 = X[t, 64];
```

## D24.10.10 CNTHV\_CVAL\_EL2, Counter-timer Virtual Timer CompareValue Register (EL2)

The CNTHV\_CVAL\_EL2 characteristics are:

## Purpose

Holds the compare value for the EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHV\_CVAL\_EL2 bits [63:0] are architecturally mapped to AArch32 System register CNTHV\_CVAL[63:0].

This register is present only when (IsFeatureImplemented(FEAT\_VHE) &amp;&amp; (HaveEL(EL3) || ((!HaveEL(EL3)) &amp;&amp;(!IsFeatureImplemented(FEAT\_SEL2))))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHV\_CVAL\_EL2 are UNDEFINED.

## Attributes

CNTHV\_CVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63           | 32           |              |
|--------------|--------------|--------------|
| CompareValue | CompareValue | CompareValue |
| 31           | 0            |              |
| CompareValue | CompareValue | CompareValue |

## CompareValue, bits [63:0]

Holds the EL2 virtual timer CompareValue.

When CNTHV\_CTL\_EL2.ENABLE is 1, and TimerConditionMet is TRUE for the EL2 virtual timer, the timer condition is met and all of the following are true:

- CNTHV\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHV\_CTL\_EL2.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTHV\_CTL\_EL2.ENABLE is 0, the timer condition is not met, but CNTVCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHV\_CVAL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHV\_CVAL\_EL2 or CNTV\_CVAL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHV\_CVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b010 |

if !(IsFeatureImplemented(FEAT\_VHE) &amp;&amp; (HaveEL(EL3) || (!HaveEL(EL3) &amp;&amp;

↪ → !IsFeatureImplemented(FEAT\_SEL2))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

X[t, 64] = CNTHV\_CVAL\_EL2;

elsif PSTATE.EL == EL3 then

X[t, 64] = CNTHV\_CVAL\_EL2;

MSR CNTHV\_CVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b010 |

if !(IsFeatureImplemented(FEAT\_VHE) &amp;&amp; (HaveEL(EL3) || (!HaveEL(EL3) &amp;&amp;

↪ → !IsFeatureImplemented(FEAT\_SEL2))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

CNTHV\_CVAL\_EL2 = X[t, 64];

elsif PSTATE.EL == EL3 then

CNTHV\_CVAL\_EL2 = X[t, 64];

MRS &lt;Xt&gt;, CNTV\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x168]; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CVAL_EL0;
```

MSR CNTV\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else
```

```
CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x168] = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CVAL_EL0 = X[t, 64];
```

## D24.10.11 CNTHV\_TVAL\_EL2, Counter-timer Virtual Timer TimerValue Register (EL2)

The CNTHV\_TVAL\_EL2 characteristics are:

## Purpose

Holds the timer value for the EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHV\_TVAL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHV\_TVAL[31:0].

This register is present only when (IsFeatureImplemented(FEAT\_VHE) &amp;&amp; (HaveEL(EL3) || ((!HaveEL(EL3)) &amp;&amp;(!IsFeatureImplemented(FEAT\_SEL2))))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to CNTHV\_TVAL\_EL2 are UNDEFINED.

## Attributes

CNTHV\_TVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL2 virtual timer.

On a read of this register:

- If CNTHV\_CTL\_EL2.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHV\_CTL\_EL2.ENABLE is 1, the value returned is (CNTHV\_CVAL\_EL2 - CNTVCT\_EL0).

On a write of this register, CNTHV\_CVAL\_EL2 is set to (CNTVCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHV\_CTL\_EL2.ENABLE is 1, the timer condition is met when (CNTVCT\_EL0 -

CNTHV\_CVAL\_EL2) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHV\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHV\_CTL\_EL2.IMASK is 0, an interrupt is generated.

When CNTHV\_CTL\_EL2.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHV\_TVAL\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CNTHV\_TVAL\_EL2 or CNTV\_TVAL\_EL0 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHV\_TVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b000 |

```
then
```

```
if !(IsFeatureImplemented(FEAT_VHE) && (HaveEL(EL3) || (!HaveEL(EL3) && ↪ → !IsFeatureImplemented(FEAT_SEL2))) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTHV\_TVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0011 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_VHE) && (HaveEL(EL3) || (!HaveEL(EL3) && ↪ → !IsFeatureImplemented(FEAT_SEL2))) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

MRS &lt;Xt&gt;, CNTV\_TVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif HaveEL(EL2) && !ELIsInHost(EL0) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else
```

```
X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif !ELIsInHost(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() CNTVOFF))<31:0>, 64); else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTV\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif HaveEL(EL2) && !ELIsInHost(EL0) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif !ELIsInHost(EL2) then
```

```
CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

## D24.10.12 CNTHVS\_CTL\_EL2, Counter-timer Secure Virtual Timer Control Register (EL2)

The CNTHVS\_CTL\_EL2 characteristics are:

## Purpose

Control register for the Secure EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHVS\_CTL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHVS\_CTL[31:0].

This register is present only when FEAT\_SEL2 is implemented, FEAT\_VHE is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHVS\_CTL\_EL2 are UNDEFINED.

## Attributes

CNTHVS\_CTL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the CNTHVS\_CTL\_EL2.ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0 then the timer interrupt is asserted.

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

For more information, see the description of the CNTHVS\_CTL\_EL2.ISTATUS bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTHVS\_TV AL\_EL2 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHVS\_CTL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTHVS_CTL_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_VHE) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED;
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else X[t, 64] = CNTHVS_CTL_EL2; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = CNTHVS_CTL_EL2;
```

MSR CNTHVS\_CTL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_VHE) &&
```

```
↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else CNTHVS_CTL_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else CNTHVS_CTL_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, CNTV\_CTL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x170]; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CTL_EL0;
```

MSR CNTV\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x170] = X[t, 64]; else
```

```
CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CTL_EL0 = X[t, 64];
```

## D24.10.13 CNTHVS\_CVAL\_EL2, Counter-timer Secure Virtual Timer CompareValue Register (EL2)

The CNTHVS\_CVAL\_EL2 characteristics are:

## Purpose

Holds the compare value for the Secure EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHVS\_CVAL\_EL2 bits [63:0] are architecturally mapped to AArch32 System register CNTHVS\_CVAL[63:0].

This register is present only when FEAT\_SEL2 is implemented, FEAT\_VHE is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHVS\_CVAL\_EL2 are UNDEFINED.

## Attributes

CNTHVS\_CVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the Secure EL2 virtual timer CompareValue.

When CNTHVS\_CTL\_EL2.ENABLE is 1, and TimerConditionMet is TRUE for the Secure EL2 virtual timer, the timer condition is met and all of the following are true:

- CNTHVS\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHVS\_CTL\_EL2.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTHVS\_CTL\_EL2.ENABLE is 0, the timer condition is not met, but CNTVCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHVS\_CVAL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHVS\_CVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b010 |

if !(IsFeatureImplemented(FEAT\_SEL2) &amp;&amp; IsFeatureImplemented(FEAT\_VHE) &amp;&amp; ↪ → IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; else X[t, 64] = CNTHVS\_CVAL\_EL2; elsif PSTATE.EL == EL3 then if SCR\_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = CNTHVS\_CVAL\_EL2;

MSR CNTHVS\_CVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b010 |

if !(IsFeatureImplemented(FEAT\_SEL2) &amp;&amp; IsFeatureImplemented(FEAT\_VHE) &amp;&amp; ↪ → IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED; else CNTHVS\_CVAL\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR\_EL3.EEL2 == '0' then UNDEFINED; else CNTHVS\_CVAL\_EL2 = X[t, 64];

MRS &lt;Xt&gt;, CNTV\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x168]; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CVAL_EL0;
```

MSR CNTV\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x168] = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CVAL_EL0 = X[t, 64];
```

## D24.10.14 CNTHVS\_TVAL\_EL2, Counter-timer Secure Virtual Timer TimerValue Register (EL2)

The CNTHVS\_TVAL\_EL2 characteristics are:

## Purpose

Holds the timer value for the Secure EL2 virtual timer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch64 System register CNTHVS\_TVAL\_EL2 bits [31:0] are architecturally mapped to AArch32 System register CNTHVS\_TVAL[31:0].

This register is present only when FEAT\_SEL2 is implemented, FEAT\_VHE is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTHVS\_TVAL\_EL2 are UNDEFINED.

## Attributes

CNTHVS\_TVAL\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL2 virtual timer.

On a read of this register:

- If CNTHVS\_CTL\_EL2.ENABLE is 0, the value returned is UNKNOWN.
- If CNTHVS\_CTL\_EL2.ENABLE is 1, the value returned is (CNTHVS\_CVAL\_EL2 - CNTVCT\_EL0).

On a write of this register, CNTHVS\_CVAL\_EL2 is set to (CNTVCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTHVS\_CTL\_EL2.ENABLE is 1, the timer condition is met when ((CNTVCT\_EL0 -

CNTHVS\_CVAL\_EL2) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTHVS\_CTL\_EL2.ISTATUS is set to 1.
- If CNTHVS\_CTL\_EL2.IMASK is 0, an interrupt is generated.

When CNTHVS\_CTL\_EL2.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTHVS\_TVAL\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTHVS\_TVAL\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_VHE) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2
```

MSR CNTHVS\_TVAL\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_VHE) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else
```

```
- PhysicalCountInt())<31:0>, 64); - PhysicalCountInt())<31:0>, 64);
```

```
CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

MRS &lt;Xt&gt;, CNTV\_TVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif HaveEL(EL2) && !ELIsInHost(EL0) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif !ELIsInHost(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() CNTVOFF))<31:0>, 64); else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTV\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif HaveEL(EL2) && !ELIsInHost(EL0) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2;
```

```
else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif !ELIsInHost(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

## D24.10.15 CNTKCTL\_EL1, Counter-timer Kernel Control Register

The CNTKCTL\_EL1 characteristics are:

## Purpose

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this register does not cause any event stream from the virtual counter to be generated, and does not control access to the counters and timers. The access to counters and timers at EL0 is controlled by CNTHCTL\_EL2.

When FEAT\_VHE is not implemented, or when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this register controls the generation of an event stream from the virtual counter, and access from EL0 to the physical counter, virtual counter, EL1 physical timers, and the virtual timer.

## Configuration

AArch64 System register CNTKCTL\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CNTKCTL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTKCTL\_EL1 are UNDEFINED.

## Attributes

CNTKCTL\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:20]

Reserved, RES0.

## CNTPMASK,bit [19]

## When FEAT\_RME is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

CNTVMASK,bit [18]

## When FEAT\_RME is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVNTIS, bit [17]

## When FEAT\_ECV is implemented:

Controls the scale of the generation of the event stream.

| EVNTIS   | Meaning                                                  |
|----------|----------------------------------------------------------|
| 0b0      | The CNTKCTL_EL1.EVNTI field applies to CNTVCT_EL0[15:0]. |
| 0b1      | The CNTKCTL_EL1.EVNTI field applies to CNTVCT_EL0[23:8]. |

This control applies regardless of the value of the CNTHCTL\_EL2.ECV bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVVCT, bit [16]

## When FEAT\_ECV is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1NVPCT, bit [15]

## When FEAT\_ECV is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVCT, bit [14]

## When FEAT\_ECV is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1TVT, bit [13]

## When FEAT\_ECV is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ECV, bit [12]

## When FEAT\_ECV is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1PTEN, bit [11]

## When FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL1PCTEN, bit [10]

## When FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL0PTEN, bit [9]

Traps EL0 accesses to the physical timer registers to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, the following registers are trapped and reported using EC syndrome value 0x18 :
- CNTP\_CTL\_EL0, CNTP\_CVAL\_EL0, and CNTP\_TVAL\_EL0.

- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 , MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTP\_CTL, CNTP\_CVAL, CNTP\_TVAL.

| EL0PTEN   | Meaning                                                          |
|-----------|------------------------------------------------------------------|
| 0b0       | EL0 accesses to the physical timer registers are trapped to EL1. |
| 0b1       | This control does not cause any instructions to be trapped.      |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0VTEN, bit [8]

Traps EL0 accesses to the virtual timer registers to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, accesses to the following registers are trapped and reported using EC syndrome value 0x18 :
- CNTV\_CTL\_EL0, CNTV\_CVAL\_EL0, and CNTV\_TVAL\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 , MRRC and MCRR accesses are trapped using EC syndrome value 0x04 :
- CNTV\_CTL, CNTV\_CVAL, and CNTV\_TVAL.

| EL0VTEN   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0       | EL0 accesses to the virtual timer registers are trapped.    |
| 0b1       | This control does not cause any instructions to be trapped. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTI, bits [7:4]

Selects which bit of CNTVCT\_EL0, as seen from EL1, is the trigger for the event stream generated from that counter when that stream is enabled.

If FEAT\_ECV is implemented, and CNTKCTL\_EL1.EVNTIS is 1, this field selects a trigger bit in the range 8 to 23 of CNTVCT\_EL0.

Otherwise, this field selects a trigger bit in the range 0 to 15 of CNTVCT\_EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTDIR, bit [3]

Controls which transition of the CNTVCT\_EL0 trigger bit, as seen from EL1 and defined by EVNTI, generates an event when the event stream is enabled.

| EVNTDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | A0to 1 transition of the trigger bit triggers an event. |
| 0b1       | A1to 0 transition of the trigger bit triggers an event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EVNTEN, bit [2]

When FEAT\_VHE is not implemented, or the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, enables the generation of an event stream from CNTVCT\_EL0 as seen from EL1.

| EVNTEN   | Meaning                    |
|----------|----------------------------|
| 0b0      | Disables the event stream. |
| 0b1      | Enables the event stream.  |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this control does not enable the event stream.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0VCTEN, bit [1]

Traps EL0 accesses to the frequency register and virtual counter registers to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, accesses to the following registers are trapped and reported using EC syndrome value 0x18 :
- CNTVCT\_EL0.
- CNTVCTSS\_EL0.
- If CNTKCTL\_EL1.EL0PCTEN is 0, CNTFRQ\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 , MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- CNTVCTand if CNTKCTL\_EL1.EL0PCTEN is 0, CNTFRQ.

| EL0VCTEN   | Meaning                                                                           |
|------------|-----------------------------------------------------------------------------------|
| 0b0        | EL0 accesses to the frequency register and virtual counter registers are trapped. |
| 0b1        | This control does not cause any instructions to be trapped.                       |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EL0PCTEN, bit [0]

Traps EL0 accesses to the frequency register and physical counter register to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, the following registers are trapped and reported using EC syndrome value 0x18 :
- CNTPCT\_EL0
- CNTPCTSS\_EL0
- If CNTKCTL\_EL1.EL0VCTEN is 0, CNTFRQ\_EL0.
- In AArch32 state, MCR or MRC accesses the following registers are trapped and reported using EC syndrome value 0x03 , MCRR or MRRC accesses are trapped and reported using EC syndrome value 0x04 :
- CNTPCT and if CNTKCTL\_EL1.EL0VCTEN is 0, CNTFRQ.

| EL0PCTEN   | Meaning                                                                           |
|------------|-----------------------------------------------------------------------------------|
| 0b0        | EL0 accesses to the frequency register and physical counter register are trapped. |
| 0b1        | This control does not cause any instructions to be trapped.                       |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this control does not cause any instructions to be trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTKCTL\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTKCTL\_EL1 or CNTKCTL\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then X[t, 64] = CNTKCTL_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTHCTL_EL2_VHE(CNTHCTL_EL2); else X[t, 64] = CNTKCTL_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CNTKCTL_EL1;
```

MSR CNTKCTL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then CNTKCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTHCTL_EL2 = CNTHCTL_EL2_VHE(X[t, 64]); else CNTKCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTKCTL_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTKCTL\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTKCTL_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CNTKCTL_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTKCTL\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTKCTL_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTKCTL_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.10.16 CNTP\_CTL\_EL0, Counter-timer Physical Timer Control Register

The CNTP\_CTL\_EL0 characteristics are:

## Purpose

Control register for the EL1 physical timer.

## Configuration

AArch64 System register CNTP\_CTL\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CNTP\_CTL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTP\_CTL\_EL0 are UNDEFINED.

## Attributes

CNTP\_CTL\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTP\_TV AL\_EL0 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_CTL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTP\_CTL\_EL0 or CNTP\_CTL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x180]; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CTL_EL2; else X[t, 64] = CNTP_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CTL_EL0;
```

MSR CNTP\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x180] = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CTL_EL2 = X[t, 64]; else CNTP_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CTL_EL0 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_CTL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVPCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = NVMem[0x180]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTP_CTL_EL0; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CNTP_CTL_EL0; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTP\_CTL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVPCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else NVMem[0x180] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTP_CTL_EL0 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTP_CTL_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.10.17 CNTP\_CVAL\_EL0, Counter-timer Physical Timer CompareValue Register

The CNTP\_CVAL\_EL0 characteristics are:

## Purpose

Holds the compare value for the EL1 physical timer.

## Configuration

AArch64 System register CNTP\_CVAL\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTP\_CVAL[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTP\_CVAL\_EL0 are UNDEFINED.

## Attributes

CNTP\_CVAL\_EL0 is a 64-bit register.

## Field descriptions

CompareValue

63

32

CompareValue

31

0

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL1 physical timer CompareValue.

When CNTP\_CTL\_EL0.ENABLE is 1, and TimerConditionMet is TRUE for the EL1 physical timer, the timer condition is met and all of the following are true:

- CNTP\_CTL\_EL0.ISTATUS is set to 1.
- If CNTP\_CTL\_EL0.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTP\_CTL\_EL0.ENABLE is 0, the timer condition is not met, but CNTPCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_CVAL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTP\_CVAL\_EL0 or CNTP\_CVAL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTP\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x178]; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHPS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHP_CVAL_EL2; else X[t, 64] = CNTP_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTP_CVAL_EL0;
```

MSR CNTP\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x178] = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = X[t, 64]; else CNTP_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_CVAL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVPCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = NVMem[0x178]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTP_CVAL_EL0; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CNTP_CVAL_EL0;
```

else

UNDEFINED;

When FEAT\_VHE is implemented MSR CNTP\_CVAL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVPCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else NVMem[0x178] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTP_CVAL_EL0 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTP_CVAL_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.10.18 CNTP\_TVAL\_EL0, Counter-timer Physical Timer TimerValue Register

The CNTP\_TVAL\_EL0 characteristics are:

## Purpose

Holds the timer value for the EL1 physical timer.

## Configuration

AArch64 System register CNTP\_TVAL\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CNTP\_TVAL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTP\_TVAL\_EL0 are UNDEFINED.

## Attributes

CNTP\_TVAL\_EL0 is a 64-bit register.

## Field descriptions

RES0

63

32

TimerValue

31

0

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL1 physical timer.

On a read of this register:

- If CNTP\_CTL\_EL0.ENABLE is 0, the value returned is UNKNOWN.
- If CNTP\_CTL\_EL0.ENABLE is 1, the value returned is (CNTP\_CVAL\_EL0 - CNTPCT\_EL0).

On a write of this register, CNTP\_CV AL\_EL0 is set to (CNTPCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTP\_CTL\_EL0.ENABLE is 1, the timer condition is met when (CNTPCT\_EL0 - CNTP\_CVAL\_EL0) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTP\_CTL\_EL0.ISTATUS is set to 1.
- If CNTP\_CTL\_EL0.IMASK is 0, an interrupt is generated.

When CNTP\_CTL\_EL0.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

Note

The value of CNTPCT\_EL0 used in these calculations is the value seen at the Exception level that the CNTPCT\_EL0 register is being read or written from.

The reset behavior of this field is:

· On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_TVAL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTP\_TVAL\_EL0 or CNTP\_TVAL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTP_TVAL_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - (PhysicalCountInt() -CNTPOFF_EL2))<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then
```

```
X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHPS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHPS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHP_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHP_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); else if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTP\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && CNTHCTL_EL2.EL1PTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then
```

```
CNTP_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTPOFF_EL2; else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHPS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHP_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); else CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTP\_TVAL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64); else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if CNTP_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTP_CVAL_EL0 - PhysicalCountInt())<31:0>, 64); else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTP\_TVAL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTP_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); else UNDEFINED;
```

## D24.10.19 CNTPCT\_EL0, Counter-timer Physical Count Register

The CNTPCT\_EL0 characteristics are:

## Purpose

Reads of CNTPCT\_EL0 return the 64-bit physical count value minus a physical offset.

## Configuration

All reads to the CNTPCT\_EL0 occur in program order relative to reads to CNTPCTSS\_EL0 or CNTPCT\_EL0.

AArch64 System register CNTPCT\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTPCT[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPCT\_EL0 are UNDEFINED.

## Attributes

CNTPCT\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## PhysicalCount, bits [63:0]

Physical count value.

If the access is not trapped and all of the following are true, then reads of CNTPCT\_EL0 from EL0 or EL1 return (PhysicalCountInt&lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;):

- EL2 is implemented and enabled in the current Security state.
- CNTHCTL\_EL2.ECV is 1.
- SCR\_EL3.ECVEn is 1.
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise, reads of CNTPCT\_EL0 return PhysicalCountInt&lt;63:0&gt;.

PhysicalCountInt is defined by 'The Physical Counter'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPCT\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTPCT_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PCTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then X[t, 64] = PhysicalCountInt() -CNTPOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then X[t, 64] = PhysicalCountInt() -CNTPOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then X[t, 64] = PhysicalCountInt();
```

## D24.10.20 CNTPCTSS\_EL0, Counter-timer Self-Synchronized Physical Count Register

The CNTPCTSS\_EL0 characteristics are:

## Purpose

Holds the self-synchronized view of the 64-bit physical count value.

## Configuration

All reads to the CNTPCTSS\_EL0 occur in program order relative to reads to CNTPCT\_EL0 or CNTPCTSS\_EL0.

This register is a view of the CNTPCT\_EL0 register for which reads appear to occur in program order relative to other instructions, without the need for any explicit synchronization. Reads of this register return a value consistent with the counter not being read until the read instruction is known to be non-speculative.

AArch64 System register CNTPCTSS\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTPCTSS[63:0].

This register is present only when FEAT\_ECV is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPCTSS\_EL0 are UNDEFINED.

## Attributes

CNTPCTSS\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                                     | 32   |
|----------------------------------------|------|
| Self-synchronized physical count value |      |
| 31                                     | 0    |
| Self-synchronized physical count value |      |

Physical count value.

If the access is not trapped and all of the following are true, then reads of CNTPCTSS\_EL0 from EL0 or EL1 return (PhysicalCountInt&lt;63:0&gt; - CNTPOFF\_EL2&lt;63:0&gt;):

- EL2 is implemented and enabled in the current Security state.
- CNTHCTL\_EL2.ECV is 1.
- SCR\_EL3.ECVEn is 1.
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise, reads of CNTPCTSS\_EL0 return PhysicalCountInt&lt;63:0&gt;.

PhysicalCountInt is defined by 'The Physical Counter'.

## SSPhysicalCount, bits [63:0]

Self-synchronized physical count value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPCTSS\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTPCTSS\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_ECV) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0PCTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL2) && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL2) && HCR_EL2.TGE == '0' && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' && !ELIsInHost(EL0) then X[t, 64] = PhysicalCountInt() -CNTPOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && CNTHCTL_EL2.EL1PCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else if IsFeatureImplemented(FEAT_ECV_POFF) && EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.ECVEn == '1') ↪ → && CNTHCTL_EL2.ECV == '1' then X[t, 64] = PhysicalCountInt() -CNTPOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then X[t, 64] = PhysicalCountInt();
```

## D24.10.21 CNTPOFF\_EL2, Counter-timer Physical Offset Register

The CNTPOFF\_EL2 characteristics are:

## Purpose

Holds the 64-bit physical offset. This is the offset for the AArch64 EL1 physical timer and counter when Enhanced Counter Virtualization is enabled.

## Configuration

The physical offset applies to:

- Direct reads of CNTPCT\_EL0 from EL0 or EL1.
- Indirect reads of the physical counter by the EL1 physical timer. See 'The Generic Timer in AArch64 state'.
- Indirect reads of the physical counter for timestamps generated by profiling logic. See 'The Statistical Profiling Extension' and 'AArch64 Self-hosted Trace'.

The physical offset only applies under conditions described by the relevant sections.

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_ECV\_POFF is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPOFF\_EL2 are UNDEFINED.

## Attributes

CNTPOFF\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63              | 32              |                 |
|-----------------|-----------------|-----------------|
| Physical offset | Physical offset | Physical offset |
| 31              | 0               |                 |
| Physical offset | Physical offset | Physical offset |

## PO, bits [63:0]

Physical offset.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPOFF\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTPOFF\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0000 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ECV_POFF) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1A8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ECVEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.ECVEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CNTPOFF_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CNTPOFF_EL2;
```

MSR CNTPOFF\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0000 | 0b110 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(IsFeatureImplemented(FEAT_ECV_POFF) && UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1A8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ECVEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.ECVEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else CNTPOFF_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTPOFF_EL2 = X[t, 64];
```

## D24.10.22 CNTPS\_CTL\_EL1, Counter-timer Physical Secure Timer Control Register

The CNTPS\_CTL\_EL1 characteristics are:

## Purpose

Control register for the secure physical timer, usually accessible at EL3 but configurably accessible at EL1 in Secure state.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPS\_CTL\_EL1 are UNDEFINED.

## Attributes

CNTPS\_CTL\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTPS\_TV AL\_EL1 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPS\_CTL\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTPS_CTL_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' then UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CNTPS_CTL_EL1; else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = CNTPS_CTL_EL1;
```

MSR CNTPS\_CTL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' then UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else CNTPS_CTL_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then CNTPS_CTL_EL1 = X[t, 64];
```

## D24.10.23 CNTPS\_CVAL\_EL1, Counter-timer Physical Secure Timer CompareValue Register

The CNTPS\_CVAL\_EL1 characteristics are:

## Purpose

Holds the compare value for the secure physical timer, usually accessible at EL3 but configurably accessible at EL1 in Secure state.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPS\_CVAL\_EL1 are UNDEFINED.

## Attributes

CNTPS\_CVAL\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the secure physical timer CompareValue.

When CNTPS\_CTL\_EL1.ENABLE is 1, and TimerConditionMet is TRUE for the EL1 secure physical timer, the timer condition is met and all of the following are true:

- CNTPS\_CTL\_EL1.ISTATUS is set to 1.
- If CNTPS\_CTL\_EL1.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTPS\_CTL\_EL1.ENABLE is 0, the timer condition is not met, but CNTPCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPS\_CVAL\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, CNTPS_CVAL_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CNTPS_CVAL_EL1; else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = CNTPS_CVAL_EL1;
```

MSR CNTPS\_CVAL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else CNTPS_CVAL_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then CNTPS_CVAL_EL1 = X[t, 64];
```

```
then
```

```
then
```

## D24.10.24 CNTPS\_TVAL\_EL1, Counter-timer Physical Secure Timer TimerValue Register

The CNTPS\_TVAL\_EL1 characteristics are:

## Purpose

Holds the timer value for the secure physical timer, usually accessible at EL3 but configurably accessible at EL1 in Secure state.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTPS\_TVAL\_EL1 are UNDEFINED.

## Attributes

CNTPS\_TVAL\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the secure physical timer.

On a read of this register:

- If CNTPS\_CTL\_EL1.ENABLE is 0, the value returned is UNKNOWN.
- If CNTPS\_CTL\_EL1.ENABLE is 1, the value returned is (CNTPS\_CVAL\_EL1 - CNTPCT\_EL0).

On a write of this register, CNTPS\_CV AL\_EL1 is set to (CNTPCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTPS\_CTL\_EL1.ENABLE is 1, the timer condition is met when (CNTPCT\_EL0 - CNTPS\_CVAL\_EL1) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTPS\_CTL\_EL1.ISTATUS is set to 1.
- If CNTPS\_CTL\_EL1.IMASK is 0, an interrupt is generated.

When CNTPS\_CTL\_EL1.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPS\_TVAL\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTPS\_TVAL\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b000 |

```
PhysicalCountInt())<31:0>, 64);
```

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' then UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else if CNTPS_CTL_EL1.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTPS_CVAL_EL1 -else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CNTPS_CTL_EL1.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTPS_CVAL_EL1 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTPS\_TVAL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b111 | 0b1110 | 0b0010 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && SCR_EL3.NS == '0' then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ST == '0' then UNDEFINED; elsif SCR_EL3.EEL2 == '1' then UNDEFINED; elsif SCR_EL3.ST == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
else CNTPS_CVAL_EL1 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then CNTPS_CVAL_EL1 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

## D24.10.25 CNTV\_CTL\_EL0, Counter-timer Virtual Timer Control Register

The CNTV\_CTL\_EL0 characteristics are:

## Purpose

Control register for the virtual timer.

## Configuration

AArch64 System register CNTV\_CTL\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CNTV\_CTL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTV\_CTL\_EL0 are UNDEFINED.

## Attributes

CNTV\_CTL\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

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

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTV\_TV AL\_EL0 continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_CTL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTV\_CTL\_EL0 or CNTV\_CTL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x170]; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CTL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CTL_EL2; else X[t, 64] = CNTV_CTL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CTL_EL0;
```

MSR CNTV\_CTL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else
```

```
CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x170] = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CTL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CTL_EL2 = X[t, 64]; else CNTV_CTL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CTL_EL0 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTV\_CTL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = NVMem[0x170]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTV_CTL_EL0; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CNTV_CTL_EL0; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTV\_CTL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else NVMem[0x170] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTV_CTL_EL0 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTV_CTL_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.10.26 CNTV\_CVAL\_EL0, Counter-timer Virtual Timer CompareValue Register

The CNTV\_CVAL\_EL0 characteristics are:

## Purpose

Holds the compare value for the virtual timer.

## Configuration

AArch64 System register CNTV\_CVAL\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTV\_CVAL[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTV\_CVAL\_EL0 are UNDEFINED.

## Attributes

CNTV\_CVAL\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63           | 32           |              |
|--------------|--------------|--------------|
| CompareValue | CompareValue | CompareValue |
| 31           | 0            |              |
| CompareValue | CompareValue | CompareValue |

## CompareValue, bits [63:0]

Holds the EL1 virtual timer CompareValue.

When CNTV\_CTL\_EL0.ENABLE is 1, and TimerConditionMet is TRUE for the EL1 virtual timer, the timer condition is met and all of the following are true:

- CNTV\_CTL\_EL0.ISTATUS is set to 1.
- If CNTV\_CTL\_EL0.IMASK is 0, an interrupt is generated.

TimerConditionMet is defined by 'Operation of the CompareValue views of the timers'.

The CompareValue view of the timer acts like a 64-bit upcounter timer.

When CNTV\_CTL\_EL0.ENABLE is 0, the timer condition is not met, but CNTVCT\_EL0 continues to count.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_CVAL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTV\_CVAL\_EL0 or CNTV\_CVAL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTV\_CVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x168]; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then X[t, 64] = CNTHVS_CVAL_EL2; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then X[t, 64] = CNTHV_CVAL_EL2; else X[t, 64] = CNTV_CVAL_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CNTV_CVAL_EL0;
```

MSR CNTV\_CVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x168] = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = X[t, 64]; elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = X[t, 64]; else CNTV_CVAL_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTV_CVAL_EL0 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTV\_CVAL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = NVMem[0x168]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = CNTV_CVAL_EL0; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CNTV_CVAL_EL0; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTV\_CVAL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then if EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1NVVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else NVMem[0x168] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTV_CVAL_EL0 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTV_CVAL_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.10.27 CNTV\_TVAL\_EL0, Counter-timer Virtual Timer TimerValue Register

The CNTV\_TVAL\_EL0 characteristics are:

## Purpose

Holds the timer value for the EL1 virtual timer.

## Configuration

AArch64 System register CNTV\_TVAL\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CNTV\_TVAL[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTV\_TVAL\_EL0 are UNDEFINED.

## Attributes

CNTV\_TVAL\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TimerValue, bits [31:0]

The TimerValue view of the EL1 virtual timer.

On a read of this register:

- If CNTV\_CTL\_EL0.ENABLE is 0, the value returned is UNKNOWN.
- If CNTV\_CTL\_EL0.ENABLE is 1, the value returned is (CNTV\_CVAL\_EL0 - CNTVCT\_EL0).

On a write of this register, CNTV\_CV AL\_EL0 is set to (CNTVCT\_EL0 + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTV\_CTL\_EL0.ENABLE is 1, the timer condition is met when (CNTVCT\_EL0 - CNTV\_CVAL\_EL0) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTV\_CTL\_EL0.ISTATUS is set to 1.
- If CNTV\_CTL\_EL0.IMASK is 0, an interrupt is generated.

When CNTV\_CTL\_EL0.ENABLE is 0, the TimerValue cannot be read but continues to decrement. When the timer is enabled, the TimerValue represents the elapsed time whether that time was spent enabled or disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_TVAL\_EL0

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CNTV\_TVAL\_EL0 or CNTV\_TVAL\_EL02 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTV\_TVAL\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif HaveEL(EL2) && !ELIsInHost(EL0) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then
```

```
if CNTHVS_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHVS_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then if CNTHV_CTL_EL2.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTHV_CVAL_EL2 - PhysicalCountInt())<31:0>, 64); elsif !ELIsInHost(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 -PhysicalCountInt())<31:0>, 64); elsif PSTATE.EL == EL3 then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() CNTVOFF))<31:0>, 64); else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - PhysicalCountInt())<31:0>, 64);
```

MSR CNTV\_TVAL\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == ↪ → '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL0) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif HaveEL(EL2) && !ELIsInHost(EL0) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_ECV) && CNTHCTL_EL2.EL1TVT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2;
```

```
else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) && IsCurrentSecurityState(SS_Secure) && IsFeatureImplemented(FEAT_SEL2) then CNTHVS_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif ELIsInHost(EL2) && !IsCurrentSecurityState(SS_Secure) then CNTHV_CVAL_EL2 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif !ELIsInHost(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) CNTVOFF; else CNTV_CVAL_EL0 = SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt();
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CNTV\_TVAL\_EL02

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then if CNTV_CTL_EL0.ENABLE == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = ZeroExtend((CNTV_CVAL_EL0 - (PhysicalCountInt() -CNTVOFF_EL2))<31:0>, 64); else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CNTV\_TVAL\_EL02, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1110 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CNTV_CVAL_EL0 = (SignExtend(X[t, 64]<31:0>, 64) + PhysicalCountInt()) -CNTVOFF_EL2; else UNDEFINED;
```

## D24.10.28 CNTVCT\_EL0, Counter-timer Virtual Count Register

The CNTVCT\_EL0 characteristics are:

## Purpose

Reads of CNTVCT\_EL0 return the 64-bit physical count value minus a virtual offset.

## Configuration

All reads to the CNTVCT\_EL0 occur in program order relative to reads to CNTVCTSS\_EL0 or CNTVCT\_EL0.

AArch64 System register CNTVCT\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTVCT[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTVCT\_EL0 are UNDEFINED.

## Attributes

CNTVCT\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## VirtualCount, bits [63:0]

Virtual count value.

When EL2 is implemented, if the access is not trapped, and any of the following are true, then reads of CNTVCT\_EL0 from EL0 and EL1 return (PhysicalCountInt&lt;63:0&gt; - CNTVOFF\_EL2&lt;63:0&gt;):

- All of the following are true:
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- CNTVCT\_EL0 is read from EL0.
- All of the following are true:
- The Effective value of HCR\_EL2.E2H is 0.
- CNTVCT\_EL0 is read from EL2.
- CNTVCT\_EL0 is read from EL1 or EL3.

Otherwise reads of CNTVCT\_EL0 return PhysicalCountInt&lt;63:0&gt;.

PhysicalCountInt is defined by 'The Physical Counter'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVCT\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTVCT\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VCTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else if HaveEL(EL2) && (!EL2Enabled() || !ELIsInHost(EL0)) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && !ELUsingAArch32(EL2) && ↪ → (!EL2Enabled() || !ELIsInHost(EL0)) then X[t, 64] = PhysicalCountInt() CNTVOFF; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else if HaveEL(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL2) && !ELIsInHost(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then X[t, 64] = PhysicalCountInt() CNTVOFF; else X[t, 64] = PhysicalCountInt();
```

## D24.10.29 CNTVCTSS\_EL0, Counter-timer Self-Synchronized Virtual Count Register

The CNTVCTSS\_EL0 characteristics are:

## Purpose

Reads of CNTVCTSS\_EL0 return the 64-bit physical count value minus a virtual offset.

## Configuration

All reads to the CNTVCTSS\_EL0 occur in program order relative to reads to CNTVCT\_EL0 or CNTVCTSS\_EL0.

This register is a view of the CNTVCT\_EL0 register for which reads appear to occur in program order relative to other instructions, without the need for any explicit synchronization. Reads of this register return a value consistent with the counter not being read until the read instruction is known to be non-speculative.

AArch64 System register CNTVCTSS\_EL0 bits [63:0] are architecturally mapped to AArch32 System register CNTVCTSS[63:0].

This register is present only when FEAT\_ECV is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTVCTSS\_EL0 are UNDEFINED.

## Attributes

CNTVCTSS\_EL0 is a 64-bit register.

## Field descriptions

| 63                                    | 32   |
|---------------------------------------|------|
| Self-synchronized virtual count value |      |
| 31                                    | 0    |
| Self-synchronized virtual count value |      |

## SSVirtualCount, bits [63:0]

Self-synchronized virtual count value.

When EL2 is implemented, if the access is not trapped, and any of the following are true, then reads of CNTVCTSS\_EL0 from EL0 and EL1 return (PhysicalCountInt&lt;63:0&gt; - CNTVOFF\_EL2&lt;63:0&gt;):

- All of the following are true:
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- CNTVCTSS\_EL0 is read from EL0.
- All of the following are true:
- The Effective value of HCR\_EL2.E2H is 0.
- CNTVCTSS\_EL0 is read from EL2.
- CNTVCTSS\_EL0 is read from EL1 or EL3.

Otherwise reads of CNTVCTSS\_EL0 return PhysicalCountInt&lt;63:0&gt;.

PhysicalCountInt is defined by 'The Physical Counter'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVCTSS\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTVCTSS\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b0000 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ECV) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && CNTKCTL_EL1.EL0VCTEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && CNTHCTL_EL2.EL0VCTEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else if HaveEL(EL2) && (!EL2Enabled() || !ELIsInHost(EL0)) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) && !ELUsingAArch32(EL2) && ↪ → (!EL2Enabled() || !ELIsInHost(EL0)) then X[t, 64] = PhysicalCountInt() CNTVOFF; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL1 then if EL2Enabled() && CNTHCTL_EL2.EL1TVCT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else if HaveEL(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL2 then if HaveEL(EL2) && !ELIsInHost(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; else X[t, 64] = PhysicalCountInt(); elsif PSTATE.EL == EL3 then if HaveEL(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then X[t, 64] = PhysicalCountInt() -CNTVOFF_EL2; elsif HaveEL(EL2) && IsFeatureImplemented(FEAT_AA32EL2) then X[t, 64] = PhysicalCountInt() CNTVOFF; else X[t, 64] = PhysicalCountInt();
```

## D24.10.30 CNTVOFF\_EL2, Counter-timer Virtual Offset Register

The CNTVOFF\_EL2 characteristics are:

## Purpose

Holds the 64-bit virtual offset. This is the offset for the AArch64 virtual timers and counters.

## Configuration

The virtual offset applies to:

- Direct reads of CNTVCT\_EL0.
- Indirect reads of the virtual counter by the EL1 virtual timer. See 'The Generic Timer in AArch64 state'.
- Indirect reads of the virtual counter for timestamps generated by profiling logic. See 'The Statistical Profiling Extension' and 'AArch64 Self-hosted Trace'.

The virtual offset only applies under conditions described by the relevant sections.

AArch64 System register CNTVOFF\_EL2 bits [63:0] are architecturally mapped to AArch32 System register CNTVOFF[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CNTVOFF\_EL2 are UNDEFINED.

## Attributes

CNTVOFF\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |                | 32   |
|------|----------------|------|
|      | Virtual offset |      |
| 31   |                | 0    |
|      | Virtual offset |      |

## VOffset, bits [63:0]

Virtual offset.

If the Generic counter is implemented at a size less than 64 bits, then this field is permitted to be implemented at the same width as the counter, and the upper bits are RES0.

The value of this field is treated as zero-extended in all counter calculations.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVOFF\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CNTVOFF\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0000 | 0b011 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then

X[t, 64] = NVMem[0x060];

elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

X[t, 64] = CNTVOFF\_EL2;

elsif PSTATE.EL == EL3 then

X[t, 64] = CNTVOFF\_EL2;

MSR CNTVOFF\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1110 | 0b0000 | 0b011 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then NVMem[0x060] = X[t, 64]; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then CNTVOFF\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CNTVOFF\_EL2 = X[t, 64];