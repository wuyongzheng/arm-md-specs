## G2.9 Watchpoint exceptions

This section describes Watchpoint exceptions in stage 1 of an AArch32 translation regime.

The PE is using an AArch32 translation regime when it is executing either:

- At EL1 or higher in an Exception level that is using AArch32.
- At EL0 using AArch32 when EL1 is using AArch32.

This section contains the following subsections:

- About Watchpoint exceptions.
- Watchpoint types and linking of watchpoints.
- Execution conditions for which a watchpoint generates Watchpoint exceptions.
- Watchpoint data address comparisons.
- Watchpoint behavior for certain instruction classes.
- Watchpoint usage constraints.
- Exception syndrome information and preferred return address.
- Pseudocode description of Watchpoint exceptions taken from AArch32 state.

## G2.9.1 About Watchpoint exceptions

A watchpoint is an event that results from the execution of an instruction, based on a data address. Watchpoints are also known as data breakpoints .

Awatchpoint operates as follows:

1. Adebugger programs the watchpoint with a data address, or a data address range.
2. The watchpoint generates a Watchpoint debug event on an access to the address, or any address in the address range.

Awatchpoint never generates a Watchpoint debug event on an instruction fetch.

An implementation can include between 2-16 watchpoints. In an implementation, DBGDIDR.WRPs shows how many are implemented.

To use an implemented watchpoint, a debugger programs the following registers for the watchpoint:

- The Watchpoint Control Register , DBGWCR&lt;n&gt;. This holds control information for the watchpoint, for example an enable control.
- The Watchpoint Value Register , DBGWVR&lt;n&gt;. This holds the data virtual address used for watchpoint matching.

The registers are numbered, so that:

- DBGWCR1and DBGWVR1 are for watchpoint number one.
- DBGWCR2and DBGWVR2 are for watchpoint number two.
- . . .
- . . .
- DBGWCRnand DBGWVRn are for watchpoint number n.

Awatchpoint can:

- Be programmed to generate Watchpoint debug events on read accesses only, on write accesses only, or on both types of access.
- Link to a Linked Context breakpoint , so that a Watchpoint debug event is only generated if the PE is in a particular context when the address match occurs.

Asingle watchpoint can be programmed to match on one or more address bytes. A watchpoint generates a Watchpoint debug event on an access to any byte that it is watching. The number of bytes a watchpoint is watching is either:

- One to eight bytes, provided that these bytes are contiguous and that they are all in the same naturally-aligned doubleword. A debugger uses the Byte Address Select field, DBGWCR&lt;n&gt;.BAS, to select the bytes. See Programming a watchpoint with eight bytes or fewer.
- Eight bytes to 2GB, provided that both of the following are true:
- -The number of bytes is a power-of-two.
- -The range starts at an address that is aligned to the range size.

Adebugger uses the MASK field, DBGWCR&lt;n&gt;.MASK, to program a watchpoint with eight bytes to 2GB. See Programming a watchpoint with eight or more bytes.

Adebugger must use either the BAS field or the MASK field. If it uses both, whether the watchpoint generates Watchpoint exceptions is CONSTRAINED UNPREDICTABLE. See Programming dependencies of the BAS and MASK fields.

For each memory access, all of the watchpoints are tested. When a watchpoint is tested, it generates a Watchpoint debug event if all of the following are true:

- The conditions specified in the DBGWCR&lt;n&gt; are met. This includes all of the following:
- -The watchpoint is enabled. See DBGWCR&lt;n&gt;.E.
- -The type of the access. See DBGWCR&lt;n&gt;.LST.
- -The Security state, Exception level, and privilege of the access. See Execution conditions for which a watchpoint generates Watchpoint exceptions.
- -If the watchpoint links to a breakpoint with linking enabled, the comparison or comparisons made by the breakpoint. See Rules for linking watchpoints.

Together, these define the context of the data access that the watchpoint matches.

- The comparison with the address held in the DBGWVR&lt;n&gt; is successful. See Watchpoint data address comparisons.
- The instruction that initiates the memory access is committed for execution.
- The instruction that initiates the memory access passes its Condition code check.

If multiple watchpoints can generate a Watchpoint debug event for an access, then for all watchpoints that are enabled and match the context of the data access, the Boolean equality comparison results of all the watchpoints are OR'd together to generate a result.

