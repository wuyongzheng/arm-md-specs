## D24.9 RAS registers

This section lists RAS registers in AArch64.

## D24.9.1 DISR\_EL1, Deferred Interrupt Status Register

The DISR\_EL1 characteristics are:

## Purpose

Records that an SError exception has been consumed by an ESB instruction.

## Configuration

AArch64 System register DISR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DISR[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to DISR\_EL1 are UNDEFINED.

## Attributes

DISR\_EL1 is a 64-bit register.

## Field descriptions

When DISR\_EL1.IDS == '0':

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers an asynchronous SError exception. If the implementation does not include any sources of SError exception that can be synchronized by an Error Synchronization Barrier, then this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:25]

Reserved, RES0.

## IDS, bit [24]

Indicates the deferred SError exception type.

| IDS   | Meaning                                             |
|-------|-----------------------------------------------------|
| 0b0   | Deferred error uses architecturally-defined format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [23:18]

Reserved, RES0.

## WU,bits [17:16]

## When FEAT\_RASv2 is implemented:

Write update. See the description of ESR\_ELx.WU for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:13]

Reserved, RES0.

## AET, bits [12:10]

Asynchronous Error Type. See the description of ESR\_ELx.AET for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [9]

External abort Type. See the description of ESR\_ELx.EA for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [8]

Reserved, RES0.

## WnRV, bit [7]

## When FEAT\_RASv2 is implemented:

Write-not-Read Valid. See the description of ESR\_ELx.WnRV for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## WnR, bit [6]

## When FEAT\_RASv2 is implemented:

Write-not-Read. See the description of ESR\_ELx.WnR for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DFSC, bits [5:0]

Fault Status Code. See the description of ESR\_ELx.DFSC for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When DISR\_EL1.IDS == '1':

<!-- image -->

| 63    | 63       | 32   | 63   |
|-------|----------|------|------|
| 31 30 | 25 24 23 | 0    |      |
| A     | RES0 IDS |      |      |

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers an asynchronous SError exception. If the implementation does not include any sources of SError exception that can be synchronized by an Error Synchronization Barrier, then this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:25]

Reserved, RES0.

## IDS, bit [24]

Indicates the deferred SError exception type.

| IDS   | Meaning                                            |
|-------|----------------------------------------------------|
| 0b1   | Deferred error uses IMPLEMENTATION DEFINED format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED syndrome. See the description of ESR\_ELx[23:0] for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DISR\_EL1

An indirect write to DISR\_EL1 made by an ESB instruction does not require an explicit synchronization operation for the value that is written to be observed by a direct read of DISR\_EL1 occurring in program order after the ESB instruction.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DISR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then X[t, 64] = VDISR_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DISR_EL1;
```

MSR DISR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then VDISR_EL2 = X[t, 64]; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64];
```

elsif PSTATE.EL == EL3 then DISR\_EL1 = X[t, 64];

## D24.9.2 ERRIDR\_EL1, Error Record ID Register

The ERRIDR\_EL1 characteristics are:

## Purpose

Defines the highest numbered index of the error records that can be accessed through the Error Record System registers.

## Configuration

