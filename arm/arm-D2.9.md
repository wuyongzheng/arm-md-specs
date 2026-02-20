## D2.9 Watchpoint exceptions

This section describes Watchpoint exceptions in stage 1 of an AArch64 translation regime.

The PE is using an AArch64 translation regime when it is executing one of the following:

- In an Exception level that is using AArch64.
- At EL0 using AArch32 when EL1 is using AArch64.
- At EL0 using AArch32 when FEAT\_VHE is implemented, EL2 is implemented and enabled in the current Security state, and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

This section contains the following subsections:

- About Watchpoint exceptions.
- Watchpoint types and linking of watchpoints.
- Execution conditions for which a watchpoint generates Watchpoint exceptions.
- Watchpoint data address comparisons.
- Watchpoint behavior for certain instruction classes.
- Watchpoint usage constraints.
- Exception syndrome information, fault address information, and preferred return address.
- Pseudocode description of Watchpoint exceptions taken from AArch64 state.

## D2.9.1 About Watchpoint exceptions

A watchpoint is an event that results from the execution of an instruction, based on a data address. Watchpoints are also known as data breakpoints .

Awatchpoint operates as follows:

1. Adebugger programs the watchpoint with a data address, or a data address range.
2. The watchpoint generates a Watchpoint debug event on an access to the address, or any address in the address range.

Awatchpoint never generates a Watchpoint debug event on an instruction fetch.

An implementation can include between 2-64 watchpoints. In an implementation, ID\_AA64DFR0\_EL1.WRPs and EDDFR1.WRPs show how many are implemented.

If AArch32 is supported at EL1 or FEAT\_Debugv8p9 is not implemented, then the PE does not implement more than 16 watchpoints.

To use an implemented watchpoint, a debugger programs the following registers for the watchpoint:

- The Watchpoint Control Register , DBGWCR&lt;n&gt;\_EL1. This contains controls for the watchpoint, for example an enable control.
- The Watchpoint Value Register , DBGWVR&lt;n&gt;\_EL1. This holds the data virtual address used for watchpoint matching.

These registers are numbered, so that:

- DBGWCR0\_EL1 and DBGWVR0\_EL1 are for watchpoint number zero.
- DBGWCR1\_EL1 and DBGWVR1\_EL1 are for watchpoint number one.
- . . .
- DBGWCR&lt;n-1&gt;\_EL1 and DBGWVR&lt;n-1&gt;\_EL1 are for watchpoint number (n-1).

Awatchpoint can:

- Be programmed to generate Watchpoint debug events on read accesses only, on write accesses only, or on both types of access.
- Link to a Context matching breakpoint with linking enabled , so that a Watchpoint debug event is generated only if the PE is in a particular context when the address match occurs.
- If FEAT\_ABLE is implemented, link to an Address matching breakpoint with linking enabled so that a executed from a specific address or in range of addressed.
- Watchpoint debug event is generated only if the address of the instruction that made the matching access was The Address matching breakpoint with linking enabled can also be linked to a Context matching breakpoint with linking enabled.
- If FEAT\_BWE2 is implemented, link to an Address mismatch breakpoint so that a Watchpoint debug event is generated only if the address of the instruction that made the access was executed from an address that was not selected. See Watchpoint data address comparisons.
- Be programmed as an address match watchpoint or an address mismatch watchpoint. See Watchpoint data address comparisons.

Asingle watchpoint can be programmed to match or mismatch on one or more address bytes. A watchpoint generates a Watchpoint debug event on an access to any byte that it is watching. The number of bytes a watchpoint is watching is either:

- One to eight bytes, provided that these bytes are contiguous and that they are all in the same naturally-aligned doubleword. A debugger uses the Byte Address Select field, DBGWCR&lt;n&gt;\_EL1.BAS, to select the bytes. See Programming a watchpoint range with eight bytes or fewer.
- Eight bytes to 2GB, provided that both of the following are true:
- -The number of bytes is a power-of-two.
- -The range starts at an address that is aligned to the range size.

Adebugger uses the MASK field, DBGWCR&lt;n&gt;\_EL1.MASK, to program a watchpoint with eight bytes to 2GB. See Programming a watchpoint range with eight or more bytes.

Adebugger must use either the BAS field or the MASK field. If it uses both, whether the watchpoint generates Watchpoint debug events is CONSTRAINED UNPREDICTABLE. See Programming dependencies of the BAS and MASK fields.

For each memory access, all of the watchpoints are tested. When a watchpoint is tested, it generates a Watchpoint debug event if all of the following are true:

- The conditions specified in the DBGWCR&lt;n&gt;\_EL1 are met. This includes all of the following:
- -The watchpoint is enabled. See DBGWCR&lt;n&gt;\_EL1.E.
- -The type of the access. That is, whether the access is a load, a store, or both. See DBGWCR&lt;n&gt;\_EL1.LST.
- -The Security state, Exception level, and privilege of the access. See Execution conditions for which a watchpoint generates Watchpoint exceptions.
- -If the watchpoint links to a breakpoint with linking enabled, the comparison or comparisons made by the breakpoint. See Rules for linking watchpoints.

Together, these define the context of the data access that the watchpoint matches.

- The comparison with the address held in the DBGWVR&lt;n&gt;\_EL1 is successful. See Watchpoint data address comparisons.
- The instruction that initiates the memory access is committed for execution.
- The instruction that initiates the memory access passes its Condition code check.
- If the access is due to a System register access instruction executed at EL1 and transformed into a memory access by the mechanism described in Enhanced support for nested virtualization and one of the following is true:
- -EDSCR.HDE is set to 1 and halting is allowed.
- -Debug exceptions are enabled at EL2. For more information, see Enabling debug exceptions from the current Exception level and Security state.

If multiple watchpoints can generate a Watchpoint debug event for an access, then, for all watchpoints that are enabled and match the context of the data access:

- The Boolean equality comparison results of all the address match watchpoints are OR'd together to generate a first result.
- The Boolean inequality comparison results of all the address mismatch watchpoints are AND'd together to generate a second result.

Awatchpoint debug event is generated if any of the following apply:

- The first result is true and all enabled watchpoints are address match watchpoints.
- The second result is true and all enabled watchpoints are address mismatch watchpoints.
- Both the first and second results are true, and both address match watchpoints and address mismatch watchpoints are enabled.

The pseudocode function AArch64.CheckWatchpoint() describes the details for combining the results of individual watchpoints to determine the final result of watchpoint match.

