## G8.2.75 HSTR, Hyp System Trap Register

The HSTR characteristics are:

## Purpose

Controls trapping to Hyp mode of Non-secure accesses, at EL1 or lower, to System registers in the coproc == 0b1111 encoding space:

- By the CRn value used to access the register using MCR or MRC instruction.
- By the CRm value used to access the register using MCRR or MRRC instruction.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HSTR bits [31:0] are architecturally mapped to AArch64 System register HSTR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HSTR are UNDEFINED.

## Attributes

HSTR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16, 14, 4]

Reserved, RES0.

## T&lt;n&gt; , bits [n], for n = 15 to 15, 13 to 5, 3 to 0

The remaining fields control whether Non-secure EL0 and EL1 accesses, using MCR or MRC instructions, reported using EC syndrome value 0x03 , and MCRR or MRRC instructions, reported using EC syndrome value 0x04 , to the System registers in the coproc == 0b1111 encoding space are trapped to Hyp mode:

| T<n>   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on Non-secure EL0 or EL1 accesses to System registers.                                                                                                                                                                                                                                                                                                                                                                                                                |
| 0b1    | Any Non-secure EL1 MCRor MRCaccess with coproc == 0b1111 and CRn == <n> is trapped to Hyp mode. ANon-secure EL0 MCRor MRCaccess with these values is trapped to Hyp mode only if the access is not UNDEFINED when the value of this field is 0. Any Non-secure EL1 MCRRor MRRCaccess with coproc == 0b1111 and CRm==<n>is trapped to Hyp mode. ANon-secure EL0 MCRRor MRRCaccess with these values is trapped to Hyp mode only if the access is not UNDEFINED when the value of this field is 0. |

For example, when HSTR.T7 is 1, for instructions executed at Non-secure EL1:

- An MCR or MRC instruction with coproc set to 0b1111 and &lt;CRn&gt; set to c7 is trapped to Hyp mode.
- An MCRR or MRRC instruction with coproc set to 0b1111 and &lt;CRm&gt; set to c7 is trapped to Hyp mode.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HSTR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b011  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HSTR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HSTR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b011  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then HSTR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HSTR = R[t];
```