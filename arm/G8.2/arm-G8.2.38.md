## G8.2.38 DACR, Domain Access Control Register

The DACR characteristics are:

## Purpose

Defines the access permission for each of the sixteen memory domains.

## Configuration

This register has no function when TTBCR.EAE is set to 1, to select the Long-descriptor translation table format.

AArch32 System register DACR bits [31:0] are architecturally mapped to AArch64 System register DACR32\_EL2[31:0].

This register is banked between DACR and DACR\_S and DACR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DACR are UNDEFINED.

## Attributes

DACRis a 32-bit register.

This register has the following instances:

- DACR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- DACR\_S, when FEAT\_AA32EL3 is implemented.
- DACR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

| 31 30 29 28 27   | 26   | 25 24   | 23 22   | 21 20   | 19 18   | 17 16   | 15 14   | 13 12   | 11 10   | 9 8   | 7 6   | 5 4   | 3 2   | 1 0   |
|------------------|------|---------|---------|---------|---------|---------|---------|---------|---------|-------|-------|-------|-------|-------|
| D15 D14          | D13  | D12     | D11     | D10     | D9      | D8      | D7      | D6      | D5      | D4    | D3    | D2    | D1    | D0    |

## D&lt;n&gt; , bits [2n+1:2n], for n = 15 to 0

Domain n access permission, where n = 0 to 15. Permitted values are:

| D<n>   | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b00   | No access. Any access to the domain generates a Domain fault.                            |
| 0b01   | Client. Accesses are checked against the permission bits in the translation tables.      |
| 0b11   | Manager. Accesses are not checked against the permission bits in the translation tables. |

The value

0b10 is reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DACR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0011 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T3 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DACR_NS; else R[t] = DACR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DACR_NS; else R[t] = DACR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = DACR_S; else R[t] = DACR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0011 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T3 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then DACR_NS = R[t]; else DACR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then DACR_NS = R[t]; else DACR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if SCR.NS == '0' then DACR_S = R[t]; else DACR_NS = R[t];
```