If halting is allowed and EDSCR.HDE is 1, Watchpoint debug events cause entry to Debug state.

Otherwise, if debug exceptions are:

- Enabled, Watchpoint debug events generate Watchpoint exceptions.
- Disabled, Watchpoint debug events are ignored.

Note

The remainder of this Watchpoint Exceptions section, including all subsections, describes watchpoints as generating Watchpoint exceptions. However, the behavior described also applies if watchpoints are causing entry to Debug state.

The debug exception enable controls describes the enable controls for Watchpoint debug events.

## G2.9.2 Watchpoint types and linking of watchpoints

When a debugger programs a watchpoint, it must program that watchpoint so that it is either:

- Used in isolation. In this case, the watchpoint is called an Unlinked watchpoint .
- Enabled for linking to a Linked Context breakpoint. In this case, the watchpoint is called a Linked watchpoint .

When a Linked watchpoint links to a Linked Context breakpoint, the Linked watchpoint only generates a Watchpoint exception if the PE is in a particular context when the data address match occurs. For example, a debugger might:

1. Program watchpoint number one with a data address.
2. Program breakpoint number five to be a Linked VMID Match breakpoint .
3. Link the watchpoint and the breakpoint together. A Watchpoint exception is only generated if both the data address matches and the VMID matches.

The Watchpoint Type field for a watchpoint, DBGWCR&lt;n&gt;.WT, controls whether the watchpoint is enabled for linking. If DBGWCR&lt;n&gt;.WT is 1, the watchpoint is enabled for linking.

## G2.9.2.1 Rules for linking watchpoints

The rules for watchpoint linking are as follows:

- Only Linked watchpoints can be linked.

- ALinked watchpoint can link to any type of Linked Context breakpoint. The Linked Breakpoint Number field, DBGWCR&lt;n&gt;.LBN, for the Linked watchpoint specifies the particular Linked Context breakpoint that the Linked watchpoint links to, and:

- DBGWCR&lt;n&gt;.WT.{SSC, HMC, PAC} for the Linked watchpoint define the execution conditions that the watchpoint generates Watchpoint exceptions for. See Execution conditions for which a watchpoint generates Watchpoint exceptions.

- DBGBCR&lt;n&gt;.{SSC, HMC, PMC} for the Linked Context breakpoint are ignored.

- ALinked watchpoint cannot link to another watchpoint. The LBN field can therefore only specify a breakpoint.

- If a Linked watchpoint links to a breakpoint that is not context-aware, the behavior of the Linked watchpoint is CONSTRAINED UNPREDICTABLE. See Watchpoint usage constraints.

- If a Linked watchpoint links to an Unlinked Context breakpoint, the Linked watchpoint never generates any Watchpoint exceptions.

- Multiple Linked watchpoints can link to a single Linked Context breakpoint.

Note

Multiple Address breakpoints can also link to a single Linked Context breakpoint. Breakpoint exceptions describes breakpoints.

Figure G2-1 shows an example of permitted watchpoint linking.

## G2.9.3 Execution conditions for which a watchpoint generates Watchpoint exceptions

Each watchpoint can be programmed so that it only generates Watchpoint exceptions for certain execution conditions. For example, a watchpoint might be programmed to generate Watchpoint exceptions only when the PE is executing at EL2.

DBGWCR&lt;n&gt;.{SSC, HMC, PAC} define the execution conditions a watchpoint generates Watchpoint exceptions for, as follows:

## Security State Control, SSC

Controls whether the watchpoint generates Watchpoint exceptions only in Secure state, only in Non-secure state, or in both Security states.

Note

This is determined by the Security state of the PE, not from the NS attribute returned by the translation of the virtual address on which the watchpoint is set.

## Higher Mode Control, HMC, and Privileged Access Control, PAC

HMCand PAC together control which Exception levels and Privilege levels the watchpoint generates Watchpoint exceptions in.

The PAC control relates to the privilege of the memory access and Privilege level at which the access was made.

PAC condition for generating a Watchpoint exception

This means that, if the PE executes a Load unprivileged or Store unprivileged instruction at PL1, the resulting data access triggers a watchpoint only if both:

- PAC is programmed to a value that generates watchpoints on PL0 accesses.
- All other conditions for generating the watchpoint are met.

