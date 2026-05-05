## C6.2.226 LDRSH (register)

Load register signed halfword (register)

This instruction calculates an address from a base register value and an offset register value, loads a halfword from memory, sign-extends it, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 11) LDRSH <Wt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDRSH <Xt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

## Decode for all variants of this encoding

```
if option<1> == '0' then EndOfDecode(Decode_UNDEF); // sub-word index constant ExtendType extend_type = DecodeRegExtend(option); constant integer shift = if S == '1' then 1 else 0;
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

```
{<amount>}}]
```

```
{<amount>}}]
```

## &lt;amount&gt;

Is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #1         |

<!-- image -->

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} regsize = 64 >> UInt(opc<0>); constant boolean nontemporal = FALSE; constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(16) data = Mem[address, 2, accdesc]; X[t, regsize] = SignExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   option | <extend>   |
|----------|------------|
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |
