## C6.2.183 LDAPRB

Load-acquire RCpc register byte

This instruction derives an address from a base register value, loads a byte from the derived address in memory, zero-extends it and writes it to a register.

If the destination register is not one of WZR or XZR , LDAPRB loads from memory with AcquirePC semantics.

For more information about memory ordering semantics, see Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LRCPC)

<!-- image -->

## Encoding

```
LDAPRB <Wt>, [<Xn|SP> {, #0}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquirepc = t != 31; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; bits(8) data; constant AccessDescriptor accdesc = CreateAccDescLDAcqPC(tagchecked, acquirepc, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; data = Mem[address, 1, accdesc]; X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