Example A32/T32 Load unprivileged and Store unprivileged instructions are LDRT and STRT .

Table G2-15 shows the valid combinations of HMC, SSC, and PAC, and for each combination shows which Privilege levels watchpoints generate Watchpoint exceptions in.

In the table:

Yor - Means that a watchpoint programmed with the values of HMC, SSC, and PAC shown in that row:

Y

Can generate Watchpoint exceptions at that Privilege level.

- Cannot generate Watchpoint exceptions at that Privilege level.

Res

Means that the combination of HMC, SSC, and PAC is reserved. See Reserved DBGWCR&lt;n&gt;.{SSC, HMC, PAC} values.

Table G2-15 Summary of watchpoint HMC, SSC, and PAC encodings

| HMC   | SSC   | PAC   | Security state the watchpoint is programmed to match in   | PL2 a   | PL1   | PL0   | Implementation   | Implementation    |
|-------|-------|-------|-----------------------------------------------------------|---------|-------|-------|------------------|-------------------|
| HMC   | SSC   | PAC   | Security state the watchpoint is programmed to match in   | PL2 a   | PL1   | PL0   | No EL3           | No EL2 and no EL3 |
| 0     | 00    | 01    | Both                                                      | -       | Y     | -     | -                | -                 |
| 0     | 00    | 10    | Both                                                      | -       | -     | Y     | -                | -                 |
| 0     | 00    | 11    | Both                                                      | -       | Y     | Y     | -                | -                 |
| 0     | 01    | 01    | Non-secure                                                | -       | Y     | -     | Res              | Res               |
| 0     | 01    | 10    | Non-secure                                                | -       | -     | Y     | Res              | Res               |
| 0     | 01    | 11    | Non-secure                                                | -       | Y     | Y     | Res              | Res               |
| 0     | 10    | 01    | Secure                                                    | -       | Y     | -     | Res              | Res               |
| 0     | 10    | 10    | Secure                                                    | -       | -     | Y     | Res              | Res               |
| 0     | 10    | 11    | Secure                                                    | -       | Y     | Y     | Res              | Res               |
| 0     | 11    | 01    | Secure                                                    | Y       | Y     | -     | -                | Res               |
| 0     | 11    | 11    | Secure                                                    | Y       | Y     | Y     | -                | Res               |
| 1     | 00    | 01    | Both                                                      | Y       | Y     | -     | -                | Res               |
| 1     | 00    | 11    | Both                                                      | Y       | Y     | Y     | -                | Res               |
| 1     | 01    | 00    | Non-secure                                                | Y       | -     | -     |                  |                   |
| 1     | 01    | 01    | Non-secure                                                | Y       | Y     | -     | Res              | Res               |
| 1     | 01    | 11    | Non-secure                                                | Y       | Y     | Y     | Res              | Res               |
| 1     | 10    | 01    | Secure                                                    | -       | Y     | -     | Res              | Res               |
| 1     | 10    | 11    | Secure                                                    | -       | Y     | Y     | Res              | Res               |

Example G2-1

| HMC   | SSC   | PAC   | Security state the watchpoint is programmed to match in   | PL2 a   | PL1   | PL0   | Implementation   | Implementation    |
|-------|-------|-------|-----------------------------------------------------------|---------|-------|-------|------------------|-------------------|
|       |       |       |                                                           |         |       |       | No EL3           | No EL2 and no EL3 |
| 1     | 11    | 00    | Both                                                      | Y       | -     | -     | -                | Res if no EL2 b   |
| 1     | 11    | 01    |                                                           | Y       | Y     | -     |                  |                   |
| 1     | 11    | 11    |                                                           | Y       | Y     | Y     |                  |                   |

All combinations of HMC, SSC, and PAC that this table does not show are reserved. See Reserved DBGWCR&lt;n&gt;.{SSC, HMC, PAC} values.

## G2.9.4 Watchpoint data address comparisons

An address comparison is successful if bits [31:2] of the current data virtual address are equal to DBGWVR&lt;n&gt;[31:2], taking into account all of the following:

- The size of the access. See Size of the data access.
- The bytes selected by DBGWVR&lt;n&gt;.BAS. See Programming a watchpoint with eight bytes or fewer.
- Any address ranges indicated by DBGWVR&lt;n&gt;.MASK. See Programming a watchpoint with eight or more bytes.

