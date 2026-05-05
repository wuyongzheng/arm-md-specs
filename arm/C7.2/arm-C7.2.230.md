## C7.2.230 LDR (immediate, SIMD&amp;FP)

Load SIMD&amp;FP register (immediate offset)

This instruction loads an element from memory, and writes the result as a scalar to the SIMD&amp;FP register. The address that is used for the load is calculated from a base register value, a signed immediate offset, and an optional offset that is a multiple of the element size.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 3 classes: Post-index, Pre-index, and Unsigned offset

## Post-index

(FEAT\_FP)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when (size == 00 && opc == 01) LDR <Bt>, [<Xn|SP>], #<simm>
```

## Encoding for the 16-bit variant

Applies when

```
LDR
```

```
(size == 01 && opc == 01) <Ht>, [<Xn|SP>], #<simm>
```

## Encoding for the 32-bit variant

Applies when (size == 10 &amp;&amp; opc == 01)

```
LDR <St>, [<Xn|SP>], #<simm>
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc == 01) LDR <Dt>, [<Xn|SP>], #<simm>
```

## Encoding for the 128-bit variant

Applies when (size == 00 &amp;&amp; opc == 11)

```
LDR <Qt>, [<Xn|SP>], #<simm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); UInt(size);
```

```
if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else constant boolean wback = TRUE; constant boolean postindex = TRUE; constant bits(64) offset = SignExtend(imm9, 64);
```

## Pre-index

(FEAT\_FP)

<!-- image -->

## Encoding for the 8-bit variant

Applies when

```
LDR
```

```
(size == 00 && opc == 01) <Bt>, [<Xn|SP>, #<simm>]!
```

## Encoding for the 16-bit variant

```
Applies when
```

```
LDR
```

```
(size == 01 && opc == 01) <Ht>, [<Xn|SP>, #<simm>]!
```

## Encoding for the 32-bit variant

```
Applies when
```

```
LDR
```

```
(size == 10 && opc == 01) <St>, [<Xn|SP>, #<simm>]!
```

## Encoding for the 64-bit variant

Applies when (size == 11 &amp;&amp; opc == 01)

```
LDR
```

```
<Dt>, [<Xn|SP>, #<simm>]!
```

## Encoding for the 128-bit variant

Applies when (size == 00 &amp;&amp; opc == 11)

```
LDR
```

```
<Qt>, [<Xn|SP>, #<simm>]!
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); UInt(size);
```

```
if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else constant boolean wback = TRUE; constant boolean postindex = FALSE; constant bits(64) offset = SignExtend(imm9, 64);
```

## Unsigned offset

(FEAT\_FP)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when
```

```
LDR
```

```
(size == 00 && opc == 01) <Bt>, [<Xn|SP>{, #<pimm>}]
```

## Encoding for the 16-bit variant

```
Applies when
```

```
LDR
```

```
(size == 01 && opc == 01) <Ht>, [<Xn|SP>{, #<pimm>}]
```

## Encoding for the 32-bit variant

```
Applies when
```

```
LDR
```

```
(size == 10 && opc == 01) <St>, [<Xn|SP>{, #<pimm>}]
```

## Encoding for the 64-bit variant

Applies when (size == 11 &amp;&amp; opc == 01)

```
LDR
```

```
<Dt>, [<Xn|SP>{, #<pimm>}]
```

## Encoding for the 128-bit variant

Applies when (size == 00 &amp;&amp; opc == 11)

```
LDR
```

```
<Qt>, [<Xn|SP>{, #<pimm>}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); UInt(size);
```

```
if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else constant boolean wback = FALSE; constant boolean postindex = FALSE; constant bits(64) offset = LSL(ZeroExtend(imm12, 64), scale);
```

## Assembler Symbols

## &lt;Bt&gt;

Is the 8-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the signed immediate byte offset, in the range -256 to 255, encoded in the 'imm9' field.

## &lt;Ht&gt;

&lt;St&gt;

## &lt;Dt&gt;

## &lt;Qt&gt;

Is the 128-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;pimm&gt;

For the '8-bit' variant: is the optional positive immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

For the '16-bit' variant: is the optional positive immediate byte offset, a multiple of 2 in the range 0 to 8190, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/2.

For the '32-bit' variant: is the optional positive immediate byte offset, a multiple of 4 in the range 0 to 16380, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/4.

For the '64-bit' variant: is the optional positive immediate byte offset, a multiple of 8 in the range 0 to 32760, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/8.

For the '128-bit' variant: is the optional positive immediate byte offset, a multiple of 16 in the range 0 to 65520, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/16.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 8 << scale; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64];
```

Is the 16-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 32-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 64-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

```
else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); V[t, datasize] = Mem[address, datasize DIV 8, accdesc]; if wback then if postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
