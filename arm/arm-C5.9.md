## C5.9 A64 System instructions for the Guarded Control Stack

This section lists the A64 System instructions for the Guarded Control Stack.

## C5.9.1 GCSPOPCX, Guarded Control Stack Pop and Compare exception return record

The GCSPOPCX characteristics are:

## Purpose

Loads an exception return record from the location indicated by the current Guarded Control Stack Pointer register, compares the values loaded with the current ELR\_ELx, SPSR\_ELx, and LR, and increments the current Guarded Control Stack Pointer register by the size of a Guarded Control Stack exception return record.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSPOPCX are UNDEFINED.

## Attributes

GCSPOPCX is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing GCSPOPCX

Rt should be encoded as 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSPOPCX

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.nGCSEPP == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif GCSEnabled(EL1) then GCSPOPCX(); elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); elsif GCSEnabled(EL2) then GCSPOPCX(); elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException();
```

elsif GCSEnabled(EL3) then GCSPOPCX();

## C5.9.2 GCSPOPM, Guarded Control Stack Pop

The GCSPOPM characteristics are:

## Purpose

Loads the 64-bit doubleword that is pointed to by the current Guarded Control Stack Pointer, writes it to the destination register, and increments the current Guarded Control Stack Pointer register by the size of a Guarded Control Stack procedure return record.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSPOPM are UNDEFINED.

## Attributes

GCSPOPMis a 64-bit System instruction.

## Field descriptions

| 63                                                             | 32   |
|----------------------------------------------------------------|------|
| Output value for Guarded Control Stack procedure return record |      |
| 31                                                             | 0    |
| Output value for Guarded Control Stack procedure return record |      |

## Output, bits [63:0]

Output value for Guarded Control Stack procedure return record.

## Executing GCSPOPM

This system instruction is an alias of the SYSL instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSPOPM {&lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif GCSEnabled(PSTATE.EL) then X[t, 64] = GCSPOPM();
```

## C5.9.3 GCSPOPX, Guarded Control Stack Pop exception return record

The GCSPOPX characteristics are:

## Purpose

Loads an exception return record from the location indicated by the current Guarded Control Stack Pointer register, checks that the record is a Guarded Control Stack exception return record, and increments the current Guarded Control Stack Pointer register by the size of a Guarded Control Stack exception return record.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSPOPX are UNDEFINED.

## Attributes

GCSPOPX is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing GCSPOPX

Rt should be encoded as 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSPOPX

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if GCSEnabled(EL1) then GCSPOPX(); elsif PSTATE.EL == EL2 then if GCSEnabled(EL2) then GCSPOPX(); elsif PSTATE.EL == EL3 then if GCSEnabled(EL3) then GCSPOPX();
```

## C5.9.4 GCSPUSHM, Guarded Control Stack Push

The GCSPUSHM characteristics are:

## Purpose

Decrements the current Guarded Control Stack Pointer register by the size of a Guarded Control Stack procedure return record and stores an entry to the Guarded Control Stack.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSPUSHM are UNDEFINED.

## Attributes

GCSPUSHMis a 64-bit System instruction.

## Field descriptions

| 63                                                            | 32   |
|---------------------------------------------------------------|------|
| Input value for Guarded Control Stack procedure return record |      |
| 31                                                            | 0    |
| Input value for Guarded Control Stack procedure return record |      |

## Input, bits [63:0]

Input value for Guarded Control Stack procedure return record.

## Executing GCSPUSHM

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSPUSHM &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if (!EL2Enabled() || HCR_EL2.TGE != '1') && GCSCRE0_EL1.PUSHMEn == '0' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && HCR_EL2.TGE == '1' && GCSCRE0_EL1.PUSHMEn == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif GCSEnabled(EL0) then GCSPUSHM(X[t, 64]); elsif PSTATE.EL == EL1 then if GCSCR_EL1.PUSHMEn == '0' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.nGCSPUSHM_EL1 == '0' then
```

AArch64.SystemAccessTrap(EL2, 0x18); elsif GCSEnabled(EL1) then GCSPUSHM(X[t, 64]); elsif PSTATE.EL == EL2 then if GCSCR\_EL2.PUSHMEn == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif GCSEnabled(EL2) then GCSPUSHM(X[t, 64]); elsif PSTATE.EL == EL3 then if GCSCR\_EL3.PUSHMEn == '0' then AArch64.SystemAccessTrap(EL3, 0x18); elsif GCSEnabled(EL3) then GCSPUSHM(X[t, 64]);

## C5.9.5 GCSPUSHX, Guarded Control Stack Push exception return record

The GCSPUSHX characteristics are:

## Purpose

Decrements the current Guarded Control Stack Pointer register by the size of a Guarded Control Stack exception return record and stores a Guarded Control Stack exception return record to the Guarded Control Stack.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSPUSHX are UNDEFINED.

## Attributes

GCSPUSHX is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing GCSPUSHX

Rt should be encoded as 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSPUSHX

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '0' then EXLOCKException(); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.nGCSEPP == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif GCSEnabled(EL1) then GCSPUSHX(); elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '0' then EXLOCKException(); elsif GCSEnabled(EL2) then GCSPUSHX(); elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '0' then EXLOCKException(); elsif GCSEnabled(EL3) then GCSPUSHX();
```

## C5.9.6 GCSSS1, Guarded Control Stack Switch Stack 1

The GCSSS1 characteristics are:

## Purpose

Validates that the stack being switched to contains a Valid cap entry, stores an In-progress cap entry on to the stack that is getting switched to and sets the current Guarded Control Stack Pointer to the stack that is getting switched to.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSSS1 are UNDEFINED.

## Attributes

GCSSS1 is a 64-bit System instruction.

## Field descriptions

| 63                                                       | 32   |
|----------------------------------------------------------|------|
| Incoming address, for the incoming Guarded Control Stack |      |
| 31                                                       | 0    |
| Incoming address, for the incoming Guarded Control Stack |      |

## IA, bits [63:0]

Incoming address, for the incoming Guarded Control Stack.

## Executing GCSSS1

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSSS1 &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_GCS) && UNDEFINED; elsif GCSEnabled(PSTATE.EL) then GCSSS1(X[t, 64]);
```

```
IsFeatureImplemented(FEAT_AA64)) then
```

## C5.9.7 GCSSS2, Guarded Control Stack Switch Stack 2

The GCSSS2 characteristics are:

## Purpose

Validates that the most recent entry of the Guarded Control Stack that is getting switched to contains an In-progress cap entry, stores a Valid cap entry to the Guarded Control Stack that is getting switched from, and sets Xt to the address of that Valid cap entry.

## Configuration

This system instruction is present only when FEAT\_GCS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to GCSSS2 are UNDEFINED.

## Attributes

GCSSS2 is a 64-bit System instruction.

## Field descriptions

| 63                                                       | 32   |
|----------------------------------------------------------|------|
| Outgoing address, for the outgoing Guarded Control Stack |      |
| 31                                                       | 0    |
| Outgoing address, for the outgoing Guarded Control Stack |      |

## OA, bits [63:0]

Outgoing address, for the outgoing Guarded Control Stack.

## Executing GCSSS2

This system instruction is an alias of the SYSL instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

GCSSS2 &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_GCS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif GCSEnabled(PSTATE.EL) then X[t, 64] = GCSSS2();
```