Note

DBGWVR&lt;n&gt;[1:0] are RES0 and are ignored.

## G2.9.4.1 Size of the data access

Because watchpoints can be programmed to generate Watchpoint exceptions on individual bytes, the size of each access must be taken into account. See Example G2-2.

Example G2-2

1. Adebugger programs a watchpoint to generate Watchpoint exceptions only when the byte at address 0x1009 is accessed.
2. The PE accesses the unaligned doubleword starting at address 0x1003 .

In this scenario, the watchpoint must generate a Watchpoint exception.

The size of data accesses initiated by DCIMVAC instructions is an IMPLEMENTATION DEFINED size that is both:

- From the inclusive range between:
- -The size that CTR.DminLine defines.
- -2KB.
- Apower-of-two.

The lowest address accessed by a DCIMVAC instruction is the address supplied to the instruction, rounded down to the nearest multiple of the access size initiated by that instruction.

The highest address accessed is (size - 1) bytes above the lowest address accessed.

See also, Watchpoint behavior on accesses by DCIMVAC instructions.

## G2.9.4.2 Programming a watchpoint with eight bytes or fewer

The Byte Address Select field, DBGWCR&lt;n&gt;.BAS, selects which bytes in the doubleword starting at the address contained in the DBGWVR&lt;n&gt; the watchpoint generates Watchpoint exceptions for.

If the address programmed into the DBGWVR&lt;n&gt; is:

- Doubleword-aligned:
- -All eight bits of DBGWCR&lt;n&gt;.BAS are used, and the descriptions given in Table G2-16 apply.
- Word-aligned but not doubleword-aligned:
- -Only DBGWCR&lt;n&gt;.BAS[3:0] are used, and the descriptions given in Table G2-17 apply. In this case, DBGWCR&lt;n&gt;.BAS[7:4] are RES0.

Table G2-16 Supported BAS values when the DBGWVRn address alignment is doubleword

| BAS value   | Description                                   |
|-------------|-----------------------------------------------|
| 0b00000000  | No byte selected.                             |
| BAS[0] == 1 | Byte at address DBGWVR<n>[31:3]:000 selected. |
| BAS[1] == 1 | Byte at address DBGWVR<n>[31:3]:001 selected. |
| BAS[2] == 1 | Byte at address DBGWVR<n>[31:3]:010 selected. |
| BAS[3] == 1 | Byte at address DBGWVR<n>[31:3]:011 selected. |
| BAS[4] == 1 | Byte at address DBGWVR<n>[31:3]:100 selected. |
| BAS[5] == 1 | Byte at address DBGWVR<n>[31:3]:101 selected. |
| BAS[6] == 1 | Byte at address DBGWVR<n>[31:3]:110 selected. |
| BAS[7] == 1 | Byte at address DBGWVR<n>[31:3]:111 selected. |

Table G2-17 Supported BAS values when the DBGWVRn address alignment is word

| BAS value a   | Description                                  |
|---------------|----------------------------------------------|
| 0b00000000    | No byte selected.                            |
| BAS[0] == 1   | Byte at address DBGWVR<n>[31:2]:00 selected. |
| BAS[1] == 1   | Byte at address DBGWVR<n>[31:2]:01 selected. |
| BAS[2] == 1   | Byte at address DBGWVR<n>[31:2]:10 selected. |
| BAS[3] == 1   | Byte at address DBGWVR<n>[31:2]:11 selected. |

If the BAS field selects more than one byte, the bytes it selects must be contiguous. For watchpoint behavior when its BAS field selects non-contiguous bytes, see Other usage constraints.

When programming the BAS field with anything other than 0b11111111 , a debugger must also program DBGWCR&lt;n&gt;.MASK to be 0b00000 . See Programming dependencies of the BAS and MASK fields.

Awatchpoint generates a Watchpoint exception whenever a watched byte is accessed, even if:

- The access size is smaller or larger than the address region being watched.

- The access is misaligned, and the base address of the access is not in the doubleword or word of memory addressed by the DBGWVR&lt;n&gt;[31:3]. See Example G2-2.

The following are some example configurations of the BAS field:

