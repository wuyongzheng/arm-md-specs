## C6.2.415 STR (register)

Store register (register)

This instruction calculates an address from a base register value and an offset register value, and stores a 32-bit word or a 64-bit doubleword to the calculated address, from a register. For information about addressing modes, see Load/Store addressing modes.

The instruction uses an offset addressing mode, that calculates the address used for the memory access from a base register value and an offset register value. The offset can be optionally shifted and extended.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (size ==

```
STR <Wt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

```
10) {<amount>}}]
```

## Encoding for the 64-bit variant

Applies when (size ==

```
STR <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

```
11) {<amount>}}]
```

## Decode for all variants of this encoding

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); // sub-word index constant ExtendType extend_type = DecodeRegExtend(option); constant integer scale = UInt(size); constant integer shift = if S == '1' then scale else 0;
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

Is the index extend/shift specifier, defaulting to LSL, and which must be omitted for the LSL option when &lt;amount&gt; is omitted, encoded in 'option':

## &lt;amount&gt;

For the '32-bit' variant: is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #2         |

For the '64-bit' variant: is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #3         |

<!-- image -->

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} datasize = 8 << scale; constant boolean nontemporal = FALSE; constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc);
```

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |

Mem[address, datasize DIV 8, accdesc] = X[t, datasize];

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
