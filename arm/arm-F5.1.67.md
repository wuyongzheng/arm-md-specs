## F5.1.67 LDM, LDMIA, LDMFD

Load Multiple (Increment After, Full Descending) loads multiple registers from consecutive memory locations using an address from a base register. The consecutive memory locations start at this address, and the address just above the highest of those locations can optionally be written back to the base register.

The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

Armv8.2 permits the deprecation of some Load Multiple ordering behaviors in AArch32 state, for more information see FEAT\_LSMAOC. The registers loaded can include the PC, causing a branch to a loaded address. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC. Related system instructions are LDM (User registers) and LDM (exception return).

This instruction is used by the alias POP (multiple registers).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

## A1

<!-- image -->

## Encoding

```
LDM{IA}{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) LDMFD{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack)
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
- The instruction executes as LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

If wback &amp;&amp; registers&lt;n&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

T1

## Encoding

```
LDM{IA}{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) LDMFD{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = constant boolean wback = (registers<n> == '0'); if BitCount(registers) < 1 then UNPREDICTABLE;
```

```
'00000000':register_list;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

T2

<!-- image -->

## Encoding

```
LDM{IA}{<c>}.W <Rn>{!}, <registers> // (Preferred syntax, if <Rn>, '!' and <registers> can be ↪ → represented in T1) LDMFD{<c>}.W <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack, if <Rn>, '!' and ↪ → <registers> can be represented in T1) LDM{IA}{<c>}{<q>} <Rn>{!}, <registers> // (Preferred syntax) LDMFD{<c>}{<q>} <Rn>{!}, <registers> // (Alternate syntax, Full Descending stack)
```

<!-- image -->

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(16) registers = P:M:register_list; constant boolean wback = (W == '1'); if n == 15 || BitCount(registers) < 2 || (P == '1' && M == '1') then UNPREDICTABLE; if wback && registers<n> == '1' then UNPREDICTABLE; if registers<13> == '1' then UNPREDICTABLE; if registers<15> == '1' && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15. If the instruction specifies writeback, the modification to the base address on writeback might differ from the number of registers loaded.

If wback &amp;&amp; registers&lt;n&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode and the content of the register that is written back is UNKNOWN. In addition, if an exception occurs during such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

If BitCount(registers) == 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction loads a single register using the specified addressing modes.
- The instruction executes as LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15.

If registers&lt;13&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction performs all of the loads using the specified addressing mode, but R13 is UNKNOWN.

If P == '1' &amp;&amp; M == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction loads the register list and either R14 or R15, both R14 and R15, or neither of these registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

IA

Is an optional suffix for the Increment After form.

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

For the 'A1' and 'T2' variants: the address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

For the 'T1' variant: the address adjusted by the size of the data loaded is written back to the base register. It is omitted if &lt;Rn&gt; is included in &lt;registers&gt; , otherwise it must be present.

## &lt;registers&gt;

For the 'A1' variant: is a list of one or more registers to be loaded, separated by commas and surrounded by { and }.

The PC can be in the list.

Arm deprecates using these instructions with both the LR and the PC in the list.

For the 'T1' variant: is a list of one or more registers to be loaded, separated by commas and surrounded by { and }. The registers in the list must be in the range R0-R7, encoded in the 'register\_list' field.

For the 'T2' variant: is a list of one or more registers to be loaded, separated by commas and surrounded by { and }. The registers in the list must be in the range R0-R12, encoded in the 'register\_list' field, and can optionally contain one of the LR or the PC. If the LR is in the list, the 'M' field is set to 1, otherwise it defaults to 0. If the PC is in the list, the 'P' field is set to 1, otherwise it defaults to 0.

If the PC is in the list:

- The LR must not be in the list.
- The instruction must be either outside any IT block, or the last instruction in an IT block.

## Alias Conditions

| Alias                    | Of variant   | Is preferred when                                               |
|--------------------------|--------------|-----------------------------------------------------------------|
| POP (multiple registers) | A1           | W == '1' && Rn == '1101' && BitCount(register_list) > 1         |
| POP (multiple registers) | T2           | W == '1' && Rn == '1101' && BitCount(P : M : register_list) > 1 |
| POP (multiple registers) | T2           | BitCount(P : M : register_list) > 1                             |

## Operation

<!-- image -->

&lt;q&gt;

## &lt;Rn&gt;

!

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) address = R[n]; bits(32) data; for i = 0 to 14 if registers<i> == '1' then if i != n then R[i] = MemS[address,4]; else data = MemS[address,4]; address = address + 4; if registers<15> == '1' then LoadWritePC(MemS[address,4]); if wback && registers<n> == '1' then R[n] = bits(32) UNKNOWN; if wback && registers<n> == '0' then R[n] = R[n] + 4*BitCount(registers); if !wback && registers<n> == '1' then R[n] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.