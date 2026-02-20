## D24.6 Activity Monitors registers

This section lists the Activity Monitors registers in AArch64.

## D24.6.1 AMCFGR\_EL0, Activity Monitors Configuration Register

The AMCFGR\_EL0 characteristics are:

## Purpose

Global configuration register for the activity monitors.

Provides information on supported features, the number of counter groups implemented, the total number of activity monitor event counters implemented, and the size of the counters. AMCFGR\_EL0 is applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch64 System register AMCFGR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCFGR[31:0].

When FEAT\_AMU\_EXT32 is implemented, AArch64 System register AMCFGR\_EL0 bits [31:0] are architecturally mapped to External register AMCFGR[31:0].

When FEAT\_AMU\_EXT64 is implemented, AArch64 System register AMCFGR\_EL0 bits [63:0] are architecturally mapped to External register AMCFGR[63:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCFGR\_EL0 are UNDEFINED.

## Attributes

AMCFGR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

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

| HDBG   | Meaning                      |
|--------|------------------------------|
| 0b0    | AMCR_EL0.HDBG is RES0.       |
| 0b1    | AMCR_EL0.HDBG is read/write. |

Access to this field is RO.

## Bits [23:14]

Reserved, RAZ.

## SIZE, bits [13:8]

Defines the size of the activity monitor event counters, minus one.

The counters are 64-bit, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. The counters are at doubleword-aligned addresses.

Reads as

0b111111

Access to this field is RO.

## N, bits [7:0]

Defines the number of activity monitor event counters implemented in all groups, minus one.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMCFGR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMCFGR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED;
```

```
elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCFGR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCFGR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCFGR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCFGR_EL0;
```

## D24.6.2 AMCG1IDR\_EL0, Activity Monitors Counter Group 1 Identification Register

The AMCG1IDR\_EL0 characteristics are:

## Purpose

Defines which auxiliary counters are implemented, and which of them have a corresponding virtual offset register, AMEVCNTVOFF1&lt;n&gt;\_EL2 implemented.

## Configuration

This register is present only when FEAT\_AMUv1p1 is implemented. Otherwise, direct accesses to AMCG1IDR\_EL0 are UNDEFINED.

## Attributes

AMCG1IDR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## AMEVCNTOFF1&lt;n&gt;\_EL2 , bits [n+16], for n = 15 to 0

Indicates which implemented auxiliary counters have a corresponding virtual offset register, AMEVCNTVOFF1&lt;n&gt;\_EL2 implemented.

| AMEVCNTOFF1<n>_EL2   | Meaning                                                             |
|----------------------|---------------------------------------------------------------------|
| 0b0                  | AMEVCNTR1<n>_EL0 does not have an offset, or is not implemented.    |
| 0b1                  | The offset AMEVCNTVOFF1<n>_EL2 is implemented for AMEVCNTR1<n>_EL0. |

## AMEVCNTR1&lt;n&gt;\_EL0 , bits [n], for n = 15 to 0

Indicates which auxiliary counters AMEVCNTR1&lt;n&gt;\_EL0 are implemented.

| AMEVCNTR1<n>_EL0   | Meaning                              |
|--------------------|--------------------------------------|
| 0b0                | AMEVCNTR1<n>_EL0 is not implemented. |
| 0b1                | AMEVCNTR1<n>_EL0 is implemented.     |

## Accessing AMCG1IDR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMCG1IDR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AMUv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCG1IDR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCG1IDR_EL0;
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCG1IDR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCG1IDR_EL0;
```

## D24.6.3 AMCGCR\_EL0, Activity Monitors Counter Group Configuration Register

The AMCGCR\_EL0 characteristics are:

## Purpose

Provides information on the number of activity monitor event counters implemented within each counter group.

## Configuration

AArch64 System register AMCGCR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCGCR[31:0].

When FEAT\_AMU\_EXT32 is implemented, AArch64 System register AMCGCR\_EL0 bits [31:0] are architecturally mapped to External register AMCGCR[31:0].

When FEAT\_AMU\_EXT64 is implemented, AArch64 System register AMCGCR\_EL0 bits [63:0] are architecturally mapped to External register AMCGCR[63:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCGCR\_EL0 are UNDEFINED.

## Attributes

AMCGCR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Counter Group 1 Number of Counters. The number of counters in the auxiliary counter group.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CG1NC        | Meaning                 |
|--------------|-------------------------|
| 0x00 .. 0x10 | The number of counters. |

All other values are reserved.

Access to this field is RO.

## CG0NC, bits [7:0]

Counter Group 0 Number of Counters. The number of counters in the architected counter group.

Reads as 0x04

Access to this field is RO.

## Accessing AMCGCR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMCGCR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCGCR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCGCR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCGCR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCGCR_EL0;
```

## D24.6.4 AMCNTENCLR0\_EL0, Activity Monitors Count Enable Clear Register 0

The AMCNTENCLR0\_EL0 characteristics are:

## Purpose

Disable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;\_EL0.

## Configuration

AArch64 System register AMCNTENCLR0\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCNTENCLR0[31:0].

AArch64 System register AMCNTENCLR0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR0[31:0].

AArch64 System register AMCNTENCLR0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR[31:0].

AArch64 System register AMCNTENCLR0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET0[31:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCNTENCLR0\_EL0 are UNDEFINED.

## Attributes

AMCNTENCLR0\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      |        |      |      |      | 32   |      |
|------|------|--------|------|------|------|------|------|
|      | RES0 | RES0   | RES0 | RES0 | RES0 | RES0 | RES0 |
| 31   |      |        | 3    | 2    | 1    | 0    |      |
| RES0 |      | RAZ/WI | P3   | P2   | P1   | P0   |      |

## Bits [63:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter disable bit for AMEVCNTR0&lt;n&gt;\_EL0.

Note

AMCGCR\_EL0.CG0NCidentifiesthenumberofarchitected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n>_EL0 is disabled. When written, has no effect.            |
| 0b1    | When read, means that AMEVCNTR0<n>_EL0 is enabled. When written, disables AMEVCNTR0<n>_EL0. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR0\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMCNTENCLR0\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENCLR0_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
else X[t, 64] = AMCNTENCLR0_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENCLR0_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCNTENCLR0_EL0;
```

MSR AMCNTENCLR0\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMCNTENCLR0_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.6.5 AMCNTENCLR1\_EL0, Activity Monitors Count Enable Clear Register 1

The AMCNTENCLR1\_EL0 characteristics are:

## Purpose

Disable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;\_EL0.

## Configuration

AArch64 System register AMCNTENCLR1\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCNTENCLR1[31:0].

AArch64 System register AMCNTENCLR1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR1[31:0].

AArch64 System register AMCNTENCLR1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET1[31:0].

AArch64 System register AMCNTENCLR1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR[63:32].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCNTENCLR1\_EL0 are UNDEFINED.

## Attributes

AMCNTENCLR1\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |                            | 32       |
|------|----------------------------|----------|
|      | RES0                       |          |
| 31   | 16 15 14 13 12 11 10 9     | 2 1 0    |
| RES0 | P15 P14 P13 P12 P11 P10 P9 | P2 P1 P0 |

## Bits [63:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter disable bit for AMEVCNTR1&lt;n&gt;\_EL0.

Possible values of each bit are:

| P<n>   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n>_EL0 is disabled. When written, has no effect.            |
| 0b1    | When read, means that AMEVCNTR1<n>_EL0 is enabled. When written, disables AMEVCNTR1<n>_EL0. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMCGCR\_EL0.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR1\_EL0

If there are no auxiliary monitor event counters implemented, reads and writes of AMCNTENCLR1\_EL0 are UNDEFINED.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR\_EL0.NCG == 0b0000 .

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, AMCNTENCLR1_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENCLR1_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENCLR1_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENCLR1_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCNTENCLR1_EL0;
```

MSR AMCNTENCLR1\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMCNTENCLR1_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.6.6 AMCNTENSET0\_EL0, Activity Monitors Count Enable Set Register 0

The AMCNTENSET0\_EL0 characteristics are:

## Purpose

Enable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;\_EL0.

## Configuration

AArch64 System register AMCNTENSET0\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCNTENSET0[31:0].

AArch64 System register AMCNTENSET0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET0[31:0].

AArch64 System register AMCNTENSET0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET[31:0].

AArch64 System register AMCNTENSET0\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR0[31:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCNTENSET0\_EL0 are UNDEFINED.

## Attributes

AMCNTENSET0\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |      |        |      |      |      | 32   |      |
|------|------|--------|------|------|------|------|------|
|      | RES0 | RES0   | RES0 | RES0 | RES0 | RES0 | RES0 |
| 31   |      |        | 3    | 2    | 1    | 0    |      |
| RES0 |      | RAZ/WI | P3   | P2   | P1   | P0   |      |

## Bits [63:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter enable bit for AMEVCNTR0&lt;n&gt;\_EL0.

Note

AMCGCR\_EL0.CG0NCidentifiesthenumberofarchitected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n>_EL0 is disabled. When written, has no effect.           |
| 0b1    | When read, means that AMEVCNTR0<n>_EL0 is enabled. When written, enables AMEVCNTR0<n>_EL0. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET0\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMCNTENSET0\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENSET0_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMCNTEN0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
else X[t, 64] = AMCNTENSET0_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENSET0_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCNTENSET0_EL0;
```

MSR AMCNTENSET0\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMCNTENSET0_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.6.7 AMCNTENSET1\_EL0, Activity Monitors Count Enable Set Register 1

The AMCNTENSET1\_EL0 characteristics are:

## Purpose

Enable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;\_EL0.

## Configuration

AArch64 System register AMCNTENSET1\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCNTENSET1[31:0].

AArch64 System register AMCNTENSET1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET1[31:0].

AArch64 System register AMCNTENSET1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENCLR1[31:0].

AArch64 System register AMCNTENSET1\_EL0 bits [31:0] are architecturally mapped to External register AMCNTENSET[63:32].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCNTENSET1\_EL0 are UNDEFINED.

## Attributes

AMCNTENSET1\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |                            | 32       |
|------|----------------------------|----------|
|      | RES0                       |          |
| 31   | 16 15 14 13 12 11 10 9     | 2 1 0    |
| RES0 | P15 P14 P13 P12 P11 P10 P9 | P2 P1 P0 |

## Bits [63:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter enable bit for AMEVCNTR1&lt;n&gt;\_EL0.

Possible values of each bit are:

| P<n>   | Meaning                                                                                    |
|--------|--------------------------------------------------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n>_EL0 is disabled. When written, has no effect.           |
| 0b1    | When read, means that AMEVCNTR1<n>_EL0 is enabled. When written, enables AMEVCNTR1<n>_EL0. |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMCGCR\_EL0.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET1\_EL0

If there are no auxiliary monitor event counters implemented, reads and writes of AMCNTENSET1\_EL0 are UNDEFINED.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR\_EL0.NCG == 0b0000 .

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, AMCNTENSET1_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENSET1_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMCNTEN1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENSET1_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCNTENSET1_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCNTENSET1_EL0;
```

MSR AMCNTENSET1\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMCNTENSET1_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.6.8 AMCR\_EL0, Activity Monitors Control Register

The AMCR\_EL0 characteristics are:

## Purpose

Global control register for the activity monitors implementation. AMCR\_EL0 is applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch64 System register AMCR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMCR[31:0].

When FEAT\_AMU\_EXT32 is implemented, AArch64 System register AMCR\_EL0 bits [31:0] are architecturally mapped to External register AMCR[31:0].

When FEAT\_AMU\_EXT64 is implemented, AArch64 System register AMCR\_EL0 bits [63:0] are architecturally mapped to External register AMCR[63:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMCR\_EL0 are UNDEFINED.

## Attributes

AMCR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:18]

Reserved, RES0.

## CG1RZ, bit [17]

## When FEAT\_AMUv1p1 is implemented:

Counter Group 1 Read Zero.

| CG1RZ   | Meaning                                                                                                                                                                                                |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | System register reads of AMEVCNTR1<n>_EL0 return the event count at all implemented and enabled Exception levels.                                                                                      |
| 0b1     | If the current Exception level is the highest implemented Exception level, system register reads of AMEVCNTR1<n>_EL0 return the event count. Otherwise, reads of AMEVCNTR1<n>_EL0 return a zero value. |

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

## Accessing AMCR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCR_EL0;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMCR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMCR_EL0;
```

MSR AMCR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMCR_EL0 = X[t, 64]; else UNDEFINED;
```

## D24.6.9 AMEVCNTR0&lt;n&gt;\_EL0, Activity Monitors Event Counter Registers 0, n = 0 - 3

The AMEVCNTR0&lt;n&gt;\_EL0 characteristics are:

## Purpose

Provides access to the architected activity monitor event counters.

## Configuration

AArch64 System register AMEVCNTR0&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMEVCNTR0&lt;n&gt;[31:0].

AArch64 System register AMEVCNTR0&lt;n&gt;\_EL0 bits [63:0] are architecturally mapped to External register AMEVCNTR0[63:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMEVCNTR0&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

AMEVCNTR0&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

ACNT

63

32

ACNT

31

0

<!-- image -->

## ACNT, bits [63:0]

Architected activity monitor event counter n.

Value of architected activity monitor event counter n, where n is the number of this register and is a number from 0 to 3.

If all of the following are true, reads of the AMEVCNTR0&lt;n&gt;\_EL0 registers from EL0 or EL1 return (PCount&lt;63:0&gt; - AMEVCNTVOFF0&lt;n&gt;\_EL2&lt;63:0&gt;), where PCount is the physical count returned when AMEVCNTR0&lt;n&gt;\_EL0 is read from EL2 or EL3:

- FEAT\_AMUv1p1 is implemented.
- HCR\_EL2.AMVOFFEN and SCR\_EL3.AMVOFFEN are 1.
- EL2 is implemented and enabled in the current Security state, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

If the counter is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR0&lt;n&gt;\_EL0

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads and writes of AMEVCNTR0&lt;n&gt;\_EL0 are UNDEFINED.

Note

AMCGCR\_EL0.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b010 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMEVCNTR0<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVCNTR0_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMEVCNTR0<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVCNTR0_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVCNTR0_EL0[m]; elsif PSTATE.EL == EL3 then X[t, 64] = AMEVCNTR0_EL0[m];
```

MSR AMEVCNTR0&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b010 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMEVCNTR0_EL0[m] = X[t, 64]; else UNDEFINED;
```

## D24.6.10 AMEVCNTR1&lt;n&gt;\_EL0, Activity Monitors Event Counter Registers 1, n = 0 - 15

The AMEVCNTR1&lt;n&gt;\_EL0 characteristics are:

## Purpose

Provides access to the auxiliary activity monitor event counters.

## Configuration

AArch64 System register AMEVCNTR1&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMEVCNTR1&lt;n&gt;[31:0].

AArch64 System register AMEVCNTR1&lt;n&gt;\_EL0 bits [63:0] are architecturally mapped to External register AMEVCNTR1[63:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMEVCNTR1&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

AMEVCNTR1&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

ACNT

63

32

ACNT

31

0

<!-- image -->

## ACNT, bits [63:0]

Auxiliary activity monitor event counter n.

Value of auxiliary activity monitor event counter n, where n is the number of this register and is a number from 0 to 15.

If all of the following are true, reads of the AMEVCNTR1&lt;n&gt;\_EL0 registers from EL0 or EL1 return (PCount&lt;63:0&gt; - AMEVCNTVOFF1&lt;n&gt;\_EL2&lt;63:0&gt;), where PCount is the physical count returned when AMEVCNTR1&lt;n&gt;\_EL0 is read from EL2 or EL3:

- FEAT\_AMUv1p1 is implemented.
- HCR\_EL2.AMVOFFEN and SCR\_EL3.AMVOFFEN are 1.
- AMCR\_EL0.CG1RZ is 0.
- EL2 is implemented and enabled in the current Security state, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

If the counter is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR1&lt;n&gt;\_EL0

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads and writes of AMEVCNTR1&lt;n&gt;\_EL0 are UNDEFINED.

Note

AMCGCR\_EL0.CG1NC identifies the number of auxiliary activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMEVCNTR1&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b110 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMEVCNTR1<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif AMCR_EL0.CG1RZ == '1' then X[t, 64] = Zeros(64); else X[t, 64] = AMEVCNTR1_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMEVCNTR1<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsHighestEL(PSTATE.EL) && AMCR_EL0.CG1RZ == '1' then X[t, 64] = Zeros(64); else X[t, 64] = AMEVCNTR1_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsHighestEL(PSTATE.EL) && AMCR_EL0.CG1RZ == '1' then X[t, 64] = Zeros(64); else X[t, 64] = AMEVCNTR1_EL0[m]; elsif PSTATE.EL == EL3 then X[t, 64] = AMEVCNTR1_EL0[m];
```

```
MSR AMEVCNTR1<m>_EL0, <Xt> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b110 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) then AMEVCNTR1_EL0[m] = X[t, 64]; else UNDEFINED;
```

## D24.6.11 AMEVCNTVOFF0&lt;n&gt;\_EL2, Activity Monitors Event Counter Virtual Offset Registers 0, n = 0 - 15

The AMEVCNTVOFF0&lt;n&gt;\_EL2 characteristics are:

## Purpose

Holds the 64-bit virtual offset for architected activity monitor events.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_AMUv1p1 is implemented. Otherwise, direct accesses to AMEVCNTVOFF0&lt;n&gt;\_EL2 are UNDEFINED.

## Attributes

AMEVCNTVOFF0&lt;n&gt;\_EL2 is a 64-bit register.

## Field descriptions

| 63             | 32   |
|----------------|------|
| Virtual offset |      |
| 31             | 0    |
| Virtual offset |      |

## VOffset, bits [63:0]

Virtual offset.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMEVCNTVOFF0&lt;n&gt;\_EL2

If &lt;n&gt; is not 0, 2 or 3, reads and writes of AMEVCNTVOFF0&lt;n&gt;\_EL2 are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b100 | 0b1101 | 0b100 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1p1) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif !(m IN {0, 2, 3}) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0xA00 + (8 * m)]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.AMVOFFEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.AMVOFFEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVCNTVOFF0_EL2[m]; elsif PSTATE.EL == EL3 then X[t, 64] = AMEVCNTVOFF0_EL2[m];
```

MSR AMEVCNTVOFF0&lt;m&gt;\_EL2, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b100 | 0b1101 | 0b100 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1p1) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif !(m IN {0, 2, 3}) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0xA00 + (8 * m)] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.AMVOFFEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.AMVOFFEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AMEVCNTVOFF0_EL2[m] = X[t, 64]; elsif PSTATE.EL == EL3 then AMEVCNTVOFF0_EL2[m] = X[t, 64];
```

