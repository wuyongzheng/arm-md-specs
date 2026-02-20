## G8.6 RAS registers

This section lists RAS Extension registers in AArch32.

## G8.6.1 DISR, Deferred Interrupt Status Register

The DISR characteristics are:

## Purpose

Records that an SError exception has been consumed by an ESB instruction.

## Configuration

AArch32 System register DISR bits [31:0] are architecturally mapped to AArch64 System register DISR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DISR are UNDEFINED.

## Attributes

DISR is a 32-bit register.

## Field descriptions

When the ESB instruction is executed at EL2:

<!-- image -->

| 31 30   | 12 11 10 9 8   |
|---------|----------------|
| A       | AET EA RES0    |

## A, bit [31]

Set to 1 when an ESB instruction defers an asynchronous SError exception. If the implementation does not include any sources of SError exception that can be synchronized by an Error Synchronization Barrier, then this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:12]

Reserved, RES0.

## AET, bits [11:10]

Asynchronous Error Type. See the description of HSR.AET for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [9]

External abort Type. See the description of HSR.EA for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:6]

Reserved, RES0.

## DFSC, bits [5:0]

Fault Status Code. See the description of HSR.DFSC for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When the ESB instruction is executed at EL0 or EL1 and where TTBCR.EAE == 0:

<!-- image -->

## A, bit [31]

Set to 1 when an ESB instruction defers an asynchronous SError exception. If the implementation does not include any sources of SError exception that can be synchronized by an Error Synchronization Barrier, then this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

Asynchronous Error Type. See the description of DFSR.AET for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

External abort Type. See the description of DFSR.ExT for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## FS, bits [10, 3:0]

Fault Status Code. See the description of DFSR.FS for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LPAE, bit [9]

Format.

| LPAE   | Meaning                                              |
|--------|------------------------------------------------------|
| 0b0    | Using the Short-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:4]

Reserved, RES0.

## When the ESB instruction is executed at EL0 or EL1 and where TTBCR.EAE == 1:

<!-- image -->

## A, bit [31]

Set to 1 when an ESB instruction defers an asynchronous SError exception. If the implementation does not include any sources of SError exception that can be synchronized by an Error Synchronization Barrier, then this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

Asynchronous Error Type. See the description of DFSR.AET for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

External abort Type. See the description of DFSR.ExT for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:10]

Reserved, RES0.

## LPAE, bit [9]

Format.

| LPAE   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b1    | Using the Long-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:6]

Reserved, RES0.

## STATUS, bits [5:0]

Fault Status Code. See the description of DFSR.FS for an SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DISR

An indirect write to DISR made by an ESB instruction does not require an explicit synchronization operation for the value that is written to be observed by a direct read of DISR occurring in program order after the ESB instruction.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (HCR_EL2.AMO == ↪ → '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && IsHCRXEL2Enabled() && HCRX_EL2.TMEA == ↪ → '1')) then R[t] = VDISR_EL2<31:0>; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.AMO == '1' ↪ → then R[t] = VDISR; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then R[t] = Zeros(32); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then R[t] = Zeros(32); else R[t] = DISR; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then R[t] = Zeros(32); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then R[t] = Zeros(32); else R[t] = DISR; elsif PSTATE.EL == EL3 then R[t] = DISR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (HCR_EL2.AMO == ↪ → '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && IsHCRXEL2Enabled() && HCRX_EL2.TMEA == ↪ → '1')) then VDISR_EL2 = R[t]; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.AMO == '1' ↪ → then VDISR = R[t]; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then return; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then return; else DISR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then return; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then return; else DISR = R[t]; elsif PSTATE.EL == EL3 then DISR = R[t];
```

## G8.6.2 ERRIDR, Error Record ID Register

The ERRIDR characteristics are:

## Purpose

Defines the highest numbered index of the error records that can be accessed through the Error Record System registers.

## Configuration

AArch32 System register ERRIDR bits [31:0] are architecturally mapped to AArch64 System register ERRIDR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERRIDR are UNDEFINED.

## Attributes

ERRIDR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## NUM,bits [15:0]

Highest numbered index of the records that can be accessed through the Error Record System registers plus one. Zero indicates that no records can be accessed through the Error Record System registers.

Each implemented record is owned by a node. A node might own multiple records.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing ERRIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0011 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERRIDR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERRIDR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERRIDR;
```

