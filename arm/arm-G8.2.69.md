## G8.2.69 HMAIR0, Hyp Memory Attribute Indirection Register 0

The HMAIR0 characteristics are:

## Purpose

Along with HMAIR1, provides the memory attribute encodings corresponding to the possible AttrIndx values in a Long-descriptor format translation table entry for stage 1 translations for memory accesses from Hyp mode.

AttrIndx[2] indicates the HMAIR register to be used:

- When AttrIndx[2] is 0, HMAIR0 is used.
- When AttrIndx[2] is 1, HMAIR1 is used.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HMAIR0 bits [31:0] are architecturally mapped to AArch64 System register MAIR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HMAIR0 are UNDEFINED.

## Attributes

HMAIR0 is a 32-bit register.

## Field descriptions

When TTBCR.EAE == '1':

<!-- image -->

## Attr&lt;n&gt; , bits [8n+7:8n], for n = 3 to 0

The memory attribute encoding for an AttrIndx[2:0] entry in a Long descriptor format translation table entry, where:

- AttrIndx[2:0] gives the value of &lt;n&gt; in Attr&lt;n&gt;.
- AttrIndx[2] defines which MAIR to access. Attr7 to Attr4 are in MAIR1, and Attr3 to Attr0 are in MAIR0.

Bits [7:4] are encoded as follows:

| Attr<n>[7:4]        | Meaning                                                                    |
|---------------------|----------------------------------------------------------------------------|
| 0b0000              | Device memory. See encoding of Attr<n>[3:0] for the type of Device memory. |
| 0b00 RW, RWnot 0b00 | Normal memory, Outer Write-Through Transient.                              |
| 0b0100              | Normal memory, Outer Non-cacheable.                                        |
| 0b01 RW, RWnot 0b00 | Normal memory, Outer Write-Back Transient.                                 |
| 0b10 RW             | Normal memory, Outer Write-Through Non-transient.                          |
| 0b11 RW             | Normal memory, Outer Write-Back Non-transient.                             |

R=Outer Read-Allocate policy, W = Outer Write-Allocate policy.

The meaning of bits [3:0] depends on the value of bits [7:4]:

| Attr<n>[3:0]        | Meaning when Attr<n>[7:4] is 0b0000   | Meaning when Attr<n>[7:4] is not 0b0000                      |
|---------------------|---------------------------------------|--------------------------------------------------------------|
| 0b0000              | Device-nGnRnE memory                  | UNPREDICTABLE                                                |
| 0b00 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Through Transient                 |
| 0b0100              | Device-nGnRE memory                   | Normal memory, Inner Non-cacheable                           |
| 0b01 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Back Transient                    |
| 0b1000              | Device-nGRE memory                    | Normal memory, Inner Write-Through Non-transient (RW= 0b00 ) |
| 0b10 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Through Non-transient             |
| 0b1100              | Device-GRE memory                     | Normal memory, Inner Write-Back Non-transient (RW= 0b00 )    |
| 0b11 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Back Non-transient                |

R=Inner Read-Allocate policy, W = Inner Write-Allocate policy.

The R and W bits in some Attr&lt;n&gt; fields have the following meanings:

| R or W   | Meaning     |
|----------|-------------|
| 0b0      | No Allocate |
| 0b1      | Allocate    |

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HMAIR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HMAIR0; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HMAIR0;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HMAIR0 = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HMAIR0 = R[t];
```