- To program a watchpoint to generate a Watchpoint exception on the byte at address 0x1003 , program:
- -DBGWVR&lt;n&gt;with 0x1000 .
- -DBGWCR&lt;n&gt;\_EL1.BAS to be 0b00001000 .
- To program a watchpoint to generate a Watchpoint exception on the bytes at addresses 0x2003 , 0x2004 and 0x2005 , program:
- -DBGWVR&lt;n&gt;with 0x2000 .
- -DBGWCR&lt;n&gt;\_EL1.BAS to be 0b00111000 .
- If the address programmed into the DBGWVR&lt;n&gt; is doubleword-aligned:
- -To generate a Watchpoint exception when any byte in the word starting at the doubleword-aligned address is accessed, program DBGWCR&lt;n&gt;.BAS to be 0b00001111 .
- -To generate a Watchpoint exception when any byte in the word starting at address DBGWVR&lt;n&gt;[31:3]:100 is accessed, program DBGWCR&lt;n&gt;.BAS to be 0b11110000 .

Note

Arm deprecates programming a DBGWVR&lt;n&gt; with an address that is not doubleword-aligned.

## G2.9.4.3 Programming a watchpoint with eight or more bytes

Adebugger can use the MASK field, DBGWCR&lt;n&gt;.MASK, to program a single watchpoint with a data address range. The data address range must meet all of the following criteria:

- It is a size that is both:
- -Apower-of-two.
- -Aminimum of eight bytes.
- -Amaximum of 2GB.
- It starts at an address that is aligned to the size.

The MASK field specifies the number of least significant data address bits that must be masked. Up to 31 least significant bits can be masked.

If n least significant address bits are masked, the watchpoint generates a Watchpoint exception on all of the following:

- Address DBGWVR&lt;n&gt;[31: n ]:000 . . .
- Address DBGWVR&lt;n&gt;[31: n ]:111 . . .
- Any address between these two addresses.

For example, if the four least significant address bits are masked, Watchpoint exceptions are generated for all addresses between DBGWVR&lt;n&gt;[31:4]:0000 and DBGWVR&lt;n&gt;[31:4]:1111, including these addresses.

## Note

- The most significant bit cannot be masked. This means that the full address cannot be masked.
- For watchpoint behavior when its MASK field is programmed with a reserved value, see Reserved DBGWCR&lt;n&gt;.MASK values.

When masking address bits, a debugger must both:

- Program DBGWCR&lt;n&gt;.BAS to be 0b11111111 . See Programming dependencies of the BAS and MASK fields.
- In the DBGWVR&lt;n&gt;, set the masked address bits to 0. For watchpoint behavior when any of the masked address bits are not 0, see Other usage constraints.

## G2.9.5 Watchpoint behavior for certain instruction classes

Under normal operating conditions, the following do not generate Watchpoint exceptions:

- Instruction cache maintenance instructions.
- Address translation instructions.
- TLB maintenance instructions.
- Prefetch instructions.
- All data cache maintenance instructions except DCIMVAC .

However, the debug architecture allows for IMPLEMENTATION DEFINED controls, such as those in ACTLR registers, to enable watchpoints on an IMPLEMENTATION DEFINED subset of these instructions. Whether a watchpoint treats the instruction as a load or a store, and the access size of instruction cache maintenance, address translation, and TLB maintenance instructions are IMPLEMENTATION DEFINED.

The access size of the IMPLEMENTATION DEFINED instruction cache maintenance, address translation, and TLB maintenance instructions that generate Watchpoint exceptions are IMPLEMENTATION DEFINED.

## See also:

- Watchpoint behavior on accesses by Store-Exclusive instructions.
- Watchpoint behavior on accesses by DCIMVAC instructions.

## G2.9.5.1 Watchpoint behavior on accesses by Store-Exclusive instructions

If a watchpoint matches on a data access caused by a Store-Exclusive instruction, then:

- If the store fails because an Exclusives monitor does not permit it, it is IMPLEMENTATION DEFINED whether the watchpoint generates a Watchpoint exception.
- Otherwise, the watchpoint generates a Watchpoint exception.

## G2.9.5.2 Watchpoint behavior on accesses by DCIMVAC instructions

It is IMPLEMENTATION DEFINED whether DCIMVAC operations can generate Watchpoint exceptions. If they can, they are treated as data stores. This means that for a watchpoint to match on an access caused by a DCIMVAC instruction, the debugger must program DBGWCR&lt;n&gt;.LSC to be one of the following:

