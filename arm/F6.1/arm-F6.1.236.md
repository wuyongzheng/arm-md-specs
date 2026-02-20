## F6.1.236 VST1 (single element from one lane)

Store single element from one lane of one register stores one element to memory from one element of a register. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, and A3) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
1111)
```

```
VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
m != 13);
```

```
if size == '11' then UNDEFINED; if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer alignment = 1; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && if n == 15 then UNPREDICTABLE;
```

A2

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
1111)
```

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
11x1) <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if index_align<1> != '0' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer alignment = if index_align<0> == '0' then 1 else constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

A3

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
(Rm != 11x1) <Rm>
```

```
2;
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if index_align<2> != '0' then UNDEFINED; if index_align<1:0> != '00' && index_align<1:0> != '11' then constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer alignment = if index_align<1:0> == '00' then 1 else constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

Applies when (Rm ==

```
VST1{<c>}{<q>}.<size>
```

```
1101) <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
m != 13);
```

```
if size == '11' then UNDEFINED; if index_align<0> != '0' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer alignment = 1; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && if n == 15 then UNPREDICTABLE;
```

```
UNDEFINED; 4;
```

T2

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm ==

```
VST1{<c>}{<q>}.<size>
```

```
1111) <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if index_align<1> != '0' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer alignment = if index_align<0> == '0' then 1 else constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

T3

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

```
2;
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1)
```

```
VST1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
UNDEFINED; 4;
```

```
if size == '11' then UNDEFINED; if index_align<2> != '0' then UNDEFINED; if index_align<1:0> != '00' && index_align<1:0> != '11' then constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer alignment = if index_align<1:0> == '00' then 1 else constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

For the 'A1 Offset', 'A1 Post-indexed', 'A2 Offset', 'A2 Post-indexed', 'A3 Offset', and 'A3 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset', 'T1 Post-indexed', 'T2 Offset', 'T2 Post-indexed', 'T3 Offset', and 'T3 Post-indexed'

```
<c> variants: see Standard assembler syntax fields. <q> See Standard assembler syntax fields. <size>
```

Is the data size, encoded in 'size':

## &lt;list&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the single 64-bit name of the SIMD&amp;FP register holding the element.

The list must be { &lt;Dd&gt;[&lt;index&gt;] } .

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

The permitted values and encoding of &lt;index&gt; depend on &lt;size&gt; :

```
<size> == 8 <index> is in the range 0 to 7, encoded in the 'index_align<3:1>' field. <size> == 16 <index> is in the range 0 to 3, encoded in the 'index_align<3:2>' field. <size> == 32 <index> is 0 or 1, encoded in the 'index_align<3>' field.
```

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;align&gt;

When &lt;size&gt; == 8, &lt;align&gt; must be omitted, otherwise it is the optional alignment.

Whenever &lt;align&gt; is omitted, the standard alignment is used, see Unaligned data access, and the encoding depends on &lt;size&gt; :

```
<size> == 8 Encoded in the 'index_align<0>' field as 0. <size> == 16 Encoded in the 'index_align<1:0>' field as 0b00 . <size> == 32 Encoded in the 'index_align<2:0>' field as 0b000 .
```

Whenever &lt;align&gt; is present, the permitted values and encoding depend on &lt;size&gt; :

```
<size> == 16 <align> is 16, meaning 16-bit alignment, encoded in the 'index_align<1:0>' field as 0b01 . <size> == 32 <align> is 32, meaning 32-bit alignment, encoded in the 'index_align<2:0>' field as 0b011 .
```

- : is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field. For more information about the variants of this instruction, see Advanced SIMD addressing mode.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); MemU[address,ebytes] = Elem[D[d],index,8*ebytes]; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + ebytes;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.