## D24.6.12 AMEVCNTVOFF1&lt;n&gt;\_EL2, Activity Monitors Event Counter Virtual Offset Registers 1, n = 0 - 15

The AMEVCNTVOFF1&lt;n&gt;\_EL2 characteristics are:

## Purpose

Holds the 64-bit virtual offset for auxiliary activity monitor events.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_AMUv1p1 is implemented. Otherwise, direct accesses to AMEVCNTVOFF1&lt;n&gt;\_EL2 are UNDEFINED.

## Attributes

AMEVCNTVOFF1&lt;n&gt;\_EL2 is a 64-bit register.

## Field descriptions

| 63             | 32   |
|----------------|------|
| Virtual offset |      |
| 31             | 0    |
| Virtual offset |      |

## VOffset, bits [63:0]

Virtual offset.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMEVCNTVOFF1&lt;n&gt;\_EL2

Note

AMCG1IDR\_EL0 identifies which auxiliary activity monitor event counters have a corresponding virtual offset implemented.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, AMEVCNTVOFF1<m>_EL2 ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b100 | 0b1101 | 0b101 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1p1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorOffsetImplemented(m) then
```

```
UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0xA80 + (8 * m)]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.AMVOFFEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.AMVOFFEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVCNTVOFF1_EL2[m]; elsif PSTATE.EL == EL3 then X[t, 64] = AMEVCNTVOFF1_EL2[m];
```

MSR AMEVCNTVOFF1&lt;m&gt;\_EL2, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b100 | 0b1101 | 0b101 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1p1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorOffsetImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0xA80 + (8 * m)] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.AMVOFFEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.AMVOFFEN == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AMEVCNTVOFF1_EL2[m] = X[t, 64]; elsif PSTATE.EL == EL3 then AMEVCNTVOFF1_EL2[m] = X[t, 64];
```