10 Match on data stores only.

11 Match on data stores and data loads.

Note

For the size of data accesses performed by DCIMVAC instructions, see Watchpoint data address comparisons. The size of all data accesses must be considered because watchpoints can be programmed to match on individual bytes.

## G2.9.6 Watchpoint usage constraints

See the following:

- Reserved DBGWCR&lt;n&gt;.{SSC, HMC, PAC} values.
- Reserved DBGWCR&lt;n&gt;.LBN values.
- Programming dependencies of the BAS and MASK fields.
- Reserved DBGWCR&lt;n&gt;.BAS values.
- Reserved DBGWCR&lt;n&gt;.MASK values.
- Other usage constraints.

## G2.9.6.1 Reserved DBGWCR&lt;n&gt;.{SSC, HMC, PAC} values

Table G2-18 shows when particular combinations of DBGWCR&lt;n&gt;.{SSC, HMC, PAC} are reserved.

## Table G2-18 Reserved SSC, HMC, and PAC combinations

| HMC, SSC, and PAC combination                                           | Reserved                                            |
|-------------------------------------------------------------------------|-----------------------------------------------------|
| All combinations with SSC set to 0b01 or 0b10 .                         | When EL3 is not implemented and EL2 is implemented. |
| Any combination where HMCorSSCis nonzero                                | When both of EL2 and EL3 are not implemented        |
| The combination with HMCset to 1, SSC set to 0b11 , and PAC set to 0b00 | When EL2 is not implemented                         |
| The combinations with SSC set to 0b11 and PAC set to 0b01 or 0b11       | When Secure EL2 is not implemented                  |
| The combination with HMCset to 1, SSC set to 0b01 and PAC set to 0b00   | When Secure EL2 is not implemented                  |
| Combinations not included in Table G2-15.                               | Always                                              |

If a watchpoint is programmed with one of these reserved combinations:

- The watchpoint must behave as if it is either:
- -Disabled.
- -Programmed with a combination that is not reserved, other than for a direct or external read of DBGWCR&lt;n&gt;.
- For a direct or external read of DBGWCR&lt;n&gt;, if the reserved combination:
- -Has no function for any execution conditions, the value read back for each of SSC, HMC, and PMC is UNKNOWN.
- -Has a function for execution conditions other than the current execution conditions, the value read back is the value written. This permits software to save and restore the combination so that the watchpoint functions for the other execution conditions.

The behavior of watchpoints with reserved combinations of SSC, HMC, and PAC might change in future revisions of the architecture. For this reason, software must not rely on the behavior described here.

## G2.9.6.2 Reserved DBGWCR&lt;n&gt;.LBN values

## For Linked watchpoints

ALinked watchpoint must link to a context-aware breakpoint. For a Linked watchpoint, any DBGWCR&lt;n&gt;.LBN value that is not for a context-aware breakpoint is reserved.

If a Linked watchpoint links to a breakpoint that is not implemented, or that is not context-aware, then reads of DBGWCR&lt;n&gt;.LBN return an UNKNOWN value and the behavior is CONSTRAINED UNPREDICTABLE. The Linked watchpoint behaves as if it is either:

- Disabled.
- Linked to an UNKNOWN context-aware breakpoint.

If a Linked watchpoint links to a breakpoint that is implemented and is context-aware, but that is either not enabled or not programmed as a Linked Context breakpoint, it behaves as if it is disabled.

## For Unlinked watchpoints

For Unlinked watchpoints, DBGWCR&lt;n&gt;.LBN reads UNKNOWN and its value is ignored.

## G2.9.6.3 Programming dependencies of the BAS and MASK fields

When programming a watchpoint, a debugger must use either:

- The MASK field, to program the watchpoint with an address range that can be eight bytes to 2GB.
- The BAS field, to select which bytes in the doubleword or word starting at the address contained in the DBGWVR&lt;n&gt;the watchpoint must generate Watchpoint exceptions for.

If the debugger uses the:

- MASKfield, it must program BAS to be 0b11111111 , so that all bytes in the doubleword or word are selected.
- BAS field, it must program MASK to be 0b00000 , so that the MASK field does not indicate any address ranges.

