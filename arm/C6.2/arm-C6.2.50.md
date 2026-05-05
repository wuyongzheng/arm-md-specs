## C6.2.50 BTI

## Branch target identification

This instruction is used to guard against the execution of instructions that are not the intended target of a branch.

Outside of a guarded memory region, a BTI instruction executes as a NOP . Within a guarded memory region, while PSTATE.BTYPE != 0b00 , a BTI instruction compatible with the current value of PSTATE.BTYPE will not generate a Branch Target Exception and will allow execution of subsequent instructions within the memory region. For more information, see PSTATE.BTYPE.

The operand &lt;targets&gt; passed to a BTI instruction determines the values of PSTATE.BTYPE that the BTI instruction is compatible with.

## System

(FEAT\_BTI)

<!-- image -->

## Encoding

BTI {&lt;targets&gt;}

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_BTI) then EndOfDecode(Decode_NOP); // Check branch target compatibility between BTI instruction SetBTypeCompatible(BTypeCompatible_BTI(op2<2:1>));
```

## Assembler Symbols

## &lt;targets&gt;

Is the type of indirection, encoded in 'op2&lt;2:1&gt;':

## Operation

SetBTypeNext('00');

and PSTATE.BTYPE

|   op2<2:1> | <targets>   |
|------------|-------------|
|         00 | [absent]    |
|         01 | c           |
|         10 | j           |
|         11 | jc          |
