## C6.2.229 LDRSW (register)

Load register signed word (register)

This instruction calculates an address from a base register value and an offset register value, loads a word from memory, sign-extends it to form a 64-bit value, and writes it to a register. The offset register value can be shifted left by 0 or 2 bits. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
LDRSW <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> {<amount>}}]
```

## Decode for this encoding

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); constant ExtendType extend_type constant integer shift = if S == '1' then 2 else 0;
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Wm&gt;

When option&lt;0&gt; is set to 0, is the 32-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;Xm&gt;

When option&lt;0&gt; is set to 1, is the 64-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;extend&gt;

Is the index extend/shift specifier, defaulting to LSL, and which must be omitted for the LSL option when &lt;amount&gt; is omitted, encoded in 'option':

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |

```
// sub-word index = DecodeRegExtend(option);
```

## &lt;amount&gt;

Is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #2         |

## Shared Decode

```
= FALSE;
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean nontemporal constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(32) data = Mem[address, 4, accdesc]; X[t, 64] = SignExtend(data, 64);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