If halting is allowed and EDSCR.HDE is 1, Watchpoint debug events cause entry to Debug state. Otherwise, if debug exceptions are:

- Enabled, Watchpoint debug events generate Watchpoint exceptions.
- Disabled, Watchpoint debug events are ignored.

Note

The remainder of this Watchpoint Exceptions section, including all subsections, describes watchpoints as generating Watchpoint exceptions.

However, unless specified otherwise, the behavior described also applies if watchpoints are causing entry to Debug state.

The debug exception enable controls describes the enable controls for Watchpoint debug events.

## D2.9.2 Accessing watchpoint System registers

| R MLRFY   | The rules in Accessing breakpoint System registers that apply to MDSELR_EL1.BANK when accessing breakpoint registers also apply to watchpoint registers. SeeR MLTYN ,R JGQGB , and I HMNFZ .                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YKKCH   | The MRS and MSR System register names for accessing breakpoint control registers DBGWCR<n>_EL1 and breakpoint value registers DBGWVR<n>_EL1 are mapped to physical registers as follows: • The register names DBGWCR0_EL1 through DBGWCR15_EL1 are mapped to the physical registers DBGWCR<BANK × 16+0>_EL1 throughDBGWCR<BANK × 16+15>_EL1. • The register names DBGWVR0_EL1 through DBGWVR15_EL1 are mapped to the physical registers |
| I XMTTT   | MSR and MRS instructions using the watchpoint System register names inR YKKCH make indirect reads of MDSELR_EL1.BANK. This means that direct writes to MDSELR_EL1.BANK must be explicitly synchronized before a direct read or direct write using any of these System register names.                                                                                                                                                   |

## D2.9.3 Watchpoint types and linking of watchpoints

When a debugger programs a watchpoint, it must program that watchpoint so that:

- It is either:
- -Used in isolation. In this case, the watchpoint is called an Unlinked watchpoint .
- -Linked to a breakpoint with linking enabled. In this case, the watchpoint is called a Linked watchpoint .
- And is either:
- -An address match watchpoint.
- -An address mismatch watchpoint.

When a Linked watchpoint links to an Address matching breakpoint with linking enabled, the Linked watchpoint generates a Watchpoint exception only if the address of the instruction that made the matching access was executed from a specific address or in range of addresses.

When a Linked watchpoint links to a Context matching breakpoint with linking enabled, or a Linked watchpoint links to a Linked Address matching breakpoint with linking enabled that links to a Context matching breakpoint with linking enabled, the Linked watchpoint generates a Watchpoint exception only if the PE is in a particular context when the data address match occurs.

Example D2-3 Linking a watchpoint and an Address matching breakpoint

For example, a debugger might:

1. Program watchpoint number one with a data address.
2. Program breakpoint number five to be a Linked VMID Match breakpoint .
3. Link the watchpoint and the breakpoint together. A Watchpoint exception is generated only if both the data address matches and the VMID matches.

## D2.9.3.1 Rules for linking watchpoints

The rules for watchpoint linking are as follows:

- Only Linked watchpoints can be linked.
- ALinked watchpoint can be linked to any breakpoint with linking enabled.
- ALinked watchpoint can link to any type of breakpoint with linking enabled. The Linked Breakpoint Number field, DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN}, for the Linked watchpoint specifies the particular breakpoint that the Linked watchpoint links to, and:
- -DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} for the Linked watchpoint defines the execution conditions that the watchpoint generates Watchpoint exceptions for. See Execution conditions for which a watchpoint generates Watchpoint exceptions.
- -DBGBCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PMC} for the breakpoint with linking enabled are ignored.
- ALinked watchpoint cannot link to another watchpoint. The {LBNX, LBN} fields always specify a breakpoint.
- If any of the following apply, then the behavior of the Linked watchpoint is CONSTRAINED UNPREDICTABLE:
- -The Linked watchpoint is linked to a breakpoint that does not support linking.
- -FEAT\_ABLE is not implemented and the Linked watchpoint is linked to a breakpoint that is not context aware.
- -FEAT\_ABLE is not implemented and the Linked watchpoint is linked to an Address matching breakpoint.
- -The Linked watchpoint is linked to an unimplemented breakpoint.
- -The Linked watchpoint or Linked breakpoint is linked to a breakpoint that does not have linking enabled.

See Watchpoint usage constraints.

- If the access is due to a System register access instruction executed at EL1 and transformed into a memory access by the mechanism described in Enhanced support for nested virtualization, and the watchpoint is linked to a Context matching breakpoint with linking enabled, or a Linked Address matching breakpoint with linking enabled that is linked to a Context matching breakpoint with linking enabled, then it is CONSTRAINED UNPREDICTABLE whether there is a watchpoint match.
- If an instruction address generates a breakpoint match for more than one enabled Address matching breakpoint with linking enabled, then it is CONSTRAINED UNPREDICTABLE whether Watchpoint exceptions and debug events are generated.

- Multiple Linked watchpoints can link to a single breakpoint with linking enabled.

Note

Multiple Address breakpoints can also link to a single breakpoint with linking enabled. Breakpoint exceptions describes breakpoints.

Figure D2-1 shows an example of permitted watchpoint linking.

## D2.9.4 Execution conditions for which a watchpoint generates Watchpoint exceptions

Each watchpoint can be programmed so that it generates Watchpoint exceptions only for certain execution conditions. For example, a watchpoint might be programmed to generate Watchpoint exceptions only for Non-secure EL2 accesses.

DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} define the execution conditions a watchpoint generates Watchpoint exceptions for, as follows:

## Security State Control Extension, SSCE, and Security State Control, SSC

SSCE and SSC control whether the watchpoint generates Watchpoint exceptions in only one Security state or in multiple Security states.

Note

This is determined by the Security state of the PE, not from the physical address space attribute returned by the translation of the virtual address on which the watchpoint is set.

## Higher Mode Control, HMC, and Privileged Access Control, PAC

HMCand PAC together control which Exception levels and privilege levels the watchpoint generates Watchpoint exceptions in.

The PAC control relates to the privilege of the memory access and the Exception level at which the access was made:

- Unprivileged memory accesses generated by unprivileged memory access instructions are treated as unprivileged EL0 accesses.
- System register accesses executed at EL1 and transformed into a memory access by the mechanism described in Enhanced support for nested virtualization are treated as EL2 accesses.

Example D2-4

PAC condition for generating a Watchpoint exception

This means that, if the PE executes an unprivileged memory access instruction at EL1, any resulting Explicit Memory Effect that is unprivileged triggers a watchpoint only if both:

