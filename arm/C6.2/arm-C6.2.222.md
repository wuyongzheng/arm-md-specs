## C6.2.222 LDRH (register)

Load register halfword (register)

This instruction calculates an address from a base register value and an offset register value, loads a halfword from memory, zero-extends it, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

```
LDRH <Wt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> {<amount>}}]
```

## Decode for this encoding

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); // sub-word constant ExtendType extend_type = DecodeRegExtend(option); constant integer shift = if S == '1' then 1 else 0;
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

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |

```
index
```

## &lt;amount&gt;

Is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #1         |

## Shared Decode

```
= FALSE;
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean nontemporal constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(16) data = Mem[address, 2, accdesc]; X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