If an enabled watchpoint has a MASK field that is nonzero and a BAS field that is not set to 0b11111111 , then for each byte in the address range, it is CONSTRAINED UNPREDICTABLE whether or not a Watchpoint exception is generated.

## G2.9.6.4 Reserved DBGWCR&lt;n&gt;.BAS values

The BAS field must be programmed with a value Zeros (8-n-m): Ones (n): Zeros (m) , where:

- n is a nonzero positive integer less-than-or-equal-to 8.
- m is a positive integer less-than 8.
- n+m is less-than-or-equal-to 8.

All other values are reserved.

```
Note is an empty bitstring.
```

If x is zero, then Zeros (x)

If DBGWVR&lt;n&gt;[2] is 1, DBGWCR&lt;n&gt;.BAS[7:4] are RES0 and are ignored.

If a watchpoint is programmed with a reserved BAS value:

- It is CONSTRAINED UNPREDICTABLE whether the watchpoint generates a Watchpoint exception for each byte in the doubleword or word of memory addressed by the DBGWVR&lt;n&gt;.
- Adirect or external read of DBGWCR&lt;n&gt;.BAS returns an UNKNOWN value.

Software must not rely on these properties as the behavior of reserved values might change in a future revision of the architecture.

## G2.9.6.5 Reserved DBGWCR&lt;n&gt;.MASK values

If a watchpoint is programmed with a reserved MASK value:

- The watchpoint must behave as if it is either:
- -Disabled.
- -Programmed with an UNKNOWN value that is not reserved, that might be 0b00000 , other than for a direct or external read of DBGWCR&lt;n&gt;.
- Adirect or external read of DBGWCR&lt;n&gt;.MASK returns an UNKNOWN value.

## G2.9.6.6 Other usage constraints

For all watchpoints:

- DBGWVR&lt;n&gt;[1:0] are RES0 and are ignored.
- If DBGWCR&lt;n&gt;.MASK is nonzero, and any masked bits of DBGWVR&lt;n&gt; are not 0, it is CONSTRAINED UNPREDICTABLE whether the watchpoint generates a Watchpoint exception when the unmasked bits match.
- Awatchpoint never generates any Watchpoint exceptions if DBGWCR&lt;n&gt;.LSC is 0b00 .

## G2.9.7 Exception syndrome information, fault address information, and preferred return address

See the following:

- Exception syndrome information.
- Fault address information.
- Preferred return address.

## G2.9.7.1 Exception syndrome information

The PE takes a Watchpoint exception as either:

- AData Abort exception, if it is taken to PL1. In this case, it is taken to Abort mode.
- AHyptrap exception, if it is taken to PL2 because HCR.TGE or HDCR.TDE is 1. In this case, it is taken to Hyp mode.

If the exception is taken to:

## Abort mode

The PE sets all of the following:

- DBGDSCRext.MOE to 0b1010 , to indicate a Watchpoint exception.
- DFSR.CM to indicate whether a cache maintenance instruction caused the exception.
- DFSR.WnR to indicate whether the exception was generated on a read instruction or a write instruction.

## In addition, if using the:

- Short-descriptor format, the PE sets DFSR.FS to the code for a debug exception, 0b00010 , and DFSR.Domain to an UNKNOWN value.
- Long-descriptor format, the PE sets DFSR.STATUS to the code for a debug exception, 0b100010 .

## The PE does all of the following:

- Records information about the exception in the Hypervisor Syndrome Register , HSR. See Table G2-19.
- Sets DBGDSCRext.MOE to 0b1001 , to indicate a Watchpoint exception.

## Table G2-19 Information recorded in the HSR

| HSR field               | Information recorded                                                               |
|-------------------------|------------------------------------------------------------------------------------|
| Exception Class , EC    | The PE sets this to the code for a Data Abort exception routed to Hyp mode, 0x24 . |
| Instruction Length , IL | The PE sets this to 1.                                                             |

## Hyp mode