AArch64 System register ERRIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERRIDR[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERRIDR\_EL1 are UNDEFINED.

## Attributes

ERRIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32   |
|----------|------|
| RES0     | 0    |
| 31 16 15 |      |
| RES0     | NUM  |

## Bits [63:16]

Reserved, RES0.

## NUM,bits [15:0]

Highest numbered index of the records that can be accessed through the Error Record System registers plus one. Zero indicates no records can be accessed through the Error Record System registers.

Each implemented record is owned by a node. A node might own multiple records.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing ERRIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERRIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERRIDR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERRIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERRIDR_EL1;
```

## D24.9.3 ERRSELR\_EL1, Error Record Select Register

The ERRSELR\_EL1 characteristics are:

## Purpose

Selects an error record to be accessed through the Error Record System registers.

## Configuration

If ERRIDR\_EL1 indicates that zero error records are implemented, then it is IMPLEMENTATION DEFINED whether ERRSELR\_EL1 is UNDEFINED or RES0.

AArch64 System register ERRSELR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERRSELR[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERRSELR\_EL1 are UNDEFINED.

## Attributes

ERRSELR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32   |
|----------|------|
| RES0     | 0    |
| 31 16 15 |      |
| RES0     | SEL  |

## Bits [63:16]

Reserved, RES0.

## SEL, bits [15:0]

Selects the error record accessed through the ERX registers.

For example, if ERRSELR\_EL1.SEL is 0x0004 , then direct reads and writes of ERXSTATUS\_EL1 access ERR4STATUS.

If ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then all of the following apply:

- The value read back from ERRSELR\_EL1.SEL is UNKNOWN.
- Unless the access to an ERX*\_EL1 register generates a higher priority exception, one of the following occurs:
- An UNKNOWN error record is selected.
- The ERX*\_EL1 registers are RAZ/WI.
- ERX*\_EL1 register reads and writes are NOPs.
- ERX*\_EL1 register reads and writes are UNDEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ERRSELR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERRSELR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERRSELR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERRSELR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERRSELR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERRSELR_EL1;
```

MSR ERRSELR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERRSELR_EL1 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERRSELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERRSELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERRSELR_EL1 = X[t, 64];
```

## D24.9.4 ERXADDR\_EL1, Selected Error Record Address Register

The ERXADDR\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;ADDR for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXADDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXADDR[31:0].

AArch64 System register ERXADDR\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXADDR2[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXADDR\_EL1 are UNDEFINED.

## Attributes

ERXADDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32       |          |
|----------|----------|----------|
| ERRnADDR | ERRnADDR | ERRnADDR |
| 31       | 0        |          |
| ERRnADDR | ERRnADDR | ERRnADDR |

## ERRnADDR, bits [63:0]

ERXADDR\_EL1 accesses ERR&lt;n&gt;ADDR, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXADDR\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXADDR\_EL1 is RAZ/WI.
- Direct reads and writes of ERXADDR\_EL1 are NOPs.
- Direct reads and writes of ERXADDR\_EL1 are UNDEFINED.

ERR&lt;n&gt;ADDR describes additional constraints that also apply when ERR&lt;n&gt;ADDR is accessed through ERXADDR\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXADDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXADDR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXADDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXADDR_EL1;
```

MSR ERXADDR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXADDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXADDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXADDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXADDR_EL1 = X[t, 64];
```

## D24.9.5 ERXCTLR\_EL1, Selected Error Record Control Register

The ERXCTLR\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;CTLR for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXCTLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXCTLR[31:0].

AArch64 System register ERXCTLR\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXCTLR2[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXCTLR\_EL1 are UNDEFINED.

## Attributes

ERXCTLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |          | 32   |
|------|----------|------|
|      | ERRnCTLR |      |
| 31   |          | 0    |
|      | ERRnCTLR |      |

## ERRnCTLR, bits [63:0]

ERXCTLR\_EL1 accesses ERR&lt;n&gt;CTLR, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXCTLR\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXCTLR\_EL1 is RAZ/WI.
- Direct reads and writes of ERXCTLR\_EL1 are NOPs.
- Direct reads and writes of ERXCTLR\_EL1 are UNDEFINED.

If ERRSELR\_EL1.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;CTLR is not present, meaning reads and writes of ERXCTLR\_EL1 are RES0.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXCTLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXCTLR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXCTLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXCTLR_EL1;
```

MSR ERXCTLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXCTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXCTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXCTLR_EL1 = X[t, 64];
```

## D24.9.6 ERXFR\_EL1, Selected Error Record Feature Register

The ERXFR\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;FR for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXFR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXFR[31:0].

AArch64 System register ERXFR\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXFR2[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXFR\_EL1 are UNDEFINED.

## Attributes

ERXFR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |        | 32   |
|------|--------|------|
|      | ERRnFR |      |
| 31   |        | 0    |
|      | ERRnFR |      |

## ERRnFR, bits [63:0]

ERXFR\_EL1 accesses ERR&lt;n&gt;FR, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXFR\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXFR\_EL1 is RAZ.
- Direct reads of ERXFR\_EL1 are NOPs.
- Direct reads of ERXFR\_EL1 are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXFR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXFR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXFR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXFR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXFR_EL1;
```

## D24.9.7 ERXGSR\_EL1, Selected Error Record Group Status Register

The ERXGSR\_EL1 characteristics are:

## Purpose

Shows the status for the records in a group of error records.

Accesses ERRGSR for the group of error records &lt;n&gt; selected by ERRSELR\_EL1.SEL[15:6].

## Configuration

This register is present only when FEAT\_RASv2 is implemented. Otherwise, direct accesses to ERXGSR\_EL1 are UNDEFINED.

## Attributes

ERXGSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
| S<q> |      |
| 31   | 0    |

## S&lt;q&gt; , bits [q], for q = 63 to 0

## When error record m is implemented and error record m supports this type of reporting:

The status for error record &lt;m&gt;, where m = q + (UInt(ERRSELR\_EL1.SEL[15:6]) × 64). A read-only copy of ERR&lt;m&gt;STATUS.V.

| S<q>   | Meaning             |
|--------|---------------------|
| 0b0    | No error.           |
| 0b1    | One or more errors. |

## Otherwise:

Reserved, RES0.

## Accessing ERXGSR\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN group of error records are selected.
- ERXGSR\_EL1 is RAZ.
- Direct reads of ERXGSR\_EL1 are NOPs.
- Direct reads of ERXGSR\_EL1 are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXGSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_RASv2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nERXGSR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXGSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXGSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXGSR_EL1;
```

## D24.9.8 ERXMISC0\_EL1, Selected Error Record Miscellaneous Register 0

The ERXMISC0\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;MISC0 for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXMISC0\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXMISC0[31:0].

AArch64 System register ERXMISC0\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXMISC1[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXMISC0\_EL1 are UNDEFINED.

## Attributes

ERXMISC0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| ERRnMISC0 | ERRnMISC0 | ERRnMISC0 |
| 31        | 0         |           |
| ERRnMISC0 | ERRnMISC0 | ERRnMISC0 |

## ERRnMISC0, bits [63:0]

ERXMISC0\_EL1 accesses ERR&lt;n&gt;MISC0, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXMISC0\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC0\_EL1 is RAZ/WI.
- Direct reads and writes of ERXMISC0\_EL1 are NOPs.
- Direct reads and writes of ERXMISC0\_EL1 are UNDEFINED.

ERR&lt;n&gt;MISC0 describes additional constraints that also apply when ERR&lt;n&gt;MISC0 is accessed through ERXMISC0\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXMISC0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXMISC0_EL1;
```

MSR ERXMISC0\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC0_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC0_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXMISC0_EL1 = X[t, 64];
```

## D24.9.9 ERXMISC1\_EL1, Selected Error Record Miscellaneous Register 1

The ERXMISC1\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;MISC1 for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXMISC1\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXMISC2[31:0].

AArch64 System register ERXMISC1\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXMISC3[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXMISC1\_EL1 are UNDEFINED.

## Attributes

ERXMISC1\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| ERRnMISC1 | ERRnMISC1 | ERRnMISC1 |
| 31        | 0         |           |
| ERRnMISC1 | ERRnMISC1 | ERRnMISC1 |

## ERRnMISC1, bits [63:0]

ERXMISC1\_EL1 accesses ERR&lt;n&gt;MISC1, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXMISC1\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC1\_EL1 is RAZ/WI.
- Direct reads and writes of ERXMISC1\_EL1 are NOPs.
- Direct reads and writes of ERXMISC1\_EL1 are UNDEFINED.

ERR&lt;n&gt;MISC1 describes additional constraints that also apply when ERR&lt;n&gt;MISC1 is accessed through ERXMISC1\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXMISC1_EL1;
```

MSR ERXMISC1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC1_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC1_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXMISC1_EL1 = X[t, 64];
```

## D24.9.10 ERXMISC2\_EL1, Selected Error Record Miscellaneous Register 2

The ERXMISC2\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;MISC2 for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXMISC2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXMISC4[31:0].

AArch64 System register ERXMISC2\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXMISC5[31:0].

This register is present only when FEAT\_RASv1p1 is implemented. Otherwise, direct accesses to ERXMISC2\_EL1 are UNDEFINED.

## Attributes

ERXMISC2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| ERRnMISC2 | ERRnMISC2 | ERRnMISC2 |
| 31        | 0         |           |
| ERRnMISC2 | ERRnMISC2 | ERRnMISC2 |

## ERRnMISC2, bits [63:0]

ERXMISC2\_EL1 accesses ERR&lt;n&gt;MISC2, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXMISC2\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC2\_EL1 is RAZ/WI.
- Direct reads and writes of ERXMISC2\_EL1 are NOPs.
- Direct reads and writes of ERXMISC2\_EL1 are UNDEFINED.

ERR&lt;n&gt;MISC2 describes additional constraints that also apply when ERR&lt;n&gt;MISC2 is accessed through ERXMISC2\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXMISC2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b010 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXMISC2_EL1;
```

MSR ERXMISC2\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b010 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC2_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC2_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXMISC2_EL1 = X[t, 64];
```

## D24.9.11 ERXMISC3\_EL1, Selected Error Record Miscellaneous Register 3

The ERXMISC3\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;MISC3 for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXMISC3\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXMISC6[31:0].

AArch64 System register ERXMISC3\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ERXMISC7[31:0].

This register is present only when FEAT\_RASv1p1 is implemented. Otherwise, direct accesses to ERXMISC3\_EL1 are UNDEFINED.

## Attributes

ERXMISC3\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| ERRnMISC3 | ERRnMISC3 | ERRnMISC3 |
| 31        | 0         |           |
| ERRnMISC3 | ERRnMISC3 | ERRnMISC3 |

## ERRnMISC3, bits [63:0]

ERXMISC3\_EL1 accesses ERR&lt;n&gt;MISC3, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXMISC3\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC3\_EL1 is RAZ/WI.
- Direct reads and writes of ERXMISC3\_EL1 are NOPs.
- Direct reads and writes of ERXMISC3\_EL1 are UNDEFINED.

ERR&lt;n&gt;MISC3 describes additional constraints that also apply when ERR&lt;n&gt;MISC3 is accessed through ERXMISC3\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXMISC3\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC3_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXMISC3_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXMISC3_EL1;
```

MSR ERXMISC3\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0101 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXMISCn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC3_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXMISC3_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXMISC3_EL1 = X[t, 64];
```

## D24.9.12 ERXPFGCDN\_EL1, Selected Pseudo-fault Generation Countdown Register

The ERXPFGCDN\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;PFGCDN for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

This register is present only when FEAT\_RASv1p1 is implemented. Otherwise, direct accesses to ERXPFGCDN\_EL1 are UNDEFINED.

## Attributes

ERXPFGCDN\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 32         |            |
|------------|------------|------------|
| ERRnPFGCDN | ERRnPFGCDN | ERRnPFGCDN |
| 31         | 0          |            |
| ERRnPFGCDN | ERRnPFGCDN | ERRnPFGCDN |

## ERRnPFGCDN, bits [63:0]

ERXPFGCDN\_EL1 accesses ERR&lt;n&gt;PFGCDN, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXPFGCDN\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXPFGCDN\_EL1 is RAZ/WI.
- Direct reads and writes of ERXPFGCDN\_EL1 are NOPs.
- Direct reads and writes of ERXPFGCDN\_EL1 are UNDEFINED.

If ERRSELR\_EL1.SEL selects an error record owned by a node that does not implement the Common Fault Injection Model Extension, then one of the following occurs:

- ERXPFGCDN\_EL1 is RAZ/WI.
- Direct reads and writes of ERXPFGCDN\_EL1 are NOPs.
- Direct reads and writes of ERXPFGCDN\_EL1 are UNDEFINED.

Note

A node does not implement the Common Fault Injection Model Extension if ERR&lt;q&gt;FR.INJ reads as 0b00 . &lt;q&gt; is the index of the first error record owned by the same node as error record &lt;n&gt;, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL. If the node owns a single record then q = n.

If ERRSELR\_EL1.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;PFGCDN is not present, meaning reads and writes of ERXPFGCDN\_EL1 are RES0.

ERR&lt;n&gt;PFGCDN describes additional constraints that also apply when ERR&lt;n&gt;PFGCDN is accessed through ERXPFGCDN\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXPFGCDN\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b110 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.FIEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXPFGCDN_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGCDN_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGCDN_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXPFGCDN_EL1;
```

MSR ERXPFGCDN\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b110 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.FIEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXPFGCDN_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXPFGCDN_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXPFGCDN_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXPFGCDN_EL1 = X[t, 64];
```

## D24.9.13 ERXPFGCTL\_EL1, Selected Pseudo-fault Generation Control Register

The ERXPFGCTL\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;PFGCTL for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

This register is present only when FEAT\_RASv1p1 is implemented. Otherwise, direct accesses to ERXPFGCTL\_EL1 are UNDEFINED.

## Attributes

ERXPFGCTL\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 32         |            |
|------------|------------|------------|
| ERRnPFGCTL | ERRnPFGCTL | ERRnPFGCTL |
| 31         | 0          |            |
| ERRnPFGCTL | ERRnPFGCTL | ERRnPFGCTL |

## ERRnPFGCTL, bits [63:0]

ERXPFGCTL\_EL1 accesses ERR&lt;n&gt;PFGCTL, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXPFGCTL\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXPFGCTL\_EL1 is RAZ/WI.
- Direct reads and writes of ERXPFGCTL\_EL1 are NOPs.
- Direct reads and writes of ERXPFGCTL\_EL1 are UNDEFINED.

If ERRSELR\_EL1.SEL selects an error record owned by a node that does not implement the Common Fault Injection Model Extension, then one of the following occurs:

- ERXPFGCTL\_EL1 is RAZ/WI.
- Direct reads and writes of ERXPFGCTL\_EL1 are NOPs.
- Direct reads and writes of ERXPFGCTL\_EL1 are UNDEFINED.

Note

A node does not implement the Common Fault Injection Model Extension if ERR&lt;q&gt;FR.INJ reads as 0b00 . &lt;q&gt; is the index of the first error record owned by the same node as error record &lt;n&gt;, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL. If the node owns a single record then q = n.

If ERRSELR\_EL1.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;PFGCTL is not present, meaning reads and writes of ERXPFGCTL\_EL1 are RES0.

ERR&lt;n&gt;PFGCTL describes additional constraints that also apply when ERR&lt;n&gt;PFGCTL is accessed through ERXPFGCTL\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXPFGCTL\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b101 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.FIEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXPFGCTL_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGCTL_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGCTL_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXPFGCTL_EL1;
```

MSR ERXPFGCTL\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b101 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.FIEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXPFGCTL_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXPFGCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXPFGCTL_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXPFGCTL_EL1 = X[t, 64];
```

## D24.9.14 ERXPFGF\_EL1, Selected Pseudo-fault Generation Feature Register

The ERXPFGF\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;PFGF for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

This register is present only when FEAT\_RASv1p1 is implemented. Otherwise, direct accesses to ERXPFGF\_EL1 are UNDEFINED.

## Attributes

ERXPFGF\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 32       |          |
|----------|----------|----------|
| ERRnPFGF | ERRnPFGF | ERRnPFGF |
| 31       | 0        |          |
| ERRnPFGF | ERRnPFGF | ERRnPFGF |

## ERRnPFGF, bits [63:0]

ERXPFGF\_EL1 accesses ERR&lt;n&gt;PFGF, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXPFGF\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXPFGF\_EL1 is RAZ.
- Direct reads of ERXPFGF\_EL1 are NOPs.
- Direct reads of ERXPFGF\_EL1 are UNDEFINED.

If ERRSELR\_EL1.SEL selects an error record owned by a node that does not implement the Common Fault Injection Model Extension, then one of the following occurs:

- ERXPFGF\_EL1 is RAZ.
- Direct reads of ERXPFGF\_EL1 are NOPs.
- Direct reads of ERXPFGF\_EL1 are UNDEFINED.

Note

A node does not implement the Common Fault Injection Model Extension if ERR&lt;q&gt;FR.INJ reads as 0b00 . &lt;q&gt; is the index of the first error record owned by the same node as error record &lt;n&gt;, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL. If the node owns a single record then q = n.

If ERRSELR\_EL1.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;PFGF is not present, meaning reads of ERXPFGF\_EL1 are RES0.

ERR&lt;n&gt;PFGF describes additional constraints that also apply when ERR&lt;n&gt;PFGF is accessed through ERXPFGF\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ERXPFGF\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_RASv1p1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.FIEN == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXPFGF_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGF_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FIEN == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FIEN == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXPFGF_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXPFGF_EL1;
```

## D24.9.15 ERXSTATUS\_EL1, Selected Error Record Primary Status Register

The ERXSTATUS\_EL1 characteristics are:

## Purpose

Accesses ERR&lt;n&gt;STATUS for the error record &lt;n&gt; selected by ERRSELR\_EL1.SEL.

## Configuration

AArch64 System register ERXSTATUS\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ERXSTATUS[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to ERXSTATUS\_EL1 are UNDEFINED.

## Attributes

ERXSTATUS\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 32         |            |
|------------|------------|------------|
| ERRnSTATUS | ERRnSTATUS | ERRnSTATUS |
| 31         | 0          |            |
| ERRnSTATUS | ERRnSTATUS | ERRnSTATUS |

## ERRnSTATUS, bits [63:0]

ERXSTATUS\_EL1 accesses ERR&lt;n&gt;STATUS, where &lt;n&gt; is the value in ERRSELR\_EL1.SEL.

## Accessing ERXSTATUS\_EL1

If ERRIDR\_EL1.NUM is 0x0000 or ERRSELR\_EL1.SEL is greater than or equal to ERRIDR\_EL1.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXSTATUS\_EL1 is RAZ/WI.
- Direct reads and writes of ERXSTATUS\_EL1 are NOPs.
- Direct reads and writes of ERXSTATUS\_EL1 are UNDEFINED.

ERR&lt;n&gt;STATUS describes additional constraints that also apply when ERR&lt;n&gt;STATUS is accessed through ERXSTATUS\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b010 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ERXSTATUS_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXSTATUS_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ERXSTATUS_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ERXSTATUS_EL1;
```

MSR ERXSTATUS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0100 | 0b010 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TERR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.ERXSTATUS_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else ERXSTATUS_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SCR_EL3.TWERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ERXSTATUS_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ERXSTATUS_EL1 = X[t, 64];
```

## D24.9.16 VDISR\_EL2, Virtual Deferred Interrupt Status Register (EL2)

The VDISR\_EL2 characteristics are:

## Purpose

Records that a virtual SError exception has been consumed by an ESB instruction executed at EL1.

An indirect write to VDISR\_EL2 made by an ESB instruction does not require an explicit synchronization operation for the value written to be observed by a direct read of one of the following registers occurring in program order after the ESB instruction:

- DISR\_EL1.
- DISR.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VDISR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register VDISR[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to VDISR\_EL2 are UNDEFINED.

## Attributes

VDISR\_EL2 is a 64-bit register.

## Field descriptions

When EL1 is using AArch64:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers a virtual SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:25]

Reserved, RES0.

## IDS, bit [24]

The value copied from VSESR\_EL2.IDS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ISS, bits [23:0]

The value copied from VSESR\_EL2.ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When EL1 is using AArch32 and VDISR\_EL2.LPAE == '0':

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers a virtual SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

The value copied from VSESR\_EL2.AET.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

The value copied from VSESR\_EL2.ExT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## FS, bits [10, 3:0]

Fault status code. Set to 0b10110 when an ESB instruction defers a virtual SError exception.

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LPAE, bit [9]

Format.

Set to TTBCR.EAE when an ESB instruction defers a virtual SError exception.

| LPAE   | Meaning                                              |
|--------|------------------------------------------------------|
| 0b0    | Using the Short-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:4]

Reserved, RES0.

## When EL1 is using AArch32 and VDISR\_EL2.LPAE == '1':

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers a virtual SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

The value copied from VSESR\_EL2.AET.

The reset behavior of this field is:

| FS      | Meaning                        |
|---------|--------------------------------|
| 0b10110 | Asynchronous SError exception. |

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

The value copied from VSESR\_EL2.ExT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:10]

