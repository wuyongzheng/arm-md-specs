## C5.8 A64 System instructions for the Trace Extension

This section lists the A64 System instructions for the Trace Extension.

## C5.8.1 TRCIT, Trace Instrumentation

The TRCIT characteristics are:

## Purpose

Generates an instrumentation packet in the trace.

## Configuration

This system instruction is present only when FEAT\_ITE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCIT are UNDEFINED.

## Attributes

TRCIT is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63    | 32    |       |
|-------|-------|-------|
| VALUE | VALUE | VALUE |
| 31    | 0     |       |
| VALUE | VALUE | VALUE |

## VALUE, bits [63:0]

Value to be included in the Instrumentation packet.

## Executing TRCIT

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TRCIT &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0010 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL1 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL2 then AArch64.TRCIT(X[t, 64]); elsif PSTATE.EL == EL3 then AArch64.TRCIT(X[t, 64]);
```