## G8.6.3 ERRSELR, Error Record Select Register

The ERRSELR characteristics are:

## Purpose

Selects an error record to be accessed through the Error Record System registers.

## Configuration

If ERRIDR indicates that zero error records are implemented, then it is IMPLEMENTATION DEFINED whether ERRSELR is UNDEFINED or RES0.

AArch32 System register ERRSELR bits [31:0] are architecturally mapped to AArch64 System register ERRSELR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERRSELR are UNDEFINED.

## Attributes

ERRSELR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## SEL, bits [15:0]

Selects the error record accessed through the ERX registers.

For example, if ERRSELR.SEL is 0x0004 , then direct reads and writes of ERXSTATUS access ERR4STATUS.

If ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then all of the following apply:

- The value read back from ERRSELR.SEL is UNKNOWN.
- One of the following occurs:
- An UNKNOWN error record is selected.
- The ERX* registers are RAZ/WI.
- ERX* register reads and writes are NOPs.
- ERX* register reads and writes are UNDEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ERRSELR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0011 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERRSELR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERRSELR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException();
```

```
else R[t] = ERRSELR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0011 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERRSELR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERRSELR = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERRSELR = R[t];
```

## G8.6.4 ERXADDR, Selected Error Record Address Register

The ERXADDR characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;ADDR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXADDR bits [31:0] are architecturally mapped to AArch64 System register ERXADDR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXADDR are UNDEFINED.

## Attributes

ERXADDRis a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnADDR 31 0
```

## ERRnADDRlo, bits [31:0]

ERXADDRaccesses bits [31:0] of ERR&lt;n&gt;ADDR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXADDR

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXADDRis RAZ/WI.
- Direct reads and writes of ERXADDR are NOPs.
- Direct reads and writes of ERXADDR are UNDEFINED.

ERR&lt;n&gt;ADDR describes additional constraints that also apply when ERR&lt;n&gt;ADDR is accessed through ERXADDR.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXADDR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXADDR = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXADDR = R[t];
```

## G8.6.5 ERXADDR2, Selected Error Record Address Register 2

The ERXADDR2 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;ADDR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXADDR2 bits [31:0] are architecturally mapped to AArch64 System register ERXADDR\_EL1[63:32].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXADDR2 are UNDEFINED.

## Attributes

ERXADDR2is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnADDR 31 0
```

## ERRnADDRhi, bits [31:0]

ERXADDR2accesses bits [63:32] of ERR&lt;n&gt;ADDR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXADDR2

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXADDR2is RAZ/WI.
- Direct reads and writes of ERXADDR2 are NOPs.
- Direct reads and writes of ERXADDR2 are UNDEFINED.

ERR&lt;n&gt;ADDR describes additional constraints that also apply when ERR&lt;n&gt;ADDR is accessed through ERXADDR2.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR2; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXADDR2;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXADDR2 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXADDR2 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXADDR2 = R[t];
```

## G8.6.6 ERXCTLR, Selected Error Record Control Register

The ERXCTLR characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;CTLR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXCTLR bits [31:0] are architecturally mapped to AArch64 System register ERXCTLR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXCTLR are UNDEFINED.

## Attributes

ERXCTLR is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnCTLR 31 0
```

## ERRnCTLRlo, bits [31:0]

ERXCTLR accesses bits [31:0] of ERR&lt;n&gt;CTLR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXCTLR

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXCTLR is RAZ/WI.
- Direct reads and writes of ERXCTLR are NOPs.
- Direct reads and writes of ERXCTLR are UNDEFINED.