- PAC is programmed to a value that generates watchpoints on EL0 accesses.
- All other conditions for generating the watchpoint are met.

Example A64 unprivileged memory access instructions are LDTR and STTR .

Table D2-13 shows the valid combinations of HMC, SSCE, SSC, and PAC, and for each combination shows which Exception levels watchpoints generate Watchpoint exceptions in.

In the table:

NS

Non-secure state.

S

Secure state.

RL

In implementations that include FEAT\_RME, Realm state.

RT

In implementations that include FEAT\_RME, Root state.

- Yor -

Means that a watchpoint programmed with the values of HMC, SSCE, SSC, and PAC shown in that row:

Y

Can generate Watchpoint exceptions in that Exception level and Security state.

- -

Cannot generate Watchpoint exceptions in that Exception level and Security state.

Table D2-13 Summary of watchpoint HMC, SSCE, SSC, and PAC encodings

|   HMC |   SSCE |   SSC |   PAC | Security states   | EL3 a   | EL2   | EL1   | EL0   |
|-------|--------|-------|-------|-------------------|---------|-------|-------|-------|
|     0 |      0 |    00 |    01 | RL, S, NS         | -       | -     | Y     | -     |
|     0 |      0 |    00 |    10 | RL, S, NS         | -       | -     | -     | Y     |
|     0 |      0 |    00 |    11 | RL, S, NS         | -       | -     | Y     | Y     |
|     0 |      0 |    01 |    01 | NS                | -       | -     | Y     | -     |
|     0 |      0 |    01 |    10 | NS                | -       | -     | -     | Y     |
|     0 |      0 |    01 |    11 | NS                | -       | -     | Y     | Y     |
|     0 |      0 |    10 |    01 | S                 | -       | -     | Y     | -     |
|     0 |      0 |    10 |    10 | S                 | -       | -     | -     | Y     |
|     0 |      0 |    10 |    11 | S                 | -       | -     | Y     | Y     |
|     0 |      0 |    11 |    00 | S                 | -       | Y     | -     | -     |
|     0 |      0 |    11 |    01 | S                 | -       | Y     | Y     | -     |
|     0 |      0 |    11 |    11 | S                 | -       | Y     | Y     | Y     |
|     0 |      1 |    01 |    01 | RL                | -       | -     | Y     | -     |
|     0 |      1 |    01 |    10 | RL                | -       | -     | -     | Y     |
|     0 |      1 |    01 |    11 | RL                | -       | -     | Y     | Y     |
|     1 |      0 |    00 |    01 | RT, RL, S, NS     | Y       | Y     | Y     | -     |
|     1 |      0 |    00 |    11 | RT, RL, S, NS     | Y       | Y     | Y     | Y     |
|     1 |      0 |    01 |    00 | NS                | -       | Y     | -     | -     |
|     1 |      0 |    01 |    01 | NS                | -       | Y     | Y     | -     |
|     1 |      0 |    01 |    11 | NS                | -       | Y     | Y     | Y     |
|     1 |      0 |    10 |    00 | RT or S b         | Y       | -     | -     | -     |
|     1 |      0 |    10 |    01 | RT, S             | Y       | Y     | Y     | -     |
|     1 |      0 |    10 |    11 | RT, S             | Y       | Y     | Y     | Y     |
|     1 |      0 |    11 |    00 | RL, S, NS         | -       | Y     | -     | -     |
|     1 |      0 |    11 |    01 | RL, S, NS         | -       | Y     | Y     | -     |
|     1 |      0 |    11 |    11 | RL, S, NS         | -       | Y     | Y     | Y     |
|     1 |      1 |    01 |    00 | RL                | -       | Y     | -     | -     |
|     1 |      1 |    01 |    01 | RL                | -       | Y     | Y     | -     |
|     1 |      1 |    01 |    11 | RL                | -       | Y     | Y     | Y     |

All combinations of HMC, SSCE, SSC, and PAC that Table D2-13 does not show are reserved. A combination in Table D2-13 might be reserved if an Exception level or Security state is not implemented. For information about which combinations of HMC, SSCE, SSC and PAC are reserved if an Exception level or Security state are not implemented or enabled, see Reserved DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} values.

## D2.9.5 Watchpoint data address comparisons

In this subsection, the term AddrTop represents the most significant bit of a virtual address used by watchpoint data address comparisons. AddrTop is:

- 55, if address tagging is used for the address. See Address tagging.
- 63, otherwise.

Note

When stage 1 translation is enabled, in AArch64 state, the virtual address size is determined by the configured input address size for the stage 1 translation. Software can configure a smaller address width for a virtual address. See Input address size configuration. Attempting to translate an address that is larger than the configured input address size generates a Translation fault.

When stage 1 translation is disabled, using an address that is larger than the implemented PA size generates an Address size fault. The implemented PA size is IMPLEMENTATION DEFINED, as described in Implemented physical address size. These faults have a higher priority than watchpoints.

Bits [ AddrTop :2] of the data address are compared with DBGWVR&lt;n&gt;\_EL1[ AddrTop :2], taking into account all of the following:

- The size of the access. See Size of the data access.
- The bytes selected by DBGWVR&lt;n&gt;\_EL1.BAS. See Programming a watchpoint range with eight bytes or fewer.
- Any address ranges indicated by DBGWVR&lt;n&gt;\_EL1.MASK. See Programming a watchpoint range with eight or more bytes.

The comparison is successful if any of following are true:

- The watchpoint is an address match watchpoint, and the two values being compared match.
- The watchpoint is an address mismatch watchpoint, and the two values being compared do not match.

If EL1 is using AArch64 and EL0 is using AArch32, AArch32 instructions can be executed in stage 1 of an AArch64 translation regime. In this case, the 32-bit data address is zero-extended before comparison with the watchpoint.

Note

- DBGWVR&lt;n&gt;\_EL1 is a 64-bit register. The most significant bits of this register are sign-extension bits.
- DBGWVR&lt;n&gt;\_EL1[1:0] are RES0 and are ignored.

## D2.9.5.1 Size of the data access

Because watchpoints can be programmed to generate Watchpoint exceptions on individual bytes, the size of each data access must be taken into account. The address of every byte in a data access is compared, and:

- In the case of an address match watchpoint, the watchpoint generates a Watchpoint exception if any byte address matches. See Example D2-5.
- In the case of an address mismatch watchpoint, the watchpoint generates a Watchpoint exception if any byte address does not match. See Example D2-6.

Example D2-5