Reserved, RES0.

## LPAE, bit [9]

Format.

Set to TTBCR.EAE when an ESB instruction defers a virtual SError exception.

| LPAE   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b1    | Using the Long-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:6]

Reserved, RES0.

## STATUS, bits [5:0]

Fault status code. Set to 0b010001 when an ESB instruction defers a virtual SError exception.

| STATUS   | Meaning                        |
|----------|--------------------------------|
| 0b010001 | Asynchronous SError exception. |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VDISR\_EL2

An indirect write to VDISR\_EL2 made by an ESB instruction does not require an explicit synchronization operation for the value that is written to be observed by a direct read of one of the following registers occurring in program order after the ESB instruction:

- DISR\_EL1.
- DISR.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VDISR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1100 | 0b0001 | 0b001 |

if !IsFeatureImplemented(FEAT\_RAS) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x500]; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VDISR\_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = VDISR\_EL2;

MSR VDISR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1100 | 0b0001 | 0b001 |

if !IsFeatureImplemented(FEAT\_RAS) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then NVMem[0x500] = X[t, 64]; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VDISR\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then VDISR\_EL2 = X[t, 64];

MRS &lt;Xt&gt;, DISR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then X[t, 64] = VDISR_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DISR_EL1;
```

MSR DISR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then VDISR_EL2 = X[t, 64]; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then DISR_EL1 = X[t, 64];
```

