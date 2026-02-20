## F5.1.228 STMDB, STMFD

Store Multiple Decrement Before (Full Descending) stores multiple registers to consecutive memory locations using an address from a base register. The consecutive memory locations end just below this address, and the address of the first of those locations can optionally be written back to the base register.

The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

Armv8.2 permits the deprecation of some Store Multiple ordering behaviors in AArch32 state, for more information see FEAT\_LSMAOC. For details of related system instructions see STM (User registers).

This instruction is used by the alias PUSH (multiple registers).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
STMDB{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) STMFD{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = register_list; constant boolean wback = (W == '1'); if n == 15 || BitCount(registers) < 1 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as an STM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers stored.

T1

<!-- image -->

## Encoding

```
STMDB{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) STMFD{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = P:M:register_list; constant boolean wback = (W == '1'); if n == 15 || BitCount(registers) < 2 then UNPREDICTABLE; if wback && registers<n> == '1' then UNPREDICTABLE; if registers<13> == '1' then UNPREDICTABLE; if registers<15> == '1' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as an STM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers stored.

If wback &amp;&amp; registers&lt;n&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction executes but the value stored for the base register is UNKNOWN.

If BitCount(registers) == 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction operates as an STM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15.

If registers&lt;13&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The store instruction performs all of the stores using the specified addressing mode but the value of R13 is UNKNOWN.

If registers&lt;15&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The store instruction performs all of the stores using the specified addressing mode but the value of R15 is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

&lt;q&gt;

## &lt;Rn&gt;

!

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

## &lt;registers&gt;

For the 'A1' variant: is a list of one or more registers to be stored, separated by commas and surrounded by { and }.

The PC can be in the list. However, Arm deprecates the use of instructions that include the PC in the list.

If base register writeback is specified, and the base register is not the lowest-numbered register in the list, such an instruction stores an UNKNOWN value for the base register.

For the 'T1' variant: is a list of one or more registers to be stored, separated by commas and surrounded by { and }.

The registers in the list must be in the range R0-R12, encoded in the 'register\_list' field, and can optionally contain the LR. If the LR is in the list, the 'M' field is set to 1, otherwise it defaults to 0.

## Alias Conditions

| Alias                     | Of variant   | Is preferred when                                           |
|---------------------------|--------------|-------------------------------------------------------------|
| PUSH (multiple registers) | A1           | W == '1' && Rn == '1101' && BitCount(register_list) > 1     |
| PUSH (multiple registers) | T1           | W == '1' && Rn == '1101' && BitCount(M : register_list) > 1 |
| PUSH (multiple registers) | T1           | BitCount(M : register_list) > 1                             |

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[n] - 4*BitCount(registers); for i = 0 to 14 if registers<i> == '1' then if i == n && wback && i != LowestSetBit(registers) then MemS[address,4] = bits(32) UNKNOWN; // Only possible for encoding A1 else MemS[address,4] = R[i]; address = address + 4; if registers<15> == '1' then // Only possible for encoding A1 MemS[address,4] = PCStoreValue(); if wback then R[n] = R[n] - 4*BitCount(registers);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.