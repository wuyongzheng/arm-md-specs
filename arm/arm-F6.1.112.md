## F6.1.112 VLDM, VLDMDB, VLDMIA

Load Multiple SIMD&amp;FP registers loads multiple registers from consecutive locations in the Advanced SIMD and floating-point register file using an address from a general-purpose register.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information, see Enabling Advanced SIMD and floating-point support.

This instruction is used by the alias VPOP.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0 && W == VLDMDB{<c>}{<q>}{.<size>} <Rn>!, <dreglist>
```

## Encoding for the Increment After variant

```
Applies when (P == 0 && U == 1) VLDM{<c>}{<q>}{.<size>} <Rn>{!}, <dreglist> // (Preferred syntax) VLDMIA{<c>}{<q>}{.<size>} <Rn>{!}, <dreglist>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then SEE "Related encodings"; if P == '1' && W == '0' then SEE "VLDR"; if P == U && W == '1' then UNDEFINED; // Remaining combinations are PUW = 010 (IA without !), 011 (IA with !), 101 (DB with !) constant boolean single_regs = FALSE; constant boolean add = (U == '1'); constant boolean wback = (W == '1'); constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant integer regs = UInt(imm8) DIV 2; // If UInt(imm8) is odd, see "FLDM*X". if n == 15 && (wback || CurrentInstrSet() != InstrSet_A32) then UNPREDICTABLE; if regs == 0 || regs > 16 || (d+regs) > 32 then UNPREDICTABLE; if imm8<0> == '1' && (d+regs) > 16 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If regs == 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as a VLDM with the same addressing mode but loads no registers.

If regs &gt; 16 || (d+regs) &gt; 32 , then one of the following behaviors must occur:

```
1)
```

A2

<!-- image -->

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0 && W == 1) VLDMDB{<c>}{<q>}{.<size>} <Rn>!, <sreglist>
```

## Encoding for the Increment After variant

```
Applies when
```

```
(P == 0 && U == 1) VLDM{<c>}{<q>}{.<size>} <Rn>{!}, <sreglist> // (Preferred syntax) VLDMIA{<c>}{<q>}{.<size>} <Rn>{!}, <sreglist>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then SEE "Related encodings"; if P == '1' && W == '0' then SEE "VLDR"; if P == U && W == '1' then UNDEFINED; // Remaining combinations are PUW = 010 (IA without !), 011 (IA with !), 101 (DB with !) constant boolean single_regs = TRUE; constant boolean add = (U == '1'); constant boolean wback = (W == '1'); constant integer d = UInt(Vd:D); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant integer regs = UInt(imm8); if n == 15 && (wback || CurrentInstrSet() != InstrSet_A32) then UNPREDICTABLE; if regs == 0 || (d+regs) > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If regs == 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as a VLDM with the same addressing mode but loads no registers.

If (d+regs) &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.
- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

T1

<!-- image -->

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0 && W == VLDMDB{<c>}{<q>}{.<size>} <Rn>!, <dreglist>
```

## Encoding for the Increment After variant

```
Applies when (P == 0 && U == 1) VLDM{<c>}{<q>}{.<size>} <Rn>{!}, <dreglist> // (Preferred syntax) VLDMIA{<c>}{<q>}{.<size>} <Rn>{!}, <dreglist>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then SEE "Related encodings"; if P == '1' && W == '0' then SEE "VLDR"; if P == U && W == '1' then UNDEFINED; // Remaining combinations are PUW = 010 (IA without !), 011 (IA with !), 101 (DB with !) constant boolean single_regs = FALSE; constant boolean add = (U == '1'); constant boolean wback = (W == '1'); constant integer d = UInt(D:Vd); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant integer regs = UInt(imm8) DIV 2; // If UInt(imm8) is odd, see "FLDM*X". if n == 15 && (wback || CurrentInstrSet() != InstrSet_A32) then UNPREDICTABLE; if regs == 0 || regs > 16 || (d+regs) > 32 then UNPREDICTABLE; if imm8<0> == '1' && (d+regs) > 16 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If regs == 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as a VLDM with the same addressing mode but loads no registers.

If regs &gt; 16 || (d+regs) &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

```
1)
```

T2

<!-- image -->

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0 && W == 1) VLDMDB{<c>}{<q>}{.<size>} <Rn>!, <sreglist>
```

## Encoding for the Increment After variant

```
Applies when (P == 0 && U == 1) VLDM{<c>}{<q>}{.<size>} <Rn>{!}, <sreglist> // (Preferred syntax) VLDMIA{<c>}{<q>}{.<size>} <Rn>{!}, <sreglist>
```

## Decode for all variants of this encoding

```
if P == '0' && U == '0' && W == '0' then SEE "Related encodings"; if P == '1' && W == '0' then SEE "VLDR"; if P == U && W == '1' then UNDEFINED; // Remaining combinations are PUW = 010 (IA without !), 011 (IA with !), 101 (DB with !) constant boolean single_regs = TRUE; constant boolean add = (U == '1'); constant boolean wback = (W == '1'); constant integer d = UInt(Vd:D); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); constant integer regs = UInt(imm8); if n == 15 && (wback || CurrentInstrSet() != InstrSet_A32) then UNPREDICTABLE; if regs == 0 || (d+regs) > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If regs == 0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as a VLDM with the same addressing mode but loads no registers.

If (d+regs) &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. If the instruction specifies writeback, the base register becomes UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VLDM.

Related encodings: See Advanced SIMD and floating-point 64-bit move for the T32 instruction set, or Advanced SIMD and floating-point 64-bit move for the A32 instruction set.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;size&gt;

An optional data size specifier. If present, it must be equal to the size in bits, 32 or 64, of the registers being transferred.

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field. If writeback is not specified, the PC can be used.

## &lt;dreglist&gt;

Is the list of consecutively numbered 64-bit SIMD&amp;FP registers to be transferred. The first register in the list is encoded in 'D:Vd', and 'imm8' is set to twice the number of registers in the list. The list must contain at least one register, and must not contain more than 16 registers.

!

Specifies base register writeback, encoded in 'W':

## &lt;sreglist&gt;

Is the list of consecutively numbered 32-bit SIMD&amp;FP registers to be transferred. The first register in the list is encoded in 'Vd:D', and 'imm8' is set to the number of registers in the list. The list must contain at least one register.

## Alias Conditions

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); bits(32) address = if add then R[n] else R[n]-imm32; for r = 0 to regs-1 if single_regs then S[d+r] = MemA[address,4]; address = address+4; else
```

|   W | !         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

| Alias   | Is preferred when                          |
|---------|--------------------------------------------|
| VPOP    | P == '0' && U == '1' && W == '1' == '1101' |

```
constant bits(32) word1 = MemA[address,4]; constant bits(32) word2 = MemA[address+4,4]; address = address+8; // Combine the word-aligned words in the correct order for current endianness. D[d+r] = if BigEndian(AccessType_ASIMD) then word1:word2 else word2:word1; if wback then R[n] = if add then R[n]+imm32 else R[n]-imm32;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.