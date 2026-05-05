## C6.2.170 GCSSTTR

Guarded Control Stack store register (unprivileged)

This instruction stores a doubleword from a register to memory. The address that is used for the store is calculated from a base register.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1 and the Effective value of HCR\_EL2.{NV1, NV} is not {1, 1}.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

## Integer

(FEAT\_GCS)

<!-- image -->

## Encoding

```
GCSSTTR
```

```
<Xt>, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_GCS) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant bits(2) effective_el = if AArch64.IsUnprivAccessPriv() then PSTATE.EL else EL0; if effective_el == PSTATE.EL then CheckGCSSTREnabled(); constant boolean privileged = effective_el != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_STORE, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64];
```

Mem[address, 8, accdesc] = X[t, 64];