1. Adebugger programs an address match watchpoint to generate Watchpoint exceptions only when the byte at address 0x1009 is accessed.
2. The PE accesses the unaligned doubleword starting at address 0x1003 .

In this scenario, the watchpoint generates a Watchpoint exception.

Example D2-6

1. Adebugger programs an address mismatch watchpoint to generate Watchpoint exceptions when any address other than the byte at address 0x1009 is accessed.
2. The PE accesses the unaligned doubleword starting at address 0x1003 .

In this scenario, the watchpoint generates a Watchpoint exception.

The size of data accesses initiated by DC ZVA instructions is the DC ZV A block size that DCZID\_EL0.BS defines.

The size of data accesses initiated by DC IVAC instructions is an IMPLEMENTATION DEFINED size that is both:

- From the inclusive range between:
- -The size that CTR\_EL0.DminLine defines.
- -2KB.
- Apower-of-two.

For both of these instructions:

- The lowest address accessed by the instruction is the address supplied to the instruction, rounded down to the nearest multiple of the access size initiated by that instruction.
- The highest address accessed is (size - 1) bytes above the lowest address accessed.

See also Watchpoint behavior on accesses by the DC IV AC instruction and the DC ZV A, DC GV A, and DC GZVA instructions.

## D2.9.5.2 Programming a watchpoint range with eight bytes or fewer

The Byte Address Select field, DBGWCR&lt;n&gt;\_EL1.BAS, selects bytes in the doubleword starting at the address contained in DBGWVR&lt;n&gt;\_EL1.

If the address programmed into the DBGWVR&lt;n&gt;\_EL1 is:

- Doubleword-aligned:
- -All eight bits of DBGWCR&lt;n&gt;\_EL1.BAS are used.
- Word-aligned but not doubleword-aligned:
- -Only DBGWCR&lt;n&gt;\_EL1.BAS[3:0] are used. In this case, DBGWCR&lt;n&gt;\_EL1.BAS[7:4] are RES0.

An address match watchpoint generates a Watchpoint exception when an access accesses any byte address that DBGWCR&lt;n&gt;\_EL1.BAS selects. An address mismatch watchpoint generates a Watchpoint exception when an access accesses any byte address that DBGWCR&lt;n&gt;\_EL1.BAS does not select.

Table D2-14 Supported BAS values when the DBGWVR&lt;n&gt;\_EL1 address alignment is doubleword

| BAS value   | Description                                               |
|-------------|-----------------------------------------------------------|
| 0b00000000  | No byte selected.                                         |
| BAS[0] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 000 selected. |
| BAS[1] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 001 selected. |
| BAS[2] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 010 selected. |
| BAS[3] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 011 selected. |

| BAS value   | Description                                               |
|-------------|-----------------------------------------------------------|
| BAS[4] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 100 selected. |
| BAS[5] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 101 selected. |
| BAS[6] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 110 selected. |
| BAS[7] == 1 | Byte at address DBGWVR<n>_EL1[ AddrTop :3]: 111 selected. |

Table D2-15 Supported BAS values when the DBGWVR&lt;n&gt;\_EL1 address alignment is word

| BAS value a   | Description                                              |
|---------------|----------------------------------------------------------|
| 0b00000000    | No byte selected.                                        |
| BAS[0] == 1   | Byte at address DBGWVR<n>_EL1[ AddrTop :2]: 00 selected. |
| BAS[1] == 1   | Byte at address DBGWVR<n>_EL1[ AddrTop :2]: 01 selected. |
| BAS[2] == 1   | Byte at address DBGWVR<n>_EL1[ AddrTop :2]: 10 selected. |
| BAS[3] == 1   | Byte at address DBGWVR<n>_EL1[ AddrTop :2]: 11 selected. |

- a. DBGWCR&lt;n&gt;\_EL1.BAS[7:4] are RES0.

If the BAS field selects more than one byte, the bytes it selects must be contiguous. For watchpoint behavior when its BAS field selects non-contiguous bytes, see Other usage constraints.

When programming the BAS field with anything other than 0b11111111 , a debugger must program DBGWCR&lt;n&gt;\_EL1.MASK to 0b00000 . See Programming dependencies of the BAS and MASK fields.

Awatchpoint generates a Watchpoint exception whenever a watched byte is accessed, even if:

- The access size is smaller or larger than the address region being watched.
- The access is misaligned, and the base address of the access is not in the doubleword or word of memory addressed by the DBGWVR&lt;n&gt;\_EL1[ AddrTop :3]. See Example D2-5.

Example D2-7

The following are some example configurations of the BAS field:

- To program an address match watchpoint to generate a Watchpoint exception on the byte at address 0x1003 , program:
- -DBGWVR&lt;n&gt;\_EL1 with 0x1000 .
- -DBGWCR&lt;n&gt;\_EL1.BAS to be 0b00001000 .
- To program an address match watchpoint to generate a Watchpoint exception on the bytes at addresses 0x2003 , 0x2004 and 0x2005 , program:
- -DBGWVR&lt;n&gt;\_EL1 with 0x2000 .
- -DBGWCR&lt;n&gt;\_EL1.BAS to be 0b00111000 .
- If the address programmed into the DBGWVR&lt;n&gt;\_EL1 is doubleword-aligned:
- -To generate a Watchpoint exception when any byte in the word starting at the doubleword-aligned address is accessed, program DBGWCR&lt;n&gt;\_EL1.BAS to be 0b00001111 .
- -To generate a Watchpoint exception when any byte in the word starting at address DBGWVR&lt;n&gt;\_EL1[31:3]:100 is accessed, program DBGWCR&lt;n&gt;\_EL1.BAS to be 0b11110000 .

Note

Arm deprecates programming a DBGWVR&lt;n&gt;\_EL1 with an address that is not doubleword-aligned.

## D2.9.5.3 Programming a watchpoint range with eight or more bytes

Adebugger can use the MASK field, DBGWCR&lt;n&gt;\_EL1.MASK, to program a single watchpoint with a data address range. The range must meet all of the following criteria:

- It is a size that is:
- -Apower-of-two.
- -Aminimum of eight bytes.
- -Amaximum of 2GB.
- It starts at an address that is aligned to the size.

The MASK field specifies the number of least significant data address bits that must be masked. Up to 31 least significant bits can be masked.

If m least significant address bits are masked, an address match watchpoint generates a Watchpoint exception on all of the following:

- Address DBGWVR&lt;n&gt;\_EL1[ AddrTop : m ]:000 . . . 0.
- Address DBGWVR&lt;n&gt;\_EL1[ AddrTop : m ]:111 . . . 1.
- Any address between these two addresses.

