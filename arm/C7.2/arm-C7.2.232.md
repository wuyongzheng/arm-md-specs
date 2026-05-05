## C7.2.232 LDR (register, SIMD&amp;FP)

Load SIMD&amp;FP register (register offset)

This instruction loads a SIMD&amp;FP register from memory. The address that is used for the load is calculated from a base register value and an offset register value. The offset can be optionally shifted and extended.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## SIMD&amp;FP registers

(FEAT\_FP)

<!-- image -->

## Encoding for the 8-bit with extended register offset variant

Applies when (size == 00 &amp;&amp; opc == 01 &amp;&amp; option != 011)

```
LDR <Bt>, [<Xn|SP>, (<Wm>|<Xm>), <extend>
```

```
{<amount>}]
```

## Encoding for the 8-bit with shifted register offset variant

Applies when (size == 00 &amp;&amp; opc == 01 &amp;&amp; option ==

```
LDR <Bt>, [<Xn|SP>, <Xm>{, LSL
```

## Encoding for the 16-bit variant

```
Applies when (size == 01 && opc == 01) LDR <Ht>, [<Xn|SP>, (<Wm>|<Xm>){, <extend> {<amount>}}]
```

## Encoding for the 32-bit variant

Applies when

```
(size == 10 && opc == 01) LDR <St>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc == 01) LDR <Dt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

## Encoding for the 128-bit variant

```
Applies when (size == 00 && opc == 11)
```

```
LDR <Qt>, [<Xn|SP>, (<Wm>|<Xm>){, <extend>
```

```
011) <amount>}]
```

```
{<amount>}}]
```

```
{<amount>}}]
```

```
{<amount>}}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if option<1> == '0' then EndOfDecode(Decode_UNDEF); // sub-word index if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else UInt(size); constant ExtendType extend_type = DecodeRegExtend(option); constant integer shift = if S == '1' then scale else 0;
```

## Assembler Symbols

## &lt;Bt&gt;

Is the 8-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Wm&gt;

When option&lt;0&gt; is set to 0, is the 32-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;Xm&gt;

When option&lt;0&gt; is set to 1, is the 64-bit name of the general-purpose index register, encoded in the 'Rm' field.

## &lt;extend&gt;

For the '8-bit with extended register offset' variant: is the index extend specifier, encoded in 'option':

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      110 | SXTW       |
|      111 | SXTX       |

For the '128-bit', '16-bit', '32-bit', and '64-bit' variants: is the index extend/shift specifier, defaulting to LSL, and which must be omitted for the LSL option when &lt;amount&gt; is omitted, encoded in 'option':

|   option | <extend>   |
|----------|------------|
|      010 | UXTW       |
|      011 | LSL        |
|      110 | SXTW       |
|      111 | SXTX       |

## &lt;amount&gt;

For the '8-bit with extended register offset' and '8-bit with shifted register offset' variants: is the index shift amount, it must be #0 , encoded in 'S' as 0 if omitted, or as 1 if present.

For the '16-bit' variant: is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

## &lt;Ht&gt;

&lt;St&gt;

&lt;Dt&gt;

&lt;Qt&gt;

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #1         |

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

For the '128-bit' variant: is the index shift amount, optional only when &lt;extend&gt; is not LSL. Where it is permitted to be optional, it defaults to #0. It is encoded in 'S':

|   S | <amount>   |
|-----|------------|
|   0 | #0         |
|   1 | #4         |

Is the 16-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 32-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 64-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 128-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer{} datasize = 8 << scale; constant boolean nontemporal = FALSE; constant boolean tagchecked = TRUE;
```

## Operation

```
AArch64.CheckFPEnabled(); constant bits(64) offset = ExtendReg(m, extend_type, shift, 64); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); V[t, datasize] = Mem[address, datasize DIV 8, accdesc];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
