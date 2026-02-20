## F5.1.68 LDM (exception return)

Load Multiple (exception return) loads multiple registers from consecutive memory locations using an address from a base register. The SPSR of the current mode is copied to the CPSR. An address adjusted by the size of the data loaded can optionally be written back to the base register.

The registers loaded include the PC. The word loaded for the PC is treated as an address and a branch occurs to that address.

The PE checks the encoding that is copied to the CPSR for an illegal return event. See Illegal return events from AArch32 state.

Load Multiple (exception return) is:

- UNDEFINED in Hyp mode.
- UNPREDICTABLE in debug state, and in User mode and System mode.

<!-- image -->

## Encoding

```
LDM{<amode>}{<c>}{<q>} <Rn>{!}, <registers_with_pc>^
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(15) registers = register_list; constant boolean wback = (W == '1'); constant boolean increment = (U == '1'); constant boolean wordhigher = (P == U); if n == 15 then UNPREDICTABLE; if wback && registers<n> == '1' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If wback &amp;&amp; registers&lt;n&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all the loads using the specified addressing mode and the content of the register being written back is UNKNOWN. In addition, if an exception occurs during the execution of this instruction, the base address might be corrupted so that the instruction cannot be repeated.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

## &lt;amode&gt;

is one of:

- DA Decrement After. The consecutive memory addresses end at the address in the base register. Encoded as P = 0, U = 0.
- FA Full Ascending. For this instruction, a synonym for DA .
- DB Decrement Before. The consecutive memory addresses end one word below the address in the base register. Encoded as P = 1, U = 0.

&lt;c&gt;

&lt;q&gt;

## &lt;Rn&gt;

!

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

## &lt;registers\_with\_pc&gt;

Is a list of one or more registers, separated by commas and surrounded by { and }. It specifies the set of registers to be loaded. The registers are loaded with the lowest-numbered register from the lowest memory address, through to the highest-numbered register from the highest memory address. The PC must be specified in the register list, and the instruction causes a branch to the address (data) loaded into the PC. See also Encoding of lists of general-purpose registers and the PC.

Instructions with similar syntax but without the PC included in the registers list are described in LDM (User registers).

## Operation

- if ConditionPassed() then
- EA Empty Ascending. For this instruction, a synonym for DB .
- IA Increment After. The consecutive memory addresses start at the address in the base register. This is the default. Encoded as P = 0, U = 1.
- FD Full Descending. For this instruction, a synonym for IA .
- IB Increment Before. The consecutive memory addresses start one word above the address in the base register. Encoded as P = 1, U = 1.
- ED Empty Descending. For this instruction, a synonym for IB .

```
EncodingSpecificOperations(); if PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; // UNDEFINED or NOP else constant integer length = 4*BitCount(registers) + 4; bits(32) address = if increment then R[n] else R[n]-length; if wordhigher then address = address+4; bits(32) data; for i = 0 to 14 if registers<i> == '1' then if i != n then R[i] = MemS[address,4]; else data = MemS[address,4]; address = address + 4; constant bits(32) new_pc_value = MemS[address,4]; if wback && registers<n> == '1' then R[n] = bits(32) UNKNOWN; if wback && registers<n> == '0' then R[n] = if increment then R[n]+length else R[n]-length; if !wback && registers<n> == '1' then R[n] = data;
```

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

AArch32.ExceptionReturn(new\_pc\_value, SPSR\_curr[]);

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User,M32\_System} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.