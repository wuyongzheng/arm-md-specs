## F5.1.69 LDM (User registers)

Load Multiple (User registers)

In an EL1 mode other than System mode, Load Multiple (User registers) loads multiple User mode registers from consecutive memory locations using an address from a base register. The registers loaded cannot include the PC. The PE reads the base register value normally, using the current mode to determine the correct Banked version of the register. This instruction cannot writeback to the base register.

Load Multiple (User registers) is UNDEFINED in Hyp mode, and UNPREDICTABLE in User and System modes.

Armv8.2 permits the deprecation of some Load Multiple ordering behaviors in AArch32 state, for more information see FEAT\_LSMAOC.

<!-- image -->

## Encoding

```
LDM{<amode>}{<c>}{<q>} <Rn>, <registers_without_pc>^
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(15) registers = register_list; constant boolean increment = (U == '1'); constant boolean wordhigher = (P == U); if n == 15 || BitCount(registers) < 1 then
```

## CONSTRAINED UNPREDICTABLE behavior

If BitCount(registers) &lt; 1 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as an LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

## &lt;amode&gt;

is one of:

- DA Decrement After. The consecutive memory addresses end at the address in the base register. Encoded as P = 0, U = 0.
- FA Full Ascending. For this instruction, a synonym for DA .
- DB Decrement Before. The consecutive memory addresses end one word below the address in the base register. Encoded as P = 1, U = 0.
- EA Empty Ascending. For this instruction, a synonym for DB .
- IA Increment After. The consecutive memory addresses start at the address in the base register. This is the default. Encoded as P = 0, U = 1.
- FD Full Descending. For this instruction, a synonym for IA .
- IB Increment Before. The consecutive memory addresses start one word above the address in the base register. Encoded as P = 1, U = 1.

W

```
UNPREDICTABLE;
```

ED Empty Descending. For this instruction, a synonym for IB .

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <Rn>
```

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;registers\_without\_pc&gt;

Is a list of one or more registers, separated by commas and surrounded by { and }. It specifies the set of registers to be loaded by the LDM instruction. The registers are loaded with the lowest-numbered register from the lowest memory address, through to the highest-numbered register from the highest memory address. The PC must not be in the register list. See also Encoding of lists of general-purpose registers and the PC.

Instructions with similar syntax but with the PC included in &lt;registers\_without\_pc&gt; are described in LDM (exception return).

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; else constant integer length = 4*BitCount(registers); bits(32) address = if increment then R[n] else R[n]-length; if wordhigher then address = address+4; for i = 0 to 14 if registers<i> == '1' then // Load User mode register Rmode[i, M32_User] = MemS[address,4]; address = address + 4;
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User,M32\_System} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction operates as an LDM with the same addressing mode but targeting an unspecified set of registers. These registers might include R15.

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.