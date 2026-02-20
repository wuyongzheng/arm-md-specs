## F5.1.218 STL

Store-Release Word stores a word from a register to memory. The instruction also has memory ordering semantics as described in Load-Acquire, Store-Release.

For more information about support for shared memory see Synchronization and semaphores. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
STL{<c>}{<q>} <Rt>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); if t == 15 || n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
STL{<c>}{<q>} <Rt>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); if t == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

sz

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;q&gt;

&lt;Rt&gt;

&lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = MemO[address, 4] = R[t];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
R[n];
```