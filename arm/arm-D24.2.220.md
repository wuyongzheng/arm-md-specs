## D24.2.220 VNCR\_EL2, Virtual Nested Control Register

The VNCR\_EL2 characteristics are:

## Purpose

When FEAT\_NV2 is implemented, holds the base address that is used to define the memory location that is accessed by transformed reads and writes of System registers.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_NV2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to VNCR\_EL2 are UNDEFINED.

## Attributes

VNCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## BADDR, bits [63:12]

Base Address. When a register read/write is transformed to be a Load or Store, the address of the load/store is to VNCR\_EL2.BADDR:Offset&lt;11:0&gt;.

Bits[63:n] are RESS where n is one of the following:

- If FEAT\_LVA3 is implemented, n is 57.
- Otherwise, if FEAT\_LVA is implemented, n is 53.
- If FEAT\_LVA is not implemented, n is 49.

If the bits marked as RESS do not all have the same value as bit[n-1], then there is a CONSTRAINED UNPREDICTABLE choice between:

- Generating a Translation fault when translating the transformed register read/write.
- The bits behave as the same value as bit[n-1] for all purposes other than reading back the register.
- The bits are treated as the same value as bit[n-1] for all purposes.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing VNCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VNCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0010 | 0b000 |

if !(IsFeatureImplemented(FEAT\_NV2) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then

X[t, 64] = NVMem[0x0B0];

elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then

AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

X[t, 64] = VNCR\_EL2;

elsif PSTATE.EL == EL3 then

X[t, 64] = VNCR\_EL2;

MSR VNCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0010 | 0b000 |

if !(IsFeatureImplemented(FEAT\_NV2) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'1x1'} then NVMem[0x0B0] = X[t, 64]; elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VNCR\_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then VNCR\_EL2 = X[t, 64];