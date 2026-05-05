## C6.2.169 GCSSTR

Guarded Control Stack store register

This instruction stores a doubleword from a register to memory. The address that is used for the store is calculated from a base register.

## Integer

(FEAT\_GCS)

<!-- image -->

## Encoding

```
GCSSTR <Xt>, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_GCS) then EndOfDecode(Decode_UNDEF);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant bits(2) effective_el = PSTATE.EL; if effective_el == PSTATE.EL then CheckGCSSTREnabled(); constant boolean privileged = effective_el != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_STORE, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; Mem[address, 8, accdesc] = X[t, 64];
```