An address mismatch breakpoint generates a Watchpoint exception for any address outside of the range.

Example D2-8

If the four least significant address bits are masked, Watchpoint exceptions are generated for all addresses between DBGWVR&lt;n&gt;\_EL1[ AddrTop :4]:0000 and DBGWVR&lt;n&gt;\_EL1[ AddrTop :4]:1111, including these addresses.

When masking address bits, a debugger must both:

- Program DBGWCR&lt;n&gt;\_EL1.BAS to be 0b11111111 . See Programming dependencies of the BAS and MASK fields.
- In the DBGWVR&lt;n&gt;\_EL1, set the masked address bits to 0. For watchpoint behavior when any of the masked address bits are not 0, see Other usage constraints.

## D2.9.6 Watchpoint behavior for certain instruction classes

Under normal operating conditions, the following do not generate Watchpoint exceptions:

- Instruction cache maintenance instructions.
- Address translation instructions.
- TLB maintenance instructions.
- Prefetch memory instructions.
- All data cache maintenance instructions except DC IVAC.

Note

Despite their mnemonics, the DC ZVA, DC GVA, and DC GZVA instructions are not data cache maintenance instructions.

However, the debug architecture allows for IMPLEMENTATION DEFINED controls, such as those in ACTLR registers, to enable watchpoints on an IMPLEMENTATION DEFINED subset of these instructions. Whether a watchpoint treats the instruction as a load or a store, and the access size of instruction cache, address translation, and TLB operations are IMPLEMENTATION DEFINED.

The access size of the IMPLEMENTATION DEFINED instruction cache, address translation, and TLB operations which generate Watchpoint exceptions are IMPLEMENTATION DEFINED.

See also the following subsections:

- Watchpoint behavior on accesses by Store-Exclusive instructions.
- Watchpoint behavior on accesses by the DC IV AC instruction and the DC ZV A, DC GVA, and DC GZVA instructions.
- Watchpoint behavior on accesses by SVE and SME instructions.
- Watchpoint behavior on accesses by Allocation tag load and store instructions.

## D2.9.6.1 Watchpoint behavior on accesses by Store-Exclusive instructions

If a watchpoint matches on a data access caused by a Store-Exclusive instruction, then:

- If the store fails because an Exclusives monitor does not permit it, it is IMPLEMENTATION DEFINED whether the watchpoint generates a Watchpoint exception.
- Otherwise, the watchpoint generates a Watchpoint exception.

## D2.9.6.2 Watchpoint behavior on accesses by the DC IVAC instruction and the DC ZVA, DC GVA, and DC GZVA instructions

DC ZVA , DC GVA and DC GZVA operations can generate Watchpoint exceptions.

If DC IVAC is not treated as a NOP , it can generate Watchpoint exceptions.

DC IVAC , DC ZVA , DC GZVA and DC GVA operations are treated as data stores by DBGWCR&lt;n&gt;\_EL1.LSC.

Note

For the size of data accesses performed by the DC IVAC instruction and the DC ZVA instruction, see Watchpoint data address comparisons. The size of all data accesses must be considered because watchpoints can be programmed to match on individual bytes.

## D2.9.6.3 Watchpoint behavior on accesses by SVE and SME instructions

| R ZRWTZ   | For SVE predicated vector load or store instructions which are not First-fault vector loads or Non-fault vector loads, when the instruction performs a non-speculative single-copy atomic access matching a configured watchpoint due to an Active element , a Watchpoint exception is generated.       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GLRCD   | For SVE predicated non-contiguous vector load or store instructions, if the instruction performs an access due to an Inactive element , a Watchpoint exception is not generated.                                                                                                                        |
| R DYGMS   | For SVE Non-fault vector load instructions, when the instruction performs an access, a Watchpoint exception is not generated other than as permitted byR LVLYV .                                                                                                                                        |
| R LKKQG   | For SVE Non-fault vector load instructions, when the instruction performs a non-speculative single-copy atomic access matching a configured watchpoint due to an Active element , the access is reported in the FFR.                                                                                    |
| R TLSCX   | For SVE First-fault vector load instructions, when the instruction performs a non-speculative single-copy atomic access matching a configured watchpoint due to the First active element , a Watchpoint event is generated.                                                                             |
| R XBBLW   | For SVE First-fault vector load instructions, when the instruction performs a non-speculative single-copy atomic access matching a configured watchpoint due to an Active element that is not the First active element , a Watchpoint exception is not generated and the access is reported in the FFR. |
| I CKZFP   | Watchpoints are not a mechanism for preventing access to memory.                                                                                                                                                                                                                                        |

IZHXGG

DTDYYR

RLVLYV

IYVSFL

For SVE Non-fault and First-fault vector load instructions that do not generate a Watchpoint exception, an access that matches a configured watchpoint can return the data and set the appropriate FFR elements to FALSE.

A relaxed watchpoint access is a memory access or set of contiguous memory accesses generated by any of:

- SIMD&amp;FP load/store instruction when the PE is in Streaming SVE mode.
- SVE contiguous vector load/store instruction.
- SMEload/store instruction.

If all the following are true for a relaxed watchpoint access , then it is CONSTRAINED UNPREDICTABLE whether or not a watchpoint is triggered:

- The watchpoint matches a range where the lowest accessed address is rounded down to the nearest multiple of 16 bytes and the highest accessed address is rounded up to the nearest multiple of 16 bytes minus 1.
- The watchpoint does not the match the range of the original access or set of contiguous accesses.
- Either the watchpoint generates a Watchpoint exception, or FEAT\_EDHSR is implemented.

If a Watchpoint exception is triggered by a match on a rounded access address range that would not have been triggered by the original access address range, then this may report a false-positive match. The debugger should attempt to detect and step over false-positive matches. The architecture does not permit missed, or false-negative matches.

## D2.9.6.4 Watchpoint behavior on accesses by Allocation tag load and store instructions

If FEAT\_MTE is implemented, an instruction that loads or stores an Allocation Tag is considered a load or store to each location in the associated Tag Granule for the purpose of triggering Watchpoint exceptions.

## D2.9.7 Watchpoint usage constraints

See the following:

- Reserved DBGBCR&lt;n&gt;\_EL1.{BT2, BT} values when using Watchpoints.
- Reserved DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} values.
- Usage constraints on DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN} values.
- Programming dependencies of the BAS and MASK fields.
- Reserved DBGWCR&lt;n&gt;\_EL1.BAS values.
- Reserved DBGWCR&lt;n&gt;\_EL1.MASK values.
- Other usage constraints.

