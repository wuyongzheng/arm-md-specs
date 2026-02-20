## G8.2.78 HTTBR, Hyp Translation Table Base Register

The HTTBR characteristics are:

## Purpose

Holds the base address of the translation table for the initial lookup for stage 1 of an address translation in the EL2 translation regime, and other information for this translation regime.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HTTBR bits [47:0] are architecturally mapped to AArch64 System register TTBR0\_EL2[47:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HTTBR are UNDEFINED.

## Attributes

HTTBR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## BADDR, bits [47:1]

Translation table base address, bits[47:x], Bits [x-1:1] are RES0, with the additional requirement that if bits[x-1:3] are not all zero, this is a misaligned translation table base address, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Register bits [x-1:3] are treated as if all the bits are zero. The value read back from these bits is either the value written or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

x is determined from the value of HTCR.T0SZ as follows:

- If HTCR.T0SZ is 0 or 1, x = 5 - HTCR.T0SZ.
- If HTCR.T0SZ is greater than 1, x = 14 - HTCR.T0SZ.

If bits[47:40] of the translation table base address are not zero, an Address size fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

When FEAT\_TTCNP is implemented:

Common not Private. This bit indicates whether each entry that is pointed to by HTTBR is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of HTTBR.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by HTTBR are permitted to differ from corresponding entries for HTTBR for other PEs in the Inner Shareable domain. This is not affected by the value of HTTBR.CnP on those other PEs. |
| 0b1   | The translation table entries pointed to by HTTBR are the same as the translation table entries pointed to by HTTBR on every other PE in the Inner Shareable domain for which the value of HTTBR.CnP is 1.                     |

Note

If the value of the HTTBR.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those HTTBRs do not point to the same translation table entries when the other conditions specified for the case when the value of CnP is 1 apply, then the results of translations are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing HTTBR

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0100 |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t, t2] = HTTBR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t, t2] = HTTBR;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0100 |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); else UNDEFINED; elsif PSTATE.EL == EL2 then HTTBR = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HTTBR = R[t, t2];
```