If ERRSELR.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;CTLR[31:0] is not present, meaning reads and writes of ERXCTLR are RES0.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXCTLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXCTLR = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXCTLR = R[t];
```

## G8.6.7 ERXCTLR2, Selected Error Record Control Register 2

The ERXCTLR2 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;CTLR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXCTLR2 bits [31:0] are architecturally mapped to AArch64 System register ERXCTLR\_EL1[63:32].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXCTLR2 are UNDEFINED.

## Attributes

ERXCTLR2 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnCTLR 31 0
```

## ERRnCTLRhi, bits [31:0]

ERXCTLR2 accesses bits [63:32] of ERR&lt;n&gt;CTLR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXCTLR2

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXCTLR2 is RAZ/WI.
- Direct reads and writes of ERXCTLR2 are NOPs.
- Direct reads and writes of ERXCTLR2 are UNDEFINED.

If ERRSELR.SEL is not the index of the first error record owned by a node, then ERR&lt;n&gt;CTLR[63:32] is not present, meaning reads and writes of ERXCTLR2 are RES0.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR2; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXCTLR2;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXCTLR2 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXCTLR2 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXCTLR2 = R[t];
```

## G8.6.8 ERXFR, Selected Error Record Feature Register

The ERXFR characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;FR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXFR bits [31:0] are architecturally mapped to AArch64 System register ERXFR\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXFR are UNDEFINED.

## Attributes

ERXFR is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnFR 31 0
```

## ERRnFRlo, bits [31:0]

ERXFR accesses bits [31:0] of ERR&lt;n&gt;FR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXFR

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXFR is RAZ.
- Direct reads of ERXFR are NOPs.
- Direct reads of ERXFR are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXFR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXFR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXFR;
```

## G8.6.9 ERXFR2, Selected Error Record Feature Register 2

The ERXFR2 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;FR for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXFR2 bits [31:0] are architecturally mapped to AArch64 System register ERXFR\_EL1[63:32].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXFR2 are UNDEFINED.

## Attributes

ERXFR2 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnFR 31 0
```

## ERRnFRhi, bits [31:0]

ERXFR2 accesses bits [63:32] of ERR&lt;n&gt;FR, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXFR2

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXFR2 is RAZ.
- Direct reads of ERXFR2 are NOPs.
- Direct reads of ERXFR2 are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXFR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXFR2; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXFR2;
```

## G8.6.10 ERXMISC0, Selected Error Record Miscellaneous Register 0

The ERXMISC0 characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;MISC0 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC0 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC0\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC0 are UNDEFINED.

## Attributes

ERXMISC0 is a 32-bit register.

## Field descriptions

ERRnMISC0lo

```
Bits [31:0] of ERRnMISC0 31 0
```

## ERRnMISC0lo, bits [31:0]

ERXMISC0 accesses bits [31:0] of ERR&lt;n&gt;MISC0, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC0

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC0 is RAZ/WI.
- Direct reads and writes of ERXMISC0 are NOPs.
- Direct reads and writes of ERXMISC0 are UNDEFINED.

ERR&lt;n&gt;MISC0 describes additional constraints that also apply when ERR&lt;n&gt;MISC0 is accessed through ERXMISC0.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC0; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC0;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC0 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC0 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC0 = R[t];
```

## G8.6.11 ERXMISC1, Selected Error Record Miscellaneous Register 1

The ERXMISC1 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;MISC0 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC1 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC0\_EL1[63:32].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC1 are UNDEFINED.

## Attributes

ERXMISC1 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnMISC0 31 0
```

## ERRnMISC0hi, bits [31:0]

ERXMISC1 accesses bits [63:32] of ERR&lt;n&gt;MISC0, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC1

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC1 is RAZ/WI.
- Direct reads and writes of ERXMISC1 are NOPs.
- Direct reads and writes of ERXMISC1 are UNDEFINED.

ERR&lt;n&gt;MISC0 describes additional constraints that also apply when ERR&lt;n&gt;MISC0 is accessed through ERXMISC1.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC1; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC1;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC1 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC1 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC1 = R[t];
```

## G8.6.12 ERXMISC2, Selected Error Record Miscellaneous Register 2

