## F6.1.238 VST2 (single 2-element structure from one lane)

Store single 2-element structure from one lane of two registers stores one 2-element structure to memory from corresponding elements of two registers. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1, A2, and A3) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the Offset variant

Applies when

```
<list>, [<Rn>{:<align>}]
```

```
(Rm == 1111) VST2{<c>}{<q>}.<size>
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer inc = 1; constant integer alignment = if index_align<0> == '0' then 1 else constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
2;
```

## A2

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm == 1111)

```
VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1)
```

```
VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer inc = if index_align<1> == '0' then 1 else 2; constant integer alignment = if index_align<0> == '0' then 1 else 4; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

## A3

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm == 1111)

```
VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if index_align<1> != '0' then UNDEFINED; constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer inc = if index_align<2> == '0' then 1 else 2; constant integer alignment = if index_align<0> == '0' then 1 else constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

```
<Rm>
```

```
8;
```

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1)
```

```
VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer ebytes = 1; constant integer index = UInt(index_align<3:1>); constant integer inc = 1; constant integer alignment = if index_align<0> == '0' then 1 else 2; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

T2

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when (Rm !=

```
11x1)
```

```
VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; constant integer ebytes = 2; constant integer index = UInt(index_align<3:2>); constant integer inc = if index_align<1> == '0' then 1 else 2; constant integer alignment = if index_align<0> == '0' then 1 else 4; constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

T3

<!-- image -->

## Encoding for the Offset variant

Applies when (Rm == 1111)

```
VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VST2{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

Applies when

```
(Rm != 11x1) VST2{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if index_align<1> != '0' then UNDEFINED; constant integer ebytes = 4; constant integer index = UInt(index_align<3>); constant integer inc = if index_align<2> == '0' then 1 else 2; constant integer alignment = if index_align<0> == '0' then 1 else constant integer d = UInt(D:Vd); constant integer d2 = d + inc; constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d2 > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d2 &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The memory locations specified by the instruction and the number of registers specified by the instruction become UNKNOWN. If the instruction specifies writeback, then that register becomes UNKNOWN. This behavior does not affect any other memory locations.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VST2 (single 2-element structure from one lane).

```
<Rm>
```

```
8;
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 Offset', 'A1 Post-indexed', 'A2 Offset', 'A2 Post-indexed', 'A3 Offset', and 'A3 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset', 'T1 Post-indexed', 'T2 Offset', 'T2 Post-indexed', 'T3 Offset', and 'T3 Post-indexed' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size, encoded in 'size':

## &lt;list&gt;

&lt;q&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of the two SIMD&amp;FP registers holding the element.

## &lt;Rn&gt;

## &lt;align&gt;

The list must be one of: { &lt;Dd&gt;[&lt;index&gt;], &lt;Dd+1&gt;[&lt;index&gt;] } Single-spaced registers, encoded as 'spacing' = 0. { &lt;Dd&gt;[&lt;index&gt;], &lt;Dd+2&gt;[&lt;index&gt;] } Double-spaced registers, encoded as 'spacing' = 1. Not permitted when &lt;size&gt; == 8. The encoding of 'spacing' depends on &lt;size&gt; : &lt;size&gt; == 16 'spacing' is encoded in the 'index\_align&lt;1&gt;' field. &lt;size&gt; == 32 'spacing' is encoded in the 'index\_align&lt;2&gt;' field. The register &lt;Dd&gt; is encoded in the 'D:Vd' field. The permitted values and encoding of &lt;index&gt; depend on &lt;size&gt; : &lt;size&gt; == 8 &lt;index&gt; is in the range 0 to 7, encoded in the 'index\_align&lt;3:1&gt;' field. &lt;size&gt; == 16 &lt;index&gt; is in the range 0 to 3, encoded in the 'index\_align&lt;3:2&gt;' field. &lt;size&gt; == 32 &lt;index&gt; is 0 or 1, encoded in the 'index\_align&lt;3&gt;' field. Is the general-purpose base register, encoded in the 'Rn' field. Is the optional alignment. Whenever &lt;align&gt; is omitted, the standard alignment is used, see Unaligned data access, and the encoding depends on &lt;size&gt; : &lt;size&gt; == 8 Encoded in the 'index\_align&lt;0&gt;' field as 0. &lt;size&gt; == 16 Encoded in the 'index\_align&lt;0&gt;' field as 0. &lt;size&gt; == 32 Encoded in the 'index\_align&lt;1:0&gt;' field as 0b00 . Whenever &lt;align&gt; is present, the permitted values and encoding depend on &lt;size&gt; :

```
<size> == 8 <align> is 16, meaning 16-bit alignment, encoded in the 'index_align<0>' field as 1. <size> == 16 <align> is 32, meaning 32-bit alignment, encoded in the 'index_align<0>' field as 1. <size> == 32 <align> is 64, meaning 64-bit alignment, encoded in the 'index_align<1:0>' field as 0b01 .
```

: is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); MemU[address, ebytes] = Elem[D[d], index,8*ebytes]; MemU[address+ebytes,ebytes] = Elem[D[d2],index,8*ebytes]; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + 2*ebytes;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.