## G8.5 Activity Monitors registers

This section lists the Activity Monitoring registers in AArch32.

## G8.5.1 AMCFGR, Activity Monitors Configuration Register

The AMCFGR characteristics are:

## Purpose

Global configuration register for the activity monitors.

Provides information on supported features, the number of counter groups implemented, the total number of activity monitor event counters implemented, and the size of the counters. AMCFGR is applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch32 System register AMCFGR bits [31:0] are architecturally mapped to AArch64 System register AMCFGR\_EL0[31:0].

AArch32 System register AMCFGR bits [31:0] are architecturally mapped to External register AMCFGR[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCFGR are UNDEFINED.

## Attributes

AMCFGRis a 32-bit register.

## Field descriptions

<!-- image -->

## NCG, bits [31:28]

Defines the number of counter groups implemented, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NCG    | Meaning                         |
|--------|---------------------------------|
| 0b0000 | One counter group implemented.  |
| 0b0001 | Two counter groups implemented. |

All other values are reserved.

Access to this field is RO.

## Bits [27:25]

Reserved, RES0.

## HDBG, bit [24]

Halt-on-debug supported.

This feature must be supported, and so this bit is 0b1 .

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## Bits [23:14]

Reserved, RAZ.

## SIZE, bits [13:8]

Defines the size of the activity monitor event counters, minus one.

The counters are 64-bit, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. The counters are at doubleword-aligned addresses.

Reads as 0b111111

Access to this field is RO.

## N, bits [7:0]

Defines the number of activity monitor event counters implemented in all groups, minus one.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMCFGR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

| HDBG   | Meaning                 |
|--------|-------------------------|
| 0b0    | AMCR.HDBGis RES0.       |
| 0b1    | AMCR.HDBGis read/write. |

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCFGR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCFGR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCFGR; elsif PSTATE.EL == EL3 then R[t] = AMCFGR;
```

## G8.5.2 AMCGCR, Activity Monitors Counter Group Configuration Register

The AMCGCR characteristics are:

## Purpose

Provides information on the number of activity monitor event counters implemented within each counter group.

## Configuration

AArch32 System register AMCGCR bits [31:0] are architecturally mapped to AArch64 System register AMCGCR\_EL0[31:0].

AArch32 System register AMCGCR bits [31:0] are architecturally mapped to External register AMCGCR[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCGCR are UNDEFINED.

## Attributes

AMCGCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Counter Group 1 Number of Counters. The number of counters in the auxiliary counter group.

In an implementation that includes FEAT\_AMUv1, the permitted range of values is 0 to 16.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CG0NC, bits [7:0]

Counter Group 0 Number of Counters. The number of counters in the architected counter group.

Reads as 0x04

Access to this field is RO.

## Accessing AMCGCR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCGCR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCGCR;
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCGCR; elsif PSTATE.EL == EL3 then R[t] = AMCGCR;
```

## G8.5.3 AMCNTENCLR0, Activity Monitors Count Enable Clear Register 0

The AMCNTENCLR0 characteristics are:

## Purpose

Disable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;.

## Configuration

AArch32 System register AMCNTENCLR0 bits [31:0] are architecturally mapped to AArch64 System register AMCNTENCLR0\_EL0[31:0].

AArch32 System register AMCNTENCLR0 bits [31:0] are architecturally mapped to External register AMCNTENCLR0[31:0].

AArch32 System register AMCNTENCLR0 bits [31:0] are architecturally mapped to External register AMCNTENSET0[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCNTENCLR0 are UNDEFINED.

## Attributes

AMCNTENCLR0is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 16 15   | 3 2 1 0     |
|------|---------|-------------|
| RES0 | RAZ/WI  | P3 P2 P1 P0 |

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter disable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n> is disabled. When written, has no effect. |

0b1

When read, means that AMEVCNTR0&lt;n&gt; is enabled. When written, disables AMEVCNTR0&lt;n&gt;.

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR0

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR0; elsif PSTATE.EL == EL3 then R[t] = AMCNTENCLR0;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) then AMCNTENCLR0 = R[t];
```

else

UNDEFINED;

## G8.5.4 AMCNTENCLR1, Activity Monitors Count Enable Clear Register 1

The AMCNTENCLR1 characteristics are:

## Purpose

Disable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;.

## Configuration

AArch32 System register AMCNTENCLR1 bits [31:0] are architecturally mapped to AArch64 System register AMCNTENCLR1\_EL0[31:0].

AArch32 System register AMCNTENCLR1 bits [31:0] are architecturally mapped to External register AMCNTENCLR1[31:0].

AArch32 System register AMCNTENCLR1 bits [31:0] are architecturally mapped to External register AMCNTENSET1[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCNTENCLR1 are UNDEFINED.

## Attributes

AMCNTENCLR1is a 32-bit register.

## Field descriptions

| 31   | 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------|

## Bits [31:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter disable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P<n>   | Meaning                                                                             |
|--------|-------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n> is disabled. When written, has no effect.        |
| 0b1    | When read, means that AMEVCNTR1<n> is enabled. When written, disables AMEVCNTR1<n>. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR1

If there are no auxiliary monitor event counters implemented, reads and writes of AMCNTENCLR1 are UNDEFINED.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0011 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR1; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENCLR1; elsif PSTATE.EL == EL3 then R[t] = AMCNTENCLR1;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0011 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) then AMCNTENCLR1 = R[t]; else UNDEFINED;
```

## G8.5.5 AMCNTENSET0, Activity Monitors Count Enable Set Register 0

The AMCNTENSET0 characteristics are:

## Purpose

Enable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;.

## Configuration

AArch32 System register AMCNTENSET0 bits [31:0] are architecturally mapped to AArch64 System register AMCNTENSET0\_EL0[31:0].

AArch32 System register AMCNTENSET0 bits [31:0] are architecturally mapped to External register AMCNTENSET0[31:0].

AArch32 System register AMCNTENSET0 bits [31:0] are architecturally mapped to External register AMCNTENCLR0[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCNTENSET0 are UNDEFINED.

## Attributes

AMCNTENSET0 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 16 15   | 3 2 1 0     |
|------|---------|-------------|
| RES0 | RAZ/WI  | P3 P2 P1 P0 |

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter enable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n> is disabled. When written, has no effect. |

0b1

When read, means that AMEVCNTR0&lt;n&gt; is enabled. When written, enables AMEVCNTR0&lt;n&gt;.

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET0

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET0; elsif PSTATE.EL == EL3 then R[t] = AMCNTENSET0;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) then AMCNTENSET0 = R[t];
```

else

UNDEFINED;

## G8.5.6 AMCNTENSET1, Activity Monitors Count Enable Set Register 1

The AMCNTENSET1 characteristics are:

## Purpose

Enable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;.

## Configuration

AArch32 System register AMCNTENSET1 bits [31:0] are architecturally mapped to AArch64 System register AMCNTENSET1\_EL0[31:0].

AArch32 System register AMCNTENSET1 bits [31:0] are architecturally mapped to External register AMCNTENSET1[31:0].

AArch32 System register AMCNTENSET1 bits [31:0] are architecturally mapped to External register AMCNTENCLR1[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCNTENSET1 are UNDEFINED.

## Attributes

AMCNTENSET1 is a 32-bit register.

## Field descriptions

| 31   | 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------|

## Bits [31:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter enable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P<n>   | Meaning                                                                            |
|--------|------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n> is disabled. When written, has no effect.       |
| 0b1    | When read, means that AMEVCNTR1<n> is enabled. When written, enables AMEVCNTR1<n>. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET1

If there are no auxiliary monitor event counters implemented, reads and writes of AMCNTENSET1 are UNDEFINED.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0011 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET1; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCNTENSET1; elsif PSTATE.EL == EL3 then R[t] = AMCNTENSET1;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0011 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) then AMCNTENSET1 = R[t]; else UNDEFINED;
```

## G8.5.7 AMCR, Activity Monitors Control Register

The AMCR characteristics are:

## Purpose

Global control register for the activity monitors implementation. AMCR is applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch32 System register AMCR bits [31:0] are architecturally mapped to AArch64 System register AMCR\_EL0[31:0].

AArch32 System register AMCR bits [31:0] are architecturally mapped to External register AMCR[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMCR are UNDEFINED.

## Attributes

AMCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## CG1RZ, bit [17]

## When FEAT\_AMUv1p1 is implemented:

Counter Group 1 Read Zero.

| CG1RZ   | Meaning                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | System register reads of AMEVCNTR1<n> return the event count at all implemented and enabled Exception levels.                                                                                  |
| 0b1     | If the current Exception level is the highest implemented Exception level, System register reads of AMEVCNTR1<n> return the event count. Otherwise, reads of AMEVCNTR1<n> return a zero value. |

Note

Reads from the memory-mapped view are unaffected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:11]

Reserved, RES0.

## HDBG, bit [10]

This bit controls whether activity monitor counting is halted when the PE is halted in Debug state.

| HDBG   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | Activity monitors do not halt counting when the PE is halted in Debug state. |
| 0b1    | Activity monitors halt counting when the PE is halted in Debug state.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [9:0]

Reserved, RES0.

## Accessing AMCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMCR; elsif PSTATE.EL == EL3 then R[t] = AMCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) then AMCR = R[t]; else UNDEFINED;
```

## G8.5.8 AMEVCNTR0&lt;n&gt;, Activity Monitors Event Counter Registers 0, n = 0 - 3

The AMEVCNTR0&lt;n&gt; characteristics are:

## Purpose

Provides access to the architected activity monitor event counters.

## Configuration

AArch32 System register AMEVCNTR0&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register AMEVCNTR0&lt;n&gt;\_EL0[63:0].

AArch32 System register AMEVCNTR0&lt;n&gt; bits [63:0] are architecturally mapped to External register AMEVCNTR0[63:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMEVCNTR0&lt;n&gt; are UNDEFINED.

## Attributes

AMEVCNTR0&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      | 32   |
|------|------|------|
|      | ACNT |      |
| 31   |      | 0    |
|      | ACNT |      |

## ACNT, bits [63:0]

Architected activity monitor event counter n.

Value of architected activity monitor event counter n, where n is the number of this register and is a number from 0 to 3.

If FEAT\_AMUv1p1 is implemented, HCR\_EL2.AMVOFFEN is 1, SCR\_EL3.AMVOFFEN is 1, the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, and EL2 is using AArch64 and is implemented in the current Security state, access to these registers at EL0 or EL1 return (PCount&lt;63:0&gt; AMEVCNTVOFF0&lt;n&gt;\_EL2&lt;63:0&gt;).

PCount is the physical count returned when AMEVCNTR0&lt;n&gt; is read from EL2 or EL3.

If the counter is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR0&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads and writes of AMEVCNTR0&lt;n&gt; are UNDEFINED.

Note

AMCGCR.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | CRm         | opc1        |
|----------|-------------|-------------|
| 0b1111   | 0b000 :m[3] | 0b0 :m[2:0] |

```
integer m = UInt(CRm<0>:opc1<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && m < 8 && HSTR_EL2.T0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && m < 8 && ↪ → HSTR.T0 == '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMEVCNTR0<m>_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else R[t, t2] = AMEVCNTR0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && m < 8 && ↪ → HSTR_EL2.T0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && m < 8 && HSTR.T0 ↪ → == '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else R[t, t2] = AMEVCNTR0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else R[t, t2] = AMEVCNTR0[m]; elsif PSTATE.EL == EL3 then R[t, t2] = AMEVCNTR0[m];
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt; ; Where m = 0-3

| coproc   | CRm         | opc1        |
|----------|-------------|-------------|
| 0b1111   | 0b000 :m[3] | 0b0 :m[2:0] |

```
integer m = UInt(CRm<0>:opc1<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → m < 8 && HSTR_EL2.T0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && m ↪ → < 8 && HSTR.T0 == '1' then AArch32.TakeHypTrapException(0x04); elsif IsHighestEL(PSTATE.EL) then AMEVCNTR0[m] = R[t2]:R[t]; else UNDEFINED;
```

## G8.5.9 AMEVCNTR1&lt;n&gt;, Activity Monitors Event Counter Registers 1, n = 0 - 15

The AMEVCNTR1&lt;n&gt; characteristics are:

## Purpose

Provides access to the auxiliary activity monitor event counters.

## Configuration

AArch32 System register AMEVCNTR1&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register AMEVCNTR1&lt;n&gt;\_EL0[63:0].

AArch32 System register AMEVCNTR1&lt;n&gt; bits [63:0] are architecturally mapped to External register AMEVCNTR1[63:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMEVCNTR1&lt;n&gt; are UNDEFINED.

## Attributes

AMEVCNTR1&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      | 32   |
|------|------|------|
|      | ACNT |      |
| 31   |      | 0    |
|      | ACNT |      |

## ACNT, bits [63:0]

Auxiliary activity monitor event counter n.

Value of auxiliary activity monitor event counter n, where n is the number of this register and is a number from 0 to 15.

If FEAT\_AMUv1p1 is implemented, HCR\_EL2.AMVOFFEN is 1, SCR\_EL3.AMVOFFEN is 1, the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, EL2 is using AArch64 and is implemented in the current Security state, and AMCR\_EL0.CG1RZ is 0, reads to these registers at EL0 or EL1 return (PCount&lt;63:0&gt; AMEVCNTVOFF1&lt;n&gt;\_EL2&lt;63:0&gt;).

PCount is the physical count returned when AMEVCNTR1&lt;n&gt; is read from EL2 or EL3.

If the counter is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR1&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads and writes of AMEVCNTR1&lt;n&gt; are UNDEFINED.

Note

AMCGCR.CG1NC identifies the number of auxiliary activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | CRm         | opc1        |
|----------|-------------|-------------|
| 0b1111   | 0b010 :m[3] | 0b0 :m[2:0] |

```
integer m = UInt(CRm<0>:opc1<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && m >= 8 && HSTR_EL2.T5 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && m >= 8 && ↪ → HSTR.T5 == '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMEVCNTR1<m>_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); elsif IsFeatureImplemented(FEAT_AA64) && AMCR_EL0.CG1RZ == '1' then R[t, t2] = Zeros(64); elsif !IsFeatureImplemented(FEAT_AA64) && AMCR.CG1RZ == '1' then R[t, t2] = Zeros(64); else R[t, t2] = AMEVCNTR1[m]; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && m >= 8 && ↪ → HSTR_EL2.T5 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && m >= 8 && HSTR.T5 ↪ → == '1' then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); elsif !IsHighestEL(PSTATE.EL) && IsFeatureImplemented(FEAT_AA64) && AMCR_EL0.CG1RZ == '1' then R[t, t2] = Zeros(64); elsif !IsHighestEL(PSTATE.EL) && !IsFeatureImplemented(FEAT_AA64) && AMCR.CG1RZ == '1' then R[t, t2] = Zeros(64); else R[t, t2] = AMEVCNTR1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); elsif !IsHighestEL(PSTATE.EL) && IsFeatureImplemented(FEAT_AA64) && AMCR_EL0.CG1RZ == '1' then R[t, t2] = Zeros(64); elsif !IsHighestEL(PSTATE.EL) && !IsFeatureImplemented(FEAT_AA64) && AMCR.CG1RZ == '1' then R[t, t2] = Zeros(64); else R[t, t2] = AMEVCNTR1[m]; elsif PSTATE.EL == EL3 then R[t, t2] = AMEVCNTR1[m];
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt; ; Where m = 0-15

| coproc   | CRm         | opc1        |
|----------|-------------|-------------|
| 0b1111   | 0b010 :m[3] | 0b0 :m[2:0] |

```
integer m = UInt(CRm<0>:opc1<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → m >= 8 && HSTR_EL2.T5 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && m ↪ → >= 8 && HSTR.T5 == '1' then AArch32.TakeHypTrapException(0x04); elsif IsHighestEL(PSTATE.EL) then AMEVCNTR1[m] = R[t2]:R[t]; else UNDEFINED;
```

## G8.5.10 AMEVTYPER0&lt;n&gt;, Activity Monitors Event Type Registers 0, n = 0 - 3

The AMEVTYPER0&lt;n&gt; characteristics are:

## Purpose

Provides information on the events that an architected activity monitor event counter AMEVCNTR0&lt;n&gt; counts.

## Configuration

AArch32 System register AMEVTYPER0&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register AMEVTYPER0&lt;n&gt;\_EL0[31:0].

AArch32 System register AMEVTYPER0&lt;n&gt; bits [31:0] are architecturally mapped to External register AMEVTYPER0[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMEVTYPER0&lt;n&gt; are UNDEFINED.

## Attributes

AMEVTYPER0&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the architected activity monitor event counter AMEVCNTR0&lt;n&gt;. The value of this field is architecturally mandated for each architected counter.

The following table shows the mapping between required event numbers and the corresponding counters:

| evtCount   | Meaning                     | Applies when   |
|------------|-----------------------------|----------------|
| 0x0011     | Processor frequency cycles. | n == 0         |
| 0x4004     | Constant frequency cycles.  | n == 1         |
| 0x0008     | Instructions retired.       | n == 2         |
| 0x4005     | Memory stall cycles.        | n == 3         |

Access to this field is RO.

## Accessing AMEVTYPER0&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads and writes of AMEVTYPER0&lt;n&gt; are UNDEFINED.

Note

AMCGCR.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-3

| coproc   | opc1   | CRn    | CRm         | opc2   |
|----------|--------|--------|-------------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b011 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER0[m]; elsif PSTATE.EL == EL3 then R[t] = AMEVTYPER0[m];
```

## G8.5.11 AMEVTYPER1&lt;n&gt;, Activity Monitors Event Type Registers 1, n = 0 - 15

The AMEVTYPER1&lt;n&gt; characteristics are:

## Purpose

Provides information on the events that an auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt; counts.

## Configuration

AArch32 System register AMEVTYPER1&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register AMEVTYPER1&lt;n&gt;\_EL0[31:0].

AArch32 System register AMEVTYPER1&lt;n&gt; bits [31:0] are architecturally mapped to External register AMEVTYPER1[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMEVTYPER1&lt;n&gt; are UNDEFINED.

## Attributes

AMEVTYPER1&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt;.

It is IMPLEMENTATION DEFINED what values are supported by each counter.

If software writes a value to this field which is not supported by the corresponding counter AMEVCNTR1&lt;n&gt;, then:

- It is UNPREDICTABLE which event will be counted.
- The value read back is UNKNOWN.

The event counted by AMEVCNTR1&lt;n&gt; might be fixed at implementation. In this case, the field is read-only and writes are UNDEFINED.

If the corresponding counter AMEVCNTR1&lt;n&gt; is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMEVTYPER1&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads and writes of AMEVTYPER1&lt;n&gt; are UNDEFINED.

| Note                                                                             |
|----------------------------------------------------------------------------------|
| AMCGCR.CG1NC identifies the number of auxiliary activity monitor event counters. |

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm         | opc2   |
|----------|--------|--------|-------------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b111 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && AMUSERENR_EL0.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && AMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HAFGRTR_EL2.AMEVTYPER1<m>_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER1[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMEVTYPER1[m]; elsif PSTATE.EL == EL3 then R[t] = AMEVTYPER1[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm         | opc2   |
|----------|--------|--------|-------------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b111 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif PSTATE.EL == EL1 && EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → HSTR.T13 == '1' then AArch32.TakeHypTrapException(0x03); elsif IsHighestEL(PSTATE.EL) && !boolean IMPLEMENTATION_DEFINED "AMEVCNTR1[m] is fixed" then AMEVTYPER1[m] = R[t]; else UNDEFINED;
```

## G8.5.12 AMUSERENR, Activity Monitors User Enable Register

The AMUSERENR characteristics are:

## Purpose

Global user enable register for the activity monitors. Enables or disables EL0 access to the activity monitors. AMUSERENRis applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch32 System register AMUSERENR bits [31:0] are architecturally mapped to AArch64 System register AMUSERENR\_EL0[31:0].

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to AMUSERENR are UNDEFINED.

## Attributes

AMUSERENRis a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 1 0   |
|------|-------|
|      | EN    |

## Bits [31:1]

Reserved, RES0.

## EN, bit [0]

Traps EL0 accesses to the activity monitors registers to EL1.

| EN   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 accesses to the activity monitors registers are trapped to EL1.                                                    |
| 0b1  | This control does not cause any instructions to be trapped. Software can access all activity monitor registers at EL0. |

Note

- AMUSERENRcan always be read at EL0 and is not governed by this bit.

Note

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMUSERENR

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T13 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && CPTR_EL2.TAM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCPTR.TAM == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMUSERENR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMUSERENR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = AMUSERENR; elsif PSTATE.EL == EL3 then R[t] = AMUSERENR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1101 | 0b0010 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AMUv1) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T13 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T13 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TAM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TAM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else AMUSERENR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TAM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else AMUSERENR = R[t]; elsif PSTATE.EL == EL3 then AMUSERENR = R[t];
```