## D2.9.7.1 Reserved DBGBCR&lt;n&gt;\_EL1.{BT2, BT} values when using Watchpoints

It is CONSTRAINED UNPREDICTABLE whether Watchpoint exceptions and debug events are generated if DBGBCR&lt;n&gt;\_EL1.{BT2, BT} is a reserved value. See Reserved DBGBCR&lt;n&gt;\_EL1.{BT2, BT} values .

## D2.9.7.2 Reserved DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} values

Table D2-16 shows when particular combinations of DBGWCR&lt;n&gt;\_EL1.{SSCE, SSC, HMC, PAC} are reserved.

## Table D2-16 Reserved SSCE, SSC, HMC, and PAC combinations

| HMC, SSCE, SSC, and PAC combination                                                                                                                                 | Reserved                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| All combinations with SSCE set to 1.                                                                                                                                | When FEAT_RME is not implemented.                   |
| All combinations with HMCset to 0, SSCE set to 0, and SSC set to 0b01 or 0b10 .                                                                                     | When Secure state is not implemented.               |
| All combinations with SSCE set to 0 and SSC set to 0b01 or 0b10 , except for the combination with HMCset to 1, SSCE set to 0, SSC set to 0b01 , and PAC set to 0b00 | When EL3 is not implemented and EL2 is implemented. |

| HMC, SSCE, SSC, and PAC combination                                                                                                                                                                   | Reserved                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| All combinations with SSCE set to 0 where HMCorSSCis nonzero, except for the combination with HMCset to 1, SSCE set to 0, SSC set to 0b01 , and PAC set to 0b00 or combinations with SSC set to 0b11. | When both EL2 and EL3 are not implemented. |
| The combination with HMCset to 1, SSCE set to 0, SSC set to 0b11 , and PAC set to 0b00 .                                                                                                              | When EL2 is not implemented.               |
| The combinations with SSC set to 0b11 except the combination with HMCset to 1, SSCE set to 0, SSC set to 0b11 , and PAC set to 0b00 .                                                                 | When Secure EL2 is not implemented.        |
| The combination with HMCset to 1, SSCE set to 0, SSC set to 0b01 , and PAC set to 0b00 .                                                                                                              | When Secure EL2 is not implemented.        |
| Combinations not included in Table D2-13.                                                                                                                                                             | Always.                                    |

If a watchpoint is programmed with one of these reserved combinations:

- The watchpoint must behave as if it is either:
- -Disabled.
- -Programmed with a combination that is not reserved, other than for a direct or external read of DBGWCR&lt;n&gt;\_EL1.
- For a direct or external read of DBGWCR&lt;n&gt;\_EL1, if the reserved combination:
- -Has no function for any execution conditions, the value read back for each of SSCE, SSC, HMC, and PMCis UNKNOWN.
- -Has a function for execution conditions other than the current execution conditions, the value read back is the value written. This permits software to save and restore the combination so that the watchpoint functions for the other execution conditions.

The behavior of watchpoints with reserved combinations of SSCE, SSC, HMC, and PAC might change in future revisions of the architecture. For this reason, software must not rely on the behavior described here.

## D2.9.7.3 Usage constraints on DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN} values

## For Linked Watchpoints

ALinked watchpoint must link to a context-aware breakpoint. For a Linked watchpoint, any DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN} value that is not for a context-aware breakpoint is reserved.

If a Linked watchpoint links to a breakpoint that is not implemented, or does not support linking, then reads of DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN} return an UNKNOWN value and the behavior is CONSTRAINED UNPREDICTABLE. The Linked watchpoint behaves as if it is either:

- Disabled
- Linked to an UNKNOWN breakpoint that supports linking.

If a Linked watchpoint links to one of the following implemented breakpoints, then it behaves as if it is disabled:

- Abreakpoint that is context-aware , but that is either not enabled or not programmed as a Context matching breakpoint with linking enabled.
- Abreakpoint that supports address matching with linking and is not programmed as an Address matching breakpoint with linking enabled.

It is CONSTRAINED UNPREDICTABLE whether Watchpoint exceptions and debug events are generated if an instruction address generates a breakpoint match for more than one enabled Address matching breakpoint with linking enabled.

For Unlinked Watchpoints For Unlinked watchpoints, DBGWCR&lt;n&gt;\_EL1.{LBNX, LBN} reads UNKNOWN and its value is ignored.

## D2.9.7.4 Programming dependencies of the BAS and MASK fields

When programming a watchpoint, a debugger must use either:

- The MASK field, to program the watchpoint with an address range that can be eight bytes to 2GB.
- The BAS field, to select which bytes in the doubleword or word starting at the address contained in the DBGWVR&lt;n&gt;\_EL1 the watchpoint must generate Watchpoint exceptions for.

If the debugger uses the:

- MASKfield, it must program BAS to be 0b11111111 , so that all bytes in the doubleword or word are selected.
- BAS field, it must program MASK to be 0b00000 , so that the MASK field does not indicate any address ranges.

If an enabled watchpoint has a MASK field that is nonzero and a BAS field that is not set to 0b11111111 , then for each byte in the address range, it is CONSTRAINED UNPREDICTABLE whether or not a Watchpoint exception is generated.

## D2.9.7.5 Reserved DBGWCR&lt;n&gt;\_EL1.BAS values

The BAS field must be programmed with a value Zeros(8-n-m):Ones(n):Zeros(m) , where:

- n is a nonzero positive integer less-than-or-equal-to 8.
- m is a positive integer less-than 8.
- n+m is less-than-or-equal-to 8.

All other values are reserved.

Note

If x is zero, then Zeros(x) is an empty bitstring.

If DBGWVR&lt;n&gt;\_EL1[2] is 1, DBGWCR&lt;n&gt;\_EL1.BAS[7:4] are RES0 and are ignored.

If a watchpoint is programmed with a reserved BAS value:

- It is CONSTRAINED UNPREDICTABLE whether the watchpoint generates a Watchpoint exception for each byte in the doubleword or word of memory addressed by the DBGWVR&lt;n&gt;\_EL1.
- Adirect or external read of DBGWCR&lt;n&gt;\_EL1.BAS returns an UNKNOWN value.

Software must not rely on these properties as the behavior of reserved values might change in a future revision of the architecture.

## D2.9.7.6 Reserved DBGWCR&lt;n&gt;\_EL1.MASK values

If a watchpoint is programmed with a reserved MASK value:

