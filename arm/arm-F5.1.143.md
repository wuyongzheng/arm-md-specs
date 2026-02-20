## F5.1.143 PUSH

Push Multiple Registers to Stack stores multiple general-purpose registers to the stack, storing to consecutive memory locations ending just below the address in SP, and updates SP to point to the start of the stored data.

The lowest-numbered register is stored to the lowest memory address, through to the highest-numbered register to the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

<!-- image -->

## Encoding

```
PUSH{<c>}{<q>} <registers> // (Preferred syntax) STMDB{<c>}{<q>} SP!, <registers> // (Alternate syntax)
```

## Decode for this encoding

```
constant bits(16) registers = constant boolean UnalignedAllowed = FALSE; if BitCount(registers) < 1 then UNPREDICTABLE;
```

```
'0':M:'000000':register_list;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction targets an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;registers&gt;

Is a list of one or more registers to be stored, separated by commas and surrounded by { and }.

The registers in the list must be in the range R0-R7, encoded in the 'register\_list' field, and can optionally include the LR. If the LR is in the list, the 'M' field is set to 1, otherwise this field defaults to 0.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[13] - 4*BitCount(registers); for i = 0 to 14 if registers<i> == '1' then if i == 13 && i != LowestSetBit(registers) then // Only possible for encoding A1 MemA[address,4] = bits(32) UNKNOWN; else if UnalignedAllowed then MemU[address,4] = R[i]; else MemA[address,4] = R[i]; address = address + 4; if registers<15> == '1' then // Only possible for encoding A1 or A2 if UnalignedAllowed then MemU[address,4] = PCStoreValue(); else MemA[address,4] = PCStoreValue(); R[13] = R[13] - 4*BitCount(registers);
```