The ERXMISC2 characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;MISC1 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC2 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC1\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC2 are UNDEFINED.

## Attributes

ERXMISC2 is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnMISC1 31 0
```

## ERRnMISC1lo, bits [31:0]

ERXMISC2 accesses bits [31:0] of ERR&lt;n&gt;MISC1, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC2

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC2 is RAZ/WI.
- Direct reads and writes of ERXMISC2 are NOPs.
- Direct reads and writes of ERXMISC2 are UNDEFINED.

ERR&lt;n&gt;MISC1 describes additional constraints that also apply when ERR&lt;n&gt;MISC1 is accessed through ERXMISC2.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC2; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC2;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC2 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC2 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC2 = R[t];
```

## G8.6.13 ERXMISC3, Selected Error Record Miscellaneous Register 3

The ERXMISC3 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;MISC1 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC3 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC1\_EL1[63:32].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC3 are UNDEFINED.

## Attributes

ERXMISC3 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnMISC1 31 0
```

## ERRnMISC1hi, bits [31:0]

ERXMISC3 accesses bits [63:32] of ERR&lt;n&gt;MISC1, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC3

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC3 is RAZ/WI.
- Direct reads and writes of ERXMISC3 are NOPs.
- Direct reads and writes of ERXMISC3 are UNDEFINED.

ERR&lt;n&gt;MISC1 describes additional constraints that also apply when ERR&lt;n&gt;MISC1 is accessed through ERXMISC3.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC3; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC3; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC3;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC3 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC3 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC3 = R[t];
```

## G8.6.14 ERXMISC4, Selected Error Record Miscellaneous Register 4

The ERXMISC4 characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;MISC2 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC4 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC2\_EL1[31:0].

This register is present only when FEAT\_RASv1p1 is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC4 are UNDEFINED.

## Attributes

ERXMISC4 is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnMISC2 31 0
```

## ERRnMISC2lo, bits [31:0]

ERXMISC4 accesses bits [31:0] of ERR&lt;n&gt;MISC2, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC4

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC4 is RAZ/WI.
- Direct reads and writes of ERXMISC4 are NOPs.
- Direct reads and writes of ERXMISC4 are UNDEFINED.

ERR&lt;n&gt;MISC2 describes additional constraints that also apply when ERR&lt;n&gt;MISC2 is accessed through ERXMISC4.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC4; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC4; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC4;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC4 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC4 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC4 = R[t];
```

## G8.6.15 ERXMISC5, Selected Error Record Miscellaneous Register 5

The ERXMISC5 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;MISC2 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC5 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC2\_EL1[63:32].

This register is present only when FEAT\_RASv1p1 is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC5 are UNDEFINED.

## Attributes

ERXMISC5 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnMISC2 31 0
```

## ERRnMISC2hi, bits [31:0]

ERXMISC5 accesses bits [63:32] of ERR&lt;n&gt;MISC2, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC5

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC5 is RAZ/WI.
- Direct reads and writes of ERXMISC5 are NOPs.
- Direct reads and writes of ERXMISC5 are UNDEFINED.

ERR&lt;n&gt;MISC2 describes additional constraints that also apply when ERR&lt;n&gt;MISC2 is accessed through ERXMISC5.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC5; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC5; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC5;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC5 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC5 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC5 = R[t];
```

## G8.6.16 ERXMISC6, Selected Error Record Miscellaneous Register 6

The ERXMISC6 characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;MISC3 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC6 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC3\_EL1[31:0].

This register is present only when FEAT\_RASv1p1 is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC6 are UNDEFINED.

## Attributes

ERXMISC6 is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnMISC3 31 0
```

## ERRnMISC3lo, bits [31:0]

ERXMISC6 accesses bits [31:0] of ERR&lt;n&gt;MISC3, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC6

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC6 is RAZ/WI.
- Direct reads and writes of ERXMISC6 are NOPs.
- Direct reads and writes of ERXMISC6 are UNDEFINED.

ERR&lt;n&gt;MISC3 describes additional constraints that also apply when ERR&lt;n&gt;MISC3 is accessed through ERXMISC6.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b110  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC6; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC6; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC6;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b110  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC6 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC6 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC6 = R[t];
```

