## F5.1.126 MVN, MVNS (register-shifted register)

Bitwise NOT (register-shifted register) writes the bitwise inverse of a register-shifted register value to the destination register. It can optionally update the condition flags based on the result.

<!-- image -->

## Encoding for the Flag setting variant

Applies when

```
MVNS{<c>}{<q>} <Rd>, <Rm>, <shift>
```

```
(S == 1) <Rs>
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0)
```

```
MVN{<c>}{<q>} <Rd>, <Rm>, <shift> <Rs>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant boolean setflags = (S == '1'); constant SRType shift_t = DecodeRegShift(stype); if d == 15 || m == 15 || s == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

Is the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

## &lt;Rs&gt;

Is the general-purpose source register holding a shift amount in its bottom 8 bits, encoded in the 'Rs' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) result = NOT(shifted); R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |