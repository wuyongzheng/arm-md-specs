## G8.2.173 VTTBR, Virtualization Translation Table Base Register

The VTTBR characteristics are:

## Purpose

Holds the base address of the translation table for the initial lookup for stage 2 of an address translation in the Non-secure PL1&amp;0 translation regime, and other information for this translation regime.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register VTTBR bits [63:0] are architecturally mapped to AArch64 System register VTTBR\_EL2[63:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to VTTBR are UNDEFINED.

## Attributes

VTTBR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## VMID, bits [55:48]

The VMID for the translation table.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to 0x00 .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## BADDR, bits [47:1]

Translation table base address, bits[47:x], Bits [x-1:1] are RES0, with the additional requirement that if bits[x-1:3] are not all zero, this is a misaligned translation table base address, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Register bits [x-1:3] are treated as if all the bits are zero. The value read back from these bits is either the value written or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

x is determined from the value of VTCR.SL0 and VTCR.T0SZ as follows:

- If VTCR.SL0 is 0b00 , meaning that lookup starts at level 2, then x is 14 - VTCR.T0SZ.
- If VTCR.SL0 is 0b01 , meaning that lookup starts at level 1, then x is 5 - VTCR.T0SZ.

- If VTCR.SL0 is either 0b10 or 0b11 then a stage 2 level 1 Translation fault is generated.

If bits[47:40] of the translation table base address are not zero, an Address size fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

## When FEAT\_TTCNP is implemented:

Common not Private. This bit indicates whether each entry that is pointed to by VTTBR is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of VTTBR.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                             |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by VTTBR are permitted to differ from the entries for VTTBR for other PEs in the Inner Shareable domain. This is not affected by the value of the current VMID.                            |
| 0b1   | The translation table entries pointed to by VTTBR are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of VTTBR.CnP is 1 and theVMID is the same as the current VMID. |

When a TLB combines entries from stage 1 translation and stage 2 translation into a single entry, that entry can only be shared between different PEs if the value of the CnP bit is 1 for both stage 1 and stage 2.

Note

If the value of the VTTBR.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those VTTBRs do not point to the same translation table entries when the VMID value is the same as the current VMID, then the results of translations are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing VTTBR

Accesses to this register use the following encodings in the System register encoding space:

```
MRRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <Rt2>, <CRm>
```

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0110 |

```
if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t, t2] = VTTBR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t, t2] = VTTBR;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0110 |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); else UNDEFINED; elsif PSTATE.EL == EL2 then VTTBR = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else VTTBR = R[t, t2];
```