## G8.6.17 ERXMISC7, Selected Error Record Miscellaneous Register 7

The ERXMISC7 characteristics are:

## Purpose

Accesses bits [63:32] of ERR&lt;n&gt;MISC3 for the error record &lt;n&gt; selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXMISC7 bits [31:0] are architecturally mapped to AArch64 System register ERXMISC3\_EL1[63:32].

This register is present only when FEAT\_RASv1p1 is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXMISC7 are UNDEFINED.

## Attributes

ERXMISC7 is a 32-bit register.

## Field descriptions

```
Bits [63:32] of ERRnMISC3 31 0
```

## ERRnMISC3hi, bits [31:0]

ERXMISC7 accesses bits [63:32] of ERR&lt;n&gt;MISC3, where &lt;n&gt; is the value in ERRSELR.SEL.

## Accessing ERXMISC7

If ERRIDR.NUM is 0x0000 or ERRSELR.SEL is greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN error record is selected.
- ERXMISC7 is RAZ/WI.
- Direct reads and writes of ERXMISC7 are NOPs.
- Direct reads and writes of ERXMISC7 are UNDEFINED.

ERR&lt;n&gt;MISC3 describes additional constraints that also apply when ERR&lt;n&gt;MISC3 is accessed through ERXMISC7.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC7; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC7; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXMISC7;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0101 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_RASv1p1) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC7 = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXMISC7 = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXMISC7 = R[t];
```

## G8.6.18 ERXSTATUS, Selected Error Record Primary Status Register

The ERXSTATUS characteristics are:

## Purpose

Accesses bits [31:0] of ERR&lt;n&gt;STATUS for the error record selected by ERRSELR.SEL.

## Configuration

AArch32 System register ERXSTATUS bits [31:0] are architecturally mapped to AArch64 System register ERXSTATUS\_EL1[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ERXSTATUS are UNDEFINED.

## Attributes

ERXSTATUS is a 32-bit register.

## Field descriptions

```
Bits [31:0] of ERRnSTATUS 31 0
```

## ERRnSTATUSlo, bits [31:0]

ERXSTATUS accesses bits [31:0] of ERR&lt;n&gt;STATUS, where n is the value in ERRSELR.SEL.

## Accessing ERXSTATUS

If ERRIDR.NUM == 0 or ERRSELR.SEL is set to a value greater than or equal to ERRIDR.NUM, then one of the following occurs:

- An UNKNOWN record is selected.
- ERXSTATUS is RAZ/WI.
- Direct reads and writes of ERXSTATUS are NOPs.
- Direct reads and writes of ERXSTATUS are UNDEFINED.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXSTATUS; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = ERXSTATUS; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else R[t] = ERXSTATUS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0100 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TERR == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR2.TERR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SCR.TERR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXSTATUS = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && SCR_EL3.TWERR == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SCR.TERR == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TERR == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.TWERR == ↪ → '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.TERR == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else ERXSTATUS = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SCR.TERR == '1' then AArch32.TakeMonitorTrapException(); else ERXSTATUS = R[t];
```

## G8.6.19 VDFSR, Virtual SError Exception Syndrome Register

The VDFSR characteristics are:

## Purpose

Provides the syndrome value reported to software on taking a virtual SError exception exception to EL1, or on executing an ESB instruction at EL1.

When the virtual SError exception injected using HCR.V A is taken to EL1 using AArch32, then the syndrome value is reported in DFSR.{AET, ExT} and the remainder of DFSR is set as defined by VMSAv8-32. For more information, see The AArch32 Virtual Memory System Architecture.

If the virtual SError exception injected using HCR.V A is deferred by an ESB instruction, then the syndrome value is written to VDISR.

## Configuration

If EL2 is not implemented, then VDFSR is RES0 from Monitor mode when SCR.NS == 1.

AArch32 System register VDFSR bits [31:0] are architecturally mapped to AArch64 System register VSESR\_EL2[31:0].

