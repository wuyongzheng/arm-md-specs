## F5.1.227 STMDA, STMED

Store Multiple Decrement After (Empty Descending) stores multiple registers to consecutive memory locations using an address from a base register. The consecutive memory locations end at this address, and the address just below the lowest of those locations can optionally be written back to the base register.

The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

Armv8.2 permits the deprecation of some Store Multiple ordering behaviors in AArch32 state, for more information see FEAT\_LSMAOC. For details of related system instructions see STM (User registers).

<!-- image -->

## Encoding

```
STMDA{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) STMED{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Empty Descending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = register_list; constant boolean wback = (W == '1'); if n == 15 || BitCount(registers) < 1 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction targets an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers stored.

If n == 15 &amp;&amp; wback , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction uses the addressing mode described in the equivalent immediate offset instruction.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

```
<Rn> Is the general-purpose base register, encoded in the 'Rn' field. !
```

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

## &lt;registers&gt;

Is a list of one or more registers to be stored, separated by commas and surrounded by { and }.

The PC can be in the list. However, Arm deprecates the use of instructions that include the PC in the list.

If base register writeback is specified, and the base register is not the lowest-numbered register in the list, such an instruction stores an UNKNOWN value for the base register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[n] - 4*BitCount(registers) + 4; for i = 0 to 14 if registers<i> == '1' then if i == n && wback && i != LowestSetBit(registers) then MemS[address,4] = bits(32) UNKNOWN; else MemS[address,4] = R[i]; address = address + 4; if registers<15> == '1' then MemS[address,4] = PCStoreValue(); if wback then R[n] = R[n] - 4*BitCount(registers);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.