## D24.9.17 VDISR\_EL3, Virtual Deferred Interrupt Status Register (EL3)

The VDISR\_EL3 characteristics are:

## Purpose

Records that a delegated SError exception has been consumed by an ESB instruction executed at EL2 or EL1 when the Effective value of SCR\_EL3.DSE is 1.

An indirect write to VDISR\_EL3 made by an ESB instruction does not require an explicit synchronization operation for the value written to be observed by a direct read of DISR\_EL1 occurring in program order after the ESB instruction.

## Configuration

Note

The encoding for this register is subject to change.

This register is present only when FEAT\_E3DSE is implemented. Otherwise, direct accesses to VDISR\_EL3 are UNDEFINED.

## Attributes

VDISR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## A, bit [31]

Set to 1 when an ESB instruction defers a delegated SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:25]

Reserved, RES0.

## IDS, bit [24]

The value copied from VSESR\_EL3.IDS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ISS, bits [23:0]

The value copied from VSESR\_EL3.ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VDISR\_EL3

An indirect write to VDISR\_EL3 made by an ESB instruction does not require an explicit synchronization operation for the value that is written to be observed by a direct read of DISR\_EL1 occurring in program order after the ESB instruction.

Note

The accessibility pseudocode for DISR\_EL1 has not been updated to show the effect of VDISR\_EL3.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VDISR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_E3DSE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = VDISR_EL3;
```

MSR VDISR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_E3DSE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then VDISR_EL3 = X[t, 64];
```