- The watchpoint must behave as if it is either:
- -Disabled.
- -Programmed with an UNKNOWN value that is not reserved, that might be 0b00000 , other than for a direct or external read of DBGWCR&lt;n&gt;\_EL1.
- Adirect or external read of DBGWCR&lt;n&gt;\_EL1.MASK returns an UNKNOWN value.

## D2.9.7.7 Other usage constraints

## For all watchpoints:

- DBGWVR&lt;n&gt;\_EL1[1:0] are RES0 and are ignored.
- If DBGWCR&lt;n&gt;\_EL1.MASK is nonzero, and any masked bits of DBGWVR&lt;n&gt;\_EL1 are not 0, it is CONSTRAINED UNPREDICTABLE whether the watchpoint generates a Watchpoint exception when the unmasked bits match.
- Awatchpoint never generates any Watchpoint exceptions if DBGWCR&lt;n&gt;\_EL1.LSC is 0b00 .

## D2.9.8 Exception syndrome information, fault address information, and preferred return address

On taking a Watchpoint exception or entering Debug state for a Watchpoint debug event, the PE records the following:

- Information about the debug event or exception in a syndrome register . No information is recorded if the watchpoint causes the PE to enter Debug state and FEAT\_EDHSR is not implemented.
- An address that the debugger can use to determine the memory location that caused the watchpoint, in a Fault Address Register . No address is recorded if the PE sets the FnV bit in the syndrome register to 1, as described in Fault address information.

The syndrome register and fault address register used are one of the following:

- For a Watchpoint exception taken to EL1, ESR\_EL1 and FAR\_EL1.
- For a Watchpoint exception taken to EL2, ESR\_EL2 and FAR\_EL2.
- For a Watchpoint debug event that causes entry to Debug state, EDHSR, if implemented, and EDWAR.

In cases where one instruction triggers multiple watchpoints, only one address is recorded.

See ISS encoding for an exception from a Watchpoint exception for more information.

Note

Watchpoint exceptions cannot be taken to EL3 using AArch64.

This section uses the following terms:

## Naturally-aligned block of memory

## Means:

- Apower-of-two size.
- No larger than the DC ZVA block size defined by the DCZID\_EL0.BS field, if ESR\_ELx.FnP or EDHSR.FnP is 0.
- No larger than the smallest implemented translation granule if ESR\_ELx.FnP or EDHSR.FnP is 1.
- Contains a watchpointed address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint, or a watchpointed address in the address range permitted by RLVLYV in Watchpoint behavior on accesses by SVE and SME instructions.

The size of the naturally-aligned block of memory is IMPLEMENTATION DEFINED. There is no architectural means of discovering the size.

## Watchpointed address

Is defined as follows:

- If all watchpoints are address match watchpoints, then a watchpointed address is any address for which at least one of the address match watchpoints generates a watchpoint match.
- If all watchpoints are address mismatch watchpoints, then a watchpointed address is any address for which all address mismatch watchpoints generate a watchpoint match.
- Otherwise, a watchpointed address is any address for which at least one of the address match watchpoints generates a watchpoint match and all address mismatch watchpoints generate a watchpoint match.

For more information, see the subsections that follow. These are:

- Exception syndrome information.
- Fault address information.
- Preferred return address.

RSQDKJ

## D2.9.8.1 Exception syndrome information

If an instruction generates a watchpoint match where the watchpointed data address or data address range is not accessed by the instruction, the PE:

- Sets ESR\_ELx.WPF to 1, on taking a Watchpoint exception generated by the watchpoint match.
- If FEAT\_EDHSR is implemented, sets EDHSR.WPF to 1, on entering Debug state on a Watchpoint debug event generated by the watchpoint match.

Otherwise, ESR\_ELx.WPF or EDHSR.WPF is set to an IMPLEMENTATION DEFINED choice of 0 or 1.

Example D2-9

When RLVLYV in Watchpoint behavior on accesses by SVE and SME instructions applies, a relaxed watchpoint access might generate a watchpoint match for a data address or data address range that the instruction does not access. Arm strongly recommends that ESR\_ELx.WPF or EDHSR.WPF is set to 0 for all other cases.

| R KSSHC   | If a watchpoint matches an access that is due to a relaxed watchpoint access , then the PE: • Sets ESR_ELx.FnV to an IMPLEMENTATION DEFINED value, 0 or 1, on taking a Watchpoint exception generated by the watchpoint match. • If FEAT_EDHSR is implemented, sets EDHSR.FnV to an IMPLEMENTATION DEFINED value, 0 or 1, on entering Debug state on a Watchpoint debug event generated by the watchpoint match.                                                                                                                                                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RLWSF   | When the PE sets ESR_ELx.FnV to 0 on taking a Watchpoint exception generated by a watchpoint match: • If the lowest watchpointed address that is higher than or equal to the address recorded in FAR_ELx might not have been accessed by the instruction, other than as permitted byR LVLYV , the PE sets ESR_ELx.FnP to 1. • Otherwise, the PE sets ESR_ELx.FnP to 0.                                                                                                                                                                                                              |
| R CJWYX   | When FEAT_EDHSR is implemented and the PE sets EDHSR.FnV to 0 on entering Debug state on a Watchpoint debug event generated by a watchpoint match: • If the lowest watchpointed address that is higher than or equal to the address recorded in EDWARmight not have been accessed by the instruction, other than as permitted byR LVLYV , the PE sets EDHSR.FnP to 1.                                                                                                                                                                                                               |
| R TLMWP   | When FEAT_Debugv8p2 is implemented and FEAT_Debugv8p9 is not implemented, the PE behavior on taking a Watchpoint exception is as follows: • If the PE sets ESR_ELx.FnV to 1 or ESR_ELx.FnP to 1, then the PE sets ESR_ELx.WPTV to 1. • If the address recorded in FAR_ELx is not within a naturally-aligned block of memory, then the PE sets ESR_ELx.WPTV to 1.                                                                                                                                                                                                                    |
| R RLFQK   | When FEAT_Debugv8p2 is implemented and FEAT_Debugv8p9 is not implemented, the PE behavior on entering Debug state on a Watchpoint debug event is as follows: • If FEAT_EDHSR is implemented and the PE sets EDHSR.FnV to 1 or EDHSR.FnP to 1, then the PE sets EDHSR.WPTV to 1. • If the address recorded in EDWARis not within a naturally-aligned block of memory, where the naturally-aligned block of memory is defined by then the PE sets EDHSR.WPTV to 1. • Otherwise, if FEAT_EDHSR is implemented, then the PE sets EDHSR.WPTV to an IMPLEMENTATION DEFINED value, 0 or 1. |
| R WVSZS   | When FEAT_Debugv8p9 is implemented, on a watchpoint match the PE: • Sets ESR_ELx.WPTV to 1 on taking a Watchpoint exception generated by the watchpoint match. • Sets EDHSR.WPTV to 1 on entering Debug state on a Watchpoint debug event generated by the watchpoint match.                                                                                                                                                                                                                                                                                                        |
| R PVYNL   | On a watchpoint match generated by watchpoint <n> :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

