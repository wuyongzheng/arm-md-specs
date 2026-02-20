## F5.1.70 LDMDA, LDMFA

Load Multiple Decrement After (Full Ascending) loads multiple registers from consecutive memory locations using an address from a base register. The consecutive memory locations end at this address, and the address just below the lowest of those locations can optionally be written back to the base register.

The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

Armv8.2 permits the deprecation of some Load Multiple ordering behaviors in AArch32 state, for more information see FEAT\_LSMAOC. The registers loaded can include the PC, causing a branch to a loaded address. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC. Related system instructions are LDM (User registers) and LDM (exception return).

<!-- image -->

## Encoding

```
LDMDA{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) LDMFA{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Ascending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = register_list; constant boolean wback = (W == '1'); if n == 15 || BitCount(registers) < 1 then if wback && registers<n> == '1' then UNPREDICTABLE;
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as an LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

If wback &amp;&amp; registers&lt;n&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such as instruction, the base address might be corrupted so that the instruction cannot be repeated.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rn&gt;

!

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

## &lt;registers&gt;

Is a list of one or more registers to be loaded, separated by commas and surrounded by { and }.

The PC can be in the list.

Arm deprecates using these instructions with both the LR and the PC in the list.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[n] - 4*BitCount(registers) + 4; bits(32) data; for i = 0 to 14 if registers<i> == '1' then if i != n then R[i] = MemS[address,4]; else data = MemS[address,4]; address = address + 4; if registers<15> == '1' then LoadWritePC(MemS[address,4]); if wback && registers<n> == '1' then R[n] = bits(32) UNKNOWN; if wback && registers<n> == '0' then R[n] = R[n] - 4*BitCount(registers); if !wback && registers<n> == '1' then R[n] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the general-purpose base register, encoded in the 'Rn' field.