| HSR field                           | Information recorded                         | Information recorded                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instruction Specific Syndrome , ISS | ISV[24] ISS[9] ISS[8] ISS[7] ISS[6] ISS[5:0] | Instruction Syndrome Valid (ISV). The PE sets this to 0. RES0. External Abort type (EA). The PE sets this to 0 . Cache Maintenance (CM). The PE sets this to indicate whether a cache maintenance instruction caused the exception. RES0 . Write not Read (WnR). The PE sets this to indicate whether the exception generated on a read instruction or a write instruction . Data Fault Status Code (DFSC). The PE sets this to the code for a debug |
| Instruction Specific Syndrome , ISS | ISS[23:10]                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Instruction Specific Syndrome , ISS |                                              | was                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Instruction Specific Syndrome , ISS |                                              | exception, 0b100010 .                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Instruction Specific Syndrome , ISS |                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Instruction Specific Syndrome , ISS |                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Instruction Specific Syndrome , ISS |                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Note

For information about how debug exceptions can be routed to PL2, see Routing debug exceptions.

## G2.9.7.2 Fault address information

On a Watchpoint exception, the PE records an address in a Fault Address Register that the debugger can use to determine the memory location that triggered the watchpoint.

The Fault Address Register (FAR) used is one of the following:

- For a Watchpoint taken as an exception to Abort mode, DFAR.
- For a Watchpoint taken as an exception to Hyp mode, EHDFAR.
- For a Watchpoint debug event that causes entry to Debug state, EDWAR.

In cases where one instruction triggers multiple watchpoints, only one address is recorded.

Note

If Debug state was entered from AArch32 state, then EDWAR[63:32] is UNKNOWN and must be ignored by the debugger.

In the following subsection, a watchpointed address is defined as any address for which at least one of the watchpoints generates a watchpoint match.

## G2.9.7.2.1 Address recorded for Watchpoint exceptions generated by data cache maintenance instructions

For a watchpoint triggered by a Data Cache maintenance operation, the address recorded in DFAR, HDFAR, or EDWAR is both:

- Any address accessed by the instruction.
- Within a naturally-aligned block of memory.

## G2.9.7.2.2 Address recorded for Watchpoint exceptions generated by instructions other than data cache maintenance instructions

The address recorded in DFAR, HDFAR, or EDWAR is both:

- From the inclusive range between:
- -The lowest address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint.
- -The highest watchpointed address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint.
- Within a naturally-aligned block of memory that is all of the following:
- -Apower-of-two size.
- -No larger than the DC ZVA block size.

- -Contains a watchpointed address accessed by the memory access or set of contiguous memory accesses that triggered the watchpoint.

The size of the naturally-aligned block of memory is IMPLEMENTATION DEFINED. There is no architectural means of discovering the size.

## Example G2-3 Address recorded for a watchpoint programmed on 0x8019

Adebugger programs a watchpoint to generate a Watchpoint exception on any access to the byte 0x8019 .

An A32 load multiple instruction then loads nine registers starting from address 0x8004 upwards. This triggers the watchpoint.

If the DC ZVA block size is:

- 32 bytes, the address that the PE records must be between 0x8004 and 0x8019 inclusive.
- 16 bytes, the address that the PE records must be between 0x8010 and 0x8019 inclusive.

## G2.9.7.3 Preferred return address

The preferred return address of a Watchpoint exception is the address of the instruction that was not executed because the PE took the Watchpoint exception instead.

This means that the preferred return address is the address of the instruction that caused the exception.

## G2.9.8 Pseudocode description of Watchpoint exceptions taken from AArch32 state

AArch32.WatchpointByteMatch() tests an individual byte accessed by an operation.

AArch32.StateMatch() tests the values in DBGWCR&lt;n&gt;.{HMC, SSC, PAC}, and if the watchpoint is Linked, also tests the Linked Context breakpoint that the watchpoint links to.

AArch32.WatchpointMatch() tests the value in DBGWVR&lt;n&gt;.

AArch32.CheckWatchpoint() generates a FaultRecord . AWatchpoint exception is taken if all of the following are true:

- DBGDSCRext.MDBGen is 1.
- Debug exceptions are enabled from the current Exception level and Security state. See Enabling debug exceptions.
- All of the conditions required for Watchpoint exception generation are met. See About Watchpoint exceptions.

Note

AArch32.CheckWatchpoint might halt the PE and cause it to enter Debug state. External debug uses Debug state.

The AArch32.Abort() function processes the FaultRecord object returned by AArch32.CheckWatchpoint() , as described in Abort exceptions. If a Watchpoint exception is taken to AArch32 state, the AArch32.Abort() function generates a Data Abort exception.