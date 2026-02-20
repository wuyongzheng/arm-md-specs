## F6.1.245 VSTR

Store SIMD&amp;FP register stores a single register from the Advanced SIMD and floating-point register file to memory, using an address from a general-purpose register, with an optional offset.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when
```

```
(size == 01) VSTR{<c>}{<q>}.16 <Sd>, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VSTR{<c>}{<q>}{.32} <Sd>, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VSTR{<c>}{<q>}{.64}
```

```
<Dd>, [<Rn>{, #{+/-}<imm>}]
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean add = (U == '1'); constant integer esize = 8 << UInt(size); constant integer imm32 = UInt(imm8) << (if size == '01' then 1 else 2); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = UInt(Rn); if n == 15 && CurrentInstrSet() != InstrSet_A32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when

```
(size == 01)
```

```
VSTR{<c>}{<q>}.16
```

```
<Sd>, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Single-precision scalar variant

Applies when (size ==

```
VSTR{<c>}{<q>}{.32}
```

```
10)
```

```
<Sd>, [<Rn>{, #{+/-}<imm>}]
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
VSTR{<c>}{<q>}{.64}
```

```
11) <Dd>, [<Rn>{, #{+/-}<imm>}]
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean add = (U == '1'); constant integer esize = 8 << UInt(size); constant integer imm32 = UInt(imm8) << (if size == '01' then 1 else 2); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer n = UInt(Rn); if n == 15 && CurrentInstrSet() != InstrSet_A32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vd:D' field.

<!-- image -->

<!-- image -->

&lt;Sd&gt;

## &lt;Rn&gt;

+/-

Is the general-purpose base register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |

## &lt;imm&gt;

For the 'A1 Half-precision scalar' and 'T1 Half-precision scalar' variants: is the optional unsigned immediate byte offset, a multiple of 2, in the range 0 to 510, defaulting to 0, and encoded in the 'imm8' field as &lt;imm&gt;/2.

For the 'A1 Double-precision scalar', 'A1 Single-precision scalar', 'T1 Double-precision scalar', and 'T1 Single-precision scalar' variants: is the optional unsigned immediate byte offset, a multiple of 4, in the range 0 to 1020, defaulting to 0, and encoded in the 'imm8' field as &lt;imm&gt;/4.

Is an optional data size specifier for 32-bit memory accesses that can be used in the assembler source code, but is otherwise ignored.

Is an optional data size specifier for 64-bit memory accesses that can be used in the assembler source code, but is otherwise ignored.

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'D:Vd' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant bits(32) address = if add then (R[n] + imm32) else (R[n] imm32); case esize of when 16 MemA[address,2] = H[d]; when 32 MemA[address,4] = S[d]; when 64 // Store as two word-aligned words in the correct order for current endianness. if BigEndian(AccessType_ASIMD) then MemA[address,4] = D[d]<63:32>; MemA[address+4,4] = D[d]<31:0>; else MemA[address,4] = D[d]<31:0>; MemA[address+4,4] = D[d]<63:32>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

## .32

.64

## &lt;Dd&gt;