RXQBQN

RGBDMM

- If the PE sets ESR\_ELx.WPTV to 1 on taking a Watchpoint exception generated by the watchpoint match, then ESR\_ELx.WPT is set to &lt;n&gt; .
- If FEAT\_EDHSR is implemented and the PE sets EDHSR.WPTV to 1 on entering Debug state on a Watchpoint debug event generated by the watchpoint match, then EDHSR.WPT is set to &lt;n&gt; .
- Otherwise, ESR\_ELx.WPT or EDHSR.WPT is UNKNOWN.

When an instruction generates multiple watchpoint matches and the PE sets ESR\_ELx.WPTV to 1 on taking a Watchpoint exception generated by the watchpoint match, or FEAT\_EDHSR is implemented and the PE sets EDHSR.WPTV to 1 on entering Debug state on a Watchpoint debug event generated by the watchpoint match, then the value &lt;n&gt; reported in ESR\_ELx.WPT or EDHSR.WPT, is defined as follows:

- If all the matching watchpoints are address match watchpoints or all the matching watchpoints are address mismatch watchpoints, then &lt;n&gt; is any watchpoint that generates a watchpoint match.
- Otherwise, &lt;n&gt; is any address match watchpoint that generates a watchpoint match.

## D2.9.8.2 Fault address information

## D2.9.8.2.1 Address recorded for Watchpoint exceptions generated by Memory Copy and Memory Set instructions

RFMRLD If FEAT\_MOPS is implemented, when a watchpoint is triggered by a Memory Copy or Memory Set instruction, the address recorded in FAR\_ELx or EDWAR is all of:

- If the watchpoint is triggered by a write made by a Memory Copy or Memory Set instruction, in the inclusive range between:
- -The lowest address written to by the instruction that triggered the watchpoint.
- -The highest watchpointed address written to by the instruction that triggered the watchpoint.
- If the watchpoint is triggered by a read made by a Memory Copy instruction, in the inclusive range between:
- -The lowest address read from by the instruction that triggered the watchpoint.
- -The highest watchpointed address read from by the instruction that triggered the watchpoint.
- If the watchpoint generates an entry to Debug state and FEAT\_EDHSR is not implemented, within a naturally-aligned block of memory.
- Within the current translation granule of the watchpointed address.

## D2.9.8.2.2 Address recorded for Watchpoint exceptions generated by zeroing and data cache maintenance instructions

For a watchpoint triggered by a DC ZVA, DC GVA, DC GZVA, or STZGM instruction, or a Data Cache maintenance operation, the address recorded in FAR\_ELx or EDWAR is both:

- Any address accessed by the instruction.
- Within a naturally-aligned block of memory.

Note

Despite their mnemonics, the DC ZVA, DC GVA, and DC GZVA instructions are not data cache maintenance instructions.

## D2.9.8.2.3 Address recorded for Watchpoint exceptions generated by SVE and SME instructions

RGVKYZ For a watchpoint triggered by an SVE contiguous load/store instruction or by an SME load/store instruction, the address recorded in FAR\_ELx or EDWAR is both:

- In the inclusive range between:
- -The lowest address accessed by the vector instruction that triggered the watchpoint, or the lowest rounded address as permitted by RLVLYV in Watchpoint behavior on accesses by SVE and SME instructions.
- -The highest watchpointed address accessed by the vector instruction that triggered the watchpoint, or the highest rounded address as permitted by RLVLYV.
- If either the watchpoint generates an entry to Debug state and FEAT\_EDHSR is not implemented, or FEAT\_Debugv8p2 is not implemented, then the range is further restricted such that:
- -The range includes a watchpointed address.
- -The range does not include any Inactive elements.

Otherwise, the range might include Inactive elements that have not been accessed by the instruction. See RRLWSF and RCJWYX. However, other than as permitted by RLVLYV, the watchpoint was triggered by an Active element.

- Within a naturally-aligned block of memory.

## D2.9.8.2.4 Address recorded for Watchpoint exceptions generated by other instructions

The address recorded by other instructions must be both:

- From the inclusive range between:
- -The lowest address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint.
- -The highest watchpointed address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint.
- Within a naturally-aligned block of memory.

Example D2-10 Address recorded for a watchpoint programmed on 0x8019

Adebugger programs a watchpoint to generate a Watchpoint exception on any access to the byte 0x8019 .

An A32 load multiple instruction then loads nine registers starting from address 0x8004 upwards. This triggers the watchpoint.

If the DC ZVA block size is:

- 32 bytes, the address that the PE records must be between 0x8004 and 0x8019 inclusive.
- 16 bytes, the address that the PE records must be between 0x8010 and 0x8019 inclusive.

## D2.9.8.3 Preferred return address

The preferred return address of a Watchpoint exception is the address of the instruction that was not executed because the PE took the Watchpoint exception instead.

This means that the preferred return address is the address of the instruction that caused the exception.

## D2.9.9 Pseudocode description of Watchpoint exceptions taken from AArch64 state

AArch64.WatchpointByteMatch() tests an individual byte accessed by an operation.

AArch64.StateMatch() tests the values in DBGWCR&lt;n&gt;\_EL1.{HMC, SSCE, SSC, PAC}, and if the watchpoint links to a breakpoint with linking enabled, also tests the breakpoint that the watchpoint links to.

AArch64.WatchpointMatch() tests the value in DBGWVR&lt;n&gt;\_EL1.

AArch64.CheckWatchpoint() generates a FaultRecord that AArch64.Abort() raises a Watchpoint exception for if all of the following are true:

- MDSCR\_EL1.MDE is 1.
- Debug exceptions are enabled from the current Exception level and Security state. See Enabling debug exceptions from the current Exception level and Security state.
- All of the conditions required for Watchpoint exception generation are met. See About Watchpoint exceptions.

Note

AArch64.CheckWatchpoint() might halt the PE and cause it to enter Debug state. External debug uses Debug state.

AArch64.WatchpointException() is called to generate a Watchpoint exception.

These functions are defined in Pseudocode for AArch64 operation.