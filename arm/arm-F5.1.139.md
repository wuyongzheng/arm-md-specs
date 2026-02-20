## F5.1.139 POP

Pop Multiple Registers from Stack loads multiple general-purpose registers from the stack, loading from consecutive memory locations starting at the address in SP, and updates SP to point just above the loaded data.

The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

The registers loaded can include the PC, causing a branch to a loaded address. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

<!-- image -->

## Encoding

```
POP{<c>}{<q>} <registers> // (Preferred syntax) LDM{<c>}{<q>} SP!, <registers> // (Alternate syntax)
```

## Decode for this encoding

```
constant bits(16) registers = P:'0000000':register_list; constant boolean UnalignedAllowed = FALSE; if BitCount(registers) < 1 then UNPREDICTABLE; if registers<15> == '1'
```

```
&& InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction targets an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;registers&gt;

Is a list of one or more registers to be loaded, separated by commas and surrounded by { and }.

The registers in the list must be in the range R0-R7, encoded in the 'register\_list' field, and can optionally include the PC. If the PC is in the list, the 'P' field is set to 1, otherwise this field defaults to 0.

If the PC is in the list, the instruction must be either outside any IT block, or the last instruction in an IT block.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[13]; for i = 0 to 14 if registers<i> == '1' then R[i] = if UnalignedAllowed then MemU[address,4] else address = address + 4; if registers<15> == '1' then if UnalignedAllowed then if address<1:0> == '00' then LoadWritePC(MemU[address,4]); else UNPREDICTABLE; else LoadWritePC(MemA[address,4]); if registers<13> == '0' then R[13] = R[13] + 4*BitCount(registers); if registers<13> == '1' then R[13] = bits(32) UNKNOWN;
```

```
MemA[address,4];
```