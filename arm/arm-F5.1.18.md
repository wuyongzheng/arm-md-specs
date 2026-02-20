## F5.1.18 B

Branch causes a branch to a target address.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, T3, and T4).

A1

<!-- image -->

## Encoding

```
B{<c>}{<q>} <label>
```

## Decode for this encoding

```
constant bits(32) imm32 = SignExtend(imm24:'00', 32);
```

T1

## Encoding

```
B<c>{<q>} <label> // (Not permitted in IT block)
```

## Decode for this encoding

```
if cond == '1110' then SEE "UDF"; if cond == '1111' then SEE "SVC"; constant bits(32) imm32 = if InITBlock() then UNPREDICTABLE;
```

T2

## Encoding

```
B{<c>}{<q>} <label> // (Outside or last in IT block)
```

<!-- image -->

```
SignExtend(imm8:'0', 32);
```

<!-- image -->

## Decode for this encoding

```
constant bits(32) imm32 = SignExtend(imm11:'0', 32); if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

T3

<!-- image -->

## Encoding

```
B<c>.W <label> // (Not permitted in IT block, and <label> can be represented in T1) B<c>{<q>} <label> // (Not permitted in IT block)
```

## Decode for this encoding

```
if cond<3:1> == '111' then SEE "Related encodings"; constant bits(32) imm32 = SignExtend(S:J2:J1:imm6:imm11:'0', 32); if InITBlock() then UNPREDICTABLE;
```

T4

<!-- image -->

## Encoding

```
B{<c>}{<q>} <label> B{<c>}.W <label> // (<label> can be represented in T2)
```

## Decode for this encoding

```
constant bit I1 = NOT(J1 EOR S); constant bit I2 = NOT(J2 EOR S); constant bits(32) imm32 = if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

```
SignExtend(S:I1:I2:imm10:imm11:'0', 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Branches and miscellaneous control.

## Assembler Symbols

&lt;c&gt;

For the 'A1', 'T2', and 'T4' variants: see Standard assembler syntax fields.

For the 'T1' and 'T3' variants: see Standard assembler syntax fields. Must not be AL or omitted.

See Standard assembler syntax fields.

## &lt;label&gt;

For the 'A1' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the B instruction to this label, then selects an encoding that sets imm32 to that offset.

Permitted offsets are multiples of 4 in the range -33554432 to 33554428.

For the 'T1' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the B instruction to this label, then selects an encoding that sets imm32 to that offset. Permitted offsets are even numbers in the range -256 to 254.

For the 'T2' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the B instruction to this label, then selects an encoding that sets imm32 to that offset. Permitted offsets are even numbers in the range -2048 to 2046.

For the 'T3' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the B instruction to this label, then selects an encoding that sets imm32 to that offset.

Permitted offsets are even numbers in the range -1048576 to 1048574.

For the 'T4' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the B instruction to this label, then selects an encoding that sets imm32 to that offset.

Permitted offsets are even numbers in the range -16777216 to 16777214.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); BranchWritePC(PC32
```

<!-- image -->

```
+ imm32, BranchType_DIR);
```