This register is present only when FEAT\_RAS is implemented and FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to VDFSR are UNDEFINED.

## Attributes

VDFSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## AET, bits [15:14]

When a virtual SError exception is taken to EL1 using AArch32, DFSR[15:14] is set to VDFSR.AET.

When a virtual SError exception is deferred by an ESB instruction, VDISR[15:14] is set to VDFSR.AET.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

When a virtual SError exception is taken to EL1 using AArch32, DFSR[12] is set to VDFSR.ExT.

When a virtual SError exception is deferred by an ESB instruction, VDISR[12] is set to VDFSR.ExT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing VDFSR

Direct reads and writes of VDFSR are UNDEFINED if EL3 is implemented and using AArch32 in all Secure privileged modes other than Monitor mode.

If EL2 is not implemented, then VDFSR is RES0 from Monitor mode when SCR.NS == 1.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0101 | 0b0010 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = VDFSR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = VDFSR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0101 | 0b0010 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

else

```
UNDEFINED; elsif PSTATE.EL == EL2 then VDFSR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else VDFSR = R[t];
```

## G8.6.20 VDISR, Virtual Deferred Interrupt Status Register

The VDISR characteristics are:

## Purpose

Records that an SError exception has been consumed by an ESB instruction.

## Configuration

If EL2 is not implemented, then VDISR is RES0 from Monitor mode when SCR.NS == 1.

AArch32 System register VDISR bits [31:0] are architecturally mapped to AArch64 System register VDISR\_EL2[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_RAS is implemented. Otherwise, direct accesses to VDISR are UNDEFINED.

## Attributes

VDISR is a 32-bit register.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## A, bit [31]

Set to 1 when an ESB instruction defers a virtual SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

The value copied from VDFSR.AET.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

The value copied from VDFSR.ExT.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## FS, bits [10, 3:0]

Fault status code. Set to 0b10110 when an ESB instruction defers a virtual SError exception.

| FS      | Meaning                        |
|---------|--------------------------------|
| 0b10110 | Asynchronous SError exception. |

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

When TTBCR.EAE == '1':

<!-- image -->

## A, bit [31]

Set to 1 when an ESB instruction defers a virtual SError exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [30:16]

Reserved, RES0.

## AET, bits [15:14]

The value copied from VDFSR.AET.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## ExT, bit [12]

The value copied from VDFSR.ExT.

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

## Accessing VDISR

Direct reads and writes of VDFSR are UNDEFINED if EL3 is implemented and using AArch32 in all Secure privileged modes other than Monitor mode.

An indirect write to VDISR made by an ESB instruction does not require an explicit synchronization operation for the value that is written to be observed by a direct read of DISR occurring in program order after the ESB instruction.

If EL2 is not implemented, then VDISR is RES0 from Monitor mode when SCR.NS == 1.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_RAS)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = VDISR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = VDISR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_RAS)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then VDISR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else VDISR = R[t];
```

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (HCR_EL2.AMO == ↪ → '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && IsHCRXEL2Enabled() && HCRX_EL2.TMEA == ↪ → '1')) then R[t] = VDISR_EL2<31:0>; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.AMO == '1' ↪ → then R[t] = VDISR; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then R[t] = Zeros(32); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then R[t] = Zeros(32); else R[t] = DISR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then R[t] = Zeros(32); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then R[t] = Zeros(32); else R[t] = DISR; elsif PSTATE.EL == EL3 then R[t] = DISR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0001 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_RAS) && IsFeatureImplemented(FEAT_AA32EL1)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && (HCR_EL2.AMO == ↪ → '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && IsHCRXEL2Enabled() && HCRX_EL2.TMEA == ↪ → '1')) then VDISR_EL2 = R[t]; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.AMO == '1' ↪ → then VDISR = R[t]; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then return; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then return; else DISR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && !Halted() && ↪ → SCR_EL3.EA == '1' then return; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && !Halted() && ↪ → SCR.EA == '1' then return; else DISR = R[t]; elsif PSTATE.EL == EL3 then DISR = R[t];
```