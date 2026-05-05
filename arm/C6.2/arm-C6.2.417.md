## C6.2.417 STRB (register)

Store register byte (register)

This instruction calculates an address from a base register value and an offset register value, and stores a byte from a 32-bit register to the calculated address. For information about addressing modes, see Load/Store addressing modes.

The instruction uses an offset addressing mode, that calculates the address used for the memory access from a base register value and an offset register value. The offset can be optionally shifted and extended.

<!-- image -->

## Encoding for the Extended register variant

Applies when (option !=

```
011) STRB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend>
```

## Encoding for the Shifted register variant

```
Applies when (option == 011) STRB <Wt>, [<Xn|SP>, <Xm>{, LSL
```

```
<amount>}]
```

## Decode for all variants of this encoding

```
// sub-word index = DecodeRegExtend(option);
```

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); constant ExtendType extend_type constant integer shift = 0;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Wm&gt;

When option&lt;0&gt; is set to 0, is the 32-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;Xm&gt;

When option&lt;0&gt; is set to 1, is the 64-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;extend&gt;

Is the index extend specifier, encoded in 'option':

```
{<amount>}]
```

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |

## &lt;amount&gt;

Is the index shift amount, it must be #0 , encoded in 'S' as 0 if omitted, or as 1 if present.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean nontemporal constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Mem[address, 1, accdesc] = X[t, 8];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
= FALSE;
```

|   option | <extend>   |
|----------|------------|
|      110 | SXTW       |
|      111 | SXTX       |
