## C6.2.224 LDRSB (register)

Load register signed byte (register)

This instruction calculates an address from a base register value and an offset register value, loads a byte from memory, sign-extends it, and writes it to a register. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding for the 32-bit with extended register offset variant

Applies when (opc == 11 &amp;&amp; option !=

```
LDRSB <Wt>, [<Xn|SP>, (<Wm>|<Xm>), <extend>
```

```
011) {<amount>}]
```

## Encoding for the 32-bit with shifted register offset variant

011)

```
Applies when (opc == 11 && option == LDRSB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]
```

## Encoding for the 64-bit with extended register offset variant

```
Applies when (opc == 10 && option != 011) LDRSB <Xt>, [<Xn|SP>, (<Wm>|<Xm>), <extend>
```

```
{<amount>}]
```

## Encoding for the 64-bit with shifted register offset variant

```
Applies when (opc == 10 && option == 011) LDRSB <Xt>, [<Xn|SP>, <Xm>{, LSL <amount>}]
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

## &lt;amount&gt;

Is the index shift amount, it must be #0 , encoded in 'S' as 0 if omitted, or as 1 if present.

<!-- image -->

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} regsize = 64 >> UInt(opc<0>); constant boolean nontemporal = FALSE; constant boolean tagchecked = TRUE;
```

## Operation

```
constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(8) data = Mem[address, 1, accdesc]; X[t, regsize] = SignExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      110 | SXTW       |
|      111 | SXTX       |