MRS &lt;Xt&gt;, DISR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then X[t, 64] = VDISR_EL2; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then X[t, 64] = VDISR_EL3; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then X[t, 64] = Zeros(64); else X[t, 64] = DISR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DISR_EL1;
```

MSR DISR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && (HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && ↪ → IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) then VDISR_EL2 = X[t, 64]; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_E3DSE) && SCR_EL3.EnDSE == '1' then VDISR_EL3 = X[t, 64]; elsif HaveEL(EL3) && !Halted() && SCR_EL3.EA == '1' then return; else DISR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then DISR_EL1 = X[t, 64];
```

## D24.9.18 VSESR\_EL2, Virtual SError Exception Syndrome Register (EL2)

The VSESR\_EL2 characteristics are:

## Purpose

Provides the syndrome value reported to software on taking a virtual SError exception to EL1, or on executing an ESB instruction at EL1.

When the virtual SError exception injected using HCR\_EL2.VSE is taken to EL1 using AArch64, then the syndrome value is reported in ESR\_EL1.

When the virtual SError exception injected using HCR\_EL2.VSE is taken to EL1 using AArch32, then the syndrome value is reported in DFSR.{AET, ExT} and the remainder of DFSR is set as defined by VMSAv8-32. For more information, see The AArch32 Virtual Memory System Architecture.

When the virtual SError exception injected using HCR\_EL2.VSE is deferred by an ESB instruction, then the syndrome value is written to VDISR\_EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VSESR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register VDFSR[31:0].

This register is present only when FEAT\_RAS is implemented. Otherwise, direct accesses to VSESR\_EL2 are UNDEFINED.

## Attributes

VSESR\_EL2 is a 64-bit register.

## Field descriptions

When EL1 is using AArch32:

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## AET, bits [15:14]

When a virtual SError exception is taken to EL1 using AArch32, DFSR[15:14] is set to VSESR\_EL2.AET.

When a virtual SError exception is deferred by an ESB instruction, VDISR\_EL2[15:14] is set to VSESR\_EL2.AET.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

When a virtual SError exception is taken to EL1 using AArch32, DFSR[12] is set to VSESR\_EL2.ExT.

When a virtual SError exception is deferred by an ESB instruction, VDISR\_EL2[12] is set to VSESR\_EL2.ExT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## When EL1 is using AArch64:

<!-- image -->

## Bits [63:25]

Reserved, RES0.

## IDS, bit [24]

When a virtual SError exception is taken to EL1 using AArch64, ESR\_EL1[24] is set to VSESR\_EL2.IDS.

When a virtual SError exception is deferred by an ESB instruction, VDISR\_EL2[24] is set to VSESR\_EL2.IDS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ISS, bits [23:0]

When a virtual SError exception is taken to EL1 using AArch64, ESR\_EL1[23:0] is set to VSESR\_EL2.ISS.

When a virtual SError exception is deferred by an ESB instruction, VDISR\_EL2[23:0] is set to VSESR\_EL2.ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VSESR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VSESR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x508]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VSESR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = VSESR_EL2;
```

MSR VSESR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0010 | 0b011 |

```
if !IsFeatureImplemented(FEAT_RAS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x508] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VSESR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then VSESR_EL2 = X[t, 64];
```

## D24.9.19 VSESR\_EL3, Virtual SError Exception Syndrome Register (EL3)

The VSESR\_EL3 characteristics are:

## Purpose

Provides the syndrome value reported to software when the Effective value of SCR\_EL3.DSE is 1 on taking a delegated SError exception to EL2 or EL1, or on executing an ESB instruction at EL2 or EL1.

When the delegated SError exception injected using SCR\_EL3.DSE is taken to EL2 using AArch64, then the syndrome value is reported in ESR\_EL2.

When the delegated SError exception injected using SCR\_EL3.DSE is taken to EL1 using AArch64, then the syndrome value is reported in ESR\_EL1.

When the delegated SError exception injected using SCR\_EL3.DSE is deferred by an ESB instruction, then the syndrome value is written to VDISR\_EL3.

## Configuration

This register is present only when FEAT\_E3DSE is implemented. Otherwise, direct accesses to VSESR\_EL3 are UNDEFINED.

## Attributes

VSESR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:25]

Reserved, RES0.

## IDS, bit [24]

When a delegated SError exception triggered by SCR\_EL3.DSE is taken to EL2 or EL1 using AArch64, ESR\_ELx[24] is set to VSESR\_EL3.IDS.

When a delegated SError exception triggered by SCR\_EL3.DSE is deferred by an ESB instruction, VDISR\_EL3[24] is set to VSESR\_EL3.IDS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ISS, bits [23:0]

When a delegated SError exception triggered by SCR\_EL3.DSE is taken to EL2 or EL1 using AArch64, ESR\_ELx[23:0] is set to VSESR\_EL3.ISS.

When a delegated SError exception triggered by SCR\_EL3.DSE is deferred by an ESB instruction, VDISR\_EL3[23:0] is set to VSESR\_EL3.ISS.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VSESR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VSESR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0101 | 0b0010 | 0b011 |

if !IsFeatureImplemented(FEAT\_E3DSE) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = VSESR\_EL3;

MSR VSESR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0101 | 0b0010 | 0b011 |

if !IsFeatureImplemented(FEAT\_E3DSE) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

VSESR\_EL3 = X[t, 64];