## D24.6.13 AMEVTYPER0&lt;n&gt;\_EL0, Activity Monitors Event Type Registers 0, n = 0 - 3

The AMEVTYPER0&lt;n&gt;\_EL0 characteristics are:

## Purpose

Provides information on the events that an architected activity monitor event counter AMEVCNTR0&lt;n&gt;\_EL0 counts.

## Configuration

AArch64 System register AMEVTYPER0&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMEVTYPER0&lt;n&gt;[31:0].

AArch64 System register AMEVTYPER0&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to External register AMEVTYPER0[31:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMEVTYPER0&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

AMEVTYPER0&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63            | 32   |
|---------------|------|
| RES0 31 16 15 | 0    |
| RES0          |      |

## Bits [63:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the architected activity monitor event counter AMEVCNTR0&lt;n&gt;\_EL0. The value of this field is architecturally mandated for each architected counter.

The following table shows the mapping between required event numbers and the corresponding counters:

| evtCount   | Meaning                     | Applies when   |
|------------|-----------------------------|----------------|
| 0x0011     | Processor frequency cycles. | n == 0         |
| 0x4004     | Constant frequency cycles.  | n == 1         |
| 0x0008     | Instructions retired.       | n == 2         |
| 0x4005     | Memory stall cycles.        | n == 3         |

Access to this field is RO.

## Accessing AMEVTYPER0&lt;n&gt;\_EL0

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads and writes of AMEVTYPER0&lt;n&gt;\_EL0 are UNDEFINED.

Note

AMCGCR\_EL0.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, AMEVTYPER0<m>_EL0 ; Where m = 0-3
```

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b011 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= 4 then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER0_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER0_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER0_EL0[m];
```

elsif PSTATE.EL == EL3 then X[t, 64] = AMEVTYPER0\_EL0[m];

## D24.6.14 AMEVTYPER1&lt;n&gt;\_EL0, Activity Monitors Event Type Registers 1, n = 0 - 15

The AMEVTYPER1&lt;n&gt;\_EL0 characteristics are:

## Purpose

Provides information on the events that an auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt;\_EL0 counts.

## Configuration

AArch64 System register AMEVTYPER1&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMEVTYPER1&lt;n&gt;[31:0].

AArch64 System register AMEVTYPER1&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to External register AMEVTYPER1[31:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMEVTYPER1&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

AMEVTYPER1&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt;\_EL0.

It is IMPLEMENTATION DEFINED what values are supported by each counter.

If software writes a value to this field which is not supported by the corresponding counter AMEVCNTR1&lt;n&gt;\_EL0, then:

- It is UNPREDICTABLE which event will be counted.
- The value read back is UNKNOWN.

The event counted by AMEVCNTR1&lt;n&gt;\_EL0 might be fixed at implementation. In this case, the field is read-only and writes are UNDEFINED.

If the corresponding counter AMEVCNTR1&lt;n&gt;\_EL0 is enabled, writes to this register have UNPREDICTABLE results.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMEVTYPER1&lt;n&gt;\_EL0

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads and writes of AMEVTYPER1&lt;n&gt;\_EL0 are UNDEFINED.

Note

AMCGCR\_EL0.CG1NC identifies the number of auxiliary activity monitor event counters.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMEVTYPER1&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b111 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif AMUSERENR_EL0.EN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HAFGRTR_EL2.AMEVTYPER1<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER1_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HAFGRTR_EL2.AMEVTYPER1<m>_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER1_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMEVTYPER1_EL0[m]; elsif PSTATE.EL == EL3 then X[t, 64] = AMEVTYPER1_EL0[m];
```

```
MSR AMEVTYPER1<m>_EL0, <Xt> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b11  | 0b011 | 0b1101 | 0b111 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif m >= NUM_AMU_CG1_MONITORS then UNDEFINED; elsif !IsG1ActivityMonitorImplemented(m) then UNDEFINED; elsif IsHighestEL(PSTATE.EL) && !boolean IMPLEMENTATION_DEFINED "AMEVCNTR1_EL0[m] is fixed" then AMEVTYPER1_EL0[m] = X[t, 64]; else UNDEFINED;
```

## D24.6.15 AMUSERENR\_EL0, Activity Monitors User Enable Register

The AMUSERENR\_EL0 characteristics are:

## Purpose

Global user enable register for the activity monitors. Enables or disables EL0 access to the activity monitors. AMUSERENR\_EL0 is applicable to both the architected and the auxiliary counter groups.

## Configuration

AArch64 System register AMUSERENR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register AMUSERENR[31:0].

This register is present only when FEAT\_AMUv1 is implemented. Otherwise, direct accesses to AMUSERENR\_EL0 are UNDEFINED.

## Attributes

AMUSERENR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:1]

Reserved, RES0.

## EN, bit [0]

Traps EL0 accesses to the activity monitors registers to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, accesses to the following registers are trapped, reported using EC syndrome value 0x18 :
- AMCFGR\_EL0, AMCGCR\_EL0, AMCNTENCLR0\_EL0, AMCNTENCLR1\_EL0, AMCNTENSET0\_EL0, AMCNTENSET1\_EL0, AMCR\_EL0, AMEVCNTR0&lt;n&gt;\_EL0, AMEVCNTR1&lt;n&gt;\_EL0, AMEVTYPER0&lt;n&gt;\_EL0, and AMEVTYPER1&lt;n&gt;\_EL0.
- In AArch32 state, MRC and MCR accesses to the following registers are trapped and reported using EC syndrome value 0x03 , MRRC and MCRR accesses are trapped and reported using EC syndrome value 0x04 :
- AMCFGR, AMCGCR, AMCNTENCLR0, AMCNTENCLR1, AMCNTENSET0, AMCNTENSET1, AMCR, AMEVCNTR0&lt;n&gt;, AMEVCNTR1&lt;n&gt;, AMEVTYPER0&lt;n&gt;, and AMEVTYPER1&lt;n&gt;.

| EN   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 accesses to the activity monitors registers are trapped.                                                           |
| 0b1  | This control does not cause any instructions to be trapped. Software can access all activity monitor registers at EL0. |

Note

- AMUSERENR\_EL0 can always be read at EL0 and is not governed by this bit.

Note

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMUSERENR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMUSERENR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMUSERENR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMUSERENR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = AMUSERENR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = AMUSERENR_EL0;
```

MSR AMUSERENR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AMUv1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TAM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AMUSERENR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TAM == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TAM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AMUSERENR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then AMUSERENR_EL0 = X[t, 64];
```