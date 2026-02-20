## G8.2.170 VMPIDR, Virtualization Multiprocessor ID Register

The VMPIDR characteristics are:

## Purpose

Holds the value of the Virtualization Multiprocessor ID. This is the value returned by Non-secure EL1 reads of MPIDR, which in a multiprocessor system, provides an additional PE identification system.

## Configuration

If EL2 is not implemented but EL3 is implemented, this register takes the value of the MPIDR.

AArch32 System register VMPIDR bits [31:0] are architecturally mapped to AArch64 System register VMPIDR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to VMPIDR are UNDEFINED.

## Attributes

VMPIDR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31 30 29   | 25 24 23   | 16   | 8 7   |      |
|------------|------------|------|-------|------|
| M U        | MT         | Aff2 | Aff1  | Aff0 |

## M, bit [31]

Indicates whether this implementation includes the functionality introduced by the Armv7 Multiprocessing Extensions.

| M   | Meaning                                                                                  |
|-----|------------------------------------------------------------------------------------------|
| 0b0 | This implementation does not include the Armv7 Multiprocessing Extensions functionality. |
| 0b1 | This implementation includes the Armv7 Multiprocessing Extensions functionality.         |

Access to this field is RES1.

## U, bit [30]

Indicates a Uniprocessor system, as distinct from PE 0 in a multiprocessor system.

| U   | Meaning                                       |
|-----|-----------------------------------------------|
| 0b0 | Processor is part of a multiprocessor system. |
| 0b1 | Processor is part of a uniprocessor system.   |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MPIDR.U.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [29:25]

Reserved, RES0.

## MT, bit [24]

Indicates whether the lowest level of affinity consists of logical PEs that are implemented using a multithreading type approach. See the description of Aff0 for more information about affinity levels.

| MT   | Meaning                                                                 |
|------|-------------------------------------------------------------------------|
| 0b0  | Performance of PEs at the lowest affinity level is largely independent. |
| 0b1  | Performance of PEs at the lowest affinity level is very interdependent. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MPIDR.MT.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Aff2, bits [23:16]

Affinity level 2. See the description of Aff0 for more information.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MPIDR.Aff2.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Aff1, bits [15:8]

Affinity level 1. See the description of Aff0 for more information.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MPIDR.Aff1.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Aff0, bits [7:0]

Affinity level 0. The value of the MPIDR.{Aff2, Aff1, Aff0} or MPIDR\_EL1.{Aff3, Aff2, Aff1, Aff0} set of fields of each PE must be unique within the system as a whole.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MPIDR.Aff0.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing VMPIDR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0000 | 0b0000 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = VMPIDR; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then R[t] = MPIDR; elsif SCR.NS == '0' then UNDEFINED; else R[t] = VMPIDR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0000 | 0b0000 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then VMPIDR = R[t]; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then return; elsif SCR.NS == '0' then UNDEFINED; else VMPIDR = R[t];
```

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b101  |

if !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) then R[t] = VMPIDR\_EL2&lt;31:0&gt;; elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) then R[t] = VMPIDR; else R[t] = MPIDR; elsif PSTATE.EL == EL2 then R[t] = MPIDR; elsif PSTATE.EL == EL3 then R[t] = MPIDR;