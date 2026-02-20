## F5.1.182 SEL

Select Bytes selects each byte of its result from either its first operand or its second operand, according to the values of the PSTATE.GE flags.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
SEL{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
SEL{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); R[d]<7:0> = if PSTATE.GE<0> == '1' then R[n]<7:0> else R[m]<7:0>; R[d]<15:8> = if PSTATE.GE<1> == '1' then R[n]<15:8> else R[m]<15:8>; R[d]<23:16> = if PSTATE.GE<2> == '1' then R[n]<23:16> else R[m]<23:16>; R[d]<31:24> = if PSTATE.GE<3> == '1' then R[n]<31:24> else R[m]<31:24>;
```