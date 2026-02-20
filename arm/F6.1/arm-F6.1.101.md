## F6.1.101 VLD1 (single element to all lanes)

Load single 1-element structure and replicate to all lanes of one register

Load single 1-element structure and replicate to all lanes of one register loads one element from memory into every element of one or two vectors. For details of the addressing mode, see Advanced SIMD addressing mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]!
```

## Encoding for the Post-indexed variant

```
Applies when (Rm != 11x1) VLD1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}],
```

```
<Rm>
```

## Decode for all variants of this encoding

```
if size == '11' || (size == '00' && a == '1') then UNDEFINED; constant integer ebytes = 1 << UInt(size); constant integer regs = if T == '0' then 1 else 2; constant integer alignment = if a == '0' then 1 else ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

T1

<!-- image -->

## Encoding for the Offset variant

```
Applies when (Rm == 1111) VLD1{<c>}{<q>}.<size>
```

```
<list>, [<Rn>{:<align>}]
```

## Encoding for the Post-indexed variant

```
Applies when (Rm == 1101) VLD1{<c>}{<q>}.<size>
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
VLD1{<c>}{<q>}.<size> <list>, [<Rn>{:<align>}], <Rm>
```

## Decode for all variants of this encoding

```
if size == '11' || (size == '00' && a == '1') then UNDEFINED; constant integer ebytes = 1 << UInt(size); constant integer regs = if T == '0' then 1 else 2; constant integer alignment = if a == '0' then 1 else ebytes; constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = (m != 15); constant boolean register_index = (m != 15 && m != 13); if n == 15 || d+regs > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If d+regs &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VLD1 (single element to all lanes).

## Assembler Symbols

&lt;c&gt;

For the 'A1 Offset' and 'A1 Post-indexed' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Offset' and 'T1 Post-indexed' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size, encoded in 'size':

## &lt;list&gt;

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;align&gt;

When &lt;size&gt; == 8, &lt;align&gt; must be omitted, otherwise it is the optional alignment.

Whenever &lt;align&gt; is omitted, the standard alignment is used, see Unaligned data access, and is encoded in the 'a' field as 0.

Whenever &lt;align&gt; is present, the permitted values and encoding depend on &lt;size&gt; :

```
<size> == 16 <align> is 16, meaning 16-bit alignment, encoded in the 'a' field as 1. <size> == 32 <align> is 32, meaning 32-bit alignment, encoded in the 'a' field as 1.
```

: is the preferred separator before the &lt;align&gt; value, but the alignment can be specified as @&lt;align&gt; , see Advanced SIMD addressing mode.

## &lt;Rm&gt;

Is the general-purpose index register containing an offset applied after the access, encoded in the 'Rm' field.

For more information about the variants of this instruction, see Advanced SIMD addressing mode.

## Operation

&lt;q&gt;

|   size |   <size> |
|--------|----------|
|     00 |        8 |
|     01 |       16 |
|     10 |       32 |

Is a list containing the 64-bit names of the SIMD&amp;FP registers.

The list must be one of:

```
{ <Dd>[] } Encoded in the 'T' field as 0. { <Dd>[], <Dd+1>[] } Encoded in the 'T' field as 1.
```

The register &lt;Dd&gt; is encoded in the 'D:Vd' field.

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(32) address = R[n]; constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if !IsAligned(address, alignment) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); constant integer esize = 8 * ebytes; constant bits(esize) element = MemU[address,ebytes]; constant bits(64) replicated_element = Replicate(element, 64 DIV esize); for r = 0 to regs-1 D[d+r] = replicated_element; if wback then if register_index then R[n] = R[n] + R[m]; else R[n] = R[n] + ebytes;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.